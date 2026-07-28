
# Guia d'estil d'Aperture Holistics Consulting (capítol)

> **Què és aquest llibre.** No és un tutorial de "com fer" una oferta o una presentació — això ja ho tens als tutorials de cada tema. Aquest és el **manual de normes** que Aperture exigeix a tots els projectes, sigui quina sigui la tecnologia. Es consulta, no es "segueix pas a pas": obriu el capítol que us calgui quan el necessiteu.
>
> **Per què importa de veritat.** Cada capítol es correspon directament amb un punt de l'auditoria interna que us puntua a RA4. No són "bones maneres" opcionals: si no ho compliu, hi ha una casella concreta de la rúbrica que ho reflecteix.

```destacat-warning
- **Què s'audita d'aquesta guia**: organització de carpetes, nomenclatura d'arxius i versions, documentació de referències (web, IA), ús de la IA.
- **Quan**: auditoria interna a final de cada projecte (setmana 5).
- **Qui ho revisa**: el professor, amb el checklist de l'annex de seguiment.
```
```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics
```

```bloc-vídeo
Aquest bloc d'informació és fonamental dins del curs. Haureu de venir molts cops a refrescar la vostra memòria i a seguir el que s'hi explica. Us deixem un vídeo general perquè pugueu consultar en qualsevol moment.

<!-- Placeholder per a vídeo de resum -->
```

---

## Capítol 1. Organització del projecte (capítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

Un projecte a Aperture pot durar setmanes i passar per diverses mans. Si no hi ha ordre, ningú —ni vosaltres mateixos d'aquí a un mes— sabrà trobar res. L'ordre no és estètica, és temps que estalvieu.
```
### 1.1 El món professional no és un enunciat de classe (subcapítol)

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Consultor sènior · Mentor de l'equip júnior

Al món real, les coses no són mai ideals. Passen coses i no sempre bones. Cap projecte acaba com s'esperava. A l'institut un projecte és un enunciat i sempre comença i sempre acaba bé.

Tot el que se us demana que compliu aquí, no és ni un caprici ni una exageració. El desordre i la manca de responsabilitat costen diners i llocs de feina. Els projectes són d'Aperture i no dels consultors que hi treballen. Els projectes de l'institut són dels estudiants. 

Tot el que s'exposa a continuació és una necessitat empresarial. Qualsevol treballador ha de poder entrar a un projecte i treballar immediatament. No pot perdre temps mirant "com va tot". L'ordre i la documentació no són per vosaltres: són perquè qualsevol altra persona pugui agafar el que heu deixat i continuar sense haver-vos de trucar.
```

```destacat-alert
- Allò d'"El temps és or", a les empreses s'ho prenen seriosament. Perdre temps és perdre diners.
- La responsabilitat i l'organització són fonamentals dins de l'entorn laboral. No us ho prengueu a broma.
```

### 1.2 Estructura de carpetes (subcapítol)

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Consultor sènior · Mentor de l'equip júnior

Feu servir sempre aquesta estructura de base. Adapteu-la si el projecte ho demana, però no us en allunyeu sense motiu:

📁 **01_DOCUMENTACIO_CLIENT**
- Tot el que us dona el client: plec, correus, especificacions.
- **Només lectura.** No es modifica mai. Si necessiteu anotar-hi res, copieu-ho a una altra carpeta.

📁 **02_OFERTA**
- Tota la documentació de l'oferta: anàlisi, disseny, pressupost, memòria.
- Versions intermèdies (`_v01`, `_v02`...) + una versió `FINAL`.
- Un cop aprovada, es posa en només lectura.

📁 **03_PROJECTE**
- La implementació: tot el que treballeu per entregar al client.
- Subcarpetes a mida (configuracions, proves, documentació tècnica).

📁 **04_QUALITAT_SEGUIMENT**
- Checklists de qualitat i protocols de proves.
- Actes de reunions i seguiment amb el client.
- Garanties i fitxes tècniques de qualsevol material comprat.

