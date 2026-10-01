#!/usr/bin/env python3
"""Generate remireminder.app's guides, guides hub, support page, 404, sitemap.xml and robots.txt.

Run:  python3 _gen/gen_site.py      (from anywhere; paths are relative to this file)

Content lives in _gen/pages.py. The homepage (index.html), privacy.html and terms.html are
hand-written and NOT generated. Generated files are build output: never hand-edit them.
Modelled on AlarmPlanner's website/_gen/gen_guides.py (same structure, same campaign rules).
Jekyll/GitHub Pages skips _-prefixed directories, so _gen/ is not deployed.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from pages import PAGES, CLUSTERS, HUB_FAQS

DOMAIN = "https://remireminder.app"
APP_ID = "6759194352"
TODAY = "2026-10-01"

# ---- App Analytics campaign attribution (same rules as AlarmPlanner's generator) -------------
# Apple's campaign-link form is /app/apple-store/id<id>?pt=&ct=&mt=8. BOTH tokens are required:
# a ct without the provider token reports nothing. ct: <= 30 chars, no leading/trailing space.
# Coarse buckets on purpose: a campaign only shows in App Analytics after FIVE first-time downloads,
# so per-page tokens would report nothing. Per-page clicks are in PostHog (data-ph + page path).
PROVIDER_TOKEN = "2187944"
CT_HOME = "Website_Home"      # homepage, support, legal, 404
CT_GUIDE = "Website_Guide"    # every /guides/ page

def store_url(campaign):
    assert 0 < len(campaign) <= 30 and campaign == campaign.strip(), f"bad ct: {campaign!r}"
    return (f"https://apps.apple.com/app/apple-store/id{APP_ID}"
            f"?pt={PROVIDER_TOKEN}&amp;ct={campaign}&amp;mt=8")

# Analytics: copied from the homepage <head> at build time so the two never drift.
_index = open(os.path.join(SITE, "index.html"), encoding="utf-8").read()
_ph = re.search(r"<script>\s*!function\(t,e\).*?</script>", _index, re.S)
_ahrefs = re.search(r'<script src="https://analytics\.ahrefs\.com[^>]*></script>', _index)
assert _ph and "remi_web" in _ph.group(0), "PostHog snippet with app_name remi_web not found in index.html"
ANALYTICS = _ph.group(0) + ("\n" + _ahrefs.group(0) if _ahrefs else "")

CLICK_JS = """<script>
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-ph]');
    if (el && window.posthog) { posthog.capture(el.getAttribute('data-ph'), { page: location.pathname }); }
  });
  (function () {
    var t = document.getElementById('theme-toggle');
    if (!t) return;
    t.addEventListener('click', function () {
      var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  })();
</script>"""

THEME_BOOT = """<script>
  (function () {
    var t = null;
    try { t = localStorage.getItem('theme'); } catch (e) {}
    if (!t) t = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', t);
  })();
</script>"""

SUN = '<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>'
MOON = '<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>'

def header(campaign=CT_HOME):
    return f"""<nav class="site-nav" aria-label="Main">
  <a href="/" class="nav-brand"><img src="/assets/appicon-128.png" alt="" class="nav-icon" width="32" height="32"><span class="nav-name">Remi</span></a>
  <div class="nav-right">
    <ul class="nav-links">
      <li><a href="/#how-it-works">How It Works</a></li>
      <li><a href="/guides/">Guides</a></li>
      <li><a href="/#faq">FAQ</a></li>
      <li><a href="/#pricing">Pricing</a></li>
    </ul>
    <a href="{store_url(campaign)}" class="nav-cta" data-ph="appstore_click">Download</a>
    <button class="theme-toggle" id="theme-toggle" aria-label="Toggle dark mode">{SUN}{MOON}</button>
  </div>
</nav>"""

def footer(campaign=CT_HOME):
    return f"""<footer class="site-footer">
  <div class="footer-brand">Remi</div>
  <div class="footer-tagline">A to-do list that doesn't rush you.</div>
  <div class="footer-links">
    <a href="/guides/">Guides</a>
    <a href="{store_url(campaign)}" data-ph="appstore_click">App Store</a>
    <a href="/support/">Support</a>
    <a href="/privacy.html">Privacy</a>
    <a href="/terms.html">Terms</a>
  </div>
  <div class="footer-more">More from the same maker: <a href="https://alarmclockplanner.com/" data-ph="xsell_alarmplanner_footer">Alarm Clock Planner</a> &middot; <a href="https://risemorning.app/" data-ph="xsell_rise_footer">Rise</a></div>
  <div class="footer-copy">Made by <a href="https://ozols.dev" rel="author">Emils Ozols</a> &middot; &copy; 2026 Remi. Apple, iPhone and App Store are trademarks of Apple Inc.</div>
</footer>"""

def head(title, desc, canonical, og_type="article"):
    t = title if title.endswith("Remi") else f"{title} | Remi"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{ANALYTICS}
{THEME_BOOT}
<title>{t}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Remi">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/ogshare.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{DOMAIN}/assets/ogshare.png">
<link rel="icon" type="image/png" href="/assets/appicon-128.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/site.css">
"""

def jsonld(*objs):
    return "\n".join(f'<script type="application/ld+json">\n{json.dumps(o, indent=2, ensure_ascii=False)}\n</script>' for o in objs)

def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs, heading="Questions"):
    items = "\n".join(f"""  <details class="faq-item"><summary>{q}</summary><p>{a}</p></details>""" for q, a in faqs)
    return f"""<section class="faq" id="faq">
  <h2>{heading}</h2>
{items}
</section>"""

def cta_html(h, p, campaign):
    return f"""<aside class="cta-box">
  <img src="/assets/appicon-128.png" alt="" width="64" height="64" class="cta-icon">
  <h2>{h}</h2>
  <p>{p}</p>
  <a href="{store_url(campaign)}" class="app-store-badge" data-ph="appstore_click"><img src="https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/en-us?size=250x83" alt="Download Remi on the App Store" width="180" height="60"></a>
</aside>"""

def xsell_html(x):
    h, p = x
    return f"""<aside class="xsell"><h2>{h}</h2><p>{p}</p></aside>"""

BY_SLUG = {p["slug"]: p for p in PAGES}

def related_html(slugs):
    cards = "\n".join(f"""    <a class="related-card" href="/guides/{s}/"><span>{BY_SLUG[s]['h1']}</span></a>""" for s in slugs)
    return f"""<section class="related"><h2>Related guides</h2>
  <div class="related-grid">
{cards}
  </div>
</section>"""

def write(rel, html):
    path = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    assert "—" not in html, f"em dash in {rel}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return rel

built = []

# ---------- guide pages ----------
for p in PAGES:
    for s in p["related"]:
        assert s in BY_SLUG, f"{p['slug']}: unknown related slug {s}"
    canonical = f"{DOMAIN}/guides/{p['slug']}/"
    article = {"@context": "https://schema.org", "@type": "Article", "headline": p["h1"],
               "description": p["meta"], "datePublished": TODAY, "dateModified": TODAY,
               "mainEntityOfPage": canonical, "image": f"{DOMAIN}/assets/ogshare.png",
               "author": {"@type": "Person", "name": "Emils Ozols", "url": "https://ozols.dev"},
               "publisher": {"@type": "Organization", "name": "Remi",
                             "logo": {"@type": "ImageObject", "url": f"{DOMAIN}/assets/appicon.png"}}}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
        {"@type": "ListItem", "position": 2, "name": "Guides", "item": f"{DOMAIN}/guides/"},
        {"@type": "ListItem", "position": 3, "name": p["h1"], "item": canonical}]}
    lds = [article, crumbs] + ([faq_ld(p["faqs"])] if p.get("faqs") else [])
    html = head(p["title"], p["meta"], canonical) + jsonld(*lds) + "\n</head>\n<body>\n" + header(CT_GUIDE) + f"""
<main class="article">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span>/</span> <a href="/guides/">Guides</a></nav>
  <h1>{p['h1']}</h1>
  <p class="lede">{p['lede']}</p>
  <div class="quick">{p['quick']}</div>
  {p['body'].strip()}
  {xsell_html(p['xsell']) if p.get('xsell') else ''}
  {faq_html(p['faqs']) if p.get('faqs') else ''}
  {cta_html(p['cta_h'], p['cta_p'], CT_GUIDE)}
  {related_html(p['related'])}
  <p class="updated">Updated {TODAY}. Written by <a href="https://ozols.dev" rel="author">Emils Ozols</a>, who makes Remi.</p>
</main>
""" + footer(CT_GUIDE) + "\n" + CLICK_JS + "\n</body>\n</html>\n"
    built.append(write(f"guides/{p['slug']}/index.html", html))

