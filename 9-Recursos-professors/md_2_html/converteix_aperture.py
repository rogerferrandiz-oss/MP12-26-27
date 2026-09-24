#!/usr/bin/env python3
"""
Conversor Aperture: Markdown (CONVENCIONS v2) -> HTML -> ZIP per a Moodle Book.

Ús:
    python3 converteix_aperture.py document.md [--personatges Personatges.md]
                                   [--sortida ./out] [--num 01] [--force]

Fase 1: valida (valida_aperture.py). Si hi ha errors, s'atura i no genera res.
Fase 2: genera un fitxer HTML per capítol/subcapítol i els empaqueta en un ZIP
        importable amb Book -> Importa capítols.

Els avatars es resolen des de Personatges.md pel nom (p. ex. 'albert_formal').
No cal capçalera <!-- PERSONATGES --> al document.
"""

import argparse
import html
import re
import sys
import unicodedata
import zipfile
from pathlib import Path

try:
    import markdown as mdlib
except ImportError:
    sys.exit("Cal la llibreria 'markdown':  pip install markdown")

sys.path.insert(0, str(Path(__file__).parent))
import valida_aperture as VA


# ---------------------------------------------------------------- utilitats

def normalitza(nom):
    """'Lídia_seriosa' -> 'lidia_seriosa'. Treu accents i passa a minúscula."""
    nom = unicodedata.normalize("NFD", nom.strip())
    nom = "".join(c for c in nom if unicodedata.category(c) != "Mn")
    return nom.lower()


def slug(text, maxlen=40):
    text = normalitza(text)
    text = re.sub(r"[^a-z0-9]+", "_", text).strip("_")
    return text[:maxlen].rstrip("_") or "sense_titol"


MD = mdlib.Markdown(extensions=["tables", "attr_list"])

RE_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")


def normalitza_llistes(text):
    """Markdown exigeix línia en blanc abans d'una llista i sagnats de 4.
    Aquí s'afegeix la línia i es reindenten els nivells, de manera que
    escriure la llista enganxada al paràgraf (com es fa de manera natural)
    funcioni igualment."""
    sortida, pila, dins_codi = [], [], False
    for linia in text.split("\n"):
        if linia.strip().startswith("```"):
            dins_codi = not dins_codi
            pila = []
            sortida.append(linia)
            continue
        m = RE_ITEM.match(linia) if not dins_codi else None
        if not m:
            if linia.strip():
                pila = []
            sortida.append(linia)
            continue

        sagnat = len(m.group(1).expandtabs(4))
        while pila and sagnat < pila[-1]:
            pila.pop()
        if not pila or sagnat > pila[-1]:
            pila.append(sagnat)
        nivell = len(pila) - 1

        # línia en blanc abans del primer element d'una llista de nivell 0
        if nivell == 0 and sortida and sortida[-1].strip() \
           and not RE_ITEM.match(sortida[-1]):
            sortida.append("")

        sortida.append("    " * nivell + m.group(2) + " " + m.group(3))
    return "\n".join(sortida)


def md2html(text):
    MD.reset()
    out = MD.convert(normalitza_llistes(text).strip())
    # totes les taules porten la classe del framework
    out = out.replace("<table>", '<table class="aperture-table aperture-table--neutra">')
    return out


def md_inline(text):
    """Markdown per a un fragment curt: sense <p> embolcallant."""
    out = md2html(text)
    m = re.fullmatch(r"<p>(.*)</p>", out.strip(), re.S)
    return m.group(1) if m else out


# ---------------------------------------------------------------- personatges