📁 **05_ENTREGUES_CLIENT**
- **Aquí es clona exactament tot el que lliureu al client**, organitzat per data (`Entrega_01_Setmana_4_Oferta/`).
- Motiu: si el client diu que el document té un error, heu de poder veure exactament què li vau donar.
```

```destacat-info
- **Regles generals de carpetes**
- Màxim 3 nivells de profunditat. Si en necessiteu més, repenseu l'estructura.
- No es llença res: creeu una carpeta `OLD` per als arxius antics.
- Un o dos dígits davant del nom ordena per número, no per alfabet.
```

### 1.3 Nomenclatura d'arxius i versions (subcapítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

Un nom d'arxiu ha de dir-li a qualsevol persona de l'empresa què hi ha dins sense obrir-lo. El projecte el fa Aperture, no els components del grup. Qualsevol ha de poder entrar a un projecte en qualsevol moment.
```

| Correcte | Incorrecte | Per què |
|---|---|---|
| `Memoria_tecnica_v01.docx` | `Document1.docx` | El nom no diu res del contingut |
| `Pressupost_FINAL_v02.xlsx` | `Pressupost final 2.xlsx` | Espais i sense versió clara |
| `Ping_Gaming_Servidors.png` | `Captura1.png` | Cap pista del contingut |

- Cada canvi important és una versió nova (`_v01`, `_v02`...). La versió final es marca `FINAL`.
- Data en format `AAAAMMDD-nom.arxiu` només si us interessa que els més recents quedin a dalt.
- Si un client demana canvis sobre alguna cosa que li has entregat, fas una nova versió del document.

```destacat-warning
- **Format d'entrega al client**: sempre PDF, excepte si el projecte necessita un format natiu (.xlsx, .pkt) o el client el demana expressament.
- Internament podeu treballar amb .docx, però cloneu a PDF per entregar.
- Un cop un document arriba al client, ja no es toca més.
```

---

## Capítol 2. Estàndards de documentació escrita (capítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

Els projectes no són només el que feu tècnicament. També s'han de presentar correctament. Si la teva feina no s'entén, és com si no la fessis. Si presentes la teva feina malament, el client pensa què més deus estar fent malament.

La presentació és gairebé tan important com el que fas.
```

### 2.1 Aspectes formals (subcapítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

Un document mal escrit no és un detall estètic: és el que el client veu de vosaltres. Aquests són els mínims que revisem abans que surti res de l'empresa.
```
#### Format i presentació 

- Plantilla corporativa d'Aperture sempre.
- Índex a partir de 5 pàgines, amb numeració de seccions coherent.
- Tipografia professional (Arial 11-12pt, interlineat 1,15), sense mesclar fonts.
- Totes les pàgines numerades, excepte la portada.
- Imatges amb resolució adequada, peu de figura i referenciades al text ("veure Figura 3.2").

#### Contingut i estructura

- Estructura lògica: introducció → desenvolupament → conclusions.
- Paràgrafs curts (màxim 10 línies). Sense divagacions.
- Terminologia consistent i unitats sempre especificades (Mbps, GB, m, €...).
- Nombres amb format correcte (1.234,56). Sense ambigüitats ("alguns", "bastants" → digueu quants).
- Les decisions importants s'expliquen: per què X i no Y.
- Cap secció "pendent" o "TBD" en el document final.

#### Correcció lingüística

- Corrector ortogràfic **obligatori** abans d'entregar res.
- Concordances i puntuació correctes. Cap frase a mig escriure.
- Registre formal: sense col·loquialismes.

#### Referències i ús de la IA

```destacat-warning
- **Això és el que us audita directament la rúbrica RA4.**
- Tota font externa (normativa, manual, web) es cita. Parafrasegeu, no copieu.
- Si feu servir NotebookLM o qualsevol IA generativa, ho documenteu: què heu generat i com ho heu revisat i adaptat.
- Un bon ús de la IA és fer-la servir per aprendre o accelerar una tasca ja entesa. Un mal ús és entregar contingut generat sense haver-lo revisat ni entès.
```

#### Taules i dades

