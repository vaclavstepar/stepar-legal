# Zásady ochrany osobních údajů ŠTĚPAŘ

Stav: český pracovní návrh v0.4, 11. 9. 2026. Nejde o konečnou publikovanou právní verzi pro zákazníky. Veřejně ověřitelné údaje byly doplněny; neověřené konfigurace jsou výslovně popsány v textu, bez formulářových zástupných polí. Ostatní jazykové verze zásad zatím neexistují.

## Soubory

- `cz/privacy.html`: stabilní adresa iframe, načítá aktuální obsah s parametrem času a `cache: no-store`.
- `cz/privacy-current.html`: aktuální HTML, zatím označené jako pracovní návrh.
- `privacy/cz-source.md`: obsahový zdroj; udržovat současně s HTML.
- `archive/cz/privacy-2026-09-11-draft-v02.html`: první archivovaný návrh.
- `privacy/iframe-cz.txt`: iframe pro náhled, pevná výška 900 px se standardním posouváním; bez závislosti na skriptech Weby24.

Adresa: https://vaclavstepar.github.io/stepar-legal/cz/privacy.html

## Aktualizace

Při každé obsahové změně archivovat dosavadní current pod jednoznačným názvem s datem a verzí, upravit zdroj a current ve stejném commitu. Zachovat loader a jeho URL. Uvést změnu a zdroje v záznamu `privacy/reviews/YYYY-MM-DD.md`. Po commitu do main vyčkat na úspěšný existující workflow Deploy GitHub Pages a ověřit načtení veřejné adresy. Již otevřený iframe se sám periodicky neobnovuje; změna se projeví při dalším načtení po dokončení nasazení, s možným krátkým zpožděním CDN.

Před vydáním finální verze doplnit otevřené údaje, technicky zkontrolovat souhlasy a teprve potom odstranit označení pracovního návrhu. Publikování HTML nemění nastavení e-shopu. Hosting GitHub Pages a související technické požadavky návštěvníka jsou zohledněny. Nepřidávat neověřené doby uchování nebo domnělé mezinárodní záruky.

## Legislativní revize

Uživatel požaduje kontrolu jednou za šest měsíců a zapracování potvrzených relevantních změn. Kontrolovat platné i schválené budoucí předpisy, jejich účinnost, rozhodnutí a pokyny dozorových úřadů. Odlišit závazné právo, pokyny a návrhy. Změny provozu a konfigurace nelze zjistit jen právní rešerší a nesmějí se domýšlet.

Rozsah: společný základ GDPR/EU a země skutečně provozovaných e-shopů; výchozí CZ, SK, BG, ES, FR, HR, HU, PL, RO, SI a GR. Nejprve načíst aktuální soubory a kontext případných dalších domén. Aktualizovat jen skutečně existující jazykové verze privacy, nedotýkat se obchodních podmínek ani jejich samostatných automatizací.

Automatická úprava je autorizovaná pro potvrzené změny odpovídající známému provozu. Při nejasném právním dopadu, chybějícím provozním faktu nebo blokujících oprávněních připravit konkrétní návrh a oznámit, co brání dokončení; nevymýšlet fakta. Dokud je výchozí dokument draft, i legislativní aktualizace zachovávají draft. Výsledek revize zaznamenat včetně zdrojů, účinnosti, data a výsledku nasazení. Pokud se nic relevantního nezměnilo, lze zapsat výsledek bez úprav HTML a bez upozornění.

Plánovaná první kontrola: 11. 3. 2027, následně každých šest měsíců, Europe/Prague. Skutečné vytvoření automatizace potvrzuje až výsledek nástroje automatizací; samotný tento soubor žádnou úlohu nespouští. Půlroční interval není průběžný dohled mezi kontrolami.

## Otevřené technické podklady po revizi v0.4

Vyžádat export/snímky nastavení GA (uchování událostí a reset při aktivitě), Smartsupp (mazání konverzací). Dále skartační režim e-mailu a potvrzení Weby24/DragonCloud o logování, zálohách, umístění dat, přístupu podpory a přenosových zárukách. Ověřit cookie inventář a souhlasy v prohlížeči. Bez podkladů neoznačovat jako finální.

Na české doméně zjištěn konkrétní Seznam retargetingový kód s rtgId a voláním retargetingHit. Nezobecňovat na ostatní domény. Obecný wrapper Meta s lazy endpointem sám neprokazuje aktivní pixel. Uživatelské potvrzení o odstranění starého poskytovatele plateb platí.

## Aktuální provozní potvrzení uživatele — v0.4

Nejnovější výslovné potvrzení má přednost před staršími podklady i starým zadáním automatizace: remarketingové kampaně vůbec neprovozuje; zákaznické účty pravidelně nemaže; AI pouze odpovídá. Nevyžadovat nastavení členství v remarketingových publikách ani opětovné potvrzení pravomocí AI. Nalezený retargetingový kód není důkazem běžících kampaní; ověřit jeho datové přenosy a případně odstranit v administraci e-shopu. Pravidelnou revizi potřebnosti neaktivních účtů je třeba řešit jako provozní opatření; v textu neslibovat automatické mazání, které neprobíhá.
