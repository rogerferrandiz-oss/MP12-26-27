# EL PROJECTE (capítol)
```destacat-info
En aquest tutorial aprendràs a:
- Passar del disseny al projecte real.
- A saber quan i com has de provar les parts del teu projecte per assegurar que funciona.
- A informar al client sobre com va el seu projecte.
- Assegurar que ho hem provat tot i funciona.
```

(Albert) El que us explicarem aquí no està relacionat directament amb la part tècnica dels projectes. Té més a veure amb la part de la gestió del mateix i que són molt diferents respecte del que coneixeu del cicle.

```destacat-warning
**Fer un projecte no és una cursa de velocitat**. No donen premi al que acaba primer. 
- Tot es tracta de fer funcionar el que se li ha demanat que faci, i ho faci bé.
```

```destacat-video
El text és llarg. Vols un resum? Pots fer servir aquest vídeo. No substitueix completament el text. El complementa. Pots veure el vídeo i després ampliar llegint l'apartat que necessites, o llegir el tema i fer servir el vídeo per recordar. 

[placeholder per video]
```
## SEGUIM EL CICLE EN V (capítol)
(Albert) Com hem vist aquí [link al tutorial del cicle en V dels projectes] , els projectes a les empreses es fan d'una forma organitzada que facilita que es puguin acabar en temps i cost, i que faciliten la resolució dels possibles problemes que puguin aparèixer mentre el fas.

### DELS REQUISITS AL DISSENY (subcapítol)
(Albert) Amb el document de l'oferta i poder donar un preu i un calendari, hem hagut de pensar a grans trets quina és la solució al problema que ens planteja el client, els components bàsics, com es connecten entre ells i les seves configuracions. Seguint la banda esquerra descendent del projecte

1. **Requisits de l'usuari**. Comença a l'oferta. Si l'heu feta bé, serà molt fàcil completar el primer pas. Què necessita l'usuari i què vol obtenir al final.
   - Sabeu fer tot el que us demana el client? Si no és així, què necessito per aprendre / saber més sobre el que ens demana? Què és el que no sé? Com ho puc aprendre?
   - Recollir documentació, buscar casos similars, resoldre els dubtes que teniu abans de començar.
   - Reviseu els temps que heu marcat al calendari de l'oferta.
   - Sigueu honestos. Si hi ha res que no sabeu fer o que no trobeu, o teniu dubtes sobre com implementar, s'han d'informar i resoldre en aquesta fase.

2. **Definim l'arquitectura del sistema**. Com hem de fer les coses per a aconseguir els requisits. 
   - Preparar el disseny. Dibuixar i pensar. Què és el que volem en acabar el projecte? Com ho farem? De nou, la metodologia que heu descrit a l'oferta us ajudarà.
     - Quin disseny de xarxa farem? Disseny físic i lògic?
     - Quins components necesitarem? Tenim disponibilitat d'aquests? Compleixen amb les especificacions?
   - Fer prototipus. Models de treball més petits, que treballen aïllats. Tenir clar que els elements que necessiteu funcionen per separat, i fer proves de connexió parcials que assegurin que sabeu fer totes les fases del projecte abans d'abordar el global.
   - Documenteu tot el que feu. Ho podeu necessitar més endavant. No feu les coses de memòria. Manteniu una webgrafia, un devlog, una llista de referències, documents, el que millor us funcioni. I que estiguin a l'abast (en local) sempre que sigui possible.
   - No correu. Resoldre els problemes aquí implica que anireu més de pressa a les fases següents.

3. **Fem el disseny de detall**. Amb tot el que sabem i hem après, fem "els plànols" definitius del projecte, concretem tot el material, tota la documentació i tanquem la part de preparació. No sempre són plànols, però sí que heu de tenir un lloc on anar a consultar en cas de dubtes.
   - No passeu de fase fins que esteu completament segurs que ho heu mirat tot.
   - Aquí heu de resoldre ja tots els problemes i que no tingueu cap indefinició. No pot haver "això segur que no dona problemes, no cal que ho mirem"
     - Si esteu fent una xarxa, aquí fareu el detall dels equips que muntareu, la xarxa física i lògica definitives i tots els diagrames de connexionat.
     - Si esteu dissenyant una pàgina web, aquí tindreu tots els wireframes, esquemes de colors, estils, etc.

### INSTAL·LACIÓ I IMPLEMENTACIÓ DEL PROJECTE (subcapítol)
(Albert) Aquesta fase és el cor del projecte. Aquí fem la construcció real del sistema, muntem els components, etc. Fem que el sistema funcioni tal i com el tenim dissenyat.
   - Amb tot el que sabeu ja del sistema i si ho heu preparat bé, aquesta fase és molt senzilla. Només heu de seguir la documentació que heu fet.
   - Malgrat tota la preparació, SEMPRE passen imprevistos, i potser les coses no funcionen com ho havíeu previst. Documenteu els canvis i si afecten a res que el client ha demanat, informeu-lo. Si per desgràcia els canvis són molt grans i impliquen una alteració del calendari o del pressupost, és molt important que aviseu immediatament a Aperture i al client.

