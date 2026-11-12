# www.stepar-med.de – úplná sada zákaznických a právních stránek

Nová samostatná německá sada připravená 12. 11. 2026. Členění odpovídá rakouskému e-shopu, právní obsah je určen Německu.

| Sekce | Název v e-shopu | Stabilní iframe |
|---|---|---|
| Informationen für Kunden | Über unser Unternehmen | de/unternehmen.html |
| Informationen für Kunden | Versand und Zahlung | de/versand.html |
| Informationen für Kunden | Reklamationen | de/reklamace.html |
| Informationen für Kunden | Online widerrufen | de/online-widerrufen.html – pouze text nad nativním formulářem |
| Rechtliche Informationen | AGB | de/op.html |
| Rechtliche Informationen | Datenschutzerklärung | de/privacy.html |
| Rechtliche Informationen | Widerrufsbelehrung | de/otkaz.html |
| Rechtliche Informationen | Gesetzliche Gewährleistung und Verbraucherrechte | de/gewaehrleistung.html |

Základ URL: https://vaclavstepar.github.io/stepar-legal/

Rozcestník s náhledy a kopírovatelnými kódy: https://vaclavstepar.github.io/stepar-legal/de/

## Potvrzené doplnění vlastníka

Aktuální oprava vlastníka ze dne 12. 11. 2026: německý obchod používá **pouze dobírku, GoPay a platbu na účet (bankovní převod)**. PayPal se nepoužívá a platba na fakturu se splatností 14 dnů není potvrzenou německou platební metodou. Toto výslovné zadání nahrazuje dřívější převzetí rakouských platebních podmínek. Cenu dobírky ani konkrétní možnosti v bráně GoPay neodhadovat; zákazník je musí vidět před objednáním. Doprava zůstává GLS 6 EUR, zdarma při hodnotě zboží více než 200 EUR, podle dosavadního potvrzení.

GDPR nyní popisuje GoPay, bankovní převod a dobírku a neuvádí PayPal ani jeho předávání dat. GoPay je dle aktuální oficiální dokumentace GoPay Czech odštěpný závod, pobočka Worldline NV, IČO 22177469, Senovážné nám. 1736, 370 01 České Budějovice. Ostatní potvrzené služby Weby24/Nardo, POHODA/DragonCloud, GLS/Packeta, Google Analytics/Ads a Smartsupp s AI se touto opravou nemění. Konkrétní cookies, podmínky aktivace, retence a formulářový reCAPTCHA na německém webu se před startem musí zkontrolovat. Podrobnosti a zdroj ověření: de-payments-2026-11-12.md.

## Online widerrufen – nezaměňovat text s funkčním formulářem

Na rakouské stránce https://www.stepar-med.at/online-widerrufen-p1000007.htm byl ověřen nativní modul Weby24 pro vyhledání objednávky (orderLookup), pole order_number a email a tlačítko Suchen. Následující kroky nebyly bez skutečné objednávky ověřeny. Formulář nebyl odeslán a není doloženo doručení potvrzení.

V německé administraci musí být na stránce Online widerrufen pod textovým iframe vložen a správně nastaven odpovídající nativní modul Weby24. Nestačí zkopírovat rakouský action URL, který míří do cizího obchodu. Pokud nativní modul nesplňuje § 356a BGB, musí jej Weby24 upravit nebo nahradit odpovídající funkcí.

Povinná návaznost: viditelný trvalý odkaz „Vertrag widerrufen“, možnost zadat/potvrdit jméno, smlouvu nebo její část a elektronický kontakt, jasné finální tlačítko „Widerruf bestätigen“, neprodlené potvrzení s obsahem a datem/časem na trvalém nosiči. Povinný účet nesmí být bariérou pro hostovské objednávky. Vyhledání objednávky nesmí nepřiměřeně blokovat zákonné odstoupení. Finální postup je potřeba ověřit na povolené testovací objednávce včetně zákazníkova e-mailu a evidence u prodávajícího. Tato práce pouze připravila text pro vložení nad modul; německý formulář ani jeho backend nebyl nasazen nebo testovacím odstoupením aktivován.

## Oficiální oznámení EU o zákonné záruce

de/eu-gewaehrleistung-de.svg je nezměněný německý barevný vektor převzatý z oficiálního balíčku Evropské komise:

- https://commission.europa.eu/publications/practical-guidelines-and-high-resolution-vector-files-eu-notice-and-label-product-guarantees_en
- https://commission.europa.eu/document/download/27c45f1f-78a1-47a7-a7cc-adf23afee5ea_en?filename=SVG.zip
- soubor v ZIP: Legal guarantee_notice DE.svg

Je zobrazen na stránce o zákonné záruce, bez změny grafiky a s textovým vysvětlením. Samotný skrytý odkaz v patičce nesmí nahradit požadované zvýrazněné poskytnutí oznámení před objednávkou; vhodné umístění v německém obchodě ještě ověřit. GARAN obsažený v oficiálním vysvětlujícím oznámení není samostatným příslibem obchodní záruky ŠTĚPAŘ.

## Doplňující provozní omezení

Sekce „Über unser Unternehmen“ obsahuje i identifikační údaje pod označením Impressum – Anbieterkennzeichnung; v patičce je vhodný také jednoznačný odkaz Impressum na tutéž stránku. Německá doména neznamená německou provozovnu. Kontaktní e-mail info@stepar-med.de byl výslovně potvrzen vlastníkem dne 12. 11. 2026.

Nové texty nebyly vloženy do chráněného německého e-shopu ani do jeho menu. Jsou zveřejněny jako podklady a iframe zdroje. Nejde o potvrzení, že je obchod připraven k prodeji nebo že má v pořádku jednotlivé výrobky JUKL. Úplné podmínky spuštění viz de-shopstart-2026-11-12.md.

Po zveřejnění této první sady musí další úpravy zachovat archiv a projít konkrétním schválením vlastníka. Renderer scripts/render-de.py odmítá přepsat odlišný existující datovaný archiv; pro novou verzi je nutné přidat nový archivní soubor a datum. Pravidelná úloha Německa kontroluje všech osm stránek a eviduje výsledek pouze v Sites.
