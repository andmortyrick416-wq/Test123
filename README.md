# Laden of tanken?

Webapp die per dag laat zien of openbaar laden van de Cupra Formentor VZ e-Hybrid (245 pk) goedkoper is dan alleen op benzine rijden, vergeleken met de landelijke gemiddelde prijs van Euro95 en Euro98.

## Gebruik

Open `index.html` in een browser (of zet de repo op GitHub Pages). Er is geen installatie of server nodig.

- **Vandaag**: break-even kWh-prijs, prijsbord (laadpaal / Euro95 / Euro98) en de kosten van vier opties voor het aantal km dat je instelt.
- **Logboek**: vul per dag gereden km, geladen kWh en tarief in. De app rekent de kosten met laden, alleen Euro95 en alleen Euro98 uit, plus de besparing per dag en opgeteld (grafieken + tabel).
- **ANWB-factuur inlezen**: kies de maandelijkse factuurspecificatie (PDF) van ANWB. Alle laadsessies worden per dag opgeteld (kWh en kosten incl. btw) en in het logboek gezet, met de CBS-dagprijs van Euro95 voor die dag. Opnieuw inlezen geeft geen dubbele dagen. Het PDF-bestand wordt alleen in de browser gelezen.
- **Instellingen**: verbruik, laadtarief, starttarief, accugrootte en prijzen aanpassen.

Gegevens worden opgeslagen in de browser (`localStorage`) van het apparaat waarop je de app gebruikt.

## Prijzen

- **Euro95**: wordt automatisch opgehaald uit CBS open data (dataset `80416ned`, gemiddelde pompprijzen per dag). Het CBS loopt een paar dagen achter.
- **Euro98**: het CBS publiceert die niet. De app rekent met Euro95 + een instelbare toeslag (standaard €0,14), of met een prijs die je zelf invult.

## Rekenmethode

- Stroomverbruik = kWh per volle lading ÷ elektrisch bereik (45 km volgens het dashboard van de Formentor).
- Elektrische km = geladen kWh ÷ stroomverbruik, maximaal de gereden km.
- Rijmodus-advies: per rit (afstand, stad/gemengd/snelweg, accu bij vertrek) vergelijkt de app slim schakelen (E-Mode in de stad, Hybride op de snelweg), niet schakelen en alleen benzine. Verbruik per wegtype is een schatting: elektrisch stad 0,85× en snelweg 1,25× het gemiddelde, benzine stad 1,08× en snelweg 0,95×.
- Kosten met laden = kWh × tarief + starttarief + benzine voor de resterende km.
- Besparing = kosten alleen benzine − kosten met laden.
- Break-even kWh-prijs = benzineverbruik × benzineprijs ÷ stroomverbruik.

Standaardwaarden (aanpasbaar): 45 km elektrisch bereik, 11,3 kWh per volle laadbeurt, 6,6 l/100 km met lege accu, €0,39/kWh.
