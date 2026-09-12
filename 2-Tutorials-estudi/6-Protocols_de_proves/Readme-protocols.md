## ELS PROTOCOLS DE PROVES

```destacat-info
Què aprendreu a fer en aquest tutorial

- Per què s'han de provar les coses
- Què és un protocol de proves i com redactar-los
- Com fer les proves i recollir les evidències que demostren que el que fem funciona

**El protocol de proves són uns documents que defineixen, pas a pas, les instruccions i les dades d'entrada necessàries que serveixen per verificar que la resposta a aquestes entrades és la sortida que s'espera del projecte.**

```

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Durant tot el procés previ al muntatge del projecte, hem d'anar pensant què farem per demostrar que el que estem fent funciona correctament i el disseny que hem pensat compleix els requisits de l'oferta al client.
```

```destacat-video
No tens temps o no vols llegir el tutorial? Aquí tens un resum en vídeo que et donarà els conceptes principals. Però et recomanem que si pots, facis les dues coses.

[placeholder per a vídeo]

```

---

### CARACTERÍSTIQUES DELS PROTOCOLS

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Els protocols que feu han de tenir unes característiques molt concretes per tal que facin la seva feina:

- **Repetibilitat**. Un protocol de proves ha de garantir la repetibilitat. Permet que qualsevol persona seguint el protocol, repeteixi la mateixa prova de la mateixa manera i ha de poder obtenir el mateix resultat.
- **Objectivitat**. El protocol ha de donar una imatge real de l'estat del que prova, i tothom ha d'estar d'acord amb aquesta imatge. Nosaltres i el client. També serveix per donar transparència.
- **Traçabilitat**. Els protocols serveixen per crear un registre d'errades o incidents, i poder seguir la pista d'un error fins al seu origen.

De vegades és tan senzill com endollar i veure que engega, i altres cops necessita que es compleixin una sèrie de condicions prèvies per tal de poder arribar a demostrar que el que hem construït funciona.
```

---

### ESTRUCTURA D'UN PROTOCOL DE PROVES

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Un protocol de proves té una estructura definida per:

1. **Què volem demostrar**. Han de ser accions concretes. No val "funciona bé" o "no falla res". Per exemple:

   - Que els ordinadors d'una xarxa informàtica es veuen entre ells.
   - Que la pàgina web té els colors que ha demanat el client.
   - Que els usuaris d'un perfil concret no tenen accés a les carpetes més restringides del servidor.

2. **Com ho podem demostrar**. Aquesta és la part que té més dificultat en generar. Hem d'esbrinar un procediment per complir amb les característiques anteriors de repetibilitat, objectivitat i traçabilitat. La demostració ha de complir amb aquestes propietats:

    - Condicions inicials clares.
    - Estructura de passos per a aconseguir el resultat buscat.
    - Resultats esperats i condicions d'error.


| Prova | Xarxes | Web | Servidor |
| - | - | - | - |
| Condicions inicials clares | Els dos ordinadors i la xarxa estan encesos i interconnectats. | La pàgina web està visible a pantalla. | Tenim l'ordinador client i el servidor encesos, els perfils d'usuaris definits i la pantalla de login encesa al client. |
| Estructura de passos per a aconseguir el resultat buscat. | Obrir un terminal a un dels ordinadors i fer un ping a l'adreça de l'altre ordinador. | Obrir un selector de color al navegador i agafar el color que volem consultar. | S'ha de posar un usuari que no pot accedir a les carpetes del servidor i sol·licitar accés. |
| Resultats esperats i condicions d'error. | Que els paquets enviats es reben a l'altra banda. Si no es reben, és un error. | Que el color de pantalla és el que demanava el client. Si no ho és, és un error. | El servidor denega l'accés a les carpetes dient que l'usuari no té permisos. Si el deixa passar, és un error.|

enllacos:
- Guia d'estil d'Aperture | https://cv.copernic.cat/mod/book/view.php?id=23462 | fa-link

