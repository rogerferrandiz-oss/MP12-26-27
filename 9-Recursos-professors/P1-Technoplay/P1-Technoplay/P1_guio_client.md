| **GUIÓ DEL CLIENT** *Document intern · No es lliura als alumnes* | **Projecte 1 · Maquinari** Ref: 26-000-Technoplay |
| - | -: |

---

## 0 · Com fer servir aquest document

Aquest document permet que qualsevol professor faci de client en aquest projecte sense haver-lo dissenyat. Llegiu-lo sencer abans de la primera reunió.

**Regles de joc, iguals a tots els projectes:**

1. **No oferiu informació que no us demanin.** El client no sap què és rellevant. Si no pregunten pels reinicis, no en parleu.
2. **No feu de tècnic.** Davant una pregunta tècnica, la resposta és sempre alguna variant de «no ho sé, els tècnics sou vosaltres». Si el professor diagnostica, l'exercici s'acaba.
3. **No corregiu el grup dins del personatge.** Si diuen una barbaritat, el Marc no ho sap. Les correccions les fa l'Albert, en un altre moment i amb un altre barret.
4. **Contesteu exactament el que us pregunten.** Si pregunten «es reinicien els ordinadors?», la resposta és «sí», no un discurs. Si volen més, que ho preguntin.
5. **Si un grup s'encalla del tot**, feu servir les empentes de la secció 6, que estan escrites perquè totes les empentes siguin iguals per a tots els grups.

---

## 1 · El personatge

**Marc García**, propietari, 41 anys. Va obrir el local el 2022 amb els seus estalvis. No té formació informàtica: ha après mirant vídeos i preguntant a botigues.

| Com parla | Frases planeres, sense termes tècnics. Si en fa servir un, l'ha sentit en un vídeo i el fa servir malament. |
| - | - |
| Estat d'ànim | Nerviós. La competència l'angoixa. Vol solucions ràpides i li costa acceptar que una cosa trigui. |
| Què li importa de debò | Que els clients no es queixin i que no hagi de tancar cap lloc. |
| Què no li importa gens | Les marques, els models i les especificacions. Si li ho expliqueu amb números, desconnecta. |
| Com reacciona a un preu | Malament, sempre, la primera vegada. Si li justifiqueu la despesa amb el que hi guanya, ho accepta. |

**Laura Ferrer**, ajudant, 24 anys. Present a la reunió només si el grup la demana explícitament. Sap coses que el Marc no sap: què es queixen els clients i com es neteja el local de veritat.

---

## 2 · Els requisits reals

Aquesta és la llista a la qual haurien d'arribar. Serveix per corregir el document de requisits, no per dictar-la.

| # | El sistema ha de... | Prova d'acceptació | Nivell |
| - | - | - | - |
| R1 | Funcionar 4 hores seguides de joc sense que cap equip es reiniciï | Deixar 4 equips de les línies A i B jugant 4 h i comprovar que cap no s'ha reiniciat | Imprescindible |
| R2 | Donar 144 fps sostinguts als jocs competitius a la línia C | Obrir el comptador de fps i jugar 10 minuts a CS2, comprovant que no baixa de 144 | Imprescindible |
| R3 | Permetre jugar i retransmetre alhora a la sala VIP sense tirons | Jugar i retransmetre 15 minuts i comprovar que no hi ha talls d'imatge ni de so | Imprescindible |
| R4 | Mantenir el rendiment dels simuladors després d'una hora d'ús | Fer córrer un simulador 1 h i comprovar que els fps del final són els mateixos que els del principi | Imprescindible |
| R5 | Permetre a la Laura fer el manteniment setmanal sola | La Laura fa el manteniment d'un equip seguint la guia, sense ajuda i sense trucar al Marc | Imprescindible |
| R6 | Deixar el switch, el router, el PC de recepció i el portàtil tal com estan | Comprovar a l'inventari final que aquests quatre equips no s'han tocat | Imprescindible |