# ---------- guides hub ----------
def cluster_block(key, heading, intro):
    cards = "\n".join(
        f"""    <a class="guide-card" href="/guides/{p['slug']}/"><h3>{p['h1']}</h3><p>{strip_tags(p['meta'])}</p></a>"""
        for p in PAGES if p["cluster"] == key)
    return f"""<section class="cluster"><h2>{heading}</h2><p>{intro}</p>
  <div class="guide-grid">
{cards}
  </div>
</section>"""

hub_canon = f"{DOMAIN}/guides/"
hub_desc = "Practical guides for reminders on iPhone: reminders without a date, sometime next month, monthly, quarterly and yearly repeats, widgets, voice and planning your year."
collection = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Remi guides",
              "url": hub_canon, "description": hub_desc,
              "hasPart": [{"@type": "Article", "headline": p["h1"], "url": f"{DOMAIN}/guides/{p['slug']}/"} for p in PAGES]}
hub = head("Reminder Guides for iPhone", hub_desc, hub_canon, "website") + jsonld(collection, faq_ld(HUB_FAQS)) + "\n</head>\n<body>\n" + header(CT_GUIDE) + f"""
<main class="hub">
  <h1>Reminder guides for iPhone</h1>
  <p class="lede">Most reminder advice assumes everything has a due date. Real life is fuzzier: things for someday, things for "early next month", things that come round every quarter. These guides cover how to handle all of it on an iPhone, with the built-in apps where they work and with Remi where they don't.</p>
  {''.join(cluster_block(*c) for c in CLUSTERS)}
  {faq_html(HUB_FAQS, "About Remi")}
  {cta_html("Try Remi free", "Exact dates, early-mid-late in a month, or someday. Free on iPhone, one-time Premium.", CT_GUIDE)}
</main>
""" + footer(CT_GUIDE) + "\n" + CLICK_JS + "\n</body>\n</html>\n"
built.append(write("guides/index.html", hub))

