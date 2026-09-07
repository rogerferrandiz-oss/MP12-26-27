| **PROTOCOL DE PROVES** *Aperture Holistics Consulting* | Grup: _______ Projecte: _______ |
| - | -: |
 
---
 
## Com es fa servir aquest document
 
Cada prova ocupa una fitxa. Les fitxes es numeren per nivell:
 
| Codi | Nivell | Quan es passa |
| - | - | - |
| **PU-nn** | Prova unitària | Just després de muntar o configurar cada peça |
| **PI-nn** | Prova d'integració | Quan les peces ja treballen juntes |
| **PA-nn** | Prova d'acceptació | Assaig intern primer, i després davant el client |
 
```
Regla: cada requisit de l'oferta ha de tenir com a mínim una prova d'acceptació.
Si un requisit no té prova, o el requisit sobra o us n'heu oblidat.
```
 
---
 
## Taula de traçabilitat
 
Ompliu-la abans de començar a fer proves. És el resum que portareu a la reunió d'acceptació.
 
| Requisit | Proves unitàries | Proves d'integració | Prova d'acceptació |
| - | - | - | - |
| R1 | | | |
| R2 | | | |
| R3 | | | |
| R4 | | | |
| R5 | | | |
| R6 | | | |
 
---
 
## Fitxa de prova (plantilla)
 
| **Codi** | | **Requisit relacionat** | |
| - | - | - | - |
| **Què volem demostrar** | *Una frase concreta. No val «funciona bé».* | | |
| **Condicions inicials** | *Què ha d'estar muntat, encès, configurat o instal·lat abans de començar. Si una condició no es compleix, la prova no es pot passar.* | | |
| **Accions** | *Passos numerats. Qualsevol persona ha de poder seguir-los sense preguntar res.* | | |
| **Resultat esperat** | *Un valor, un missatge o un comportament concret. Ha de permetre dir sí o no sense discussió.* | | |
| **Evidència** | *Captura, fotografia, lectura d'aparell, línia de registre. Com ho guardareu.* | | |
| **Resultat obtingut** | | **Data** | |
| **Veredicte** | □ Correcte  □ Incorrecte | **Passada per** | |
| **Si és incorrecta** | *Què heu fet, què heu canviat i quin codi té la nova passada.* | | |
 
---
 
## Exemple 1 · Prova unitària
 
| **Codi** | PU-04 | **Requisit relacionat** | R1 |
| - | - | - | - |
| **Què volem demostrar** | Que la font d'alimentació nova de l'equip PC-A01 manté la tensió estable amb l'equip a plena càrrega. | | |
| **Condicions inicials** | PC-A01 muntat amb la font nova. Programari de monitoratge i de test de càrrega instal·lats. Cap altre programa obert. Torre tancada. | | |
| **Accions** | 1. Obrir el programa de monitoratge i deixar-lo registrant.<br>2. Executar el test de càrrega combinada durant 20 minuts.<br>3. Anotar la tensió mínima i màxima de la línia de 12 V.<br>4. Comprovar que l'equip no s'ha reiniciat. | | |
| **Resultat esperat** | La línia de 12 V es manté entre 11,4 V i 12,6 V durant tot el test, i l'equip continua encès en acabar. | | |
| **Evidència** | Captura del registre de monitoratge amb les tensions i el temps transcorregut. | | |
| **Resultat obtingut** | | **Data** | |
| **Veredicte** | □ Correcte  □ Incorrecte | **Passada per** | |
 
*Aquesta prova es repeteix per a cada equip on s'hagi canviat la font. Es poden agrupar en una sola taula de comprovació OK/NO amb una fila per equip, sempre que les condicions i les accions siguin exactament les mateixes.*
 
---
 
## Exemple 2 · Prova d'integració
 
| **Codi** | PI-02 | **Requisit relacionat** | R1 |
| - | - | - | - |
| **Què volem demostrar** | Que la font nova, la refrigeració netejada i la targeta gràfica de l'equip PC-A01 funcionen correctament alhora sota càrrega sostinguda. | | |
| **Condicions inicials** | PC-A01 acabat: font nova, interior net, pasta tèrmica renovada, controladors actualitzats. Torre tancada i a la seva posició habitual de la sala. Temperatura del local en condicions normals d'obertura. | | |
| **Accions** | 1. Obrir el programa de monitoratge de temperatures i tensions.<br>2. Executar càrrega simultània de processador i gràfica durant 30 minuts.<br>3. Anotar la temperatura màxima de processador i de gràfica.<br>4. Anotar la tensió mínima de la línia de 12 V.<br>5. Comprovar que l'equip no s'ha reiniciat ni ha reduït la freqüència per temperatura. | | |
| **Resultat esperat** | Temperatura de processador per sota de 85 °C i de gràfica per sota de 80 °C. Tensió estable. Cap reinici ni reducció de freqüència. | | |
| **Evidència** | Captura del registre amb les gràfiques de temperatura i tensió dels 30 minuts. | | |
| **Resultat obtingut** | | **Data** | |
| **Veredicte** | □ Correcte  □ Incorrecte | **Passada per** | |
 
*Fixeu-vos en la diferència amb la PU-04: allà es provava una peça sola, aquí es proven tres peces treballant juntes en condicions reals de la sala. Si aquesta prova falla i la PU-04 era correcta, el problema no és la font.*
 
---
 
## Exemple 3 · Prova d'acceptació
 
| **Codi** | PA-01 | **Requisit relacionat** | R1 |
| - | - | - | - |
| **Què volem demostrar** | Que cap equip de les línies A i B no es reinicia durant 4 hores seguides de joc, que és el que vam prometre a l'oferta. | | |
| **Condicions inicials** | Els 10 equips de les línies A i B acabats i verificats. Joc de la llista instal·lat i obert. Local en horari normal d'obertura. Cronòmetre visible. | | |
| **Accions** | 1. Engegar els 10 equips i anotar l'hora d'inici.<br>2. Deixar els 10 equips amb el joc en execució durant 4 hores.<br>3. Cada hora, comprovar equip per equip el temps que porten encesos.<br>4. En acabar, comprovar que els 10 equips porten 4 hores seguides sense haver-se reiniciat. | | |
| **Resultat esperat** | Els 10 equips mostren un temps d'activitat igual o superior a 4 hores. Cap reinici. | | |
| **Evidència** | Fotografia o captura del temps d'activitat dels 10 equips en acabar, i full de seguiment horari signat. | | |
| **Resultat obtingut** | | **Data** | |
| **Veredicte** | □ Correcte  □ Incorrecte | **Passada per** | |
 
```
Aquesta prova es passa DUES vegades:
la primera sense el client, per assajar i per assegurar-vos que surt bé;
la segona davant el client, el dia de l'acceptació.
Si la primera falla, encara hi sou a temps. Si falla la segona, no.
```
 
---
 
## Què fer quan una prova falla
 
| Falla una prova... | Mireu primer... |
| - | - |
| Unitària | El muntatge o la configuració d'aquella peça. Potser la peça és defectuosa. |
| D'integració | Que les proves unitàries de les peces implicades siguin correctes. Si ho són, el problema és de disseny. |
| D'acceptació | Que les proves d'integració siguin correctes. Si ho són, potser el requisit no s'havia entès bé. |
 
Passi el que passi, es documenta: què ha fallat, què heu canviat i quan heu tornat a passar la prova. Una prova repetida sense deixar constància del canvi no val res.