#!/usr/bin/env python3
"""
Validador de documents Markdown segons CONVENCIONS.md v2 (MP12).
Ús:  python3 valida_aperture.py fitxer1.md [fitxer2.md ...]
Codi de sortida: 0 si cap error, 1 si n'hi ha algun.
"""

import re
import sys
from pathlib import Path

BLOCS_DESTACAT = {
    "destacat-info", "destacat-warning", "destacat-error", "destacat-success",
    "destacat-reading", "destacat-video", "destacat-ideas", "destacat-tools",
    "destacat-audio", "destacat-critic",
}
BLOCS_ESTRUCTURA = {
    "bloc-dialeg", "bloc-correu", "bloc-passos", "bloc-boto",
    "bloc-targeta", "bloc-recursos", "bloc-desplegable",
}
BLOCS_VALIDS = BLOCS_DESTACAT | BLOCS_ESTRUCTURA

RESERVATS = {"destacat-audio"}
DEPRECATS = {"destacat-alert": "destacat-info"}

# errors de nom freqüents -> nom correcte
SUGGERIMENTS = {
    "destacat-idea": "destacat-ideas", "destacat-tool": "destacat-tools",
    "destacat-avis": "destacat-warning", "destacat-critica": "destacat-critic",
    "destacat-critical": "destacat-critic", "destacat-informacio": "destacat-info",
    "bloc-dialogue": "bloc-dialeg", "bloc-boton": "bloc-boto",
    "bloc-card": "bloc-targeta", "bloc-email": "bloc-correu",
}

METADADES_OBLIGATORIES = {
    "bloc-dialeg": ["avatar", "nom", "rol"],
    "bloc-correu": ["de", "per", "assumpte"],
    "bloc-boto": ["text", "url"],
    "bloc-targeta": ["titol"],
    "destacat-critic": ["titol"],
    "bloc-desplegable": ["titol"],
}
ESTILS_BOTO = {"primari", "secundari", "contorn"}
ESTILS_TARGETA = {"primari", "secundari"}

LLENGUATGES_CODI = {
    "", "bash", "sh", "python", "html", "css", "js", "javascript",
    "json", "yaml", "sql", "text", "txt", "ini", "xml", "md",
}