- Capçaleres clares, alineació consistent (números a la dreta, text a l'esquerra).
- Unitats sempre especificades. Totals calculats correctament (no escrits a mà).
- Gràfics amb eixos etiquetats, llegenda si cal, i colors diferenciables (eviteu vermell/verd junts).

### 2.2 Abans d'entregar (subcapítol)

```destacat-info
- **Checklist mínim**
- Corrector ortogràfic passat.
- Cap paràgraf a mig escriure ni secció "pendent".
- Totes les xifres i totals verificats a mà.
- Format PDF per al client (natiu només si cal).
```

---

## Capítol 3. Estàndards de pressupost (capítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

El pressupost és el document que el client mirarà més vegades. Un error aquí costa diners de veritat, encara que sigui una simulació.
```

### 3.1 Estructura (subcapítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

El pressupost necessita ser un document que generi poques preguntes. La seva organització és clau. Un pressupost mal fet o que no s'entén, fa que el projecte vagi malament, i gairebé sempre, acabem perdent o diners o el client. 

- **Capçalera**: nom del projecte, client, data, versió i validesa.
- **Taula principal**: concepte (agrupat per tipus), unitats, preu unitari, subtotal (sempre fórmula, mai valor escrit a mà).
- Les seccions concretes depenen del projecte. Alguns exemples habituals:

| Tipus de projecte | Seccions típiques de pressupost |
|---|---|
| Xarxes / infraestructura | Equipament de xarxa, cablejat i infraestructura passiva |
| Maquinari / estacions de treball | Maquinari, perifèrics, llicències de programari |
| Serveis (ofimàtica, formació...) | Hores de servei, llicències, material fungible |
| Tots els projectes | Serveis i mà d'obra, gestió del projecte |

```

```destacat-info
- **No copieu aquesta taula tal qual: és orientativa**. Cada projecte defineix les seves pròpies seccions segons què es lliura. El que no canvia és que **tot concepte ha d'anar agrupat per tipus i portar un subtotal**.
```

### 3.2 Contingut (subcapítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

Respecteu la plantilla i l'ordre de les columnes. Seguiu aquestes instruccions i reviseu el pressupost.

- Cada secció té un subtotal, i sense descomptes, el mateix import va al total.
- Descomptes o aclariments breus a la columna de notes; si l'explicació és un paràgraf sencer, va a la proposta tècnica, no al pressupost.
- Tots els subtotals es resumeixen al final del pressupost, i aquest resum es copia també al resum executiu de la proposta tècnica.
- Total del projecte sense impostos, IVA, i total amb impostos.
- Condicions comercials sempre presents: forma de pagament, termini d'execució, garantia.
```

### 3.3 Validacions al full de càlcul (subcapítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

El pressupost és un contracte. L'import final és el que costarà. Si el feu malament i les fórmules o els imports estan mal posats, podeu fer que el projecte sigui refusat per massa car, o que el projecte li surti molt millor de preu al client, posant Aperture els diners que no cobrarem. I això no és bo.

- Unitats: només números enters > 0.
- Preu unitari: només números > 0.
- Descompte: només 0-100%.
- Format moneda automàtic (€, 2 decimals).
- Subtotals amb fórmules protegides, no editables.

```

### 3.4 Format i estil (subcapítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

**No formateu el full al vostre gust.** Ha d'arribar al client amb la imatge d'Aperture, no la vostra.


- Files alternades (zebra) un cop el pressupost estigui complet.
- Subtotals en negreta.
- Columnes de moneda justificades a la dreta.
```

#### Generació del PDF

1. Reviseu tots els càlculs abans de tancar el document.
2. Exporteu a PDF: orientació horitzontal, escala ajustada a 1 pàgina d'ample, graella de cel·les oculta, marges normals.
3. Bloquegeu la fila de capçalera perquè surti a totes les pàgines. Afegiu números de pàgina.
4. Salts de pàgina forçats: cada bloc de conceptes comença a pàgina nova; el resum final va sol en una única pàgina.


### 3.5 Errors habituals a evitar (subcapítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

Per tancar l'apartat del pressupost, insistiré amb la importància que un pressupost sigui correcte, clar i detallat. 

- Desglossament insuficient ("PCs gaming: 50.000 €" sense detall).
- Unitats mal calculades (comproveu sempre preu unitari × unitats = subtotal).
- Fórmules trencades per edició manual.
- Pressupost sense condicions comercials.
- Sempre heu de revisar el pressupost abans de generar el PDF. 

```
---

## Capítol 4. Estàndards de presentació al client (capítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

Podeu tenir el millor projecte tècnic del món: si la presentació falla, el client se n'emporta el dubte, no la confiança.
```

### 4.1 Abans de la reunió (subcapítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

Les reunions amb els clients són tan importants com la feina de consultoria que feu al despatx. La comunicació és fonamental. La imatge de professionalitat dona al client confiança en el bon treball. Una mala imatge genera desconfiança sobre la vostra feina.

- Repasseu tots els documents (canvieu-vos els documents entre vosaltres per tenir una mirada nova).
- Valideu el pressupost: totes les fórmules, càlculs i IVA correctes.
- Comproveu enllaços i referències creuades entre documents.

**Material preparat:**
- PDFs: memòria tècnica, pressupost, topologies/plànols.
- Presentació (PowerPoint/Slides), màxim 10-15 diapositives.
- Còpia local de tot (per si falla la connexió), i també al núvol.

**Assaig:**
- Assaig complet amb cronòmetre.
- Repartiment clar de qui presenta cada part.
- Preguntes previsibles preparades.
- Tot l'equip coneix el contingut, no només qui presenta.
- A la reunió de debò: sense notes ni papers.
```

### 4.2 Durant la presentació (subcapítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

A la reunió, heu de donar imatge de seguretat i que sabeu què esteu fent.

- **Llenguatge corporal:** postura oberta (sense braços creuats ni mans a les butxaques), contacte visual amb tots els assistents, actitud natural.
- **Veu:** to clar i audible, ritme pausat, vocabulari tècnic però entenedor, sense "ehhh" ni "en plan" constants.

**Estructura de la reunió:**

| Fase | Durada | Contingut |
|---|---|---|
| Introducció | 1-2 min | Salutació, presentació de l'equip, estructura de la reunió |
| Desenvolupament | ~10 min | Ordre assajat, suports visuals, contacte amb l'audiència, justificació de decisions |
| Tancament | 2-3 min | Punts forts, beneficis clau, propers passos |
| Preguntes | 5-10 min | Escoltar tota la pregunta, no interrompre companys, "ho consultarem" si cal |

```

### 4.3 Després de la presentació (subcapítol)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans · Aperture Holistics

Les reunions no acaben quan marxes del client. Us emporteu feina d'elles. 

Envieu un correu de seguiment. Plantilla:
```

```destacat-info
**Assumpte:** Seguiment presentació oferta – [Nom del projecte]

Benvolguts/des,

Moltes gràcies per la reunió d'avui i pel vostre temps. Ha estat un plaer presentar-vos la nostra proposta per a [nom del projecte].

Tal com hem comentat, us adjuntem novament la documentació en format digital:
- Memòria tècnica (PDF)
- Pressupost desglossat (PDF + Excel)
- [Altres documents específics del projecte: plànols, topologies...]

Sobre les qüestions pendents d'aclariment durant la reunió:
- [Pregunta 1]: [Resposta]
- [Comentari]: [Resposta]

Quedem a la vostra disposició per a qualsevol altre aclariment.

Atentament,
[Nom equip] · Aperture Holistics Consulting
```

### 4.4 Errors fatals (a evitar sempre) (subcapítol)

- Arribar tard, o portar equipament que no funciona.
- Llegir el text de les diapositives o d'una nota.
- Discussions internes o contradiccions entre membres de l'equip davant del client.
- No saber respondre preguntes bàsiques del propi projecte.
- Menystenir comentaris del client, o respondre-hi agressivament.

---

## Capítol 5. Previsió i seguretat (capítol)

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Consultor sènior · Mentor de l'equip júnior

He vist grups perdre una setmana de feina el dia abans d'entregar. No per mala tècnica: per no tenir còpia de res. Això no es recupera amb una bona excusa.
```

```destacat-warning
- **Regla mínima, sense excepcions**: abans de cada entrega, verifiqueu que teniu una còpia del que lliureu en un lloc diferent d'on treballeu (per exemple: treballeu a Drive → guardeu una còpia local, o a l'inrevés).
- **Quan es comprova**: en cada checkpoint de seguiment, el professor pot demanar-vos que mostreu on teniu la còpia.
```

- No confieu que "ja ho teniu tot a Drive": un compte bloquejat, un arxiu esborrat per error o un permís mal donat us pot deixar sense res el dia de l'entrega.
- Les entregues al client (carpeta `05_ENTREGUES_CLIENT`, capítol 1) han de poder-se reproduir sempre: si el client diu "el document que em vau donar té un error", heu de poder obrir exactament aquell arxiu, no una versió posterior.