Per informar el client sobre com va el seu projecte, cal convocar sempre una reunió.

### REUNIÓ DE SEGUIMENT (capítol)
(Lídia) A Aperture tenim projectes que duren setmanes i altres que duren anys. I en tots ells mantenim una comunicació transparent amb el client, que és qui ens paga per resoldre-li el problema. Els clients han d'estar informats en tot moment sobre com està anant l'encàrrec.

Com els nostres projectes solen ser curts, com a mínim farem una reunió de seguiment amb el nostre client, per mostrar al client que:
- Mostar-li que estem treballant en el projecte.
- Com anem amb el calendari. Si estem al dia o tenim endarreriments. Ser transparent.
- Tenim el coneixement tècnic suficient i sabem fer el projecte de forma professional.
- Donar-li opció de donar-nos més detalls o resoldre dubtes que han anat apareixent.

Aquestes reunions es desenvolupen com sempre, seguiu el tutorial de reunions [link al tutorial de reunions]

### FASE DE PROVES DEL PROJECTE (capítol)
(Albert seriós) Un cop hem acabat de muntar el nostre disseny, és el moment de comprovar que tot funciona correctament. La pràctica habitual és separar les proves en diferents nivells, com s'ha explicat al procés de cicle en V [link al tutorial].
1. **Proves unitàries** En aquesta fase es prova que tots els elements físics i lògics del sistema que hem muntat funcionen correctament. Evita que el sistema doni una errada causada per un mal funcionament aliè al vostre disseny.
2. **Proves d'integració**. Demostren que les diferents parts del sistema treballen correctament quan les uneixes. Serveixen per veure que les diferents parts del total es comuniquen correctament entre elles i no hi ha problemes.
3. **Proves d'acceptació internes**. Aquestes proves van enfocades a demostrar que el que heu dissenyat resol els requisits plantejats. Les passarem dos cops. El primer cop ho fem internament. Només si superem totes les proves, podem dir que hem finalitzat l'encàrrec i podem repetir les proves davant del client, per demostrar que hem fet bé la feina. Si es passen correctament, li podeu posar el llacet al projecte. 

I finalment, aviseu al client que ja podeu entregar el projecte, i convoqueu la reunió per l'acceptació del client.
- Envieu la convocatòria de reunió.
- Prepareu una presentació perquè faci de guia.
- Assageu la reunió. No pot fallar res.
- Prepareu possibles preguntes del client.
- Reviseu que el projecte es comporta com toca.

```destacat-warning
**No correu**. Si aneu directament a les proves d'acceptació i el sistema no funciona, haureu perdut moltíssim temps, i si funciona, no sabreu si ho farà en totes les condicions o algun sistema us donarà problemes més endavant.
- Només si totes les proves unitàries són positives, passarem a la següent fase de proves.
- Només si totes les proves d'integració són positives, passarem a la següent fase de proves.
- Només si totes les proves d'acceptació internes són positives, podem dir al client que ja tenim el projecte acabat.
- Si un protocol falla, anirem tirant dels protocols del nivell anterior que deien que anava bé, fins a trobar l'error. Pot ser que sigui al disseny.
```

Si necessiteu saber més sobre les proves, teniu informació aquí [link al tutorial de protocols de proves]

### TANCAMENT DEL PROJECTE. AUDITORIA INTERNA (capítol)
(Lídia seriosa) Tancar un projecte també és un petit projecte en sí mateix. I us ho explico ràpidament.
- Els clients solen tornar si els has fet bé la feina. Per ampliar-ne un o per demanar nous projectes. Tenir la informació del client ben organitzada permet estalviar molt de temps i això vol dir fer projectes més de pressa i a millor preu.
- Els projectes llargs difícilment els acaben els mateixos components de l'equip que l'han iniciat. Això vol dir que si arriba algú nou, agafarà el ritme del projecte més de pressa si ja coneix l'estructura de carpetes, els noms dels arxius i les ubicacions.

Per això des del departament de qualitat, un cop tingueu el projecte llest per fer la reunió d'acceptació amb el client, us passarem una auditoria interna per assegurar dues coses:
1. Heu entès i aplicat els criteris d'organització de projectes que se us van explicar a l'inici del projecte.
2. No heu passat per alt res del que el client demanava en el projecte.
Pot semblar que és molt, però si treballeu bé des del primer dia, superareu sense problemes aquesta auditoria. Seguiu el que se us indica al manual d'estil d'Aperture [link al manual d'estil]

```destacat-info
L'auditoria no es es fixa en els continguts ni en la part tècnica, però sí en els aspectes formals:
- Tots els requisits tenen un o més protocols associats.
- Tots els documents fan servir la plantilla d'Aperture i els format són els correctes.
- Tots els documents estan a la seva carpeta i amb un nom fàcilment identificable.
- Tots els documents estan acabats, no hi ha faltes d'ortografia ni de gramàtica.
Així, no podreu enviar la convocatòria de reunió amb el client fins que no supereu aquesta auditoria. 
És molt important que la supereu, perquè va lligada als vostres resultats d'aprenentatge.
```