```

---

## EVIDÈNCIA I VERIFICACIÓ DELS RESULTATS

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Tots els protocols de proves que passem al projecte (unitaris, integració i acceptació) proporcionen un resultat que hem de verificar si és o no l'esperat, i documentar les evidències que certifiquen el que ha passat.

   - Si la prova realitzada dona el resultat que esperem, la prova és un encert i hem fet bé la feina.

     - Hem de recollir una evidència de l'èxit de la prova. De vegades una captura de pantalla és suficient, altres cops pot ser un missatge en un arxiu de log, o una lectura d'un aparell de mesura.
   - Si la prova realitzada no dona el resultat que esperem, la prova falla i hem d'esbrinar què ha passat. Com estem seguint el diagrama en V, és tan fàcil com anar cap enrere en el procés i veure on tenim l'errada.

     - És una errada d'implementació? Hi ha quelcom que no està ben muntat?
     - És una errada de disseny? El que hem fet no proporciona el resultat esperat.

   - Tant si ha anat bé com malament, es registren els resultats, es busca on ha fallat el projecte, es rectifica, es documenta el canvi (MOLT IMPORTANT!), es torna a passar el protocol i es mira el resultat.

```

---

### TRAÇABILITAT 

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Recursos Humans i Qualitat · Aperture Holistics Consulting

Tan important és fer tots els protocols de proves, com documentar per requisit quins protocols s'han passat, quins no i quin resultat heu obtingut. És la peça que us permetrà seguir la pista de les errades que podeu trobar

Per controlar-ho, ompliu la taula de traçabilitat abans de començar a provar res:
 
| Requisit | Proves unitàries | Proves d'integració | Prova d'acceptació |
| - | - | - | - |
| R1 | | | |
| R2 | | | |
| R3 | | | |
 
Els forats d'aquesta taula són el primer que mirarem quan reviseu el projecte.

```

```destacat-info
Pot semblar que us passareu tot el dia fent papers, però la realitat és que per la mida dels projectes que fem, aquestes llistes seran petites i segurament vosaltres les dureu al cap.

La complexitat dels procediments de proves de sistemes grans fan que aquestes taules siguin de molt d'ajut quan hi ha milers de proves unitàries, i els procediments de proves triguen mesos a superar-se.
```

---

### QUANTES PROVES NECESSITEU 
 
```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Quantes proves necessitareu? És la pregunta que us fareu tot seguit, i té resposta.
 
| Nivell | Quantes | D'on surten |
| - | - | - |
| Unitàries | Una per cada peça que munteu o configureu | De la llista de material i de configuracions del disseny |
| Integració | Una per cada connexió del vostre esquema | De les línies de l'esquema de disseny |
| Acceptació | **Com a mínim una per cada requisit de l'oferta** | De la columna «com ho comprovarem» del document de requisits |
 
La regla dura és l'última: **cap requisit no es pot quedar sense prova d'acceptació.** Si un requisit no té prova, o us n'heu oblidat o el requisit sobrava.
``` 

---


## PROVES UNITÀRIES 

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Les proves unitàries tenen l'objectiu de verificar i documentar que tots els elements físics i lògics del sistema que hem muntat funcionen correctament. Evita que el sistema doni una errada causada per un mal funcionament aliè al vostre disseny.
```

---

### PROVES UNITÀRIES DE COMPONENTS 

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Quan feu un protocol de proves unitàries per a components, aquest sol ser una llista de checks OK / NO de comprovacions per a cada característica del mateix.

   - Comproveu que tots els aparells elèctrics encenen quan els apliques alimentació elèctrica.
   - Si tenen firmware, verifiqueu que està actualitzat i que és compatible amb l'entorn en el que l'heu instal·lat (placa base, BIOS/UEFI, voltatge de companyia)
   - Reviseu que teniu la documentació dels elements actualitzada i la garantia vàlida. Si un component acabat de comprar es fa malbé, us l'han de canviar o reparar. Amb la documentació podreu veure si el que us han venut es correspon amb el que demanàveu. Haureu d'entregar la documentació de garantia i especificacions al client. El material és seu.

     - Tots els cables tenen un certificat o si els heu fet vosaltres (com un cable de xarxa) han passat una prova de validació i transmet correctament els senyals.
     - Tots els components tenen garantia vàlida i les seves especificacions permeten complir els requisits.

   - Un ventilador RGB té tots els modes de color que demanava el client.