def carrega_avatars(path="Personatges.md"):
    """Noms d'avatar amb URL vàlida a Personatges.md, normalitzats."""
    import unicodedata
    avatars = {}
    p = Path(path)
    if not p.exists():
        return avatars
    for linia in p.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^\|\s*([A-Za-zÀ-ÿ_]+)\s*\|\s*(https?://\S+?)\s*\|", linia)
        if m:
            nom = unicodedata.normalize("NFD", m.group(1).strip())
            nom = "".join(c for c in nom if unicodedata.category(c) != "Mn").lower()
            avatars[nom] = m.group(2)
    return avatars


class Report:
    def __init__(self, nom):
        self.nom = nom
        self.errors = []
        self.avisos = []

    def error(self, linia, msg):
        self.errors.append((linia, msg))

    def avis(self, linia, msg):
        self.avisos.append((linia, msg))

    def imprimeix(self):
        print(f"\nVALIDACIÓ: {self.nom}")
        tot = [("ERROR", l, m) for l, m in self.errors] + \
              [("AVÍS ", l, m) for l, m in self.avisos]
        for tipus, linia, msg in sorted(tot, key=lambda x: x[1]):
            print(f"  {tipus}   línia {linia:>4}  {msg}")
        if not tot:
            print("  0 errors, 0 avisos → llest per convertir.")
        else:
            estat = "NO es genera HTML." if self.errors else "es pot generar HTML."
            print(f"\n  {len(self.errors)} errors, {len(self.avisos)} avisos → {estat}")


def valida(path):
    text = Path(path).read_text(encoding="utf-8")
    linies = text.split("\n")
    r = Report(Path(path).name)

    # ---------- avatars disponibles (Personatges.md) ----------
    declarats = carrega_avatars()
    if not declarats:
        r.avis(1, "No s'ha trobat 'Personatges.md' a la carpeta. No es poden "
                  "comprovar els noms d'avatar.")

    # ---------- recorregut de fences ----------
    usats = set()
    dins = None            # nom del bloc obert
    acc_obert = 3
    inici = 0
    contingut = []
    n_critic = 0
    botons_seguits = 0

    for i, linia in enumerate(linies, start=1):
        strip = linia.strip()

        if strip.startswith("```"):
            n_acc = len(strip) - len(strip.lstrip("`"))
            etiqueta = strip[n_acc:].strip()
            etiqueta_crua = strip[n_acc:]

            if dins is None:
                # obertura
                if etiqueta_crua != etiqueta_crua.lstrip() and etiqueta:
                    r.error(i, f"Espai entre ``` i el nom del bloc: "
                               f"'``` {etiqueta}'. Ha de ser '```{etiqueta}'.")
                nom = etiqueta.split()[0] if etiqueta else ""
                if nom in BLOCS_VALIDS:
                    dins, inici, contingut, acc_obert = nom, i, [], n_acc
                elif nom in DEPRECATS:
                    r.error(i, f"Bloc deprecat '{nom}'. Fes servir "
                               f"'{DEPRECATS[nom]}' (CONVENCIONS §2.3).")
                    dins, inici, contingut = nom, i, []
                elif nom in SUGGERIMENTS:
                    r.error(i, f"Bloc desconegut: '{nom}' "
                               f"(volies dir '{SUGGERIMENTS[nom]}'?)")
                    dins, inici, contingut = nom, i, []
                elif nom in LLENGUATGES_CODI:
                    dins, inici, contingut = "__codi__", i, []
                else:
                    r.error(i, f"Bloc desconegut: '{nom}'. No és cap bloc de "
                               f"CONVENCIONS §2 ni un llenguatge de codi conegut.")
                    dins, inici, contingut = "__desconegut__", i, []
            else:
                if n_acc < acc_obert:
                    nom_int = etiqueta.split()[0] if etiqueta else ""
                    if nom_int in BLOCS_VALIDS:
                        r.error(i, f"Bloc '{nom_int}' imbricat dins de "
                                   f"'{dins}' (línia {inici}). La imbricació de "
                                   f"blocs no està suportada: el conversor no la "
                                   f"renderitza. Treu el bloc a fora. Si és un "
                                   f"enllaç dins d'un diàleg, fes servir la "
                                   f"secció 'enllacos:' del bloc-dialeg.")
                    contingut.append((i, linia))
                    continue
                # tancament — però si porta etiqueta, és una obertura imbricada
                if etiqueta and etiqueta.split()[0] in BLOCS_VALIDS:
                    r.error(i, f"Bloc '{etiqueta.split()[0]}' obert dins de "
                               f"'{dins}' (línia {inici}) amb el mateix nombre "
                               f"d'accents. Això tanca el bloc de fora. Cal 4 "
                               f"accents al de fora, o treure'l a fora "
                               f"(CONVENCIONS §2.13).")
                comprova_bloc(r, dins, inici, contingut, declarats, usats)
                if dins == "destacat-critic":
                    n_critic += 1
                if dins == "bloc-boto":
                    botons_seguits += 1
                elif dins not in ("__codi__",):
                    botons_seguits = 0
                dins = None
            continue

        if dins is not None:
            contingut.append((i, linia))
            comprova_linia(r, i, linia, True)
            continue

        # ---------- text lliure ----------
        comprova_linia(r, i, linia, False)

    if dins is not None:
        r.error(inici, f"Bloc '{dins}' obert i no tancat.")

    comprova_taules(r, linies)

    if n_critic > 1:
        r.avis(1, f"{n_critic} blocs 'destacat-critic' al document. "
                  f"CONVENCIONS §2.3 en recomana un com a màxim per llibre.")
    comprova_encapcalats(r, linies)
    return r


def comprova_linia(r, i, linia, dins_bloc=False):
    strip = linia.strip()
    if True:
        if re.search(r"\[\(\s*https?://", linia):
            r.error(i, "Sintaxi d'imatge incorrecta '[(url)]'. Ha de ser "
                       "'![text alternatiu](url)'. Tal com està, no es veurà "
                       "la imatge: sortirà el text literal.")
        # placeholders sense resoldre
        if re.search(r"\[(placeholder|link al|pendent)[^\]]*\]", linia, re.I):
            r.avis(i, "Placeholder sense resoldre: " + strip[:60])
        # enllaç buit
        if re.search(r"\]\(\s*\)", linia):
            r.error(i, "Enllaç Markdown amb destinació buida.")
        if re.search(r"https?://\S*\.\.\.\s*$", linia) or re.search(r"\]\(\s*\S*\.\.\.\s*\)", linia):
            r.error(i, "URL sense acabar (acaba en '...'). No carregarà res.")
        if re.fullmatch(r"\[\s*https?://[^\]]+\]", strip):
            r.error(i, "URL entre claudàtors sense sintaxi d'enllaç. Ha de ser "
                       "'[text](url)' o, si és una imatge, '![text](url)'.")
        # URL d'edició de Moodle
        if re.match(r"^enlla[cç]os\s*:\s*$", strip) and not dins_bloc:
            r.error(i, "'enllacos:' fora d'un bloc. Ha d'anar DINS del "
                       "bloc-dialeg, abans dels accents de tancament, no "
                       "després. Tal com està sortirà com a text pla.")
        if "chapterid=" in linia:
            r.avis(i, "Enllaç amb 'chapterid='. Es trenca si algun dia "
                      "reimportes el llibre sencer; l'enllaç a nivell "
                      "d'activitat ('view.php?id=<cmid>') és estable.")
        if "edit.php" in linia:
            r.error(i, "URL de Moodle d'EDICIÓ ('edit.php'). L'alumnat no hi té "
                       "permís. Ha de ser 'view.php?id=<cmid>'.")



def comprova_bloc(r, nom, inici, contingut, declarats, usats):
    if nom in ("__codi__", "__desconegut__"):
        return

    if nom in RESERVATS:
        r.avis(inici, f"Bloc '{nom}' està marcat com a RESERVAT a "
                      f"CONVENCIONS §2.3 (no usar encara).")

    # metadades: línies 'clau: valor' abans de la primera línia en blanc
    metadades = {}
    for idx, (nlin, linia) in enumerate(contingut):
        if not linia.strip():
            break
        m = re.match(r"^([A-Za-zÀ-ÿ]+)\s*:\s*(.*)$", linia)
        if m:
            clau = m.group(1)
            if clau != clau.lower():
                r.error(nlin, f"Metadada '{clau}:' amb majúscules. Les claus van "
                              f"sempre en minúscula: '{clau.lower()}:'.")
            metadades[clau.lower()] = m.group(2).strip()
        else:
            break

    for clau in METADADES_OBLIGATORIES.get(nom, []):
        if clau not in metadades or not metadades[clau]:
            r.error(inici, f"'{nom}' sense metadada obligatòria '{clau}:'.")

    if nom in METADADES_OBLIGATORIES and metadades:
        claus = len(metadades)
        if claus < len(contingut) and contingut[claus][1].strip():
            r.error(inici, f"'{nom}': falta la línia en blanc entre les "
                           f"metadades i el cos del bloc.")

    if nom in ("bloc-dialeg", "bloc-correu"):
        av = metadades.get("avatar")
        if av:
            import unicodedata
            k = unicodedata.normalize("NFD", av.strip())
            k = "".join(c for c in k if unicodedata.category(c) != "Mn").lower()
            usats.add(k)
            if declarats and k not in declarats:
                r.error(inici, f"Avatar '{av}' sense imatge a Personatges.md. "
                               f"Disponibles: {', '.join(sorted(declarats))}.")
        # cal línia en blanc entre metadades i text
        claus = len(metadades)
        if claus and claus < len(contingut):
            if contingut[claus][1].strip():
                r.error(inici, f"'{nom}': falta la línia en blanc entre les "
                               f"metadades i el text.")

    if nom == "bloc-boto":
        estil = metadades.get("estil", "primari")
        if estil not in ESTILS_BOTO:
            r.error(inici, f"bloc-boto amb estil '{estil}'. Valors admesos: "
                           f"{', '.join(sorted(ESTILS_BOTO))}.")
        url = metadades.get("url", "")
        if "docs.google.com" in url and not url.rstrip("/").endswith("/copy"):
            r.avis(inici, "Enllaç de Google Docs que no acaba en '/copy': "
                          "l'alumne editarà l'original en comptes de fer-ne còpia.")
        icona = metadades.get("icona", "")
        if icona and not icona.startswith("fa-"):
            r.error(inici, f"Icona '{icona}' sense el prefix 'fa-'.")

    if nom == "bloc-targeta":
        estil = metadades.get("estil", "primari")
        if estil not in ESTILS_TARGETA:
            r.error(inici, f"bloc-targeta amb estil '{estil}'. Valors admesos: "
                           f"{', '.join(sorted(ESTILS_TARGETA))}.")

    if nom == "bloc-dialeg":
        vist = False
        for nlin, linia in contingut:
            if re.match(r"^enlla[cç]os\s*:\s*$", linia.strip()):
                vist = True
                continue
            if vist and linia.strip().startswith("-"):
                parts = [x.strip() for x in linia.strip().lstrip("- ").split("|")]
                if len(parts) < 2 or not parts[1]:
                    r.error(nlin, "Enllaç de diàleg sense URL. Format: "
                                  "'- text | url | icona'.")

    if nom == "bloc-recursos":
        for nlin, linia in contingut:
            if linia.strip().startswith("-"):
                parts = [p.strip() for p in linia.strip("- ").split("|")]
                if len(parts) < 2 or not parts[1]:
                    r.error(nlin, "Línia de bloc-recursos sense URL. Format: "
                                  "'- text | url | icona'.")



def comprova_taules(r, linies, offset=0):
    for i, linia in enumerate(linies, start=1):
        strip = linia.strip()
        if not (strip.startswith("|") and strip.endswith("|")):
            continue
        # només la fila separadora ens interessa per comptar columnes
        if not re.fullmatch(r"\|[\s:|-]+\|", strip):
            continue
        cols = len([c for c in strip.strip("|").split("|")])
        if cols > 2:
            r.avis(offset + i, f"Taula de {cols} columnes. Necessita el "
                               f"modificador 'aperture-table--neutra' o la "
                               f"primera columna sortirà verda i l'última "
                               f"vermella (CONVENCIONS §2.12).")


def comprova_encapcalats(r, linies):
    """Comprova coherència entre el nivell de # i l'anotació (capítol)/(subcapítol)."""
    vist_h_anterior = 0
    for i, linia in enumerate(linies, start=1):
        m = re.match(r"^(#{1,6})\s+(.*)$", linia)
        if not m:
            continue
        nivell = len(m.group(1))
        titol = m.group(2)
        anot = re.search(r"\((cap[ií]tol|subcap[ií]tol)[^)]*\)", titol, re.I)
        if anot:
            tipus = anot.group(1).lower()
            es_sub = tipus.startswith("subcap")
            if not es_sub and nivell != 2:
                r.error(i, f"Anotat com a (capítol) però amb {nivell} coixinets. "
                           f"Els capítols van a '##'.")
            if es_sub and nivell != 3:
                r.error(i, f"Anotat com a (subcapítol) però amb {nivell} "
                           f"coixinets. Els subcapítols van a '###'.")
            if "capitol" in tipus or "subcapitol" in tipus:
                r.avis(i, "Anotació sense accent ('capitol'/'subcapitol').")
            r.avis(i, "El títol porta l'anotació '(" + anot.group(0).strip("()") +
                      ")'. El conversor l'esborra del títol del capítol de Moodle.")
        if nivell == 4 and vist_h_anterior < 3:
            r.error(i, "'####' sense un '###' previ.")
        if nivell >= 2:
            vist_h_anterior = nivell


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    total_errors = 0
    for path in sys.argv[1:]:
        r = valida(path)
        r.imprimeix()
        total_errors += len(r.errors)
    print(f"\n{'=' * 60}\nTOTAL: {total_errors} errors.")
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
