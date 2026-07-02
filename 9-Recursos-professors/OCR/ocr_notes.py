#!/usr/bin/env python3
"""
ocr_notes.py — Transcripció de notes manuscrites amb VLM local (Ollama)

Ús:
    # Processa un directori sencer
    python ocr_notes.py -i ./imatges -o ./textos

    # Processa amb exemples few-shot (la teva lletra → transcripció esperada)
    python ocr_notes.py -i ./imatges -o ./textos -e ./exemples

    # Fitxer únic
    python ocr_notes.py -i foto.jpg -o ./textos

    # Amb un altre model
    python ocr_notes.py -i ./imatges -o ./textos -m chandra:9b

Estructura d'exemples few-shot:
    exemples/
    ├── ex1.jpg       ← captura de la teva lletra
    ├── ex1.txt       ← transcripció correcta (mateix nom, extensió .txt)
    ├── ex2.jpg
    └── ex2.txt

Prerequisits:
    pip install pillow requests
    ollama pull qwen2.5vl:7b
"""

import argparse
import base64
import io
import sys
import time
from pathlib import Path

import requests
from PIL import Image

# ──────────────────────── CONFIGURACIÓ ────────────────────────
# OLLAMA_BASE = "http://localhost:11434"   ← original
OLLAMA_BASE = "http://localhost:1234"
MODEL       = "chandra"    # Canvia per "chandra:9b" si proves Chandra
MAX_TOKENS  = 4096
MAX_IMG_PX  = 1600               # Redueix si vas just de VRAM
IMG_EXTS    = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}

SYSTEM_PROMPT = """Ets un sistema OCR especialitzat en transcriure notes manuscrites en català i castellà.
Transcriu exactament el que veus a la imatge, conservant:
- L'estructura original (paràgrafs, llistes, taules si n'hi ha)
- Abreviatures tal com apareixen al paper
- Paraules ratllades: ~~text~~
No afegeixis comentaris ni interpretació pròpia.
Si una paraula és completament il·legible, escriu [il·legible]."""
# ──────────────────────────────────────────────────────────────


def resize_image(path: Path, max_px: int = MAX_IMG_PX) -> bytes:
    """
    Redimensiona la imatge si és massa gran (evita desbordament de tokens)
    i la converteix a JPEG per uniformitat.
    """
    img = Image.open(path)
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")
    w, h = img.size
    if max(w, h) > max_px:
        ratio = max_px / max(w, h)
        img = img.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=92)
    return buf.getvalue()


def to_b64(data: bytes) -> str:
    return base64.b64encode(data).decode("utf-8")


def make_image_msg(role: str, b64: str, text: str) -> dict:
    """Missatge en format OpenAI-compatible amb imatge inline (base64)."""
    return {
        "role": role,
        "content": [
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{b64}"}
            },
            {"type": "text", "text": text},
        ],
    }


def load_few_shot(examples_dir: Path | None) -> list[dict]:
    """
    Carrega els parells (imatge, text) del directori d'exemples.
    Cada imatge ha de tenir un .txt amb el mateix nom base.
    Retorna la llista de missatges user/assistant per a few-shot.
    """
    if not examples_dir or not examples_dir.exists():
        return []

    messages = []
    images = sorted(f for f in examples_dir.iterdir() if f.suffix.lower() in IMG_EXTS)

    loaded = 0
    for img_path in images:
        txt_path = img_path.with_suffix(".txt")
        if not txt_path.exists():
            print(f"  ⚠  {img_path.name}: no té .txt corresponent, ignorat.")
            continue
        b64 = to_b64(resize_image(img_path))
        messages.append(make_image_msg("user", b64, "Transcriu aquesta nota manuscrita."))
        messages.append({
            "role": "assistant",
            "content": txt_path.read_text(encoding="utf-8").strip(),
        })
        loaded += 1

    if loaded:
        print(f"  → {loaded} exemple(s) few-shot carregat(s) des de '{examples_dir}'")
    else:
        print(f"  ⚠  Cap exemple vàlid trobat a '{examples_dir}'.")

    return messages