```

```destacat-warning
Documenteu totes les proves unitàries i dates d'inici i final de garantia.

   - Si un component s'ha de substituir, millor ara que quan el tingui el client.
   - Si una configuració no fa el que ha de fer, es revisa fins que està fent el que s'espera.
```

### PROVES UNITÀRIES DE CONFIGURACIONS

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Quan feu un protocol de proves unitàries d'un programa (un sistema operatiu, una configuració de switch), sol tenir una sèrie de condicions inicials, unes accions i un resultat esperat.

   - Els permisos d'accés d'un usuari dins la pròpia màquina.
   - El control del tràfic de paquets dins d'una xarxa.
   - L'accés a internet d'un router.
   - La ruta a les plantilles del processador de textos apunta on es demana.
   - Si teniu un sistema operatiu on accedeixen diversos usuaris, que tots els perfils d'usuari que necessiteu estan definits i tenen els permisos que els correspon.
```

```destacat-warning
El protocol ha de descriure clarament què es prova. Pot ser que el protocol estigui ben fet i el sistema no funcioni perquè comprova una cosa diferent.
```

---

## PROVES D'INTEGRACIÓ

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Les proves unitàries proven **peces**. Les proves d'integració proven **connexions**.
 
Aquesta és tota la diferència, i val la pena entendre-la bé perquè és la que més costa. 
- **Una peça és una cosa**: una font d'alimentació, un switch, un full de càlcul. 
- **Una connexió és el que passa entre dues coses**: la font alimenta la placa, el switch encamina cap al router, el formulari escriu al full.
```

```destacat-warning
Podeu tenir totes les peces perfectes i el sistema no funcionar, perquè el que falla és el que hi ha entremig.
```

### Com saber quines proves d'integració necessiteu

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Aquí teniu la regla, i és mecànica:
```

```destacat-info
**Agafeu l'esquema del vostre disseny.
Cada línia que uneix dues coses és una prova d'integració.**

Si al vostre esquema hi ha sis línies, us calen sis proves d'integració. Si al vostre esquema no hi ha línies, el disseny està incomplet i heu de tornar enrere.

Ompliu aquesta taula abans d'escriure cap protocol:
 
| Part A | Part B | Què ha de passar entre les dues | Codi de la prova |
| - | - | - | - |
| | | | PI-01 |
| | | | PI-02 |
| | | | PI-03 |

```
---
 
### Fins on ha d'arribar una prova d'integració

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Una prova d'integració prova **una connexió, no tot el sistema**. Aquesta és l'errada més habitual.
Si feu una prova que travessa quatre connexions alhora i falla, no sabreu quina de les quatre és, i haureu perdut el temps que voleu estalviar. Val més quatre proves petites que una de gran.

| Massa gran | La mida correcta |
| - | - |
| «Un client obre el joc i juga bé» | «La targeta gràfica nova dona imatge al monitor de la sala» |
| «La xarxa funciona» | «Un equip de la línia A arriba al switch» |
| «El full de càlcul va bé» | «El formulari escriu una fila nova al full» |
```

--- 

### En quin ordre es passen

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

De les connexions més bàsiques cap a les que en depenen. Si la connexió entre l'equip i el switch no funciona, no té sentit provar la sortida a Internet, perquè fallarà segur i no us dirà res de nou.
```

#### Exemples en tres tecnologies diferents

Fixeu-vos que la tecnologia canvia del tot i la forma de la prova és sempre la mateixa: una cosa fa alguna cosa, i una altra cosa ho nota.
 
| | Maquinari | Xarxes | Ofimàtica |
| - | - | - | - |
| **Part A** | El processador arriba a 80 °C | Un equip de la línia A | El formulari de reserves |
| **Part B** | El ventilador de la torre | El switch i el router | El full de reserves |
| **Prova** | Es carrega el processador fins a 80 °C i es comprova que el ventilador puja de revolucions | Es fa una petició des de l'equip a una adreça d'Internet i es comprova que hi arriba | S'envia una reserva de prova i es comprova que apareix una fila nova amb les dades correctes |
 
