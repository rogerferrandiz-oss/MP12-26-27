!-- PERSONATGES -->
<!--
albert_formal: https://cv.copernic.cat/...
lidia_formal:  https://cv.copernic.cat/...
-->

# EL CICLE D'UN PROJECTE (capítol)

```destacat-info
En aquest tutorial aprendràs:
- Què és el cicle de desenvolupament en V per a fer projectes.
- Per què es fa això i quins avantatges té.
```

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Aquí no us explicarem cap tecnologia. Us explicarem com es fa un projecte a Aperture, sigui de xarxes, de maquinari o d'un full de càlcul. L'aplicació pràctica és el que anirem practicant durant tot el curs. Val la pena entendre-ho bé un cop i no haver-hi de tornar.

- El tutorial sobre com desenvolupar un projecte anirà explicant el detall sobre què es fa en cada etapa.
- El tutorial sobre com fer un protocol de proves i passar-lo us explicarà en detall com assegurar-nos que el que hem fet està bé.
```

Aquest tutorial és curt a propòsit. Són tres idees i tres dibuixos.

```destacat-info
- **Idea 1**: un projecte té dues meitats. A la primera decidiu, a la segona demostreu.
- **Idea 2**: tot el que decidiu, ho heu de poder demostrar.
- **Idea 3**: hi ha tres nivells de decisió, i per tant tres nivells de demostració.
```

```destacat-video
Si no tens temps de llegir tot el tema, us hem deixat un vídeo que explica el material. El podeu veure i després llegir, o a la inversa.

[placeholder de vídeo resum]

```

---

## Les dues meitats (subcapítol 1)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Recursos Humans i Qualitat · Aperture Holistics Consulting

Un projecte a Aperture té dues meitats, i vosaltres ja les coneixeu pel nom.

| Meitat | Com se'n diu aquí | Què hi feu |
|---|---|---|
| Primera | **L'oferta** | Decidiu què fareu i ho prometeu al client |
| Segona | **El projecte** | Ho feu i demostreu que heu complert la promesa |

L'oferta no és paperassa prèvia. És la llista de promeses. Quan el client la signa, es converteix en un contracte, i tot el que hi heu escrit us el podrà reclamar.

Aquesta és la diferència entre una empresa seriosa i una que no ho és. No prometre menys, sinó prometre coses que es puguin comprovar.

Un client mai no discuteix amb una prova. Discuteix sempre amb una opinió.
```

```destacat-warning
Si a l'oferta prometeu una cosa que després no podeu demostrar, teniu un problema. Per això a l'oferta no hi ha d'haver cap promesa que no sapigueu com comprovar.
```

---

## Els tres nivells de profunditat (subcapítol 2)

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Quan feu un projecte preneu decisions de tres tipus. Van de la més general a la més concreta.

Llegiu el dibuix de dalt a baix per la banda esquerra, i de baix a dalt per la banda dreta. Cada color té la seva parella al davant.


[(https://cv.copernic.cat/pluginfile.php/29447/mod_resource/content/1/Cicle%20V%20original.png)]

Es diu **cicle en V** per la forma del dibuix. La banda esquerra baixa cap al detall, la dreta puja cap al client.

| Nivell | Baixant, decidiu | Pujant, demostreu |
|---|---|---|
| **1** | Què vol el client | Que fa el que li vau prometre |
| **2** | Com ho fareu | Que totes les peces funcionen juntes |
| **3** | Què hi posareu exactament | Que cada peça funciona per separat |

I al fons de la V hi ha el muntatge: fer el projecte de veritat, un cop ja no hem de pensar ni tenir dubtes sobre com fer-ho.

**Per què es puja en aquest ordre?**. Perquè si proveu primer el conjunt i falla, no sabreu quina peça n'és la culpable i us hi passareu hores. Si abans heu comprovat cada peça per separat, quan el conjunt falli ja sabreu que el problema és a la connexió entre peces, no a les peces.

Aquesta és la part que més us costarà d'acceptar, i us ho dic ara: provar cada peça per separat sembla perdre el temps i és exactament el contrari.

El dia que us passeu tres hores buscant per què no va res i resulti que era un cable, us en recordareu.
```
---

## El mateix cicle, dos projectes molt diferents (subcapítol 3)

```bloc-dialeg
avatar: albert_formal
nom: Albert Serrano
rol: Mentor tècnic · Aperture Holistics Consulting

Aquí teniu el mateix dibuix aplicat a dos projectes que no s'assemblen gens. Compareu-los. La tecnologia canvia del tot; les caselles són les mateixes.

Exemple 1: Un projecte d'ofimàtica
[(https://cv.copernic.cat/pluginfile.php/29446/mod_resource/content/1/Cicle%20V%20ofimatica.png)]

Exemple 2: Un projecte de xarxes
[(https://cv.copernic.cat/pluginfile.php/29448/mod_resource/content/1/Cicle%20V%20xarxes.png)]

Fixeu-vos que als dos exemples, la casella de dalt a la dreta (la prova davant el client) es pot fer **davant seu i en un minut**, i no cal saber res de tecnologia per entendre si ha anat bé o malament.

```destacat-warning
No copieu el contingut d'aquests exemples al vostre projecte. El que heu de copiar és **l'estructura**, no les respostes. Cada client voldrà una cosa diferent, però el recorregut per a arribar a una entrega exitosa és sempre el mateix.
```
---

## On sou a cada moment (subcapítol 4)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Responsable de Recursos Humans

El projecte dura sis setmanes i cada setmana esteu en un punt diferent del cicle.

| Setmana | On sou al cicle | Què entregueu |
|---|---|---|
| 1 | Nivell 1, baixant | Document de requisits |
| 2 | Nivell 1, tancat | Oferta i presentació al client |
| 3 | Nivells 2 i 3, baixant | Disseny i protocols de proves |
| 4 | Fons de la V | Reunió de seguiment |
| 5 | Nivells 3 i 2, pujant | Verificació tècnica, auditoria interna i entrega |
| 6 | Nivell 1, dalt | Presentació: proves d'acceptació davant el client |
```

## La presentació final (subcapítol 5)

```bloc-dialeg
avatar: lidia_formal
nom: Lídia García
rol: Recursos Humans i Qualitat · Aperture Holistics Consulting

L'últim dia no fareu una presentació explicant el que heu fet. Fareu passar les proves davant el client. Les proves d'acceptació amaguen tota la complexitat del sistema i estan orientades a que el client la pugui entendre sense que li expliqueu res.

És més exigent i també més just: no depèn de com parleu, depèn de si funciona.
```

```destacat-critic
Titol: Errors que veiem cada any
- Prometre a l'oferta coses que després no es poden comprovar.
- Passar al muntatge sense haver escrit com es provarà.
- Provar-ho tot de cop al final, quan ja no hi ha temps per arreglar res.
- Arribar a la presentació sense haver assajat les proves.
```