**Files que es donen ja omplertes a l'enunciat de l'alumne:** R1 i R5. La R1 perquè és el problema evident i mostra com s'escriu una prova de rendiment; la R5 perquè mostra que un requisit també pot ser sobre una persona i no sobre una màquina.

**Diagnòstic real, per si el professor l'ha de tenir present:**

| Equips | Causa |
| - | - |
| Línies A i B i lloc individual (11 PC) | Font de 450 W genèrica, infradimensionada i degradada |
| Línia C (5 PC) | Gràfica insuficient per al monitor de 144 Hz |
| Sala VIP (5 PC) | 16 GB de RAM insuficients per jugar i retransmetre |
| Simuladors (3 PC) | Pols acumulada, torres a terra, sobreescalfament |
| Tots | Sense neteja interna mai, pasta tèrmica original, Windows Update desactivat |

---

## 3 · Informació que només es dona si la demanen

Aquesta és la informació que fa que la reunió sigui necessària. **No apareix a la fitxa de client.** Doneu-la només davant una pregunta que hi apunti.

| Si pregunten per... | El Marc contesta |
| - | - |
| Quins equips es reinicien | «Els de les línies A i B. El de jocs sols també, però com que s'usa menys es nota menys.» |
| Amb quina freqüència | «Cada dia n'hi ha algun. A la tarda, quan hi ha ple, més.» |
| Com es reinicien | «S'apaguen i tornen a arrencar sols. No surt cap missatge ni res.» |
| Si passa amb algun joc concret | «No. Passa amb tots, però sempre a mitja partida, mai al principi.» |
| Per la línia C | «Aquests no s'han reiniciat mai. El que passa és que els clients diuen que no els noten millors que els altres, i els monitors em van costar més.» |
| Per la sala VIP | «Aquests van bé. L'únic és que quan retransmeten es queixen que va a tirons i que el so es talla.» |
| Pels simuladors | «Al cap d'una estona van més lents i els ventiladors fan un soroll que espanta. Jo suposo que és normal, són molt potents.» |
| Hores d'encesa | «Obrim de 4 a 12 entre setmana i d'11 a 12 els caps de setmana. Els ordinadors no s'apaguen fins que tanquem.» |
| Manteniment actual | «La Laura passa el drap i escombra cada dia.» |
| Si han obert alguna torre | «No. Mai. No sabria ni per on començar.» |
| Actualitzacions de Windows | «Les vaig desactivar perquè es posaven a actualitzar amb clients jugant.» |
| Controladors gràfics | «Els que portava quan els vaig comprar, suposo.» |
| Temperatura del local | «Hi ha aire condicionat, però al fons, on són els simuladors, arriba just.» |
| Ubicació de les torres | «Les dels simuladors són a terra, sota el seient. La resta són sobre la taula.» |
| Endolls i electricitat | «No he tingut mai cap problema de llum. No ha saltat mai el diferencial.» |
| Si vol canviar monitors | «Els de la línia C són nous, aquests no. Els altres si cal, però no és el que més em preocupa.» |
| Què diuen els clients | «Que hi ha llocs millors que altres i sempre volen els mateixos. I això em desquadra les reserves.» |

**Si demanen parlar amb la Laura**, ella afegeix:

- «Els clients em demanen sempre la línia C o la sala VIP. La A i la B les deixo per als últims.»
- «Jo netejo per fora. Per dins no hi he entrat mai, ni sé si s'ha de fer.»
- «Sota els seients dels simuladors hi ha molta pols i terra del carrer.»

---

## 4 · Preguntes previsibles i respostes