def carrega_personatges(path):
    """Llegeix les taules | Nom | URL | de Personatges.md."""
    avatars = {}
    if not path or not Path(path).exists():
        return avatars
    for linia in Path(path).read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^\|\s*([A-Za-zÀ-ÿ_]+)\s*\|\s*(https?://\S+?)\s*\|", linia)
        if m:
            avatars[normalitza(m.group(1))] = m.group(2)
    return avatars


# ---------------------------------------------------------------- renderitzat

ICONES = {
    "destacat-info": "fa-circle-info",
    "destacat-warning": "fa-triangle-exclamation",
    "destacat-error": "fa-circle-xmark",
    "destacat-success": "fa-circle-check",
    "destacat-reading": "fa-book-open",
    "destacat-video": "fa-circle-play",
    "destacat-ideas": "fa-lightbulb",
    "destacat-tools": "fa-wrench",
    "destacat-audio": "fa-headphones",
}
ETIQUETES_ARIA = {
    "destacat-info": "Informació", "destacat-warning": "Avís",
    "destacat-error": "Error freqüent", "destacat-success": "Fet correctament",
    "destacat-reading": "Lectura", "destacat-video": "Vídeo",
    "destacat-ideas": "Idea opcional", "destacat-tools": "Eina necessària",
    "destacat-audio": "Àudio",
}


def parteix_metadades(cos):
    """Separa 'clau: valor' inicials del cos."""
    metadades, linies = {}, cos.split("\n")
    i = 0
    while i < len(linies):
        if not linies[i].strip():
            i += 1
            break
        m = re.match(r"^([a-zà-ÿ]+)\s*:\s*(.*)$", linies[i])
        if not m:
            break
        metadades[m.group(1).lower()] = m.group(2).strip()
        i += 1
    return metadades, "\n".join(linies[i:])


def render_bloc(nom, cos, avatars, avisos):
    md, resta = parteix_metadades(cos)

    if nom in ICONES:
        icona, aria = ICONES[nom], ETIQUETES_ARIA[nom]
        variant = nom.replace("destacat-", "aperture-alert-")
        return (
            f'<div class="aperture-alert {variant}" role="note" '
            f'aria-label="{aria}">\n'
            f'  <i class="fas {icona} aperture-alert-icon" aria-hidden="true"></i>\n'
            f'  <div class="aperture-alert-content">\n{md2html(cos)}\n  </div>\n'
            f'</div>'
        )

    if nom == "destacat-critic":
        titol = html.escape(md.get("titol", ""))
        return (
            f'<div class="aperture-alert-critical" role="alert">\n'
            f'  <div class="aperture-alert-critical-header">\n'
            f'    <div class="aperture-alert-critical-header-content">\n'
            f'      <i class="fas fa-triangle-exclamation aperture-alert-icon" '
            f'aria-hidden="true"></i>\n      <span>{titol}</span>\n'
            f'    </div>\n  </div>\n'
            f'  <div class="aperture-alert-critical-body">\n{md2html(resta)}\n'
            f'  </div>\n</div>'
        )

    if nom == "bloc-dialeg":
        enllacos_html = ""
        m = re.split(r"^enlla[cç]os\s*:\s*$", resta, maxsplit=1, flags=re.M)
        if len(m) == 2:
            resta = m[0]
            items = []
            for l in m[1].split("\n"):
                if not l.strip().startswith("-"):
                    continue
                parts = [x.strip() for x in l.strip().lstrip("- ").split("|")]
                txt = parts[0]
                url = parts[1] if len(parts) > 1 else "#"
                ico = parts[2] if len(parts) > 2 else "fa-arrow-right"
                items.append(f'        <a class="aperture-dialogue-link" '
                             f'href="{html.escape(url)}">'
                             f'<i class="fas {html.escape(ico)}" aria-hidden="true"></i> '
                             f'{html.escape(txt)}</a>')
            if items:
                enllacos_html = ('\n      <div class="aperture-dialogue-links">\n'
                                 + "\n".join(items) + "\n      </div>")
        clau = normalitza(md.get("avatar", ""))
        url = avatars.get(clau)
        if not url:
            avisos.append(f"Avatar '{clau}' no trobat a Personatges.md.")
            url = ""
        nom_p = html.escape(md.get("nom", ""))
        rol = html.escape(md.get("rol", ""))
        return (
            f'<div class="aperture-dialogue">\n'
            f'  <img class="aperture-dialogue-avatar" src="{url}" '
            f'alt="Avatar de {nom_p}">\n'
            f'  <div class="aperture-dialogue-content">\n'
            f'    <div class="aperture-dialogue-header">\n'
            f'      <p class="aperture-dialogue-name">{nom_p}</p>\n'
            f'      <span class="aperture-dialogue-role">{rol}</span>\n'
            f'    </div>\n'
            f'    <div class="aperture-dialogue-text">\n{md2html(resta)}\n'
            f'    </div>{enllacos_html}\n  </div>\n</div>'
        )

    if nom == "bloc-boto":
        estil = md.get("estil", "primari")
        icona = md.get("icona", "")
        i_html = (f'<i class="fas {html.escape(icona)}" aria-hidden="true"></i> '
                  if icona else "")
        return (f'<a class="aperture-btn aperture-btn--{estil}" '
                f'href="{html.escape(md.get("url", ""))}">'
                f'{i_html}{html.escape(md.get("text", ""))}</a>')

    if nom == "bloc-targeta":
        estil = md.get("estil", "primari")
        icona = md.get("icona", "fa-circle-info")
        return (
            f'<div class="aperture-card">\n'
            f'  <div class="aperture-card-icon aperture-card-icon--{estil}">'
            f'<i class="fas {html.escape(icona)}" aria-hidden="true"></i></div>\n'
            f'  <p class="aperture-card-title">{html.escape(md.get("titol", ""))}</p>\n'
            f'  <div class="aperture-card-description">\n{md2html(resta)}\n'
            f'  </div>\n</div>'
        )

    if nom == "bloc-recursos":
        items = []
        for linia in resta.split("\n"):
            if not linia.strip().startswith("-"):
                continue
            parts = [p.strip() for p in linia.strip().lstrip("- ").split("|")]
            text = parts[0]
            url = parts[1] if len(parts) > 1 else "#"
            icona = parts[2] if len(parts) > 2 else "fa-arrow-right"
            items.append(f'  <a class="aperture-resource-link" href="{html.escape(url)}">'
                         f'<i class="fas {html.escape(icona)}" aria-hidden="true"></i> '
                         f'{html.escape(text)}</a>')
        return '<div class="aperture-resources">\n' + "\n".join(items) + "\n</div>"

    if nom == "bloc-desplegable":
        return (f'<details class="aperture-desplegable">\n'
                f'  <summary>{html.escape(md.get("titol", ""))}</summary>\n'
                f'  <div class="aperture-desplegable-body">\n{md2html(resta)}\n'
                f'  </div>\n</details>')

    if nom == "bloc-passos":
        return '<div class="aperture-parts-list">\n' + md2html(resta) + "\n</div>"

    if nom == "bloc-correu":
        clau = normalitza(md.get("avatar", ""))
        url = avatars.get(clau, "")
        mod = " aperture-email--incorrecte" if md.get("estil") == "incorrecte" else ""
        etiqueta = ""
        if md.get("estil") == "incorrecte":
            etiqueta = ('<span class="aperture-email-label '
                        'aperture-email-label--incorrecte">Incorrecte</span>\n')
        elif md.get("estil") == "correcte":
            etiqueta = ('<span class="aperture-email-label '
                        'aperture-email-label--correcte">Correcte</span>\n')
        return (
            f'{etiqueta}<div class="aperture-email{mod}">\n'
            f'  <div class="aperture-email-header">\n'
            f'    <img class="aperture-email-avatar" src="{url}" alt="">\n'
            f'    <div class="aperture-email-meta">\n'
            f'      <div class="aperture-email-from">{html.escape(md.get("de",""))}</div>\n'
            f'      <div class="aperture-email-to">Per a: {html.escape(md.get("per",""))}</div>\n'
            f'      <div class="aperture-email-date">{html.escape(md.get("data",""))}</div>\n'
            f'      <div class="aperture-email-subject">{html.escape(md.get("assumpte",""))}</div>\n'
            f'    </div>\n  </div>\n'
            f'  <div class="aperture-email-body">\n{md2html(resta)}\n  </div>\n</div>'
        )

    # bloc de codi
    return f'<pre class="aperture-code-block"><code>{html.escape(cos)}</code></pre>'


# ---------------------------------------------------------------- estructura

def neteja_titol(t):
    """Treu l'anotació (capítol) / (subcapítol N) del títol visible."""
    return re.sub(r"\s*\((?:sub)?cap[ií]tol[^)]*\)\s*$", "", t, flags=re.I).strip()


def parteix_document(text):
    """Retorna [{nivell, titol, cos}] tallant per ## i ###."""
    seccions, actual = [], None
    dins_bloc = False
    for linia in text.split("\n"):
        if linia.strip().startswith("```"):
            dins_bloc = not dins_bloc
        m = re.match(r"^(#{2,3})\s+(.*)$", linia) if not dins_bloc else None
        if m:
            if actual:
                seccions.append(actual)
            actual = {"nivell": len(m.group(1)),
                      "titol": neteja_titol(m.group(2)),
                      "linies": []}
        elif actual is not None:
            actual["linies"].append(linia)
    if actual:
        seccions.append(actual)
    for s in seccions:
        cos = "\n".join(s["linies"])
        s["cos"] = re.sub(r"\n\s*-{3,}\s*$", "\n", cos)
    return seccions


def render_cos(cos, avatars, avisos):
    """Converteix el cos d'una secció (blocs + text lliure) a HTML."""
    trossos, buffer, dins, nom_bloc, cos_bloc = [], [], False, None, []

    def buida_buffer():
        text = "\n".join(buffer).strip()
        if text:
            trossos.append(md2html(text))
        buffer.clear()

    acc = 3
    for linia in cos.split("\n"):
        st = linia.strip()
        if st.startswith("```"):
            n = len(st) - len(st.lstrip("`"))
            if not dins:
                buida_buffer()
                etiqueta = st[n:].strip()
                nom_bloc = etiqueta.split()[0] if etiqueta else ""
                dins, cos_bloc, acc = True, [], n
                continue
            if n >= acc:
                trossos.append(render_bloc(nom_bloc, "\n".join(cos_bloc),
                                           avatars, avisos))
                dins = False
                continue
        (cos_bloc if dins else buffer).append(linia)
    buida_buffer()
    return "\n\n".join(t for t in trossos if t.strip())


PLANTILLA = """<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<title>{titol}</title>
</head>
<body>
<div class="aperture-tutorial-wrap">
{cos}
</div>
</body>
</html>
"""


# ---------------------------------------------------------------- principal

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("document")
    ap.add_argument("--personatges", default="Personatges.md")
    ap.add_argument("--sortida", default="./sortida")
    ap.add_argument("--num", default="01", help="prefix numèric del capítol")
    ap.add_argument("--force", action="store_true",
                    help="genera encara que hi hagi errors de validació")
    args = ap.parse_args()

    # ---- FASE 1: validació
    r = VA.valida(args.document)
    r.imprimeix()
    if r.errors and not args.force:
        print("\nNo es genera res. Corregeix els errors i torna-ho a passar.")
        sys.exit(1)

    # ---- FASE 2: conversió
    avatars = carrega_personatges(args.personatges)
    if not avatars:
        print(f"\nAVÍS: no s'ha pogut llegir '{args.personatges}'. "
              f"Els avatars sortiran buits.")
    avisos = []

    text = Path(args.document).read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)   # treu comentaris HTML
    seccions = parteix_document(text)
    if not seccions:
        sys.exit("No s'ha trobat cap encapçalat '##'. Revisa l'estructura.")

    sortida = Path(args.sortida)
    sortida.mkdir(parents=True, exist_ok=True)
    fitxers, cap, sub = [], 0, 0

    for s in seccions:
        cos = render_cos(s["cos"], avatars, avisos)
        pagina = PLANTILLA.format(titol=html.escape(s["titol"]), cos=cos)
        if s["nivell"] == 2:
            cap += 1
            sub = 0
            nom = f"{int(args.num) + cap - 1:02d}_{slug(s['titol'])}.html"
        else:
            sub += 1
            nom = f"{int(args.num) + max(cap, 1) - 1:02d}sub_{sub}_{slug(s['titol'])}.html"
        (sortida / nom).write_text(pagina, encoding="utf-8")
        fitxers.append((nom, s["nivell"], s["titol"]))

    zip_path = sortida / (Path(args.document).stem + ".zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for nom, _, _ in fitxers:
            z.write(sortida / nom, nom)

    print(f"\nGenerat: {zip_path}")
    for nom, niv, titol in fitxers:
        print(f"  {'  ' if niv == 3 else ''}{nom}   ({titol})")
    for a in dict.fromkeys(avisos):
        print(f"  AVÍS: {a}")


if __name__ == "__main__":
    main()
