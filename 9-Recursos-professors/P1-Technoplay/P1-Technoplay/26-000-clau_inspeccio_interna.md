# Clau de la inspecció interna · 26-000-Technoplay

Document intern. S'afegeix al guió del client.

## Quan es lliura

A l'inici de la setmana 3, quan el grup declara que ha «obert» els equips. No abans: l'oferta s'ha de fer amb l'inventari ampliat de la Laura.

## Què confirma i què afegeix

| Equips | Confirma | Afegeix |
| - | - | - |
| A, B, S01 | Font de 450 W. L'etiqueta de 12 V / 30 A dona 360 W útils, i NVIDIA recomana 550 W per a una RTX 3050 | Pasta seca, pols a la font. Troballes extra a B03 i B05 |
| C | La gràfica no arriba als 144 fps | **C02 i C04 estan configurats a 60 Hz** i amb cable dubtós. Part del problema era configuració |
| VIP | 16 GB insuficients | **V02 té la RAM en un sol canal.** Les altres tenen ranures lliures |
| Simuladors | Pols i sobreescalfament | Pols molt alta, entrada d'aire arran de terra. Ventilador trencat a SIM02 |

## Les troballes extra

**B03 · gràfica sense cargolar.** Es resol amb un cargol. Cap cost. Serveix per veure si ho documenten o ho arreglen callant.

**C02 i C04 · 60 Hz i cable.** Es resol configurant Windows i, si de cas, amb un cable DisplayPort (22 € a La Botiga). No elimina la necessitat de gràfica nova, però un grup que ho troba entén que no tot és maquinari.

**V02 · RAM en un sol canal.** Obliga a entendre el doble canal. També obre una decisió: a la VIP hi ha ranures lliures, i afegir un segon kit de 16 GB (55 €) és més barat que substituir per un de 32 GB (95 €). La resposta prudent és substituir, perquè barrejar kits pot donar problemes. Qualsevol de les dues és defensable si la justifiquen.

## Els dos imprevistos per comunicar al client

**B05 · marca de cremat al connector de 24 pins.** És l'imprevist principal. La font nova resol el problema, però la placa base pot haver quedat tocada i no hi ha manera de saber-ho del cert. Resposta professional: informar el Marc per escrit, canviar la font, fer una prova de càrrega més llarga en aquest equip i recomanar vigilar-lo. No cal canviar la placa si la prova surt bé. El que s'avalua és que ho comuniquin, no que ho resolguin.

**SIM02 · ventilador de caixa trencat.** La Botiga no ven ventiladors de caixa sols. Hi ha la caixa Corsair 4000D Airflow (95 €), que porta ventiladors i té entrada frontal amb malla. Obliga a buscar alternatives dins del catàleg i demanar aprovació al client per una despesa no prevista. Si et sembla massa per al P1, elimina aquesta troballa i deixa només B05.

## Pistes per a la guia de manteniment

Les observacions porten pistes que haurien d'aparèixer a la guia:

| Observació | Què hauria de dir la guia |
| - | - |
| Pols alta a A i B, molt alta als simuladors, mitjana a C i VIP | Freqüència de neteja diferent per zona |
| Entrada d'aire inferior sense filtre | Netejar l'entrada inferior amb més freqüència |
| Torres dels simuladors a terra | Aixecar-les del terra, o revisar-les cada setmana |
| Windows Update desactivat | Actualitzar en una franja amb el local tancat |
| La Laura mai ha obert una torre | La guia de la Laura només inclou neteja exterior. La interior la fa el Marc |

## Temps orientatius de neteja interna

Per corregir el calendari de l'oferta. Sense comptar canvis de peces.

| Nivell de pols | Minuts per equip |
| - | - |
| Mitjà | 20-25 |
| Alt | 30-40 |
| Molt alt | 45-60 |

Amb 24 equips, la neteja sola són unes 13-15 hores de feina. Un grup que al calendari hi posa «neteja: 1 dia» no ha fet els números.
