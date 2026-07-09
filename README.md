# RhinoFence Fencing Zimbabwe — Website

A fast, SEO-optimised static website for **RhinoFence Fencing Zimbabwe** — supply
and installation of clear view, palisade, diamond mesh, field, electric and game
fencing, razor wire, gates, steel structures and welding across Harare, Mvurwi
and nationwide.

Built as a **dependency-free static site** (plain HTML/CSS/JS, no build step) so
it loads fast, scores well on Core Web Vitals, and deploys anywhere.

## What's inside

```
.
├── index.html                 # Homepage
├── services/                  # 9 SEO landing pages (one per service)
│   ├── clear-view-fence.html
│   ├── palisade-fence.html
│   ├── electric-fence.html
│   ├── diamond-mesh-fence.html
│   ├── game-field-fence.html
│   ├── razor-wire.html
│   ├── gates-fabrication.html
│   ├── steel-structures.html
│   └── welding-steel-works.html
├── assets/                    # styles.css, main.js, logo.svg, social-card.svg
├── 404.html                   # Custom not-found page
├── robots.txt                 # Crawler directives + sitemap reference
├── sitemap.xml                # All indexable URLs
├── site.webmanifest           # PWA manifest
├── staticwebapp.config.json   # Azure routing, headers, 404 handling
└── .github/workflows/         # Azure Static Web Apps CI/CD
```

## SEO features baked in

- **Structured data (JSON-LD)** — `LocalBusiness`/`GeneralContractor`, per-service
  `Service`, `BreadcrumbList` and `FAQPage` schema for rich results.
- **Unique titles & meta descriptions** on every page, targeting local keywords
  (e.g. *"clear view fence Harare"*, *"electric fence Zimbabwe"*).
- **Open Graph + Twitter cards** with a branded social share image.
- **Semantic HTML**, breadcrumbs, internal linking between services.
- **`sitemap.xml` + `robots.txt`** ready for Google Search Console.
- **Fast & mobile-first** — inline SVG icons, system fonts, no external requests,
  responsive layout, `prefers-reduced-motion` support.
- Security headers via `staticwebapp.config.json` (CSP, X-Frame-Options, etc.).

## Business details

- **Phone:** 0714 194 324 · 0783 394 176
- **Email:** rhinofencefencingzimbabwe01@gmail.com
- **Harare:** 54 Jason Moyo, Three Archer House, 4th Floor
- **Mvurwi:** 57 Omeath Road, CBD
- **Facebook:** https://www.facebook.com/share/1DCCPf2GQW/
- WhatsApp quote button links to **wa.me/263714194324**.

## Deploy to Azure Static Web Apps (via GitHub)

The repo ships with a ready CI/CD workflow at
`.github/workflows/azure-static-web-apps.yml`.

1. In the [Azure Portal](https://portal.azure.com) → **Create resource** →
   **Static Web App**.
2. Choose **GitHub** as the deployment source and authorise Azure to access this
   repository (`admiremoyo/rhino`).
3. Set **Build Presets → Custom** with:
   - **App location:** `/`
   - **Api location:** *(leave blank)*
   - **Output location:** *(leave blank)*
4. Azure creates a deployment token and stores it as the repo secret
   **`AZURE_STATIC_WEB_APPS_API_TOKEN`**. (If you connect the repo through the
   portal, Azure may commit its own workflow file — you can delete the extra one
   and keep this pre-configured one, which uses `skip_app_build: true` since the
   site is already static.)
5. Push to `main` and the site deploys automatically. Every pull request gets a
   preview URL.

> **Note:** The site is static with no build step, so `skip_app_build: true` is
> set to upload files as-is.

## After going live — update the domain

Search-engine URLs (canonical tags, `sitemap.xml`, `robots.txt`, Open Graph,
JSON-LD) currently use the placeholder domain **`rhinofencezimbabwe.co.zw`**.
Once the real domain is confirmed and added in Azure (**Custom domains**),
find-and-replace that placeholder across the project, then commit.

## Regenerating service pages

Service pages are generated from a single template + content data. To edit
service copy, update `tools/build_services.py` and re-run:

```bash
python3 tools/build_services.py
```

## Recommended next steps

- Submit `sitemap.xml` in **Google Search Console** and **Bing Webmaster Tools**.
- Create/claim a **Google Business Profile** for the Harare and Mvurwi branches
  (huge for local "near me" ranking) and keep the name, address and phone (NAP)
  identical to this site.
- Add real project photos to build trust and improve image SEO.
- Gather Google reviews and add testimonials.

## Local preview

```bash
python3 -m http.server 8080
# then open http://localhost:8080
```