# ---------- support ----------
SUPPORT_FAQS = [
 ("How do I restore my Premium purchase?", "Open Remi, go to Settings and tap Upgrade, then Restore Purchase, signed in with the same Apple ID you bought it with. Premium is a one-time purchase, so it carries over to a new iPhone."),
 ("I'm not getting notifications.", "Only exact-date reminders send their own notification, at their time. Check that notifications are on in Remi's Settings, that the reminder has its bell on, and that Remi is allowed in iPhone Settings > Notifications and in any Focus you use."),
 ("Why didn't my \"early March\" reminder notify me?", "Approximate reminders (Early, Mid, Late, Anytime) cover a stretch of days, so they don't fire at a set time. They show in your lists, calendars and widgets. You can turn on a weekly or monthly summary notification in Settings > Notifications."),
 ("How do I back up my reminders?", "Remi can back up to your iCloud account from Settings. Your reminders are otherwise stored only on your iPhone."),
 ("Does Remi sync to my calendar?", "Remi can copy your reminders into the iPhone's calendar. The sync is one-way, from Remi to the calendar; changes made in the calendar are not copied back."),
 ("How do I delete my data?", "Deleting the app removes the reminders stored on your iPhone. If you used iCloud backup, you can delete the backup from your iCloud storage settings on the iPhone."),
]
sup_canon = f"{DOMAIN}/support/"
sup_desc = "Help with Remi: restoring Premium, notifications, backups, calendar sync and contacting the developer."
support = head("Remi Support", sup_desc, sup_canon, "website") + jsonld(faq_ld(SUPPORT_FAQS)) + "\n</head>\n<body>\n" + header() + f"""
<main class="article">
  <h1>Support</h1>
  <p class="lede">Remi is made by one person. Questions, bugs and ideas all land in the same inbox, and get read.</p>
  <div class="quick"><strong>Contact:</strong> <a href="mailto:info@remireminder.app">info@remireminder.app</a>. You can also send feedback from inside the app, in Settings.</div>
  {faq_html(SUPPORT_FAQS, "Common questions")}
  <p>More how-tos are in the <a href="/guides/">guides</a>. Legal: <a href="/privacy.html">Privacy Policy</a> and <a href="/terms.html">Terms of Use</a>.</p>
</main>
""" + footer() + "\n" + CLICK_JS + "\n</body>\n</html>\n"
built.append(write("support/index.html", support))

# ---------- 404 ----------
nf = head("Page not found", "This page does not exist.", f"{DOMAIN}/404.html", "website").replace(
    '<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"') + "</head>\n<body>\n" + header() + """
<main class="article notfound">
  <h1>Nothing here</h1>
  <p class="lede">This page doesn't exist, or it moved. Remi would shrug if he could.</p>
  <p><a href="/">Go to the homepage</a> or browse the <a href="/guides/">guides</a>.</p>
</main>
""" + footer() + "\n" + CLICK_JS + "\n</body>\n</html>\n"
built.append(write("404.html", nf))

# ---------- sitemap + robots ----------
urls = [(f"{DOMAIN}/", "1.0"), (hub_canon, "0.8")] + [(f"{DOMAIN}/guides/{p['slug']}/", "0.7") for p in PAGES] + \
       [(sup_canon, "0.4"), (f"{DOMAIN}/privacy.html", "0.3"), (f"{DOMAIN}/terms.html", "0.3")]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     "".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>{pr}</priority>\n  </url>\n" for u, pr in urls) + "</urlset>\n"
built.append(write("sitemap.xml", sm))
built.append(write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n"))

print("\n".join(built))
print(f"{len(PAGES)} guides, {len(built)} files")
