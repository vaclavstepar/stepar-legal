# Společné zobrazení právních iframe všech e-shopů

Úprava 12. 11. 2026: společná vrstva pro všech 40 existujících stabilních právních/zákaznických loaderů. HTML zdroje schválených dokumentů `*-current.html` a historické archivy zůstávají přesně zachovány. Zarovnání a měření se používá až v zobrazené kopii.

## Jednorázové zapojení do Weby24

Do globální vlastní HTML/JavaScript šablony společné pro microshopy vložit jednou:

```html
<script src="https://vaclavstepar.github.io/stepar-legal/assets/legal-parent.js" defer></script>
```

Patří do pole podporujícího JavaScript (např. před koncové `</body>`), nikoli do pole pouze pro meta značky. Konkrétní administrace/umístění globálního JS není z dostupných podkladů doloženo. Tento krok zatím nebyl proveden v administraci Weby24; samotné zveřejnění v GitHubu jej neprovede. Zveřejněné vzorové iframe kódy přijímač obsahují a lze je použít i jednotlivě.

Iframe na jiné doméně nemůže přímo měnit rozměr svého rodičovského prvku. Dítě proto měří skutečnou výšku obsahu a posílá `postMessage`, rodič ověřuje původ, konkrétní okno a cestu v našem repozitáři. Teprve pak ruší původní pevnou/minimální výšku, upravuje rozměr a vypíná vnitřní posuvník. U starých iframe tedy není potřeba ručně přepisovat pevné výšky, pokud bude společný rodičovský skript opravdu zapojen na daném e-shopu.

## Co je společné

- `assets/legal-loader.js`: načtení aktuálního znění, zarovnání odstavců/seznamů do bloku, jazykové dělení slov, nadpisy a poslední řádky odstavců zarovnané přirozeně, odstranění velké koncové mezery, měření skutečné výšky těla bez závislosti na starém rozměru iframe.
- Reakce na změnu šířky, obsahu, písma a načtení obrázků. Iframe se může zvětšovat i zmenšovat. U oficiálního oznámení EU se nepřepisuje jeho grafika.
- `assets/legal-parent.js`: společný přijímač pro všechny microshopy. Přijímá pouze zprávy z `https://vaclavstepar.github.io`, z přesného vloženého okna a z adres `/stepar-legal/XX/*.html`. Odmítá neplatné a nepřiměřené rozměry. Původní rozměr zůstává jako nouzová varianta, dokud nedorazí ověřené měření.
- Opakované vložení společného skriptu nepřidává další přijímače.

Používat stabilní `XX/op.html`, `XX/privacy.html`, `XX/otkaz.html` atd., nikoli přímý `*-current.html`. Přímé aktuální dokumenty zůstávají přesnými schválenými zdroji a samy nezavádějí novou zobrazovací vrstvu. Budoucí aktualizace obsahu musí stabilní loadery a společnou vrstvu zachovat.

Při zapojení ověřit na skutečném e-shopu: dlouhé OP a krátkou stránku, mobilní šířku, zmenšení i zvětšení, více iframe současně a pozdní načtení obrázku. Dokud rodičovský skript není v e-shopu, automatická výška starých vložení není globálně aktivní. Srovnání je v `demo/iframe-layout.html`.
