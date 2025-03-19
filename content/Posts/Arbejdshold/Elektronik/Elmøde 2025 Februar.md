---
date: 2025-02-16
draft: false
title: Elmøde 2025 Februar
---

## Opgaver

- Ukendt bestik find ud af hvor den går hen og om den bør være en del af navigations tavlen
- Flyt batterier
- Køb kabler og Træk kabler
- Monter Sikringer
- Lav forsynings dims (16 bolte)
- Husk krydsfiner til Jakobs hylde (120 cm bred 160-180 cm høj cirkus)

- Tjek om PV12 bliver overlastet

## Elkedel

Elkedlen bruger måske over 2000W

Er det så et problem for vores system?

Jamen vi har 420 Ah i vores forbrugssystem (den mængde kalder man C). Det er generelt set godt at bruge 0.1-0.2 C i sit system og hvis man bruger mere reducerer man levetiden drastisk. Det kan også være at man slet ikke kan bruge mere fordi spændingen bare forsvinder.

0.1C i vores system svarer til 0.1*420Ah = 42A

0.1C i vores system svarer til 0.2*420Ah = 84A

2000W = 24V*A <=> 2000W/24V =83.33 A altså præcis en smule under den maksimale grænse på 84A

Dertil medregnes der et tab fra inverteren der laver 24V om til 240V og eventuelt andre træk såsom lys eller pumper og vi er nu langt over den maksimale grænse

### Konklusion - Vi skal have en ny elkedel


## Forbrugs ledninger

### Water maker
Vi prioriterer ikke at flytte den
Hvis vi laver ledningslængder til hvor den er nu passer det fint
Vi skal sætte dem i serie og den første ledning skal være en del større end den anden

- HP tager 
- [ ] Ledningslængde til water maker


## Batteri status

- [x] Tilføj til Halvårlig status at tjekke batteri tilstand ✅ 2025-03-19
	- Fald af spænding når de bare står idle
	- Måske har battery monitors en variabel for det

Cyrix smart shunt
- Der tabes nok en spænding når batteriet bliver opladet. Når det stopper med at blive opladt (aka det er opladt) vil spænding nok ikke falde og derfor åbner skillerelæet

### Starterbatteri til lysmaskinen status

Der skal være en CHARGER og ikke en omformer eller inverter

- Morten tager det med på lørdag
- https://www.thansen.dk/vaerktoj-forbrug/batterilader-jumpstartere/batterilader/ctek-mxs-5.0a-12v-5amp-batterilader/n-233545771/pn-243231832
- https://www.victronenergy.com/chargers

## Multiplus inverter/charger

- [x] Hvor mange ampere giver multiplus inverter/charger når den oplader ✅ 2025-03-19
	- 70
- [x] Hvor langt skal ledningen være ✅ 2025-03-19
	- Kig figma
- [x] Kommer der et større draw når man når til starter batterierne (sidst i kæden) ✅ 2025-03-19
	- Ja der er nok et tab men 70 ampere er hvad den kan give så det er vel max

70 Ampere

## Komponenter

Vi kom af med lidt mere for vores komponenter end bådbutikken forslog

- BMV-702 
	- 950,00 x 2 x 0.8
- CYRIX-CT 12/24V-230A 
	- 821,00 x 2 x 0.8 

Bådbutikken:
- BMV700S
	- 806 x 2
- Victron cyrix-ct mikroprocessor relæ 120amp 12/24v
	- 360 x 2 


## Konklusion

Multiplus invertercharger kan levere 70 Ampere max.
- [x] Kan batterierne holde til det ✅ 2025-03-19
	- Ja de kan holde til 80A = 0.2 C
- [x] Hvor store ledning skal det være ✅ 2025-03-19
	- Længde + 70 ampere + online calculator
	- Victron Toolkit App


- [x] DanBrit skal køres ud til og så bytter vi den for en mindre version. Få den til at passe med Multiplus inverter/charger ✅ 2025-03-19
	- Spørg også om hvad batterierne kan holde til af ampere med hensyn til dimensionering

## Hurdles

-  Ledningslængder:
- Forbrugsbatterier -> Skillerelæ -> Navigationsbatteri -> Skillerelæ -> Starterbatteri
- Omvendt rækkefølge fra motoren
- [x] Føringsvejdesign motorrum ✅ 2025-03-19
- [x] Føringsvej mellem motorrum og Bestik ✅ 2025-03-19
- [x] Design el layout ✅ 2025-03-19
	- Fra Inverter til batteri
	- Fra batteri til batteri
		- Fra forbrug til navigation
		- Fra navigation til starter
	- Fra Batteri til forbrug
		- Forbrugsforbrug
		- Navigation
		- Starter
- [x] Charger til lysmaskinebatteriet ✅ 2025-03-19