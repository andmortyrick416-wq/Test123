# Laden of tanken?

Webapp die per dag laat zien of openbaar laden van de Cupra Formentor VZ e-Hybrid (245 pk) goedkoper is dan alleen op benzine rijden, vergeleken met de landelijke gemiddelde prijs van Euro95 en Euro98.

## Gebruik

Open `index.html` in een browser (of zet de repo op GitHub Pages). Er is geen installatie of server nodig.

- **Vandaag**: break-even kWh-prijs, prijsbord (laadpaal / Euro95 / Euro98) en de kosten van vier opties voor het aantal km dat je instelt.
- **Logboek**: vul per dag gereden km, geladen kWh en tarief in. De app rekent de kosten met laden, alleen Euro95 en alleen Euro98 uit, plus de besparing per dag en opgeteld (grafieken + tabel).
- **Instellingen**: verbruik, laadtarief, starttarief, accugrootte en prijzen aanpassen.

Gegevens worden opgeslagen in de browser (`localStorage`) van het apparaat waarop je de app gebruikt.

## Prijzen

- **Euro95**: wordt automatisch opgehaald uit CBS open data (dataset `80416ned`, gemiddelde pompprijzen per dag). Het CBS loopt een paar dagen achter.
- **Euro98**: het CBS publiceert die niet. De app rekent met Euro95 + een instelbare toeslag (standaard €0,14), of met een prijs die je zelf invult.

## Rekenmethode

- Elektrische km = geladen kWh ÷ stroomverbruik (kWh/100 km, gemeten vanaf de paal), maximaal de gereden km.
- Kosten met laden = kWh × tarief + starttarief + benzine voor de resterende km.
- Besparing = kosten alleen benzine − kosten met laden.
- Break-even kWh-prijs = benzineverbruik × benzineprijs ÷ stroomverbruik.

Standaardwaarden (aanpasbaar): 20 kWh/100 km, 6,6 l/100 km met lege accu, 11 kWh per volle laadbeurt, €0,39/kWh.
