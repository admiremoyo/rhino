# -*- coding: utf-8 -*-
"""Generate SEO-optimised service pages for RhinoFence Fencing Zimbabwe."""
import os, html

BASE = "https://rhinofencezimbabwe.co.zw"
# Output to <repo-root>/services regardless of where the script is run from
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "services")
os.makedirs(OUT, exist_ok=True)

# Each service: slug, name, title, meta, hero_sub, intro (list of paragraphs),
# benefits (list of (h,p)), applications (list), extra_h3 sections list of (h, [paras]),
# faqs (list of (q,a)), keywords
SERVICES = [
  {
    "slug":"clear-view-fence",
    "name":"Clear View Fence",
    "title":"Clear View Fence Zimbabwe | 358 Anti-Climb Security Fencing — RhinoFence",
    "meta":"Clear view (358 anti-climb) fencing supplied &amp; installed across Harare, Mvurwi and Zimbabwe. High-security, near-invisible mesh for homes, schools &amp; business. Free quote — 0714 194 324.",
    "keywords":"clear view fence Zimbabwe, 358 fence Harare, anti-climb fence, invisible wall fence, security mesh fence Zimbabwe",
    "hero_sub":"High-security, anti-climb 358 mesh fencing with almost invisible sightlines — premium perimeter protection that never blocks your view.",
    "intro":[
      "Clear view fencing (also known as 358 or &ldquo;invisible wall&rdquo; fencing) is the gold standard in modern perimeter security. Its tightly welded mesh apertures are too small for fingers or tools to grip, making it extremely difficult to climb or cut &mdash; while the slim profile keeps your view of the property virtually unobstructed.",
      "RhinoFence manufactures and installs clear view fencing across Harare, Mvurwi and the whole of Zimbabwe for homes, schools, embassies, commercial premises and high-security sites that demand both protection and a clean, professional appearance."
    ],
    "benefits":[
      ("Anti-Climb &amp; Anti-Cut","The 76.2 x 12.7&nbsp;mm mesh leaves no foothold and resists bolt cutters, delaying and deterring intruders far longer than standard fencing."),
      ("Near-Invisible Sightlines","The narrow wire profile all but disappears at a distance, preserving views, natural light and kerb appeal."),
      ("Powder-Coated &amp; Galvanised","Hot-dip galvanised then powder-coated to resist rust and fading under the Zimbabwean sun for years of low-maintenance service."),
      ("Electric-Fence Ready","Easily topped with an energised wire system or razor coil for a layered, alarmed security perimeter."),
    ],
    "applications":["Residential homes &amp; estates","Schools, colleges &amp; universities","Embassies &amp; government sites","Commercial &amp; retail premises","Substations &amp; utilities","Data centres &amp; warehouses"],
    "sections":[
      ("Why choose clear view over palisade?",["Both are excellent, but clear view offers superior anti-climb performance and a more refined look, while palisade is more economical for large industrial runs. During your free assessment we'll help you weigh security level, budget and aesthetics to pick the right system &mdash; or combine both."]),
    ],
    "faqs":[
      ("How tall can a clear view fence be?","We commonly install 1.8&nbsp;m to 3.0&nbsp;m panels, and can go higher for high-security sites. Taller panels and an electric-fence top dramatically increase deterrence."),
      ("Is clear view fencing worth the extra cost?","For security and appearance, yes. It resists climbing and cutting far better than mesh or palisade and keeps sightlines open, which is why it's specified for schools, embassies and premium homes."),
    ],
  },
  {
    "slug":"palisade-fence",
    "name":"Palisade Fence",
    "title":"Palisade Fencing Zimbabwe | Steel Palisade Supply &amp; Install — RhinoFence",
    "meta":"Durable steel palisade fencing manufactured &amp; installed in Harare, Mvurwi &amp; nationwide. Cost-effective, high-deterrent security for homes, industry &amp; farms. Free quote — 0714 194 324.",
    "keywords":"palisade fence Zimbabwe, steel palisade Harare, industrial fencing Zimbabwe, security palisade, durawall alternative",
    "hero_sub":"Rugged, cost-effective steel palisade fencing with pointed pales &mdash; a proven, high-deterrent boundary for industrial, commercial and residential sites.",
    "intro":[
      "Steel palisade fencing is one of the most popular and economical security solutions in Zimbabwe. Its vertical pales with spiked or splayed tops are hard to climb and highly visible, sending a clear message to would-be intruders while standing up to years of hard use.",
      "RhinoFence fabricates and installs palisade fencing to order &mdash; choosing pale profile, height and finish to match your security needs and budget, from single-property boundaries to large factory perimeters."
    ],
    "benefits":[
      ("Excellent Value","Palisade delivers strong physical security at a lower cost per metre than most alternatives &mdash; ideal for long industrial and farm boundaries."),
      ("High Deterrence","Pointed or splayed pale tops and a tall, rigid structure make climbing difficult and obvious."),
      ("Tough &amp; Long-Lasting","Heavy-gauge steel, galvanised and optionally powder-coated, resists corrosion and impact."),
      ("Low Maintenance","No gaps for debris, easy to inspect, and simple to repair pale-by-pale if ever damaged."),
    ],
    "applications":["Factories &amp; warehouses","Residential boundaries","Schools &amp; institutions","Farms &amp; agricultural sites","Yards &amp; depots","Substations &amp; plant"],
    "sections":[
      ("Finishes &amp; options",["Choose from &lsquo;W&rsquo; or &lsquo;D&rsquo; section pales, single or triple-pointed tops, and heights typically from 1.8&nbsp;m to 3.0&nbsp;m. Add an electric-fence top or razor coil for an extra layer of protection."]),
    ],
    "faqs":[
      ("Is palisade cheaper than clear view fencing?","Generally yes &mdash; palisade is very cost-effective for long runs, which is why it's popular for industrial and farm perimeters. Clear view offers better anti-climb performance and looks; we'll help you choose."),
      ("Can palisade be powder-coated in a colour?","Yes. We galvanise for rust protection and can powder-coat in your chosen colour for a smart, durable finish."),
    ],
  },
  {
    "slug":"electric-fence",
    "name":"Electric Fence",
    "title":"Electric Fence Installation Zimbabwe | Security Electric Fencing — RhinoFence",
    "meta":"Electric fence installation in Harare, Mvurwi &amp; across Zimbabwe. Wall-top &amp; free-standing energised security with alarm integration for homes, business &amp; farms. Free quote — 0714 194 324.",
    "keywords":"electric fence Zimbabwe, electric fence installation Harare, wall top electric fence, security electric fencing, energizer Zimbabwe",
    "hero_sub":"Energised perimeter security with alarm integration &mdash; a powerful, always-on first line of defence for walls, fences and open boundaries.",
    "intro":[
      "An electric fence is one of the most effective deterrents available: it delivers a safe but sharp shock on contact and triggers an alarm the moment the line is tampered with or cut. It turns a passive wall into an active, monitored barrier.",
      "RhinoFence supplies and installs wall-top and free-standing electric fencing throughout Zimbabwe, complete with quality energisers, warning signage and optional integration to your alarm or armed-response system."
    ],
    "benefits":[
      ("Active Deterrence &amp; Alarm","Intruders are shocked and detected &mdash; the system alarms on cut, short or climb attempts, alerting you or your response company instantly."),
      ("Safe &amp; Compliant","Energisers deliver a high-voltage, low-current pulse that deters without lasting harm, installed with the required warning signage."),
      ("Flexible Configurations","Wall-top brackets, free-standing posts or fence-topping &mdash; tailored to your existing perimeter."),
      ("Integrates With Your Security","Connect to alarms, sirens, and armed-response monitoring for a complete layered system."),
    ],
    "applications":["Home &amp; estate walls","Commercial &amp; industrial sites","Warehouses &amp; yards","Farms &amp; smallholdings","Schools &amp; institutions","Wildlife &amp; livestock control"],
    "sections":[
      ("Maintenance &amp; support",["A well-installed electric fence needs periodic checks of tension, energiser output and vegetation clearance. RhinoFence offers installation plus fault-finding and repairs to keep your system energised and reliable."]),
    ],
    "faqs":[
      ("Is an electric fence safe for my family and pets?","Yes. A compliant energiser delivers a short, high-voltage, low-current pulse &mdash; startling and painful but not dangerous. We install to standard with clear warning signs."),
      ("Can you connect the fence to my alarm?","Absolutely. We can integrate the fence energiser with sirens, alarm panels and armed-response monitoring so a breach triggers an immediate alert."),
    ],
  },
  {
    "slug":"diamond-mesh-fence",
    "name":"Diamond Mesh Fence",
    "title":"Diamond Mesh &amp; Chain Link Fencing Zimbabwe — RhinoFence",
    "meta":"Galvanised &amp; PVC-coated diamond mesh (chain link) fencing supplied &amp; installed in Harare, Mvurwi &amp; nationwide. Affordable, versatile boundaries. Free quote — 0714 194 324.",
    "keywords":"diamond mesh fence Zimbabwe, chain link fence Harare, wire mesh fencing, PVC coated fence, sports ground fencing Zimbabwe",
    "hero_sub":"Galvanised and PVC-coated chain-link fencing &mdash; the versatile, affordable choice for yards, sports grounds, schools and enclosures.",
    "intro":[
      "Diamond mesh (chain-link) fencing is the practical, budget-friendly way to define and secure a boundary. It's quick to install, lets light and air through, and suits everything from residential yards to large sports and industrial enclosures.",
      "RhinoFence supplies and installs galvanised and PVC-coated diamond mesh across Zimbabwe in a range of heights and wire gauges, on steel or concrete posts to suit your site."
    ],
    "benefits":[
      ("Affordable Coverage","The most economical way to enclose large areas without sacrificing durability."),
      ("Galvanised or PVC-Coated","Choose bright galvanised for value or green PVC-coated for extra weather resistance and a neat finish."),
      ("Versatile Heights","From low garden and pool enclosures to tall sports-ground and security perimeters."),
      ("Airy &amp; Open","Maintains visibility and airflow &mdash; ideal for schools, courts and animal enclosures."),
    ],
    "applications":["Residential yards","Schools &amp; playgrounds","Sports grounds &amp; courts","Warehouses &amp; depots","Poultry &amp; animal runs","Boundary demarcation"],
    "sections":[
      ("Posts &amp; straining",["We install on galvanised steel or precast concrete posts with properly strained line wires and tensioners, so your mesh stays taut and true for years."]),
    ],
    "faqs":[
      ("What's the difference between galvanised and PVC-coated mesh?","Galvanised mesh is zinc-coated for rust resistance and best value. PVC-coated adds a plastic layer for extra weather protection and a tidy green finish &mdash; ideal for schools and homes."),
      ("How tall can diamond mesh fencing go?","Commonly 1.2&nbsp;m to 3.0&nbsp;m. Taller runs for sports grounds and security sites are no problem with the right posts and straining."),
    ],
  },
  {
    "slug":"game-field-fence",
    "name":"Game &amp; Field Fence",
    "title":"Game &amp; Field Fencing Zimbabwe | Farm &amp; Wildlife Fencing — RhinoFence",
    "meta":"Heavy-duty game, bonnox &amp; field (veld-span) fencing for farms and wildlife reserves across Zimbabwe. Supplied &amp; installed by RhinoFence. Free quote — 0714 194 324.",
    "keywords":"game fence Zimbabwe, field fence, bonnox fence, farm fencing Zimbabwe, veldspan fence, wildlife fence, cattle fence",
    "hero_sub":"Heavy-duty bonnox, veld-span and field fencing for farms, wildlife reserves and large agricultural boundaries &mdash; built to contain and protect.",
    "intro":[
      "Game and field fencing keeps livestock and wildlife where they belong and keeps threats out, over boundaries that can stretch for kilometres. It has to be strong, correctly tensioned and built to survive the elements and the animals it contains.",
      "RhinoFence supplies and installs game fence, bonnox and field (veld-span) fencing across Zimbabwe for farms, ranches, conservancies and smallholdings &mdash; with the straining, posts and gates to match."
    ],
    "benefits":[
      ("Built for Scale","Efficient systems and experienced teams for long farm and reserve perimeters, delivered on schedule."),
      ("Strong &amp; Adaptable","Graduated mesh spacing and high-tensile wire contain everything from poultry to large game."),
      ("Weather-Resistant","Galvanised wire and treated or steel standards stand up to sun, rain and rough terrain."),
      ("Complete Systems","We add straining posts, droppers, gates and electric top-wires for predator and poaching control."),
    ],
    "applications":["Cattle &amp; livestock farms","Game reserves &amp; conservancies","Wildlife &amp; safari lodges","Cropland protection","Smallholdings &amp; plots","Boundary &amp; perimeter lines"],
    "sections":[
      ("Add an electric line",["For predator, poaching or breakout control we can top or interleave your game fence with an energised wire system &mdash; a proven way to protect livestock and wildlife over large areas."]),
    ],
    "faqs":[
      ("Do you install over long farm boundaries?","Yes. We're set up for large-scale farm and reserve fencing with the straining, posts and logistics to install kilometres of line efficiently."),
      ("Can you combine field fencing with electric wires?","Definitely. Adding energised top or offset wires greatly improves predator and poaching control and helps keep livestock contained."),
    ],
  },
  {
    "slug":"razor-wire",
    "name":"Razor Wire",
    "title":"Razor Wire Zimbabwe | Concertina &amp; Wall-Top Razor Coil — RhinoFence",
    "meta":"Concertina &amp; flat-wrap razor wire supplied &amp; installed on walls and fences across Harare, Mvurwi &amp; Zimbabwe. Formidable anti-intruder barrier. Free quote — 0714 194 324.",
    "keywords":"razor wire Zimbabwe, concertina wire Harare, wall top razor wire, barbed wire, security wire Zimbabwe",
    "hero_sub":"Concertina and flat-wrap razor coils to top walls and fences &mdash; a formidable, low-cost barrier that stops intruders in their tracks.",
    "intro":[
      "Razor wire is one of the most effective and affordable ways to reinforce an existing wall or fence. Its sharp, hooked blades make climbing over practically impossible and add a strong visual deterrent to any perimeter.",
      "RhinoFence supplies and installs concertina and flat-wrap razor wire throughout Zimbabwe &mdash; on wall tops, fence lines and as free-standing barriers &mdash; using galvanised, corrosion-resistant coils and secure fixings."
    ],
    "benefits":[
      ("Powerful Deterrent","Sharp, gripping blades make scaling a wall or fence extremely difficult and dangerous for intruders."),
      ("Cost-Effective Upgrade","An economical way to dramatically boost the security of walls and fences you already have."),
      ("Corrosion-Resistant","Galvanised coils withstand the weather for long-lasting protection."),
      ("Flexible Mounting","Wall-top, fence-top, single or double coil, or combined with electric fencing for a layered barrier."),
    ],
    "applications":["Boundary walls","Palisade &amp; mesh fence tops","Warehouses &amp; yards","Industrial sites","Farms &amp; depots","High-security perimeters"],
    "sections":[
      ("Pair it with electric fencing",["Razor wire and electric fencing work brilliantly together &mdash; the razor coil physically blocks climbing while the energised line shocks and alarms. Ask us about a combined wall-top system."]),
    ],
    "faqs":[
      ("Concertina or flat-wrap razor wire — which is better?","Concertina (spring coil) offers the most formidable barrier and is hardest to breach; flat-wrap is neater and lower-profile. We'll recommend based on your risk and budget."),
      ("Can you fit razor wire on my existing wall?","Yes. We install razor coil on wall tops and existing fences with secure brackets and fixings, on its own or combined with an electric fence."),
    ],
  },
  {
    "slug":"gates-fabrication",
    "name":"Gates Fabrication",
    "title":"Gate Fabrication Zimbabwe | Custom Sliding &amp; Swing Gates — RhinoFence",
    "meta":"Custom steel gate fabrication in Harare, Mvurwi &amp; nationwide — sliding, swing &amp; pedestrian gates with automation. Made to your design by RhinoFence. Free quote — 0714 194 324.",
    "keywords":"gate fabrication Zimbabwe, custom gates Harare, sliding gate, swing gate, automated gate Zimbabwe, driveway gate, steel gates",
    "hero_sub":"Custom-built sliding, swing and pedestrian gates &mdash; manufactured to your design and finish, with automation and access-control options.",
    "intro":[
      "Your gate is the working part of your perimeter &mdash; used every day and often the weakest point if it's poorly made. A well-fabricated gate is strong, smooth-running and matched to the fence or wall around it.",
      "RhinoFence designs and fabricates custom steel gates for homes, businesses and industrial sites across Zimbabwe &mdash; sliding, swing and pedestrian &mdash; and can automate them with remotes, keypads and intercoms."
    ],
    "benefits":[
      ("Made to Measure","Every gate is fabricated to your opening, style and security level &mdash; not an off-the-shelf compromise."),
      ("Strong &amp; Smooth","Quality steel, proper bracing and rollers or hinges for a gate that runs true for years."),
      ("Automation Ready","Add sliding or swing motors with remote, keypad or intercom access and battery backup."),
      ("Matched Finish","Galvanised and powder-coated to complement your palisade, clear view or wall."),
    ],
    "applications":["Residential driveways","Commercial entrances","Industrial &amp; yard gates","Pedestrian &amp; wicket gates","Farm &amp; estate gates","Automated access points"],
    "sections":[
      ("Automation &amp; access control",["We fit reliable gate motors with remotes, keypads, intercoms and safety beams, plus battery backup for load-shedding &mdash; turning your gate into a convenient, controlled access point."]),
    ],
    "faqs":[
      ("Can you automate an existing gate?","Often yes &mdash; if the gate is sound we can retrofit a suitable motor and access control. If it's worn, we can fabricate a new gate built for automation."),
      ("Do gate motors work during load-shedding?","Yes. We fit motors with battery backup so your gate keeps operating through power cuts."),
    ],
  },
  {
    "slug":"steel-structures",
    "name":"Steel Structures",
    "title":"Steel Structures &amp; Fabrication Zimbabwe | Carports, Trusses — RhinoFence",
    "meta":"Fabricated steel structures in Harare, Mvurwi &amp; nationwide — carports, trusses, frames, durawall posts &amp; more, engineered and welded to spec by RhinoFence. Free quote — 0714 194 324.",
    "keywords":"steel structures Zimbabwe, steel fabrication Harare, carport, roof trusses, steel frame, durawall posts Zimbabwe",
    "hero_sub":"Fabricated steel frames, carports, trusses and durawall posts &mdash; engineered, welded and installed to spec for strength that lasts.",
    "intro":[
      "From a simple carport to structural roof trusses and industrial frames, quality steelwork comes down to accurate fabrication and sound welding. Get those right and you have a structure that stands square and safe for decades.",
      "RhinoFence fabricates and installs steel structures across Zimbabwe &mdash; carports, shade frames, trusses, mezzanine and support frames, durawall posts and more &mdash; built to your drawings or ours."
    ],
    "benefits":[
      ("Engineered to Spec","Structures fabricated to your requirements and drawings, with the right sections and connections for the load."),
      ("Quality Welding","Clean, strong welds by experienced fabricators for structural integrity you can rely on."),
      ("Protected Finishes","Galvanised or painted to resist rust and weather in outdoor and industrial settings."),
      ("Supply &amp; Install","We fabricate in-shop and erect on site, keeping the whole job under one accountable team."),
    ],
    "applications":["Carports &amp; shade ports","Roof trusses &amp; purlins","Industrial &amp; support frames","Durawall &amp; fence posts","Mezzanines &amp; platforms","Custom steel projects"],
    "sections":[
      ("Bespoke fabrication",["Have a drawing or an idea? Bring it to us. Our welding and steel-works team can fabricate to your specification &mdash; one-off or in batches &mdash; and finish it to suit its environment."]),
    ],
    "faqs":[
      ("Do you work from my drawings?","Yes. We fabricate to your drawings and specifications, or help develop a practical design if you only have a concept."),
      ("Can you both fabricate and install on site?","Yes. We manufacture in our workshop and erect on site, so one team is accountable for the finished structure."),
    ],
  },
  {
    "slug":"welding-steel-works",
    "name":"Welding &amp; Steel Works",
    "title":"Welding &amp; Steel Works Zimbabwe | On-Site Fabrication &amp; Repairs — RhinoFence",
    "meta":"General welding &amp; steel fabrication in Harare, Mvurwi &amp; nationwide — burglar bars, balustrades, repairs &amp; bespoke metalwork by RhinoFence. Free quote — 0714 194 324.",
    "keywords":"welding Zimbabwe, steel works Harare, fabrication, burglar bars, balustrades, metalwork Zimbabwe, on-site welding",
    "hero_sub":"General fabrication, on-site welding and repairs &mdash; from balustrades and burglar bars to bespoke metalwork, done properly.",
    "intro":[
      "Not every job is a fence. RhinoFence's welding and steel-works division handles the everyday and the custom &mdash; security bars, balustrades, brackets, repairs and one-off fabrication &mdash; with the same standard of workmanship we put into our fencing.",
      "Based in Harare and Mvurwi and working across Zimbabwe, we offer workshop fabrication and on-site welding for homes, businesses and industry."
    ],
    "benefits":[
      ("Versatile Fabrication","Burglar bars, gates, grilles, balustrades, brackets, stands and custom pieces &mdash; if it's steel, we can make it."),
      ("On-Site Welding","Mobile welding for repairs and installations where the work can't come to the workshop."),
      ("Quality Craftsmanship","Neat, strong welds and a proper finish &mdash; work you'll be happy to show off."),
      ("Repairs &amp; Modifications","We fix, reinforce and modify existing steelwork, gates and structures."),
    ],
    "applications":["Burglar bars &amp; window guards","Balustrades &amp; railings","Custom gates &amp; grilles","Brackets, stands &amp; frames","Repairs &amp; reinforcement","Bespoke metal fabrication"],
    "sections":[
      ("Tell us what you need",["Whether it's a set of burglar bars, a balustrade for a staircase, or a custom bracket you can't buy off the shelf, send us a photo or sketch and we'll quote to fabricate and fit it."]),
    ],
    "faqs":[
      ("Do you do small welding jobs and repairs?","Yes. No job is too small &mdash; from a single repair or set of burglar bars to bespoke fabrication, we're happy to help."),
      ("Can you weld on site?","Yes. We offer mobile on-site welding for repairs and installations that can't be done in the workshop."),
    ],
  },
]

