# Objectiu
L'objectiu del treball és disposar d'una eina àgil i fàcil de fer servir per capturar les observacions d'aula dels alumnes que fem servir per fer el seguiment.

# El procediment
Tenim un formulari de Google que recull les observacions. Hi ha un formulari per grup, per simplificar la llista dels alumnes i facilitar la feina del professor.

Les pestanyes de grup SMIX2AT...2DT són les que reben les informacions. Cada grup s'acompanya d'una pestanya d'alumnes de cada grup, amb el nom i el seu correu. Això ho farem servir per les comunicacions amb els alumnes. La pestanya de Calendari té les dates d'inici i final de cada un dels 5 projectes. Les dates poden canviar segons les necessitats del curs.

## Tractament de les observacions i les valoracions
La part més importants és la de valoració de l'observació, que va de +3 fins a -2, es converteix en centèssimes de punt que multiplicaran la nota individual de l'alumne. El multiplicador base de la nota comença en 1 punt i per evitar un excés en la modificació el limitarem a una franja entre 0,5 i 1,5 punts.

Les valoracions d'observació es mostren a l'alumne com un valor enter, però es porten com una centèssima. Així un +2 serà un +0.02.

Les columnes d'observacions estan agrupades per alumne i projecte.
- P1-obs: marca la quantitat d'observacions fetes durant cada projecte.
- P1-balanç: suma el balanç d'observacions positives i negatives. S'ha de mostrar un valor entre 0,5 i 1,5 punts.
- I així per a tots els projectes.

## Panell de control general
Finalment, tenim un panell de control central on els professors podem trobar informació general per grup i els alumnes positius i negatius més destacats.

Necessitem indicadors generals de mòdul:
- Observacions totals fetes. Per mòdul i per grup.
- Observacions promig setmanals. Per mòdul i per grup.
- Professor amb més observacions.
- Professor amb menys observacions.
- Top 3 alumnes positius de cada grup.
- TOP 3 alumnes negatius de cada grup.
- Afegeix qualsevol indicador que creguis que pot fer servei durant el curs.

I després haurem de fer un programa que faci un informe massiu a final de cada projecte. Cada alumne ha de rebre un informe amb el valor del seu multiplicador de nota individual i una llista de totes les observacions que se li han fet en ordre cronològic. Se li adjuntarà com a retroacció a la tasca de Moodle. Es pot fer amb HTML i CSS simple.