| Pregunta | Resposta del Marc |
| - | - |
| Podem ampliar el pressupost? | «Depèn. Si m'expliqueu què hi guanyo, potser arribo a 7.000. Més no.» |
| Podem allargar el termini? | «No. La competència obre en un mes i mig i he d'estar llest abans.» |
| Podem canviar el switch o el router? | «No. El router és de la companyia i el switch em va costar molt. No els toqueu.» |
| Podem canviar el PC de recepció? | «No. La Laura ja s'hi ha acostumat i no vull embolics.» |
| Es poden apagar els equips a la nit? | «Sí, si em dieu com i no complica res.» |
| Podem instal·lar un altre sistema operatiu? | «Si els jocs funcionen igual, per mi bé. Però que la Laura ho sàpiga fer servir.» |
| Quant temps podem tenir el local tancat? | «Els dilluns al matí no obrim. La resta, com menys millor.» |
| Teniu factures o garanties dels equips? | «Alguna en tinc, però no totes. No sóc gaire ordenat amb això.» |
| Voleu que us formem la Laura? | «Sí, però que sigui curt. No tinc temps de fer cursets.» |
| Quin problema us preocupa més? | «Que s'apaguin. Un client al qual se li apaga l'ordinador a mitja partida no torna.» |

---

## 5 · Què concedeix i què no

| Concedeix | Amb quina condició |
| - | - |
| Pujar el pressupost a 7.000 € | Només si li justifiquen amb números què hi guanya |
| No actualitzar tots els equips | Si li expliquen l'ordre de prioritat i per què |
| Apagar equips fora d'horari | Si no complica la feina de la Laura |
| Canviar de sistema operatiu | Si els jocs van igual i la Laura se'n surt |

| No concedeix mai | |
| - | - |
| Tocar el switch, el router, el mini PC o el portàtil | És una restricció dura del projecte |
| Passar de 7.000 € | Sostre absolut |
| Allargar el termini de 4 setmanes | Sostre absolut |
| Tancar el local més d'un dilluns al matí | |

---

## 6 · Empentes per a grups encallats

Feu-les servir només si el grup no arriba, i **feu servir la mateixa empenta per a tots els grups** que estiguin igual d'encallats. Van dins del personatge.

| Si el grup no ha preguntat... | El Marc diu, com de passada |
| - | - |
| Quins equips fallen | «Ah, i que quedi clar que no fallen tots, eh? Que si no us ho penseu.» |
| Res sobre neteja ni manteniment | «Us he de dir alguna cosa del que fem per mantenir-los, o ja ho sabeu?» |
| Res sobre hores d'ús | «És que aquí, un cop obrim, no s'apaguen fins a la nit.» |
| Res sobre la línia C | «I dels monitors nous, no me'n dieu res? Perquè em van costar un ull de la cara.» |
| Res sobre els simuladors | «Els simuladors els deixem com estan, no? Encara que facin aquell soroll.» |

---

## 7 · Coses que el Marc diu malament a propòsit

Serveixen perquè els alumnes aprenguin a no acceptar el diagnòstic del client. **No les corregiu.** Si un grup les compra, es veurà al document de requisits i es corregeix allà.

- «Jo crec que deu ser un virus, perquè es reinicien.»
- «Suposo que amb més memòria RAM ho arreglem tot, no?»
- «El soroll dels ventiladors és normal, són molt potents.»
- «Vull tenir els ordinadors més potents del barri.» (incompatible amb el pressupost)

---

## 8 · Senyals per al professor

Què mirar durant la reunió, per a l'eina d'observació.

| Bon senyal | Mal senyal |
| - | - |
| Pregunten quins equips fallen abans de proposar res | Arriben amb la solució ja decidida |
| Porten les preguntes escrites i les segueixen | Improvisen i repeteixen preguntes |
| Prenen notes i un dels dos condueix | Ningú no escriu res |
| Qüestionen el diagnòstic del Marc | Accepten «deu ser un virus» sense més |
| Pregunten per l'ús real, no només pel maquinari | Només parlen de components |
| Demanen parlar amb la Laura | No es plantegen que hi hagi més usuaris |