# Nav service list for cross-linking (name -> slug)
ALL = [(s["name"], s["slug"]) for s in SERVICES]

def icon_arrow():
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def render(s):
    url = f"{BASE}/services/{s['slug']}.html"
    # related services (all others)
    related = [x for x in ALL if x[1] != s["slug"]][:6]
    related_html = "\n".join(
        f'          <li><a href="/services/{sl}.html">{nm}</a></li>' for nm, sl in related
    )
    benefits_html = "\n".join(
        f'''        <div class="card">
          <h3>{h}</h3>
          <p>{p}</p>
        </div>''' for h, p in s["benefits"]
    )
    apps_html = "\n".join(f"        <li>{a}</li>" for a in s["applications"])
    intro_html = "\n".join(f"      <p>{p}</p>" for p in s["intro"])
    sections_html = ""
    for h, paras in s["sections"]:
        ps = "\n".join(f"      <p>{p}</p>" for p in paras)
        sections_html += f"\n      <h3>{h}</h3>\n{ps}\n"
    faqs_html = "\n".join(
        f'''      <details{" open" if i==0 else ""}>
        <summary>{q}</summary>
        <p>{a}</p>
      </details>''' for i, (q, a) in enumerate(s["faqs"])
    )
    # FAQ JSON-LD
    faq_json = ",\n".join(
        '''    {
      "@type": "Question",
      "name": "%s",
      "acceptedAnswer": { "@type": "Answer", "text": "%s" }
    }''' % (q.replace('"','\\"'), _plain(a)) for q, a in s["faqs"]
    )
    name_plain = s["name"].replace("&amp;", "&")

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0f1115">
<title>{s["title"]}</title>
<meta name="description" content="{s["meta"]}">
<meta name="keywords" content="{s["keywords"]}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="RhinoFence Fencing Zimbabwe">
<meta property="og:title" content="{name_plain} — RhinoFence Fencing Zimbabwe">
<meta property="og:description" content="{s["meta"]}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_ZW">
<meta property="og:image" content="{BASE}/assets/social-card.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{name_plain} — RhinoFence Zimbabwe">
<meta name="twitter:description" content="{s["meta"]}">
<meta name="twitter:image" content="{BASE}/assets/social-card.svg">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/logo.svg">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/assets/styles.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "{name_plain}",
  "name": "{name_plain} — Zimbabwe",
  "provider": {{
    "@type": "GeneralContractor",
    "name": "RhinoFence Fencing Zimbabwe",
    "telephone": "+263714194324",
    "email": "rhinofencefencingzimbabwe01@gmail.com",
    "url": "{BASE}/"
  }},
  "areaServed": [
    {{ "@type": "Country", "name": "Zimbabwe" }},
    {{ "@type": "City", "name": "Harare" }},
    {{ "@type": "City", "name": "Mvurwi" }}
  ],
  "url": "{url}",
  "description": "{_plain(s['meta'])}"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Services", "item": "{BASE}/#services" }},
    {{ "@type": "ListItem", "position": 3, "name": "{name_plain}", "item": "{url}" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{faq_json}
  ]
}}
</script>
</head>
<body>