def transcribe(image_bytes: bytes, few_shot: list[dict]) -> str:
    """Envia la imatge a Ollama i retorna la transcripció en text pla."""
    b64 = to_b64(image_bytes)

    messages = (
        [{"role": "system", "content": SYSTEM_PROMPT}]
        + few_shot
        + [make_image_msg("user", b64, "Transcriu aquesta nota manuscrita.")]
    )

    payload = {
        "model": MODEL,
        "messages": messages,
        "max_tokens": MAX_TOKENS,
        "stream": False,
    }

    resp = requests.post(
        f"{OLLAMA_BASE}/v1/chat/completions",
        json=payload,
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()


def check_ollama():
    """Comprova que LM Studio estigui accessible i amb un model carregat."""
    try:
        resp = requests.get(f"{OLLAMA_BASE}/v1/models", timeout=5)
        resp.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("❌  LM Studio no respon a localhost:1234.")
        print("    Assegura't que el servidor local estigui engegat.")
        sys.exit(1)

    models = resp.json().get("data", [])
    if not models:
        print("⚠   Cap model carregat a LM Studio.")
        print("    Carrega un model des de la interfície i torna a intentar-ho.")
        sys.exit(1)

    loaded = models[0]["id"]
    print(f"  → Model detectat: {loaded}")

def collect_images(input_path: Path) -> list[Path]:
    """Retorna la llista d'imatges a processar (fitxer únic o directori)."""
    if input_path.is_file():
        if input_path.suffix.lower() not in IMG_EXTS:
            print(f"❌  El fitxer '{input_path}' no és una imatge suportada.")
            sys.exit(1)
        return [input_path]
    return sorted(f for f in input_path.iterdir() if f.suffix.lower() in IMG_EXTS)


def run(input_path: Path, output_dir: Path, few_shot: list[dict]):
    """Bucle principal: processa totes les imatges i desa els .txt."""
    output_dir.mkdir(parents=True, exist_ok=True)
    images = collect_images(input_path)

    if not images:
        print("❌  No s'han trobat imatges a processar.")
        sys.exit(1)

    sep = "─" * 52
    print(f"\n{sep}")
    print(f"  {len(images)} imatge(s) → {output_dir}")
    print(f"{sep}\n")

    errors = []
    for i, img_path in enumerate(images, 1):
        out_path = output_dir / img_path.with_suffix(".txt").name

        # Salta fitxers ja processats (permet reprendre sessions interrompudes)
        if out_path.exists():
            print(f"[{i:3}/{len(images)}] {img_path.name:<35} ja existeix, saltat")
            continue

        print(f"[{i:3}/{len(images)}] {img_path.name:<35}", end=" ", flush=True)
        t0 = time.time()

        try:
            image_bytes = resize_image(img_path)
            text = transcribe(image_bytes, few_shot)
            out_path.write_text(text, encoding="utf-8")
            print(f"✓  ({time.time() - t0:.1f}s)")
        except requests.exceptions.ConnectionError:
            print("✗  Connexió perduda amb Ollama.")
            sys.exit(1)
        except requests.exceptions.HTTPError as e:
            msg = f"HTTP {e.response.status_code}"
            print(f"✗  {msg}")
            errors.append((img_path.name, msg))
        except Exception as e:
            print(f"✗  {e}")
            errors.append((img_path.name, str(e)))

    print(f"\n{sep}")
    ok = len(images) - len(errors)
    print(f"  Completat: {ok}/{len(images)} transcrits.", end="")
    if errors:
        print(f"  {len(errors)} error(s):")
        for name, err in errors:
            print(f"    • {name}: {err}")
    else:
        print()
    print(sep)


def main():
    parser = argparse.ArgumentParser(
        description="OCR de notes manuscrites amb VLM local (Ollama)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--input",    "-i", required=True,
                        help="Imatge única o directori d'imatges")
    parser.add_argument("--output",   "-o", required=True,
                        help="Directori de sortida per als fitxers .txt")
    parser.add_argument("--examples", "-e", default=None,
                        help="Directori amb exemples few-shot (imatge + .txt)")
    parser.add_argument("--model",    "-m", default=MODEL,
                        help=f"Model d'Ollama (per defecte: {MODEL})")
    parser.add_argument("--max-size", "-s", type=int, default=MAX_IMG_PX,
                        help=f"Mida màxima de la imatge en píxels (per defecte: {MAX_IMG_PX})")
    args = parser.parse_args()

    global MODEL, MAX_IMG_PX
    MODEL      = args.model
    MAX_IMG_PX = args.max_size

    input_path   = Path(args.input)
    output_dir   = Path(args.output)
    examples_dir = Path(args.examples) if args.examples else None

    if not input_path.exists():
        print(f"❌  No existeix: {input_path}")
        sys.exit(1)

    print(f"Model : {MODEL}")
    print(f"Mida  : {MAX_IMG_PX}px màx.")
    check_ollama()

    print("Carregant exemples few-shot..." if examples_dir else "Mode sense exemples few-shot.")
    few_shot = load_few_shot(examples_dir)

    run(input_path, output_dir, few_shot)


if __name__ == "__main__":
    main()