# Ireland (www.stepar.ie) — legal and customer information

Version 1.0 — 12 November 2026. Operator ŠTĚPAŘ s.r.o.; contact info@stepar.ie.

| Customer page | Stable iframe URL |
|---|---|
| Terms and Conditions | https://vaclavstepar.github.io/stepar-legal/ie/op.html |
| Privacy Policy | https://vaclavstepar.github.io/stepar-legal/ie/privacy.html |
| Right of Withdrawal | https://vaclavstepar.github.io/stepar-legal/ie/otkaz.html |
| Complaints and Returns | https://vaclavstepar.github.io/stepar-legal/ie/reklamace.html |
| Statutory Consumer Rights | https://vaclavstepar.github.io/stepar-legal/ie/gewaehrleistung.html |
| Cancel an Order Online | https://vaclavstepar.github.io/stepar-legal/ie/online-widerrufen.html |
| About the Trader | https://vaclavstepar.github.io/stepar-legal/ie/unternehmen.html |
| Shipping and Payment | https://vaclavstepar.github.io/stepar-legal/ie/versand.html |

Each stable loader uses assets/legal-loader.js to render its *-current.html source. Immutable historical copies: archive/ie/2026-11-12/*.html.

## Confirmed shop facts

- Payment **GoPay only**; no cash on delivery, bank transfer, PayPal or invoice payment.
- Standard delivery free at a goods value **€200 or above**; the checkout displays the carrier/charge under €200 and actual offered options.
- Seller is Czech, not Irish; Irish-market consumer rights are reflected in the content.
- Company: ŠTĚPAŘ s.r.o., Střítežská 570, 572 01 Polička, Czech Republic; IČO 07371594; VAT CZ07371594.

## Must verify before declaring full legal launch readiness

1. Actual GoPay checkout flow, charge and method displays; order confirmation and durable copy of applicable terms.
2. Specific carriers/delivery times and any non-postable return goods; do not invent shipping amounts.
3. Live Irish cookie inventory, Google/Smartsupp/reCAPTCHA activation, retention settings, consent-revocation controls, and service-provider agreements; privacy policy describes possible integrations conditionally pending this audit.
4. Optional native Weby24 online cancellation lookup still has Czech field labels; verify localisation and end-to-end cancellation/acknowledgement on a permitted test order.
5. Dynamic iframe height is installed and live on www.stepar.ie via the default footer's hidden-title text box #1000000, which loads assets/legal-parent.js. All eight Irish document iframes were verified to resize automatically on 12 November 2026. The fixed fallback HTML height attributes remain only as a no-JavaScript fallback.
6. An additional Czech-language guarantee graphic may remain on the statutory-rights page; replace with an English notice or remove after checking layout.
7. Independent legal review recommended for a live cross-border Irish consumer shop.
8. Save PDF copies and link them to the private Sites legal-text archive when that Site is available for editing; Weby24 publication and GitHub are completed separately.

## Reference authorities

- CCPC online purchases: https://www.ccpc.ie/consumer-advice/consumer-rights/buying-goods/buying-online/
- CCPC Consumer Rights Act 2022 trader guidance: https://www.ccpc.ie/information-for-businesses/selling-goods-and-services/selling-products
- Data Protection Commission transparency: https://www.dataprotection.ie/en/organisations/know-your-obligations/transparency
- DPC cookies: https://dataprotection.ie/en/faqs/cookies/my-website-or-app-uses-cookies-and-other-tracking-do-i-have-get-consent-users

## Live iframe-height deployment (12 November 2026)

- `www.stepar.ie`: default footer container #4, text box #1000000; script loaded once, eight legal pages checked; measured frames: terms 2170px, privacy 1965px, withdrawal 1355px, complaints 935px, rights 988px, online cancellation 320px, company 572px, delivery 572px (desktop verification, content may change).
- `www.stepar.cz`: default footer container #4, text box #803; script saved separately in all 12 shop language versions (CS, BG, DE, EN, ES, FR, HR, HU, PL, RO, SK, SL). CZ terms and privacy frames verified with dynamic CSS height; the script is harmless on article pages without managed GitHub iframes.
- Other standalone Weby24 domains require their own installation of `<script src="https://vaclavstepar.github.io/stepar-legal/assets/legal-parent.js" defer></script>` in a footer text box; do not run broad microshop synchronisation merely to propagate this technical change, because it may overwrite independently maintained content.
- This parent script resizes only iframes hosted at `https://vaclavstepar.github.io/stepar-legal/{country}/{document}.html` and communicating with `assets/legal-loader.js`. Third-party legal iframes, such as `itrk.legal`, need their own supported height integration or provider-side cooperation.