<header class="site-header">
  <div class="container nav">
    <a class="brand" href="/" aria-label="RhinoFence Fencing Zimbabwe home">
      <img src="/assets/logo.svg" width="38" height="38" alt="" aria-hidden="true">
      <span>Rhino<b>Fence</b></span>
    </a>
    <nav aria-label="Primary">
      <ul class="nav-links" id="menu">
        <li><a href="/#services">Services</a></li>
        <li><a href="/#why">Why Us</a></li>
        <li><a href="/#process">Process</a></li>
        <li><a href="/#locations">Locations</a></li>
        <li><a href="/#faq">FAQ</a></li>
        <li><a href="/#contact">Contact</a></li>
      </ul>
    </nav>
    <div class="nav-cta">
      <a class="btn btn--ghost" href="tel:+263714194324">Call 0714 194 324</a>
      <a class="btn btn--primary" href="/#quote">Free Quote</a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-controls="menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<main>
<section class="page-hero">
  <div class="container">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a> &rsaquo; <a href="/#services">Services</a> &rsaquo; <span>{s["name"]}</span>
    </nav>
    <p class="eyebrow">Fencing &amp; Steel Works · Zimbabwe</p>
    <h1>{s["name"]} in Zimbabwe</h1>
    <p class="lead">{s["hero_sub"]}</p>
    <div class="hero-cta" style="margin-top:24px">
      <a class="btn btn--primary btn--lg" href="/#quote">Get a Free Quote</a>
      <a class="btn btn--wa btn--lg" href="https://wa.me/263714194324" target="_blank" rel="noopener">Chat on WhatsApp</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container layout-2col">
    <div class="prose">
{intro_html}

      <h2>Benefits of {s["name"]}</h2>
      <div class="grid grid--2" style="margin:24px 0 8px">
{benefits_html}
      </div>
{sections_html}
      <h3>Where it's used</h3>
      <ul>
{apps_html}
      </ul>

      <h2 style="margin-top:36px">{s["name"]} FAQs</h2>
      <div class="faq" style="margin-top:20px">
{faqs_html}
      </div>
    </div>

    <aside>
      <div class="sidebar-cta">
        <h3>Free {s["name"]} Quote</h3>
        <p style="font-size:.95rem">Serving Harare, Mvurwi &amp; all of Zimbabwe. Tell us about your site and we'll quote fast.</p>
        <a class="btn btn--primary" href="/#quote" style="width:100%;margin-bottom:10px">Request a Quote</a>
        <a class="btn btn--wa" href="https://wa.me/263714194324" target="_blank" rel="noopener" style="width:100%;margin-bottom:20px">WhatsApp Us</a>
        <h4 style="color:var(--white);margin:0 0 10px">Other services</h4>
        <ul>
{related_html}
        </ul>
      </div>
    </aside>
  </div>
