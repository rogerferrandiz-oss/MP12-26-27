# Convencions de producció de continguts — MP12 curs 26-27

Aquest document recull les convencions fixades durant la producció dels Llibres 1, 2 i 4, perquè qualsevol xat nou (o qualsevol persona de l'equip) pugui continuar sense haver-les de redescobrir.

## 1. Flux de treball

1. S'escriu el contingut en **Markdown**, com a document separat (mai directament a la resposta del xat, perquè els editors externs solen trencar els blocs de codi en enganxar-los).
2. Es revisa el Markdown amb en Roger.
3. Un cop validat, es genera l'**HTML** (una pàgina per capítol/subcapítol), es valida sintàcticament, i es genera un **ZIP** per importar-lo a Moodle (Book → Importa capítols).
4. Es pot importar un ZIP nou sobre un llibre existent per afegir-hi més capítols (no cal refer-lo sencer).

## 2. Sintaxi dels blocs en Markdown

### Capçalera de personatges
Cada document comença amb un bloc de comentari que mapeja els noms d'avatar fets servir al document amb la seva URL. Els diferents avatars es troben a Personatges.md al context del projecte:

```
<!-- PERSONATGES -->
<!--
cave_content:  https://cv.copernic.cat/...
albert_formal: https://cv.copernic.cat/...
lidia_formal:  https://cv.copernic.cat/...
-->
```

### Diàleg d'un personatge (`bloc-dialeg`)
Targeta amb avatar, nom, rol i text. Tres línies de metadades, línia en blanc, i després el text lliure (pot tenir diversos paràgrafs i llistes):

```
​```bloc-dialeg
avatar: cave_content
nom: Cave Johnson
rol: CEO i fundador · Aperture Science

Text del personatge, en markdown normal.
​```
```

Mapeja a `.aperture-dialogue` (avatar → `aperture-dialogue-avatar`, nom → `aperture-dialogue-name`, rol → `aperture-dialogue-role`, text → `aperture-dialogue-text`).

### Caixes destacades (`destacat-X`)
El nom del bloc porta directament el tipus, que mapeja 1 a 1 amb les variants de `.aperture-alert` ja definides a `Aperture.css`: `destacat-info`, `destacat-warning`, `destacat-error`, `destacat-success`, `destacat-video`, `destacat-reading`. El contingut és markdown lliure (normalment un títol en negreta + llista, o només un paràgraf/llista):

```
​```destacat-warning
- **Què s'avalua**: ...
- **Quan s'avalua**: ...
​```
```

- `destacat-alert` s'ha fet servir com a sinònim de `destacat-info` (caixa blava, per a resums o índexs d'apartat).
- `destacat-warning` (caixa taronja) per a avisos importants o resums de "què/quan s'avalua".
- Pendent d'ús: `destacat-success` (caixa verda, per a llistes d'expectatives positives — usada al Llibre 1).

### Taules
Taules Markdown normals (`| ... | ... |`). Es converteixen a `<table class="aperture-table">`. **Compte**: cal afegir el modificador `aperture-table--rubrica` (veure §3) sempre que la taula no sigui literalment una llista de "correcte/incorrecte" de dues columnes, perquè si no la primera columna surt verda i l'última vermella per defecte.

Per a rúbriques amb fila de punts per sota de cada criteri, la fila de punts porta la classe `aperture-table-punts` (veure §3).

## 4. Avatars habituals fets servir fins ara

| Identificador | Ús |
|---|---|
| `cave_content` | Cave Johnson, to efusiu/normal |
| `cave_formal` | Cave Johnson, to més seriós (no usat encara) |
| `albert_formal` | Albert, explicació estàndard |
| `albert_content` | Albert, valoració positiva (no usat encara) |
| `lidia_formal` | Lídia, explicació estàndard |
| `lidia_seriosa` | Lídia, avís seriós (usada per "Què passa si suspenc") |

La resta d'avatars (`albert_serios`, `albert_cansat`, `lidia_contenta`, `lidia_treballant`, `manel_formal`, `manel_content`) estan documentats a `Personatges.md` però encara no s'han fet servir.

**Regla de to** (ja aplicada, no repetir l'error): en Cave Johnson no s'utilitza per a contingut seriós amb conseqüències reals per a l'alumne (suspensos, recuperacions). Per a això es fa servir la Lídia (`lidia_seriosa`).

## 5. Nomenclatura de fitxers per a la importació Moodle

L'eina d'importació HTML de Moodle (`booktool_importhtml`) detecta subcapítols pel prefix `sub` al nom de fitxer, i ordena alfabèticament. Convenció fet servir:

```
01_nom_del_capitol.html
01sub_1_nom_subcapitol.html
01sub_2_nom_subcapitol.html
...
```

Si un llibre té diversos capítols, el número inicial (`01`, `02`...) identifica el capítol, i tots els seus subcapítols porten el mateix prefix + `sub_N_`.

## 6. Estat actual de la producció

- **Llibre 1** (Benvinguda al curs): fet, importat i validat visualment a Moodle.
- **Llibre 2** (Com serà la nota del mòdul): fet, 2 capítols (L'avaluació del projecte + Com és un projecte), ZIP generat, pendent de confirmació final d'importació completa.
- **Llibre 4** (Com es fa servir aquest Moodle): fet, ZIP generat, pendent d'importació.
- **Llibre 3**: pendent (contingut tècnic/teoria del mòdul — tutorials de competències transversals, punt 6.3 de la proposta).
- Pendent històric encara sense resoldre del document de proposta: la inconsistència de "6 projectes" / P5 "optativa" al punt 2.2, que Roger va confirmar verbalment que són 5 projectes fixos de 6 setmanes, però el text del document encara no s'ha corregit.