### Quan una prova d'integració falla

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

No toqueu res encara. Primer apliqueu la traçabilitat:

1. Mireu les proves unitàries de les dues parts implicades. Encara són correctes?
2. Si alguna falla, el problema és de la peça, no de la connexió.
3. Si totes dues són correctes, la peça va bé i la connexió no. El problema és del disseny: heu unit dues coses que no s'uneixen com havíeu previst.
```

```destacat-info
Aquesta és exactament la raó per la qual es proven les peces abans que les connexions.
Sense les proves unitàries, quan la integració falla no teniu cap manera de saber on mirar i us hi passareu hores.
```

#### Com no confondre una prova d'integració amb una prova d'acceptació

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Es confonen sovint. La diferència pràctica és qui l'entén:

- **Una prova d'integració l'entén un tècnic**. Parla de components, ports, configuracions i valors.
- **Una prova d'acceptació l'entén el client**. Parla del que ell fa i del que ell vol.

Si li heu d'explicar la prova al client perquè l'entengui, no és una prova d'acceptació.
```

## PROVES D'ACCEPTACIÓ

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Recursos Humans i Qualitat · Aperture Holistics Consulting

Aquestes proves demostren que els requisits que ha demanat el client es compleixen. El seu disseny ha d'estar enfocat a que el seu resultat sigui la necessitat que tenia el client. Aquestes proves tenen un protocol molt directe. El sistema ja està funcionant, així que només queda demostrar que funciona correctament.

Aquestes proves les passarem dos cops.

1. **Internament**. Així ens assegurarem que hem fet bé tota la feina.
2. **Davant del client**. Demostrem al client en directe que el projecte està finalitzat i fa tot el que se li demanava.
```

```destacat-info
Si parléssim d'un cotxe, les proves d'acceptació serien demostrar que el vehicle pot circular per la carretera. En el cas d'una xarxa informàtica, que comunica els diferents dispositius tal i com demanava el client, i prohibeix la comunicació entre els elements que no s'han de poder comunicar. O si és un ordinador, obrir les finestres i fer les accions que demostren el sistema operatiu té les prestacions i configuracions sol·licitades.
```

### Com ha de ser una bona prova d'acceptació

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Recursos Humans i Qualitat · Aperture Holistics Consulting

Aquesta és una guia breu per poder redactar les proves d'acceptació

| Ha de ser... | Perquè... |
| - | - |
| **Curta** | El client no us regalarà una hora. Si no es pot passar en pocs minuts, partiu-la. |
| **Entenedora sense explicacions** | Si li heu de traduir el que està veient, no li esteu demostrant res. |
| **Assajada** | La passeu internament abans. El dia de l'acceptació no és el dia de descobrir res. |
| **Lligada a un requisit** | Cada prova ha de poder dir de quin requisit de l'oferta surt. |
```

---

### Si una prova falla davant el client

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Recursos Humans i Qualitat · Aperture Holistics Consulting

Aquestes coses passen, i no és el final del projecte. El que compta és com hi reaccioneu:

- No improviseu una explicació ni la feu passar per un èxit. El client se n'adona.
- Digueu què esperàveu i què ha passat.
- Digueu quan i com ho resoldreu, amb data.
- Continueu amb la resta de proves. Una prova fallida no invalida les altres.

Un projecte amb una prova fallida i una data de resolució és un projecte seriós. Un projecte on s'ha dissimulat una errada és un client perdut.
```

```destacat-warning
   - Reviseu bé els manuals que heu d'entregar al client. Els acostumen a llegir.
   - Recolliu els protocols de proves per si el client ho demana. Potser ell directament no és tècnic, però pot tenir tècnics a l'empresa o coneguts que les revisin.
   - Verifiqueu que no passa allò d'"a la meva màquina funciona".
```