</section>

<section class="section" style="padding-top:0" id="contact">
  <div class="container">
    <div class="cta-band">
      <h2>Ready to Secure Your Property?</h2>
      <p>Get a free, no-obligation quote for {s["name"].lower()} anywhere in Zimbabwe. Call, WhatsApp or email RhinoFence today.</p>
      <div class="cta-actions">
        <a class="btn btn--primary btn--lg" href="tel:+263714194324">📞 Call 0714 194 324</a>
        <a class="btn btn--ghost btn--lg" href="https://wa.me/263714194324" target="_blank" rel="noopener">💬 WhatsApp Us</a>
        <a class="btn btn--ghost btn--lg" href="mailto:rhinofencefencingzimbabwe01@gmail.com">✉️ Email Us</a>
      </div>
    </div>
  </div>
</section>
</main>

<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div class="foot-about">
        <a class="brand" href="/" style="margin-bottom:14px">
          <img src="/assets/logo.svg" width="38" height="38" alt="" aria-hidden="true">
          <span>Rhino<b>Fence</b></span>
        </a>
        <p>RhinoFence Fencing Zimbabwe — clear view, palisade, diamond mesh, electric &amp; game fencing, razor wire, gates, steel structures and welding across Harare, Mvurwi and nationwide.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="/services/clear-view-fence.html">Clear View Fence</a></li>
          <li><a href="/services/palisade-fence.html">Palisade Fence</a></li>
          <li><a href="/services/electric-fence.html">Electric Fence</a></li>
          <li><a href="/services/diamond-mesh-fence.html">Diamond Mesh Fence</a></li>
          <li><a href="/services/razor-wire.html">Razor Wire</a></li>
        </ul>
      </div>
      <div>
        <h4>More</h4>
        <ul>
          <li><a href="/services/game-field-fence.html">Game &amp; Field Fence</a></li>
          <li><a href="/services/gates-fabrication.html">Gates Fabrication</a></li>
          <li><a href="/services/steel-structures.html">Steel Structures</a></li>
          <li><a href="/services/welding-steel-works.html">Welding &amp; Steel Works</a></li>
          <li><a href="/">Home</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul class="foot-contact">
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7l.7 3a2 2 0 0 1-.5 1.9L7.6 10a16 16 0 0 0 6 6l1.4-1.6a2 2 0 0 1 1.9-.5l3 .7A2 2 0 0 1 22 16.9z"/></svg> <a href="tel:+263714194324">0714 194 324</a></li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7l.7 3a2 2 0 0 1-.5 1.9L7.6 10a16 16 0 0 0 6 6l1.4-1.6a2 2 0 0 1 1.9-.5l3 .7A2 2 0 0 1 22 16.9z"/></svg> <a href="tel:+263783394176">0783 394 176</a></li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 6 10 7L22 6"/></svg> <a href="mailto:rhinofencefencingzimbabwe01@gmail.com">Email us</a></li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></svg> Harare &amp; Mvurwi</li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <p>© <span data-year>2026</span> RhinoFence Fencing Zimbabwe. All rights reserved.</p>
      <div class="social">
        <a href="https://www.facebook.com/share/1DCCPf2GQW/" target="_blank" rel="noopener" aria-label="RhinoFence on Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 9h3l.5-3H14V4.5c0-.9.3-1.5 1.6-1.5H18V.2A22 22 0 0 0 15.4 0C12.9 0 11 1.5 11 4.2V6H8v3h3v9h3z"/></svg></a>
        <a href="https://wa.me/263714194324" target="_blank" rel="noopener" aria-label="RhinoFence on WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.5 15.2L2 22l4.9-1.3A10 10 0 1 0 12 2zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-2.9.8.8-2.8-.2-.3A8 8 0 1 1 12 20z"/></svg></a>
      </div>
    </div>
  </div>
