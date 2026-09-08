# Convencions de producció de continguts — MP12 curs 26-27

**Versió 2** · Substitueix la v1. Els canvis principals respecte de la v1 estan marcats amb 🔸.

Aquest document recull les convencions de producció dels llibres del mòdul, perquè qualsevol xat nou (o qualsevol persona de l'equip) pugui continuar sense haver-les de redescobrir. És la referència vinculant: si una cosa no és aquí, no existeix.

---

## 1. Flux de treball

1. S'escriu el contingut en **Markdown**, com a document separat (mai directament a la resposta del xat, perquè els editors externs solen trencar els blocs de codi en enganxar-los).
2. Es revisa el Markdown amb en Roger.
3. 🔸 Un cop validat, es passa la **validació de blocs** (§4). Si hi ha **un sol error, no es genera res**: es retorna la llista d'errors amb número de línia i s'espera correcció.
4. Amb zero errors, es genera l'**HTML** (una pàgina per capítol/subcapítol), es valida sintàcticament, i es genera un **ZIP** per importar-lo a Moodle (Book → Importa capítols).
5. Es pot importar un ZIP nou sobre un llibre existent per afegir-hi més capítols (no cal refer-lo sencer).

El CSS **no** va dins de cada pàgina: viu a la configuració CSS de la secció de Moodle. Això vol dir que qualsevol classe nova s'ha d'afegir allà **abans** d'importar contingut que la faci servir, o es veurà sense estil.

---

## 2. Sintaxi dels blocs en Markdown

### 2.1 Capçalera de personatges

Cada document comença amb un bloc de comentari que mapeja els noms d'avatar fets servir al document amb la seva URL. Els avatars disponibles són a `Personatges.md`:

```
<!-- PERSONATGES -->
<!--
cave_content:  https://cv.copernic.cat/...
albert_formal: https://cv.copernic.cat/...
lidia_formal:  https://cv.copernic.cat/...
-->
```

Regla: tot avatar usat al document ha de ser a la capçalera, i tot avatar de la capçalera s'ha de fer servir com a mínim un cop. La validació ho comprova en les dues direccions.

### 2.2 Diàleg d'un personatge (`bloc-dialeg`)

Targeta amb avatar, nom, rol i text. Tres línies de metadades, línia en blanc, i després el text lliure (pot tenir diversos paràgrafs i llistes):

````
```bloc-dialeg
avatar: cave_content
nom: Cave Johnson
rol: CEO i fundador · Aperture Science

Text del personatge, en markdown normal.
```
````

Mapeja a `.aperture-dialogue` (avatar → `aperture-dialogue-avatar`, nom → `aperture-dialogue-name`, rol → `aperture-dialogue-role`, text → `aperture-dialogue-text`).

Quan un tram de text no té personatge assignat explícitament a l'original, es decideix cas per cas si es deixa com a text de narrador pla (sense targeta) o s'assigna a algú — no s'assumeix per defecte.

### 2.3 Caixes destacades (`destacat-X`)

🔸 **Taula completa.** El nom del bloc porta el tipus, que mapeja 1 a 1 amb les variants de `.aperture-alert`. La icona és **fixa per tipus**: el conversor la posa, no s'especifica al Markdown.

| Bloc Markdown | Classe CSS | Icona (Font Awesome) | Color | Freqüència |
|---|---|---|---|---|
| `destacat-info` | `aperture-alert-info` | `fa-circle-info` | Blau cian | Habitual |
| `destacat-warning` | `aperture-alert-warning` | `fa-triangle-exclamation` | Taronja | Habitual |
| `destacat-error` | `aperture-alert-error` | `fa-circle-xmark` | Vermell | Habitual |
| `destacat-success` | `aperture-alert-success` | `fa-circle-check` | Verd | Habitual |
| `destacat-reading` | `aperture-alert-reading` | `fa-book-open` | Groc palla | Habitual |
| `destacat-video` | `aperture-alert-video` | `fa-circle-play` | Lila | Puntual |
| `destacat-ideas` | `aperture-alert-ideas` | `fa-lightbulb` | Groc idea | Puntual |
| `destacat-tools` | `aperture-alert-tools` | `fa-wrench` | Gris | Puntual |
| `destacat-audio` | `aperture-alert-audio` | `fa-headphones` | Cian fosc | **Reservat** |
| `destacat-critic` | `aperture-alert-critical` | `fa-triangle-exclamation` | Vermell ple | **Excepcional** |

Sintaxi general (contingut markdown lliure: normalment un títol en negreta + llista, o només un paràgraf):

````
```destacat-warning
- **Què s'avalua**: ...
- **Quan s'avalua**: ...
```
````

**Criteri d'ús — la regla d'or.** Amb deu variants disponibles, el risc real és que hi hagi un destacat a cada pantalla i l'alumne deixi de mirar-los. Si tot destaca, res destaca. El criteri és **obligatorietat**, no temàtica:

- `destacat-info` — informació que **cal** saber per fer la feina. Resums d'apartat, índexs, relacions entre documents.
- `destacat-warning` — avís que requereix acció o precaució: *"no facis X sense Y"*.
- `destacat-error` — recull explícit d'errors freqüents o coses que no s'han de fer. Sempre en negatiu.
- `destacat-success` — expectatives positives i criteris de "això ja està ben fet".
- `destacat-reading` — remet a un **document o enllaç extern** que cal consultar.
- `destacat-video` — remet a un vídeo.
- `destacat-ideas` — 🔸 suggeriment **opcional**: bonus, millora, *"si vas sobrat de temps"*. **Aquesta és la diferència amb `info`**: `info` és obligatori, `ideas` és opcional. Sense aquesta distinció els dos blocs es faran servir indistintament i el color deixarà de significar res.
- `destacat-tools` — programari específic que cal instal·lar o obrir per a aquesta activitat (p. ex. *"per a aquest projecte necessites Cisco Packet Tracer"*). No és per a eines d'ús diari.
- `destacat-audio` — **no usar**. Definit per a una futura transcripció en àudio de les lliçons. Si es fa servir abans que aquesta funcionalitat existeixi, la validació avisa.
- `destacat-critic` — 🔸 avís amb capçalera vermella plena, per a conseqüències acadèmiques reals (suspensos, recuperacions, terminis irrecuperables). **Màxim un per llibre.** Si n'hi ha més d'un, deixa de fer por.

**Nomenclatura històrica**: `destacat-alert` es va fer servir puntualment com a sinònim de `destacat-info` als primers llibres. Està **deprecat**: la validació el marca com a error.

### 2.4 Avís crític (`destacat-critic`)

🔸 Nou a la v2. Estructura diferent de la resta: capçalera de color ple amb títol en majúscules, i cos blanc. Porta una metadada `titol:` obligatòria:

````
```destacat-critic
titol: No entregar a temps

El termini d'entrega és tancat. Un projecte entregat fora de termini es
qualifica amb un 0 i arrossega el RA sencer a recuperació extraordinària.
```
````

Genera `.aperture-alert-critical` amb `-header` (títol + icona) i `-body` (contingut).

**Regla de to** (ja aplicada, no repetir l'error): en Cave Johnson no s'utilitza per a contingut seriós amb conseqüències reals per a l'alumne. Per a això, la Lídia (`lidia_seriosa`) o un `destacat-critic` sense personatge.

### 2.5 Correu electrònic (`bloc-correu`)

🔸 Nou a la v2. El CSS ja existia (`.aperture-email` i companyia) però no tenia sintaxi Markdown assignada. És la peça per a exemples de comunicació amb el client, que és contingut central del mòdul.

````
```bloc-correu
avatar: albert_formal
de: Albert Serrano <albert.serrano@apertureholistics.cat>
per: Marc García <marc@technoplay.cat>
data: 14 d'octubre de 2026, 09:12
assumpte: Confirmació de la reunió inicial — ref. 26-000

Bon dia, Marc,

Text del correu en markdown normal.
```
````

Variant per a **contramostres** (com **no** s'ha d'escriure un correu): afegir la metadada `estil: incorrecte`, que aplica `.aperture-email--incorrecte` i pinta la vora i l'assumpte en vermell.

Les etiquetes visuals "CORRECTE" / "INCORRECTE" (`.aperture-email-label`) s'afegeixen automàticament quan hi ha `estil:`; si no hi ha `estil:`, no surt etiqueta.

### 2.6 Llista de passos numerats (`bloc-passos`)

🔸 Nou a la v2. El CSS ja existia (`.aperture-parts-list`, numeració automàtica en cercle cian) sense sintaxi documentada. És una llista Markdown normal dins del bloc; el primer fragment en **negreta** de cada element es converteix en títol del pas:

````
```bloc-passos
- **Capçalera**: qui envia, qui rep i de què va.
- **Salutació**: pel nom, sense excés de confiança.
- **Cos**: una idea per paràgraf.
```
````

Ús: descomposició d'un artefacte en parts, o procediment de 3–7 passos. Per a més de 7 passos, val més una taula o un subcapítol.

### 2.7 Botons (`bloc-boto`)

🔸 Nou a la v2.

**Regla tècnica innegociable**: un botó és sempre un enllaç `<a class="aperture-btn">`, **mai** un `<button>`. Dins d'un Book de Moodle un `<button>` no fa absolutament res (no hi ha JavaScript) i, a més, el purificador pot eliminar-lo. Qualsevol botó ha d'apuntar a una URL: una plantilla de Drive, una activitat de Moodle, un recurs extern.

````
```bloc-boto
text: Descarrega la plantilla de pressupost
url: https://docs.google.com/spreadsheets/d/.../copy
icona: fa-link
estil: primari
```
````

- `text` — obligatori. Curt i en imperatiu: què passa si hi clico.
- `url` — obligatòria.
- `icona` — opcional. Nom Font Awesome sense prefix.
- `estil` — opcional: `primari` (cian, acció principal), `secundari` (taronja, acció alternativa), `contorn` (buit, acció terciària). Per defecte `primari`.

**Criteri d'ús**: un botó és per a **l'acció principal d'una pàgina**. Si en poses tres seguits, ja no n'hi ha cap de principal. Per a llistes d'enllaços, `bloc-recursos` (§2.8).

Per a enllaços de Google Drive apuntant a plantilles, fer servir sempre l'URL acabada en `/copy` (força l'alumne a fer-se'n una còpia en comptes d'editar l'original).

### 2.8 Llista de recursos (`bloc-recursos`)

🔸 Nou a la v2. El CSS ja existia (`.aperture-resources` / `.aperture-resource-link`) sense documentar. Enllaços compactes amb icona que flueixen horitzontalment i salten de línia sols.

````
```bloc-recursos
- Document de requisits | https://docs.google.com/... | fa-file-lines
- Convocatòria de reunió | https://docs.google.com/... | fa-calendar-day
- Acta de reunió | https://docs.google.com/... | fa-file-pen
```
````

Format de cada línia: `text | url | icona` (la icona és opcional; per defecte `fa-arrow-right`).

**Aquesta és la peça per a les plantilles de documents**, no les targetes. Criteri acordat: cada plantilla es presenta **al capítol de la fase que la necessita**, en grups de 3–5, no en un índex global. L'índex global de plantilles existeix a part com a taula de referència (§2.10), sobretot per al professorat.

### 2.9 Targetes (`bloc-targeta`)

🔸 Nou a la v2.

````
```bloc-targeta
icona: fa-shield-halved
titol: Verificació tècnica
estil: primari

Text descriptiu breu, 1-3 línies. Explica què és o què s'hi fa.
```
````

- `estil` — 🔸 `primari` (cian) o `secundari` (taronja). Els colors corporatius d'Aperture, portal blau i portal taronja. **No fer servir els noms antics `blue` / `orange`**: són presentacionals i queden obsolets el dia que canviï la paleta.

**Agrupació automàtica**: dues o més `bloc-targeta` **consecutives** (només amb línies en blanc entremig) s'agrupen dins un `.aperture-grid`, que reparteix les columnes sol segons l'amplada. No cal sintaxi d'obertura ni tancament de graella. Una targeta sola també és vàlida i surt a amplada completa.

**Criteri d'ús**: 2–6 targetes, quan cada element necessita una explicació pròpia. Per a més de 6, és una taula o una llista de recursos. Les targetes són cares en vertical: cadascuna ocupa el que ocuparien quatre línies de text.

### 2.10 Desplegable (`bloc-desplegable`)

🔸 Nou a la v2. ⚠️ **Pendent de prova**: fa servir `<details>` / `<summary>`, HTML pur sense JavaScript. Cal comprovar amb una importació real que el purificador de Moodle no els elimini **abans** de fer-lo servir en producció.

````
```bloc-desplegable
titol: Plantilles de la fase d'oferta

Contingut markdown lliure, pot contenir altres blocs.
```
````

Ús previst: índex de plantilles per fases, on l'alumne només obre la fase on és. Si la prova de Moodle falla, l'alternativa és un subcapítol per fase.

### 2.11 Encapçalats dins d'una mateixa pàgina (`####`)

Quan un document Markdown té una jerarquia de 3 nivells (capítol → subcapítol → sub-secció), i el subcapítol ja genera la seva pròpia pàgina HTML, la sub-secció **no** es converteix en un altre fitxer (Moodle Book només admet 2 nivells). Es fa servir `####`: és només un encapçalat visual (`<h3>` dins la pàgina), no crea fitxer ni trenca la numeració `01sub_N_`.

```
### Subcapítol 2. Preparar una reunió
... contingut ...
#### Com és un ordre del dia
... contingut que es queda a la mateixa pàgina ...
```

### 2.12 Taules

Taules Markdown normals (`| ... | ... |`). Es converteixen a `<table class="aperture-table">`.

🔸 **Canvi de nom**: el modificador que neutralitza el pintat automàtic de columnes passa de `aperture-table--rubrica` a **`aperture-table--neutra`**. El nom antic es manté com a àlies durant la transició i s'esborrarà del CSS quan els documents ja convertits estiguin actualitzats.

**Compte**: `.aperture-table` per defecte pinta la primera columna de verd i l'última de vermell. Això només té sentit en taules literals de dues columnes correcte/incorrecte. Per a **qualsevol altra taula** cal `aperture-table--neutra`. La validació avisa quan troba una taula de 3 o més columnes sense el modificador.

Per a rúbriques amb fila de punts sota cada criteri, la fila de punts porta `aperture-table-punts`.

### 2.13 Codi

- **Codi en línia**: comes invertides simples de Markdown → `<code class="aperture-code">`.
- **Bloc de codi**: fence ``` normal (sense nom de bloc) → `<pre class="aperture-code-block">`. Opcionalment amb el llenguatge després del fence, que es mostra a la capçalera del bloc.

El botó "copia" del prototip **no s'implementa**: necessita JavaScript i no funcionaria dins d'un Book.

---

## 3. Components descartats

🔸 Decisió explícita, perquè no es tornin a plantejar:

| Component del prototip | Estat | Motiu |
|---|---|---|
| `aperture-quiz` | **Descartat** | Necessita JavaScript. L'autoavaluació es fa amb el mòdul Qüestionari de Moodle. |
| `aperture-progress` | **Descartat** | El progrés el porta Moodle (seguiment de finalització). Duplicar-lo és mentir a l'alumne. |
| `aperture-content-block` (read/configure/install) | **Descartat** | Se solapa completament amb `destacat-reading`, `destacat-tools` i `destacat-info`. Tenir dos sistemes de caixes de colors és garantia d'incoherència. |
| `aperture-code-block-copy` | **Descartat** | Necessita JavaScript. |

---

## 4. Validació abans de convertir

🔸 Nou a la v2. **El conversor no genera cap HTML si troba errors.** Fa una passada de comprovació, i o bé retorna "0 errors" i converteix, o bé retorna la llista completa amb número de línia i s'atura. Res de generar HTML amb classes inexistents en silenci.

### Errors (aturen la conversió)

1. Nom de bloc desconegut. Inclou explícitament els errors típics: `destacat-idea` (singular), `destacat-alert` (deprecat), `destacat-tool`, `bloc-dialogue`, `destacat-informacio`.
2. `bloc-dialeg` sense `avatar:`, `nom:` o `rol:`, o sense línia en blanc abans del text.
3. Avatar referenciat que no és a la capçalera `<!-- PERSONATGES -->`.
4. Avatar a la capçalera sense URL, o amb URL buida.
5. `bloc-boto` sense `text:` o sense `url:`.
6. `bloc-boto` amb `estil:` diferent de `primari` / `secundari` / `contorn`.
7. `bloc-targeta` sense `titol:`.
8. `destacat-critic` sense `titol:`.
9. `bloc-correu` sense `de:`, `per:` o `assumpte:`.
10. `bloc-recursos` amb una línia sense `|` o amb URL buida.
11. Fence obert i no tancat.
12. Enllaç Markdown amb destinació buida `[text]()`.
13. `####` sense un `###` previ a la mateixa pàgina.

### Avisos (no aturen, però surten al report)

1. Taula de 3 o més columnes sense `aperture-table--neutra`.
2. Ús de `destacat-audio` (reservat).
3. Més d'un `destacat-critic` al mateix llibre.
4. Tres o més `bloc-boto` a la mateixa pàgina.
5. Més de 6 `bloc-targeta` consecutives.
6. Avatar declarat a la capçalera i no usat.
7. Enllaç a Google Drive/Docs que **no** acaba en `/copy`.
8. Ús de `cave_*` dins d'un `destacat-critic` o en un context de conseqüències acadèmiques.

### Format del report

```
VALIDACIÓ: llibre_oferta.md
  ERROR   línia 142  Bloc desconegut: 'destacat-idea' (volies dir 'destacat-ideas'?)
  ERROR   línia 388  bloc-boto sense 'url:'
  AVÍS    línia  57  Taula de 4 columnes sense aperture-table--neutra
  AVÍS    línia 201  Enllaç de Drive sense /copy

2 errors, 2 avisos → NO es genera HTML.
```

---

## 5. CSS a fusionar a `Aperture.css` mestre

🔸 Tot el CSS d'aquesta secció està **scoped** dins `.aperture-tutorial-wrap`. Al prototip `Prova_css_tutorial.html` no ho estava: copiar-lo tal qual faria que `.aperture-card` i `.aperture-btn` s'apliquessin a tot Moodle i xoquessin amb el tema Boost.

El bloc complet, llest per enganxar, és al fitxer **`Aperture_v2_afegits.css`** que acompanya aquest document. Resum del que inclou:

- Token que faltava: `--aperture-button-min-height: 44px` (mida mínima tàctil accessible).
- Variants d'alerta que faltaven al mestre: `ideas`, `tools`, `audio`. Els tokens `--aperture-color-ideas` i `--aperture-color-audio` ja hi eren al mestre però **orfes**, sense cap regla que els fes servir.
- Peces que faltaven de l'alerta crítica: `-header-content` i el color de la icona.
- Família `aperture-btn` completa.
- `aperture-card` + `aperture-grid`, amb `--primari` / `--secundari` en comptes de `-blue` / `-orange`.
- `aperture-code` en línia i `aperture-code-block` simplificat.
- `aperture-desplegable` (`<details>`).
- `aperture-table--neutra` + àlies temporal de `--rubrica`.
- Regles responsive per a les peces noves.

---

## 6. Avatars

| Identificador | Ús |
|---|---|
| `cave_content` | Cave Johnson, to efusiu/normal |
| `cave_formal` | Cave Johnson, to més seriós (no usat encara) |
| `albert_formal` | Albert, explicació estàndard |
| `albert_content` | Albert, valoració positiva (no usat encara) |
| `lidia_formal` | Lídia, explicació estàndard |
| `lidia_seriosa` | Lídia, avís seriós |

La resta (`albert_serios`, `albert_cansat`, `lidia_contenta`, `lidia_treballant`, `manel_formal`, `manel_content`) són a `Personatges.md` però encara no s'han fet servir.

---

## 7. Nomenclatura de fitxers per a la importació Moodle

L'eina `booktool_importhtml` detecta subcapítols pel prefix `sub` al nom de fitxer, i ordena alfabèticament:

```
01_nom_del_capitol.html
01sub_1_nom_subcapitol.html
01sub_2_nom_subcapitol.html
```

Si un llibre té diversos capítols, el número inicial (`01`, `02`...) identifica el capítol, i tots els seus subcapítols porten el mateix prefix + `sub_N_`.

---

## 8. Referències externes

Quan un tutorial necessita un enllaç extern de referència ("Saber-ne més"), es prioritza contingut en català. En absència de fonts en català sense publicitat (comuna en aquest tipus de contingut, sovint de coworkings o consultories), s'accepten fonts comercials en català sempre que el contingut de fons sigui rellevant i correcte — s'ha comprovat el contingut abans d'enllaçar-lo, no només el títol.

---

## 9. Estat actual de la producció

- **Llibre 1** (Benvinguda al curs): fet, importat i validat visualment a Moodle. Icones Font Awesome **confirmades funcionant**.
- **Llibre 2** (Com serà la nota del mòdul): fet, 2 capítols. Calendari de fites corregit (setmana 4 = reunió de seguiment; setmana 5 = verificació tècnica + auditoria interna + entrega; setmana 6 = presentació + examen).
- **Llibre 4** (Com es fa servir aquest Moodle): fet, ZIP generat, pendent d'importació.
- **Llibre 3** (tutorials de competències transversals): en curs. Fets: "Com preparar i portar una reunió" i el tutorial de l'oferta.
- La resta de material és pendent de conversió, cosa que fa que el cost dels canvis d'aquesta v2 sigui baix.

### Pendents oberts d'aquesta versió

1. ⚠️ **Provar `<details>` a Moodle** abans de fer servir `bloc-desplegable` en producció.
2. Actualitzar `aperture-table--rubrica` → `--neutra` als documents ja convertits, i després esborrar l'àlies del CSS.
3. Implementar la passada de validació (§4) al conversor Python.