</footer>

<a class="fab" href="https://wa.me/263714194324" target="_blank" rel="noopener" aria-label="Chat with RhinoFence on WhatsApp">
  <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.5 15.2L2 22l4.9-1.3A10 10 0 1 0 12 2zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-2.9.8.8-2.8-.2-.3A8 8 0 1 1 12 20zm4.4-6c-.2-.1-1.4-.7-1.6-.8s-.4-.1-.5.1-.6.8-.8 1-.3.2-.5 0a6.5 6.5 0 0 1-3.2-2.8c-.2-.4.2-.4.6-1.2.1-.2 0-.3 0-.5s-.5-1.3-.7-1.7-.4-.4-.5-.4h-.5a1 1 0 0 0-.7.3A3 3 0 0 0 6.3 9c0 1.8 1.3 3.5 1.5 3.7s2.6 4 6.3 5.4c.9.4 1.6.6 2.1.5.6-.1 1.4-.6 1.6-1.1s.2-1 .2-1.1-.2-.2-.5-.4z"/></svg>
</a>

<script src="/assets/main.js" defer></script>
</body>
</html>
'''

def _plain(t):
    # strip html entities/tags for JSON-LD text
    t = t.replace("&amp;", "&").replace("&mdash;", "—").replace("&ldquo;", "“").replace("&rdquo;", "”").replace("&lsquo;","‘").replace("&rsquo;","’").replace("&nbsp;", " ")
    return t.replace('"', '\\"')

for s in SERVICES:
    path = os.path.join(OUT, f"{s['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(render(s))
    print("wrote", path)

print("done", len(SERVICES), "pages")
