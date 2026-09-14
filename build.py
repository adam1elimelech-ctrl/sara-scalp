#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).parent
WA = "https://wa.me/972508128665"
PHONE = "050-812-8665"
TEL = "tel:+972508128665"
EMAIL = "mailto:sara@sarascalpjerusalem.com"
MAP = "https://maps.google.com/?q=Hamor+1+Jerusalem"

NAV_HE = [
    ("index.html", "דף הבית"),
    ("about.html", "מי אנחנו"),
    ("scar-camouflage.html", "הסוואת צלקות", True),
    ("gallery.html", "לפני ואחרי"),
    ("testimonials.html", "המלצות"),
    ("book.html", "קביעת תור"),
]
SERVICES_HE = [
    ("scar-camouflage.html", "הסוואת צלקות"),
    ("burn-scars.html", "טשטוש כויות"),
    ("hypopigmentation.html", "היפופיגמנטציה"),
    ("stretch-marks.html", "סימני מתיחה"),
    ("birthmarks.html", "כתמי לידה"),
    ("freckles.html", "נמשים טבעיים"),
    ("cheek-enhancement.html", "הדגשת לחיים"),
    ("smp.html", "הדמיית שיער SMP"),
    ("process.html", "תהליך הטיפול"),
    ("faq.html", "שאלות נפוצות"),
]
NAV_EN = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("scar-camouflage.html", "Scar Camouflage", True),
    ("gallery.html", "Before & After"),
    ("testimonials.html", "Reviews"),
    ("book.html", "Book"),
]
SERVICES_EN = [
    ("scar-camouflage.html", "Scar Camouflage"),
    ("burn-scars.html", "Burn Scars"),
    ("hypopigmentation.html", "Hypopigmentation"),
    ("stretch-marks.html", "Stretch Marks"),
    ("birthmarks.html", "Birthmarks"),
    ("freckles.html", "Natural Freckles"),
    ("cheek-enhancement.html", "Cheek Enhancement"),
    ("smp.html", "Scalp SMP"),
    ("process.html", "The Process"),
    ("faq.html", "FAQ"),
]


def asset(lang, path):
    return path if lang == "he" else f"../{path}"


def href(lang, page):
    if lang == "he":
        return page
    return page  # en pages live in /en/


def switch_href(lang, page):
    return f"en/{page}" if lang == "he" else f"../{page}"


def header(lang, page):
    nav = NAV_HE if lang == "he" else NAV_EN
    services = SERVICES_HE if lang == "he" else SERVICES_EN
    book = "קביעת תור" if lang == "he" else "Book now"
    services_label = "טיפולים" if lang == "he" else "Treatments"
    prefix = "" if lang == "he" else ""
    a = lambda p: asset(lang, p)
    links = []
    for item in nav:
        slug, label = item[0], item[1]
        extra = item[2] if len(item) > 2 else False
        active = "active" if slug == page else ""
        if extra:
            items = "".join(f'<a href="{s}">{n}</a>' for s, n in services)
            links.append(
                f'<div class="drop"><a class="{active}" href="{slug}">{label}</a><div class="drop-menu">{items}</div></div>'
            )
        else:
            links.append(f'<a class="{active}" href="{slug}">{label}</a>')
    he_on = "on" if lang == "he" else ""
    en_on = "on" if lang == "en" else ""
    he_link = page if lang == "en" else page
    # language switch
    if lang == "he":
        he_url, en_url = page, f"en/{page}"
    else:
        he_url, en_url = f"../{page}", page
    mobile = "".join(
        [f'<a href="{slug}">{label}</a>' for slug, label, *rest in nav]
        + [f'<a href="{s}">{n}</a>' for s, n in services]
    )
    return f"""
<header class="header">
  <div class="header-inner">
    <a class="logo" href="index.html">
      <span class="logo-mark">SARA</span>
      <span class="logo-sub">SCALP JERUSALEM</span>
    </a>
    <nav class="nav">{''.join(links)}</nav>
    <div class="header-actions">
      <div class="lang">
        <a class="{he_on}" href="{he_url}" hreflang="he">עב</a>
        <a class="{en_on}" href="{en_url}" hreflang="en">EN</a>
      </div>
      <a class="btn btn-phone" href="{TEL}">{PHONE}</a>
      <a class="btn" href="{WA}" target="_blank" rel="noopener">{book}</a>
      <button class="hamburger" data-menu aria-expanded="false" aria-label="menu">☰</button>
    </div>
  </div>
  <div class="mobile-nav" data-panel>{mobile}</div>
</header>"""


def footer(lang):
    if lang == "he":
        cols = f"""
        <div>
          <h3>Sara Scalp</h3>
          <p>קליניקה לקעקוע רפואי ולהדמיית שיער בירושלים. התאמת גוון מדויקת, עבודה בשכבות, וליווי אישי.</p>
        </div>
        <div>
          <h3>טיפולים</h3>
          <p><a href="scar-camouflage.html">הסוואת צלקות</a></p>
          <p><a href="burn-scars.html">טשטוש כויות</a></p>
          <p><a href="smp.html">הדמיית שיער SMP</a></p>
          <p><a href="stretch-marks.html">סימני מתיחה</a></p>
        </div>
        <div>
          <h3>הקליניקה</h3>
          <p><a href="about.html">מי אנחנו</a></p>
          <p><a href="process.html">תהליך הטיפול</a></p>
          <p><a href="gallery.html">לפני ואחרי</a></p>
          <p><a href="faq.html">שאלות נפוצות</a></p>
        </div>
        <div>
          <h3>יצירת קשר</h3>
          <p>המור 1, ירושלים</p>
          <p><a href="{TEL}">{PHONE}</a></p>
          <p>א׳–ה׳ 09:00–18:00</p>
          <p>ו׳ וערבי חג 09:00–14:00</p>
        </div>"""
        legal = f'<span>© 2026 Sara Scalp Jerusalem</span><span><a href="privacy.html">פרטיות</a> · <a href="accessibility.html">נגישות</a> · <a href="terms.html">תנאים</a></span>'
    else:
        cols = f"""
        <div>
          <h3>Sara Scalp</h3>
          <p>Medical tattoo and scalp micropigmentation clinic in Jerusalem. Precise color matching, layered work, personal care.</p>
        </div>
        <div>
          <h3>Treatments</h3>
          <p><a href="scar-camouflage.html">Scar camouflage</a></p>
          <p><a href="burn-scars.html">Burn scars</a></p>
          <p><a href="smp.html">Scalp SMP</a></p>
          <p><a href="stretch-marks.html">Stretch marks</a></p>
        </div>
        <div>
          <h3>Clinic</h3>
          <p><a href="about.html">About</a></p>
          <p><a href="process.html">Process</a></p>
          <p><a href="gallery.html">Before & after</a></p>
          <p><a href="faq.html">FAQ</a></p>
        </div>
        <div>
          <h3>Contact</h3>
          <p>Hamor 1, Jerusalem</p>
          <p><a href="{TEL}">{PHONE}</a></p>
          <p>Sun–Thu 09:00–18:00</p>
          <p>Fri & holiday eves 09:00–14:00</p>
        </div>"""
        legal = f'<span>© 2026 Sara Scalp Jerusalem</span><span><a href="privacy.html">Privacy</a> · <a href="accessibility.html">Accessibility</a> · <a href="terms.html">Terms</a></span>'
    return f"""
<footer class="footer">
  <div class="wrap footer-grid">{cols}</div>
  <div class="wrap legal">{legal}</div>
</footer>
<a class="float-wa" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">WA</a>
<script src="{asset(lang, 'assets/js/main.js')}" defer></script>
"""


def page(lang, slug, title, description, body):
    a = lambda p: asset(lang, p)
    canonical = f"https://sara-scalp.github.io/{'' if lang=='he' else 'en/'}{slug if slug!='index.html' else ''}"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#F6F1E8">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="he" href="../{slug if lang=='en' else slug}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700&family=Cormorant+Garamond:wght@500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{a('assets/css/style.css')}">
  <link rel="icon" href="{a('assets/img/logo.svg')}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{a('assets/img/hero-clinic.jpg')}">
  <script type="application/ld+json">
  {{
    "@context":"https://schema.org",
    "@type":"MedicalBusiness",
    "name":"Sara Scalp Jerusalem",
    "telephone":"+972-50-812-8665",
    "email":"sara@sarascalpjerusalem.com",
    "address":{{"@type":"PostalAddress","streetAddress":"Hamor 1","addressLocality":"Jerusalem","addressCountry":"IL"}},
    "openingHours":["Su-Th 09:00-18:00","Fr 09:00-14:00"],
    "url":"https://sara-scalp.github.io/"
  }}
  </script>
</head>
<body>
<a class="skip" href="#main">דלג לתוכן</a>
{header(lang, slug)}
<main id="main">
{body}
</main>
{footer(lang)}
</body>
</html>
"""


def pic(lang, name, alt, extra=""):
    a = asset(lang, f"assets/img/{name}")
    webp = a.replace(".jpg", ".webp") if a.endswith(".jpg") else a
    src = a if name.endswith(".svg") else webp
    return f'<picture><source type="image/webp" srcset="{webp}"><img src="{a.replace(".webp",".jpg") if a.endswith(".webp") else a}" alt="{alt}" {extra} width="1600" height="900" loading="lazy"></picture>'


def hero_pic(lang, name, alt):
    a = asset(lang, f"assets/img/{name}")
    webp = a.replace(".jpg", ".webp")
    return f'<picture><source type="image/webp" srcset="{webp}"><img src="{a}" alt="{alt}" width="1600" height="900" fetchpriority="high"></picture>'


# ---------- content ----------
def home_he():
    return f"""
<section class="hero">
  {hero_pic("he","hero-clinic.jpg","קליניקת שרה סקאלפ בירושלים")}
  <div class="hero-shade"></div>
  <div class="hero-copy reveal">
    <div class="kicker">Medical tattoo · Jerusalem</div>
    <h1>הסוואת צלקות בקעקוע רפואי בירושלים</h1>
    <p>טשטוש צלקות לאחר ניתוח, חתך או פציעה בהתאמת צבע מדויקת לגוון העור. צוות שהוכשר בברזיל ובטורקיה.</p>
    <div class="hero-ctas">
      <a class="btn" href="{WA}" target="_blank" rel="noopener">קבעו ייעוץ בוואטסאפ</a>
      <a class="btn btn-line" href="gallery.html" style="color:#fff;border-color:#fff">לפני ואחרי</a>
    </div>
  </div>
</section>
<section class="trust">
  <div><strong>ברזיל וטורקיה</strong><span>הכשרה בינלאומית בטכניקה</span></div>
  <div><strong>התאמת גוון</strong><span>פיגמנט רפואי באור טבעי</span></div>
  <div><strong>המור 1</strong><span>קליניקה בירושלים</span></div>
  <div><strong>{PHONE}</strong><span>ייעוץ ראשוני בלי התחייבות</span></div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">הטיפולים</div>
      <h2>קעקוע רפואי שמחזיר מראה אחיד</h2>
      <p class="lead">כל טיפול מקבל עמוד משלו, תמונה מתאימה, והסבר ברור — כדי שתוכלו להבין בדיוק מה מתאים לכם.</p>
    </div>
    <div class="cards">
      <a class="card" href="scar-camouflage.html">{pic("he","skin.jpg","עור בגוון אחיד")}<div class="card-body"><h3>הסוואת צלקות</h3><p>מילוי פיגמנט בצלקת בהירה כדי שתיטמע בעור שמסביב.</p><span class="more">לעמוד הטיפול</span></div></a>
      <a class="card" href="burn-scars.html">{pic("he","pigment.jpg","ערבוב פיגמנטים רפואיים")}<div class="card-body"><h3>טשטוש כויות</h3><p>עבודה עדינה בשכבות על רקמת כוויה שהתייצבה.</p><span class="more">לעמוד הטיפול</span></div></a>
      <a class="card" href="hypopigmentation.html">{pic("he","treatment-room.jpg","חדר טיפול")}<div class="card-body"><h3>היפופיגמנטציה</h3><p>מילוי אזורים לבנים שאיבדו צבע אחרי מחלה או פציעה.</p><span class="more">לעמוד הטיפול</span></div></a>
      <a class="card" href="stretch-marks.html">{pic("he","skin.jpg","מרקם עור")}<div class="card-body"><h3>סימני מתיחה</h3><p>הפחתת הניגודיות של סימנים לבנים ומבריקים אחרי לידה.</p><span class="more">לעמוד הטיפול</span></div></a>
      <a class="card" href="freckles.html">{pic("he","freckles.jpg","נמשים טבעיים")}<div class="card-body"><h3>נמשים טבעיים</h3><p>פיזור נמשים עדין שנראה כמו עור שזוף באור יום.</p><span class="more">לעמוד הטיפול</span></div></a>
      <a class="card" href="smp.html">{pic("he","smp.jpg","הדמיית שיער מקרוב")}<div class="card-body"><h3>הדמיית שיער SMP</h3><p>נקודות מדויקות שמדמות זקיקים בשיער קצוץ.</p><span class="more">לעמוד הטיפול</span></div></a>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap split">
    <div class="copy reveal">
      <div class="kicker">הקליניקה</div>
      <h2>שרה סקאלפ היא קליניקה לקעקועים רפואיים בירושלים</h2>
      <p>אנחנו מתמחים בהחזרת ביטחון לאנשים עם צלקות, כוויות, שינויי פיגמנט, סימני מתיחה, כתמי לידה או נשירת שיער. הצוות הוכשר בברזיל ובטורקיה — שתיים מהמדינות המובילות בעולם בהסוואת צלקות ובקעקוע פרא־רפואי.</p>
      <p>המטרה פשוטה: להסתכל במראה ולהרגיש שלם יותר. לא מכסים את הצלקת בציור דקורטיבי. מחזירים לעור מראה טבעי ואחיד.</p>
      <a class="btn" href="about.html">הסיפור שלנו</a>
    </div>
    <div class="media">{pic("he","treatment-room.jpg","חדר הטיפולים בקליניקה","")}<span class="badge">המור 1, ירושלים</span></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">המלצות</div>
      <h2>מה אומרים מטופלים</h2>
    </div>
    <div class="quotes">
      <blockquote class="quote"><p>התאמת הצבע מדהימה, והבדלי הטקסטורה כבר אינם בולטים. טיפול בהיגיינה קפדנית והנחיות ברורות לבית.</p><cite>נועם ד., 29, ירושלים</cite></blockquote>
      <blockquote class="quote"><p>אחרי שתי לידות הבטן הייתה מלאה בסימני מתיחה לבנים. אחרי ההסוואה אני יכולה ללבוש בגדים בלי אי־נעימות.</p><cite>ענת מזרחי, 40, ירושלים</cite></blockquote>
      <blockquote class="quote"><p>נתנו לי ראש שנראה כמו שיער קצוץ וצפוף. גם מקרוב זה נראה טבעי. הפסקתי לחשוב על המראה בכל בוקר.</p><cite>מטופל SMP, ירושלים</cite></blockquote>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="wrap">
    <h2>יש צלקת שמפריעה לכם?</h2>
    <p>בייעוץ הראשון בודקים את הצלקת באור טבעי, מסבירים מה אפשר להשיג — ומה אי אפשר — ובונים תוכנית אישית. בלי התחייבות.</p>
    <a class="btn" href="book.html">קביעת ייעוץ</a>
  </div>
</section>
"""


def home_en():
    return f"""
<section class="hero">
  {hero_pic("en","hero-clinic.jpg","Sara Scalp clinic in Jerusalem")}
  <div class="hero-shade"></div>
  <div class="hero-copy reveal">
    <div class="kicker">Medical tattoo · Jerusalem</div>
    <h1>Scar camouflage with medical tattooing in Jerusalem</h1>
    <p>Blending surgical, injury and burn scars into the surrounding skin with precise pigment matching. Team trained in Brazil and Turkey.</p>
    <div class="hero-ctas">
      <a class="btn" href="{WA}" target="_blank" rel="noopener">Book on WhatsApp</a>
      <a class="btn btn-line" href="gallery.html" style="color:#fff;border-color:#fff">Before & after</a>
    </div>
  </div>
</section>
<section class="trust">
  <div><strong>Brazil & Turkey</strong><span>International technique training</span></div>
  <div><strong>Color match</strong><span>Medical pigment in natural light</span></div>
  <div><strong>Hamor 1</strong><span>Clinic in Jerusalem</span></div>
  <div><strong>{PHONE}</strong><span>Consult with no obligation</span></div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">Treatments</div>
      <h2>Paramedical tattooing that restores an even look</h2>
      <p class="lead">Every treatment has its own page, matching image and clear explanation — so you know exactly what fits.</p>
    </div>
    <div class="cards">
      <a class="card" href="scar-camouflage.html">{pic("en","skin.jpg","Even skin tone")}<div class="card-body"><h3>Scar camouflage</h3><p>Skin-tone pigment placed into a light scar so it blends with nearby skin.</p><span class="more">Read more</span></div></a>
      <a class="card" href="burn-scars.html">{pic("en","pigment.jpg","Mixing medical pigments")}<div class="card-body"><h3>Burn scars</h3><p>Layered work on mature burn tissue after careful assessment.</p><span class="more">Read more</span></div></a>
      <a class="card" href="smp.html">{pic("en","smp.jpg","Scalp micropigmentation close-up")}<div class="card-body"><h3>Scalp SMP</h3><p>Tiny dots that mimic shaved hair follicles.</p><span class="more">Read more</span></div></a>
      <a class="card" href="stretch-marks.html">{pic("en","skin.jpg","Skin texture")}<div class="card-body"><h3>Stretch marks</h3><p>Reduce the contrast of pale, shiny marks after pregnancy or weight change.</p><span class="more">Read more</span></div></a>
      <a class="card" href="freckles.html">{pic("en","freckles.jpg","Natural freckles")}<div class="card-body"><h3>Natural freckles</h3><p>Soft, daylight-looking freckles placed one by one.</p><span class="more">Read more</span></div></a>
      <a class="card" href="cheek-enhancement.html">{pic("en","cheeks.jpg","Natural cheek color")}<div class="card-body"><h3>Cheek enhancement</h3><p>A lasting natural flush without daily makeup or filler.</p><span class="more">Read more</span></div></a>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap split">
    <div class="copy">
      <div class="kicker">The clinic</div>
      <h2>Sara Scalp is a medical tattoo clinic in Jerusalem</h2>
      <p>We restore confidence for people living with scars, burns, pigment loss, stretch marks, birthmarks or hair loss. The team trained in Brazil and Turkey — two of the leading countries in scar camouflage and paramedical tattooing.</p>
      <p>We do not cover a scar with decorative artwork. We return a more natural, even appearance to the skin.</p>
      <a class="btn" href="about.html">Our story</a>
    </div>
    <div class="media">{pic("en","treatment-room.jpg","Treatment room")}<span class="badge">Hamor 1, Jerusalem</span></div>
  </div>
</section>
<section class="cta-band">
  <div class="wrap">
    <h2>A scar that still catches your eye?</h2>
    <p>In the first visit we assess the area in natural light, explain what can be achieved — and what cannot — and build a personal plan. No obligation.</p>
    <a class="btn" href="book.html">Book a consultation</a>
  </div>
</section>
"""


def service_template(lang, h1, kicker, lead, img, img_alt, paras, who, faqs):
    who_h = "למי זה מתאים" if lang == "he" else "Who it is for"
    faq_h = "שאלות נפוצות" if lang == "he" else "Questions"
    cta_h = "קביעת ייעוץ" if lang == "he" else "Book a consultation"
    cta_p = "נבדוק את האזור באור טבעי ונגיד בכנות מה אפשר להשיג." if lang == "he" else "We assess the area in natural light and tell you honestly what is possible."
    who_html = "".join(f"<li>{x}</li>" for x in who)
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    paras_html = "".join(f"<p>{p}</p>" for p in paras)
    return f"""
<section class="page-hero">
  <div class="wrap">
    <div class="kicker">{kicker}</div>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
<section class="section alt">
  <div class="wrap split">
    <div class="copy prose">{paras_html}
      <p><a class="btn" href="book.html">{cta_h}</a></p>
    </div>
    <div class="media">{pic(lang, img, img_alt)}</div>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div>
      <h2>{who_h}</h2>
      <ul class="list-check">{who_html}</ul>
    </div>
    <div class="faq">
      <h2>{faq_h}</h2>
      {faq_html}
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="wrap">
    <h2>{cta_h}</h2>
    <p>{cta_p}</p>
    <a class="btn" href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
  </div>
</section>
"""


PAGES = {}

# Hebrew services
PAGES[("he", "scar-camouflage.html")] = (
    "הסוואת צלקות בקעקוע רפואי בירושלים | Sara Scalp",
    "טשטוש צלקות לאחר ניתוח, קיסרי, חתך או פציעה בהתאמת פיגמנט מדויקת לגוון העור. קליניקה בירושלים.",
    service_template(
        "he",
        "הסוואת צלקות בקעקוע רפואי",
        "Scar Camouflage",
        "טשטוש צלקות לאחר ניתוח, חתך או פציעה באמצעות התאמת צבע מדויקת לגוון העור שלכם.",
        "skin.jpg",
        "עור בגוון אחיד אחרי הסוואה",
        [
            "הסוואת צלקות היא אחת הטכניקות המתקדמות בתחום הקעקוע הרפואי. המטרה היא להפחית את הנראות של הצלקת כדי שהאזור ייטמע טוב יותר בעור שמסביב — בין אם מדובר בצלקת אחרי ניתוח קיסרי, ניתוח אסתטי, ניתוח אורתופדי, חתך או פציעה.",
            "בניגוד לקעקוע דקורטיבי, כאן לא מציירים ציור על הצלקת. מחדירים פיגמנט רפואי לשכבות העליונות של רקמת הצלקת כדי למלא את הפער בצבע שנוצר בהחלמה. צלקות רבות מאבדות פיגמנט ונראות לבנות או בהירות. עבודה בשכבות דקות מפחיתה את הניגודיות.",
            "הטיפול מתאים לצלקות שטוחות יחסית שהתייצבו, בדרך כלל 12–18 חודשים אחרי הפציעה או הניתוח. צלקות היפרטרופיות או קלואידיות דורשות הערכה נפרדת, ולעיתים הכנה לפני הסוואה.",
            "חשוב לדעת: התוצאה היא שיפור משמעותי, לא מחיקה מלאה של הצלקת. המרקם נשאר כי לא משנים את מבנה העור. הצבע מתמזג והבולטות יורדת. זה מה שרוב המטופלים מחפשים — ללבוש בגדים קצרים בלי להסתיר.",
            "בקליניקה בירושלים הצוות למד את הטכניקה בברזיל ובטורקיה. התאמת הצבע נעשית באור טבעי, ממספר זוויות, עם פיגמנטים ייעודיים לקעקוע רפואי.",
        ],
        [
            "נשים אחרי ניתוח קיסרי עם צלקת בולטת בבטן",
            "צלקות אחרי מתיחת בטן, הגדלת חזה או הסרת עודפי עור",
            "צלקות אורתופדיות וכירורגיות",
            "צלקות חבלה, חתכים ותאונות",
            "צלקות אחרי הסרת שומה או נגע",
            "מי שמרגיש שהצלקת פוגעת בביטחון",
        ],
        [
            ("האם זה כואב?", "אי־הנוחות קלה בדרך כלל. אפשר להשתמש במשחת הרדמה מקומית לפני הטיפול."),
            ("כמה זמן מחזיקה התוצאה?", "התוצאה ארוכת טווח. לפי סוג העור והחשיפה לשמש ייתכן חידוש אחרי כמה שנים."),
            ("מתי אפשר להתחיל אחרי ניתוח?", "רק אחרי שהצלקת הבשילה לגמרי, לרוב 12–18 חודשים. צלקת אדומה או פעילה לא מטופלת."),
            ("אפשר לטפל בצלקות ישנות?", "כן. צלקות לבנות ישנות ומתייצבות מגיבות היטב להסוואה."),
        ],
    ),
)

PAGES[("he", "burn-scars.html")] = (
    "טשטוש צלקות כוויה בקעקוע רפואי | Sara Scalp ירושלים",
    "הסוואת צלקות כוויה עם פיגמנט רפואי בהתאמת גוון. הערכה אישית בקליניקה בירושלים.",
    service_template(
        "he",
        "טשטוש צלקות כוויה",
        "Burn scar camouflage",
        "כוויה משאירה לרוב שינוי צבע ומרקם. אחרי שהרקמה התייצבה אפשר למלא גוון חסר ולהפחית ניגודיות.",
        "pigment.jpg",
        "התאמת פיגמנט לצלקת כוויה",
        [
            "צלקת כוויה מתנהגת אחרת מצלקת ניתוח. לעיתים יש אזורים בהירים לצד כהים, ומרקם לא אחיד. לכן כל מקרה נבדק בנפרד באור יום.",
            "כשהרקמה בשלה ולא פעילה, מחדירים פיגמנט בשכבות דקות לאזורים החסרים צבע. לא מבטיחים העלמה מלאה. המטרה היא שהעין תפסיק להימשך לכתם.",
            "לפעמים נדרשת הכנה או מספר מפגשים גבוה יותר מאשר בצלקת ניתוח רגילה. בייעוץ נגיד בכנות אם האזור מתאים.",
        ],
        [
            "צלקות כוויה שהחלימו לחלוטין",
            "אזורים בהירים בתוך כוויה ישנה",
            "מי שכבר ניסה קרמים או לייזר ונותרה ניגודיות צבע",
        ],
        [
            ("כל כוויה מתאימה?", "לא. כוויה טרייה, אזור לא יציב או נטייה לקלואיד דורשים דחייה או הפניה."),
            ("כמה טיפולים?", "לרוב כמה מפגשים בהפרש של שבועות, לפי גודל האזור וקליטת הצבע."),
        ],
    ),
)

PAGES[("he", "hypopigmentation.html")] = (
    "הסוואת היפופיגמנטציה בירושלים | Sara Scalp",
    "מילוי כתמים לבנים ואזורים חסרי פיגמנט בקעקוע רפואי. התאמת גוון בקליניקה בירושלים.",
    service_template(
        "he",
        "היפופיגמנטציה — מילוי צבע חסר",
        "Hypopigmentation",
        "כתמים לבנים אחרי מחלה, פסוריאזיס, פציעה או דלקת אפשר לפעמים למזג חזרה לגוון העור.",
        "treatment-room.jpg",
        "חדר טיפול להסוואת כתמים לבנים",
        [
            "היפופיגמנטציה היא אובדן צבע מקומי. הכתם הלבן בולט כי הוא שובר את רצף העור. קעקוע רפואי ממלא את החסר בפיגמנט מותאם.",
            "מתאימים את הגוון למוצא העור באור טבעי. בימים הראשונים הצבע עשוי להיראות כהה יותר ואז מתייצב.",
            "לא כל כתם לבן מתאים. ויטיליגו פעיל, מחלה לא יציבה או אזור בפנים דורשים שיקול זהיר.",
        ],
        ["כתמים לבנים יציבים אחרי מחלה", "אובדן פיגמנט אחרי פציעה", "אזורים בהירים שמפריעים אסתטית"],
        [
            ("זה איפור?", "לא. זה פיגמנט בשכבת העור, לא כיסוי קוסמטי יומי."),
            ("נשאר לכל החיים?", "ארוך טווח. שמש ואורח חיים משפיעים על קצב הדהייה."),
        ],
    ),
)

PAGES[("he", "stretch-marks.html")] = (
    "הסוואת סימני מתיחה בקעקוע רפואי | Sara Scalp",
    "טשטוש סימני מתיחה לבנים אחרי לידה או שינוי משקל. קליניקה בירושלים.",
    service_template(
        "he",
        "הסוואת סימני מתיחה",
        "Stretch marks",
        "סימנים לבנים ומבריקים אחרי לידה או שינוי משקל אפשר למלא בגוון העור ולהוריד את הניגודיות.",
        "skin.jpg",
        "עור בטן בגוון אחיד יותר",
        [
            "סימן מתיחה בהיר בולט כי הוא מחזיר אור אחרת מהעור שמסביב. הסוואה ממלאת את הקו בפיגמנט תואם.",
            "סימנים אדומים וחדשים עדיין פעילים — ממתינים שיתהפכו ללבן־כסוף ויתייצבו.",
            "המרקם לא נעלם לגמרי. מה שנחלש הוא הכתם הלבן שמושך את העין.",
        ],
        ["אחרי לידה", "אחרי שינוי משקל", "סימנים לבנים יציבים בבטן, ירכיים או חזה"],
        [("כואב?", "ברוב המקרים סביל מאוד, עם אפשרות להרדמה מקומית.")],
    ),
)

PAGES[("he", "birthmarks.html")] = (
    "הסוואת כתם לידה בירושלים | Sara Scalp",
    "הפחתת ניגודיות של כתם לידה כהה או בהיר בעזרת קעקוע רפואי.",
    service_template(
        "he",
        "הסוואת כתמי לידה",
        "Birthmarks",
        "כתם לידה שגרם להסתרה בבגדים או בשיער אפשר לעיתים לרכך בגוון, בשכבות עדינות.",
        "pigment.jpg",
        "ערבוב גוונים לכתם לידה",
        [
            "כתם לידה כהה לא 'נמחק' בצבע בהיר. עובדים על הפחתת הניגודיות מול העור שמסביב, לפעמים בשילוב גישות לפי סוג הכתם.",
            "כל כתם נבדק בנפרד. חלק מהכתמים אינם מתאימים להסוואה בדיו.",
        ],
        ["כתם לידה בצוואר, זרוע או אזור שנחשף בקיץ", "כתם שהתייצב ואינו משתנה"],
        [("אפשר בקיץ?", "אחרי הטיפול נמנעים משמש ישירה כמה שבועות ומגנים ב־SPF.")],
    ),
)

PAGES[("he", "freckles.html")] = (
    "נמשים טבעיים באיפור קבוע בירושלים | Sara Scalp",
    "הוספת נמשים עדינים שנראים טבעיים באור יום. קליניקה בירושלים.",
    service_template(
        "he",
        "נמשים טבעיים",
        "Natural freckles",
        "פיזור נקודות קטנות בגוונים חמים, באקראיות מבוקרת — לא חותמת זהה על כל הלחי.",
        "freckles.jpg",
        "נמשים טבעיים על לחי",
        [
            "נמשים קבועים מתאימים למי שרוצה מראה שזוף ורך בלי איפור יומי. העבודה נעשית נקודה־נקודה כדי שהפיזור יישאר אמין מקרוב.",
            "הגוון מותאם לשיער, לעיניים ולגוון העור הקיים.",
        ],
        ["מי שרוצה נמשים עדינים ולא מאופרים", "השלמת נמשים קיימים"],
        [("נראה מזויף?", "כשהפיזור והגוון נכונים — לא. לכן לא עובדים בתבנית קבועה.")],
    ),
)

PAGES[("he", "cheek-enhancement.html")] = (
    "הדגשת לחיים באיפור קבוע | Sara Scalp ירושלים",
    "סומק קבוע עדין ללחיים בלי מילוי ולי איפור יומי.",
    service_template(
        "he",
        "הדגשת לחיים",
        "Cheek enhancement",
        "סומק רך שנראה כמו העור שלכם — רק חיוני יותר.",
        "cheeks.jpg",
        "סומק טבעי בלחיים",
        [
            "הדגשת לחיים באיפור קבוע יוצרת חיוניות בלי חומרי מילוי ובלי סומק כל בוקר. העבודה שטחית ועדינה.",
            "מתאים גם כשחסר צבע בלחי אחרי גיל או אחרי מחלה.",
        ],
        ["מי שרוצה מראה ערני בלי איפור", "לחיים שטוחות־צבע"],
        [("אפשר לבטל?", "הצבע דועך עם הזמן. לא מבטיחים הסרה מלאה מיידית.")],
    ),
)

PAGES[("he", "smp.html")] = (
    "הדמיית שיער SMP בירושלים | Sara Scalp",
    "מיקרופיגמנטציה לקרקפת — נקודות שמדמות שיער קצוץ טבעי. קליניקה בירושלים.",
    service_template(
        "he",
        "הדמיית שיער SMP",
        "Scalp micropigmentation",
        "נקודות קטנות ומדויקות שמדמות זקיקי שיער במראה גלח צפוף — גם מקרוב.",
        "smp.jpg",
        "קרקפת אחרי הדמיית שיער",
        [
            "SMP אינה תוספת שיער. היא מדמה את הצל של שיער קצוץ על הקרקפת. לכן האיכות נמדדת בתקריב: צורת הנקודה, המרווח והמיזוג לקו השיער.",
            "מתאים לנסיגת קו שיער, דלילות בקרקפת, צלקות בקרקפת ולמי שבוחר מראה גלח קבוע.",
            "נדרשים כמה מפגשים. בין המפגשים הצבע מתייצב. מקבלים הנחיות ברורות לטיפול ביתי.",
        ],
        ["גברים עם נסיגת קו שיער", "דלילות שמתאימה למראה קצוץ", "צלקות בקרקפת אחרי השתלה או פציעה"],
        [
            ("רואים שזה מצויר?", "עבודה טובה לא נראית כמו קווים שטוחים. היא נראית כמו נקודות זקיק."),
            ("כמה מחזיק?", "שנים. שמש ושמנים חזקים מאיצים דהייה. חידוש לפי הצורך."),
        ],
    ),
)


def simple_page(lang, h1, kicker, blocks):
    inner = ""
    for b in blocks:
        if b[0] == "text":
            inner += f'<div class="prose">{"".join(f"<p>{p}</p>" for p in b[1])}</div>'
        elif b[0] == "split":
            inner += f'<div class="split" style="margin:36px 0"><div class="copy prose">{"".join(f"<p>{p}</p>" for p in b[1])}</div><div class="media">{pic(lang,b[2],b[3])}</div></div>'
        elif b[0] == "quotes":
            inner += '<div class="quotes">' + "".join(
                f'<blockquote class="quote"><p>{t}</p><cite>{c}</cite></blockquote>' for t, c in b[1]
            ) + "</div>"
        elif b[0] == "form":
            inner += b[1]
        elif b[0] == "faq":
            inner += '<div class="faq">' + "".join(
                f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in b[1]
            ) + "</div>"
        elif b[0] == "steps":
            inner += '<div class="steps">' + "".join(
                f'<div class="step"><i>{i}</i><h3>{t}</h3><p>{p}</p></div>' for i, t, p in b[1]
            ) + "</div>"
        elif b[0] == "gallery":
            inner += '<div class="gallery">' + "".join(
                f"<figure>{pic(lang,img,cap)}<figcaption>{cap}</figcaption></figure>" for img, cap in b[1]
            ) + "</div>"
    return f"""
<section class="page-hero"><div class="wrap"><div class="kicker">{kicker}</div><h1>{h1}</h1></div></section>
<section class="section alt"><div class="wrap">{inner}</div></section>
"""


form_he = f"""
<form class="form" data-wa-form>
  <label>שם מלא<input name="name" required></label>
  <label>טלפון<input name="phone" required></label>
  <label>טיפול
    <select name="service">
      <option>הסוואת צלקות</option><option>כוויות</option><option>היפופיגמנטציה</option>
      <option>סימני מתיחה</option><option>כתם לידה</option><option>נמשים</option>
      <option>הדגשת לחיים</option><option>SMP</option>
    </select>
  </label>
  <label>הודעה<textarea name="message" rows="4" placeholder="אפשר לתאר את האזור בקצרה"></textarea></label>
  <button class="btn" type="submit">שליחה לוואטסאפ</button>
  <p>או חייגו <a href="{TEL}">{PHONE}</a> · המור 1, ירושלים</p>
</form>
"""

form_en = f"""
<form class="form" data-wa-form>
  <label>Full name<input name="name" required></label>
  <label>Phone<input name="phone" required></label>
  <label>Treatment
    <select name="service">
      <option>Scar camouflage</option><option>Burns</option><option>Hypopigmentation</option>
      <option>Stretch marks</option><option>Birthmark</option><option>Freckles</option>
      <option>Cheek enhancement</option><option>SMP</option>
    </select>
  </label>
  <label>Message<textarea name="message" rows="4"></textarea></label>
  <button class="btn" type="submit">Send to WhatsApp</button>
  <p>Or call <a href="{TEL}">{PHONE}</a> · Hamor 1, Jerusalem</p>
</form>
"""

PAGES[("he", "about.html")] = (
    "מי אנחנו | Sara Scalp ירושלים",
    "קליניקה לקעקוע רפואי בירושלים. הכשרה בברזיל ובטורקיה, רקע פרא־רפואי, המור 1.",
    simple_page("he", "הסיפור מאחורי שרה סקאלפ", "מי אנחנו", [
        ("split", [
            "שרה סקאלפ היא קליניקה מובילה לקעקועים רפואיים ומיקרופיגמנטציה בירושלים. אנחנו מחזירים ביטחון לאנשים שחיים עם צלקת, כוויה, שינוי פיגמנט, סימן מתיחה, כתם לידה או נשירת שיער.",
            "הצוות הוכשר בברזיל ובטורקיה. בצוות יש גם רקע של שיננית מוסמכת — הבנה של סטריליות, ריריות ורקמות.",
            "לא מוכרים קסם. מסבירים מה הצלקת יכולה לקבל ומה לא. עובדים באור טבעי, בשכבות, עם פיגמנטים ייעודיים.",
            "הקליניקה ברחוב המור 1, ירושלים. א׳–ה׳ 09:00–18:00, שישי וערבי חג 09:00–14:00.",
        ], "jerusalem.jpg", "ירושלים מהחלון"),
    ]),
)

PAGES[("he", "process.html")] = (
    "תהליך הטיפול בקעקוע רפואי | Sara Scalp",
    "ייעוץ, התאמת צבע, טיפול בשכבות ומעקב. כך נראה התהליך בקליניקה בירושלים.",
    simple_page("he", "איך נראה התהליך", "שקיפות מלאה", [
        ("steps", [
            ("01", "ייעוץ", "בודקים את האזור באור טבעי: סוג עור, גוון, מרקם ובשלות."),
            ("02", "התאמת צבע", "מערבבים פיגמנט רפואי עד לגוון הקרוב ביותר לעור שמסביב."),
            ("03", "טיפול", "עבודה במכשיר ייעודי ובמחטים עדינות, בשכבות דקות."),
            ("04", "מעקב", "לרוב 2–4 מפגשים. בין לבין מקבלים הנחיות בית."),
            ("05", "ייצוב", "הצבע מתייצב לאורך שבועות. התוצאה הסופית נמדדת אחרי ההחלמה."),
        ]),
        ("text", ["לא כל צלקת מתאימה באותו רגע. צלקת אדומה, פעילה או קלואידית תדחה או תופנה להכנה."]),
    ]),
)

PAGES[("he", "gallery.html")] = (
    "לפני ואחרי | Sara Scalp ירושלים",
    "גלריית תוצאות קעקוע רפואי. החליפו כאן בתמונות האמיתיות של הקליניקה עם הסכמת מטופלים.",
    simple_page("he", "לפני ואחרי", "התוצאה נמדדת באור יום", [
        ("text", [
            "כאן יופיעו צילומי לפני/אחרי של הקליניקה — אותה תאורה, אותו פריים, עם הסכמה בכתב.",
            "עד שתעלו את הצילומים האמיתיים מוצגות תמונות אווירה של הקליניקה והטכניקה בלבד. לא משתמשים בתמונות מטופלים בלי אישור.",
        ]),
        ("gallery", [
            ("skin.jpg", "הסוואת צלקות — מקום לתמונת לפני/אחרי שלכם"),
            ("pigment.jpg", "התאמת פיגמנט באור טבעי"),
            ("smp.jpg", "SMP — מקום לתקריב אמיתי"),
            ("freckles.jpg", "נמשים — מקום לתוצאה אמיתית"),
            ("cheeks.jpg", "הדגשת לחיים"),
            ("treatment-room.jpg", "חדר הטיפולים"),
        ]),
    ]),
)

PAGES[("he", "testimonials.html")] = (
    "המלצות מטופלים | Sara Scalp ירושלים",
    "חוות דעת על הסוואת צלקות, כוויות, היפופיגמנטציה, סימני מתיחה ו־SMP.",
    simple_page("he", "המלצות", "במילים של מי שעברו את זה", [
        ("quotes", [
            ("הצוות העניק לי טיפול הסוואה רפואי מקצועי לחלוטין. התאמת הצבע מדהימה, והבדלי הטקסטורה כבר אינם בולטים. היגיינה קפדנית והנחיות ברורות לבית.", "נועם ד., 29, ירושלים"),
            ("היו לי כתמים לבנים על הפנים אחרי פסוריאזיס. הצבע הותאם בדיוק לגוון העור. אני לא צריכה להתאפר כל בוקר. טיפול שמשנה חיים.", "נירית פרץ, 45, ירושלים"),
            ("ההיפופיגמנטציה בירך הפכה לאזור לבן בולט. בימים הראשונים היה כהה, אחר כך התייצב. עכשיו העור אחיד יותר.", "דרור ה., 52, ראשון לציון"),
            ("אחרי שתי לידות הבטן הייתה מלאה בסימני מתיחה לבנים ומבריקים. אחרי ההסוואה אני לובשת בגדים בלי אי־נעימות.", "ענת מזרחי, 40, ירושלים"),
            ("הייתי סקפטית. הטיפול היה ללא כאבים והצבע הותאם לשלמות. סימני המתיחה כמעט בלתי נראים.", "מלכה בן דוד, 37, בית שמש"),
            ("נולדתי עם כתם לידה כהה גדול בצוואר. הניגודיות ירדה באופן דרמטי. הצוות היה סבלני בכל שלב.", "ליאת אברהמיאן, 31, הרצליה"),
            ("כתם לידה בזרוע היה מקור בושה שנים. עבדו בשכבות עדינות בלי מראה מלאכותי. סוף סוף שרוולים קצרים בקיץ.", "זהבה לוי, 43, פתח תקווה"),
            ("רציתי סומק טבעי בלי מילוי. התוצאה נראית כמו העור שלי — רק בריאה יותר.", "טלי שמעוני, 36, תל אביב-יפו"),
            ("שיער הקרקפת הדלדל. SMP נתן מראה של שיער קצוץ וצפוף. גם מקרוב זה טבעי.", "מטופל SMP"),
        ]),
    ]),
)

PAGES[("he", "faq.html")] = (
    "שאלות נפוצות על קעקוע רפואי | Sara Scalp",
    "כאב, החלמה, משך תוצאה, מי מתאים, וצלקות קלואיד. תשובות מהקליניקה בירושלים.",
    simple_page("he", "שאלות נפוצות", "FAQ", [
        ("faq", [
            ("האם הקעקוע הרפואי מוחק צלקת?", "לא. הצלקת נשארת מבחינת מבנה. מה שמשתנה הוא הניגודיות בצבע, ולכן העין פחות נתפסת בה."),
            ("למי זה לא מתאים?", "הריון והנקה, סוכרת לא מאוזנת, נטייה לקלואיד, צלקת טרייה, מחלה עורית פעילה באזור."),
            ("כמה עולה?", "המחיר תלוי בגודל, במיקום ובמספר המפגשים. בייעוץ תקבלו הערכה."),
            ("צריך חופש מהעבודה?", "לרוב לא. האזור אדום כמה ימים. נמנעים משמש, בריכה וסאונה לפי ההנחיות."),
            ("אפשר לשלב לייזר?", "לפעמים כן, כהכנה למרקם. לא באותו יום בלי תכנון."),
        ]),
    ]),
)

PAGES[("he", "book.html")] = (
    "קביעת תור לקעקוע רפואי בירושלים | Sara Scalp",
    "קבעו ייעוץ בהסוואת צלקות, SMP ועוד. המור 1 ירושלים, 050-812-8665.",
    simple_page("he", "קביעת תור", "ייעוץ ראשון בלי התחייבות", [
        ("text", ["מלאו את הטופס ונפתח וואטסאפ עם הפרטים. אפשר גם להתקשר או להגיע לפי תיאום להמור 1, ירושלים."]),
        ("form", form_he),
    ]),
)

PAGES[("he", "privacy.html")] = (
    "מדיניות פרטיות | Sara Scalp",
    "כיצד נשמרים פרטים ותמונות מטופלים.",
    simple_page("he", "מדיניות פרטיות", "Privacy", [
        ("text", [
            "הפרטים בטופס ובשיחת וואטסאפ משמשים לחזרה אליכם ולתיאום טיפול בלבד.",
            "תמונות לפני/אחרי עולות לאתר רק עם הסכמה מפורשת בכתב.",
            "לא נמכור רשימות תפוצה. פניות: sara@sarascalpjerusalem.com או 050-812-8665.",
        ]),
    ]),
)

PAGES[("he", "accessibility.html")] = (
    "הצהרת נגישות | Sara Scalp",
    "הצהרת נגישות לאתר שרה סקאלפ.",
    simple_page("he", "הצהרת נגישות", "נגישות", [
        ("text", [
            "האתר נבנה עם HTML סמנטי, ניגודיות גבוהה, אפשרות לדלג לתוכן, וטקסט חלופי לתמונות.",
            "נתקלתם בבעיה? כתבו או התקשרו ונחזור עם תיקון. 050-812-8665.",
        ]),
    ]),
)

PAGES[("he", "terms.html")] = (
    "תנאי שימוש | Sara Scalp",
    "תנאי שימוש באתר שרה סקאלפ.",
    simple_page("he", "תנאי שימוש", "Terms", [
        ("text", [
            "המידע באתר הוא כללי ואינו מחליף ייעוץ אישי. לא כל צלקת מתאימה לטיפול.",
            "התוצאה משתנה מאדם לאדם. אין הבטחה למחיקה מלאה של צלקת.",
        ]),
    ]),
)

# English counterparts
PAGES[("en", "scar-camouflage.html")] = (
    "Scar camouflage medical tattoo in Jerusalem | Sara Scalp",
    "Blend surgical, C-section and injury scars into surrounding skin with medical-grade pigment matching.",
    service_template(
        "en",
        "Scar camouflage with medical tattooing",
        "Scar Camouflage",
        "Blurring scars after surgery, cuts or injury by matching pigment to your skin tone.",
        "skin.jpg",
        "Even skin after camouflage",
        [
            "Scar camouflage is one of the most advanced techniques in medical tattooing. The aim is to reduce how visible a scar is — after a cesarean, aesthetic surgery, orthopedic surgery, a cut or an injury — so the area blends more evenly with nearby skin.",
            "Unlike decorative tattooing, we do not draw a design over the scar. Medical pigment is placed in the upper layers of scar tissue to fill the color gap left by healing. Many scars lose pigment and look white. Thin layered work lowers that contrast.",
            "The treatment suits relatively flat scars that have matured, usually 12–18 months after injury or surgery. Hypertrophic or keloid scars need a separate assessment.",
            "The honest result is significant improvement, not total erasure. Texture remains because we do not change skin structure. Color blends and the scar is far less obvious — which is what most clients want when they put on short clothes.",
            "In Jerusalem the team trained in Brazil and Turkey. Color is matched in natural light, from several angles, with pigments made for medical tattooing.",
        ],
        ["C-section scars", "Tummy tuck, breast and body-lift scars", "Orthopedic and surgical scars", "Trauma and accident scars", "Marks after mole removal"],
        [
            ("Does it hurt?", "Discomfort is usually mild. A topical numbing cream can be used."),
            ("How long does it last?", "Long term. A refresh after some years may be wanted, depending on sun and skin."),
            ("When after surgery?", "Only once the scar is fully mature, typically 12–18 months."),
        ],
    ),
)

PAGES[("en", "burn-scars.html")] = (
    "Burn scar camouflage in Jerusalem | Sara Scalp",
    "Medical tattooing for mature burn scars after individual assessment.",
    service_template("en", "Burn scar camouflage", "Burns", "Once burn tissue is stable, missing color can be rebuilt in thin layers.", "pigment.jpg", "Matching pigment for a burn scar",
        ["Burn scars often mix light and dark patches with uneven texture. Each case is assessed in daylight.", "We do not promise a complete disappearance. The goal is that the eye no longer jumps to the patch."],
        ["Fully healed burn scars", "Pale islands inside an older burn"],
        [("Is every burn suitable?", "No. Fresh burns, unstable tissue or keloid tendency may be deferred.")],
    ),
)

PAGES[("en", "hypopigmentation.html")] = (
    "Hypopigmentation camouflage Jerusalem | Sara Scalp",
    "Fill stable white patches with custom-matched medical pigment.",
    service_template("en", "Hypopigmentation — restoring missing color", "Hypopigmentation", "Stable white patches after illness, psoriasis or injury can often be blended back toward skin tone.", "treatment-room.jpg", "Treatment room",
        ["Hypopigmentation is local loss of color. Medical tattooing fills the gap with a custom mix.", "Not every white patch is a candidate. Active vitiligo needs caution."],
        ["Stable white patches", "Pigment loss after injury"],
        [("Is this makeup?", "No. Pigment sits in the skin, not on it.")],
    ),
)

PAGES[("en", "stretch-marks.html")] = (
    "Stretch mark camouflage Jerusalem | Sara Scalp",
    "Blend pale stretch marks after pregnancy or weight change.",
    service_template("en", "Stretch mark camouflage", "Stretch marks", "Pale, shiny marks can be filled with matching tone to lower contrast.", "skin.jpg", "Skin texture",
        ["A light stretch mark reflects light differently. Camouflage fills the line with matching pigment.", "Red, new marks are still active — we wait until they turn silvery and settle."],
        ["After pregnancy", "After weight change", "Stable white marks"],
        [("Does it hurt?", "Usually well tolerated, with optional topical anesthetic.")],
    ),
)

PAGES[("en", "birthmarks.html")] = (
    "Birthmark camouflage Jerusalem | Sara Scalp",
    "Soften the contrast of a stable birthmark with layered medical pigment.",
    service_template("en", "Birthmark camouflage", "Birthmarks", "A mark that made you hide under scarves or long sleeves can sometimes be softened.", "pigment.jpg", "Custom pigment mix",
        ["A dark birthmark is not 'erased' with light ink. We reduce contrast against nearby skin when the mark is a candidate."],
        ["Stable marks on neck, arm or summer-exposed skin"],
        [("Sun after treatment?", "Avoid direct sun for several weeks and use SPF.")],
    ),
)

PAGES[("en", "freckles.html")] = (
    "Natural freckle tattoo Jerusalem | Sara Scalp",
    "Soft, daylight-looking freckles placed one by one.",
    service_template("en", "Natural freckles", "Freckles", "Warm dots placed with controlled randomness — not a stamp on every cheek.", "freckles.jpg", "Natural freckles",
        ["Permanent freckles suit anyone who wants a sun-kissed look without daily makeup. Each dot is placed so the pattern holds up in close view."],
        ["Soft freckles from scratch", "Adding to existing freckles"],
        [("Will it look fake?", "Not when tone and scatter are right.")],
    ),
)

PAGES[("en", "cheek-enhancement.html")] = (
    "Permanent blush / cheek enhancement Jerusalem | Sara Scalp",
    "A soft lasting flush without filler or daily makeup.",
    service_template("en", "Cheek enhancement", "Permanent blush", "A soft flush that looks like your skin — just more awake.", "cheeks.jpg", "Natural cheek color",
        ["Shallow, delicate work that adds vitality without filler and without putting on blush every morning."],
        ["Anyone who wants a fresh look without makeup", "Cheeks that have lost color"],
        [("Can it be removed?", "Color fades over time. Instant full removal is not promised.")],
    ),
)

PAGES[("en", "smp.html")] = (
    "Scalp micropigmentation SMP Jerusalem | Sara Scalp",
    "Tiny dots that mimic a dense buzzed hairline, judged in close-up.",
    service_template("en", "Scalp micropigmentation (SMP)", "SMP", "Precise dots that mimic shaved follicles — including in close-up.", "smp.jpg", "Scalp after SMP",
        ["SMP does not add hair. It mimics the shadow of a buzzed scalp. Quality is judged up close: dot shape, spacing and the hairline blend.", "Suits hairline recession, thinning that fits a buzzed look, and scalp scars."],
        ["Receding hairline", "Thinning suited to a cropped look", "Scalp scars"],
        [("Will it look drawn-on?", "Good work looks like follicle dots, not flat lines.")],
    ),
)

PAGES[("en", "about.html")] = (
    "About Sara Scalp Jerusalem",
    "Medical tattoo clinic in Jerusalem. Training in Brazil and Turkey. Hamor 1.",
    simple_page("en", "The story behind Sara Scalp", "About", [
        ("split", [
            "Sara Scalp is a clinic for medical tattooing and micropigmentation in Jerusalem. We help people living with scars, burns, pigment change, stretch marks, birthmarks or hair loss.",
            "The team trained in Brazil and Turkey. The studio also draws on paramedical experience, including a certified dental hygienist background — sterility and tissue respect are not extras.",
            "We do not sell magic. We explain what a scar can take. Color is matched in daylight, in layers, with medical pigments.",
            "Clinic: Hamor 1, Jerusalem. Sun–Thu 09:00–18:00. Fri and holiday eves 09:00–14:00.",
        ], "jerusalem.jpg", "Jerusalem light"),
    ]),
)

PAGES[("en", "process.html")] = (
    "How medical tattooing works | Sara Scalp",
    "Consult, color match, layered treatment and follow-up in Jerusalem.",
    simple_page("en", "How the process works", "Clear steps", [
        ("steps", [
            ("01", "Consult", "We study the area in natural light: skin type, tone, texture, maturity."),
            ("02", "Color", "Medical pigments are mixed until they meet surrounding skin."),
            ("03", "Treatment", "Fine needles, thin layers, a dedicated device."),
            ("04", "Follow-up", "Usually 2–4 visits. You leave with home-care notes."),
            ("05", "Settle", "Color settles over weeks. The final look is judged after healing."),
        ]),
    ]),
)

PAGES[("en", "gallery.html")] = (
    "Before and after | Sara Scalp Jerusalem",
    "Replace these mood images with consented clinic photographs.",
    simple_page("en", "Before & after", "Judged in daylight", [
        ("text", ["Real before/after photos will replace these studio images once you add consented clinic files to assets/img."]),
        ("gallery", [
            ("skin.jpg", "Scar camouflage — slot for your photo"),
            ("pigment.jpg", "Pigment matching"),
            ("smp.jpg", "SMP close-up slot"),
            ("freckles.jpg", "Freckles slot"),
            ("cheeks.jpg", "Cheek enhancement"),
            ("treatment-room.jpg", "Treatment room"),
        ]),
    ]),
)

PAGES[("en", "testimonials.html")] = (
    "Client reviews | Sara Scalp Jerusalem",
    "Reviews of scar camouflage, burns, stretch marks and SMP.",
    simple_page("en", "Reviews", "In their words", [
        ("quotes", [
            ("Color matching was excellent and the texture difference is no longer obvious. Strict hygiene and clear aftercare.", "Noam D., 29, Jerusalem"),
            ("White patches on my face after psoriasis were the first thing people saw. I no longer need heavy makeup every morning.", "Nirit Peretz, 45, Jerusalem"),
            ("After two births my abdomen was full of white stretch marks. I can wear clothes without discomfort.", "Anat Mizrahi, 40, Jerusalem"),
            ("SMP gave me a cropped, dense look that holds up close.", "SMP client"),
        ]),
    ]),
)

PAGES[("en", "faq.html")] = (
    "FAQ | Sara Scalp Jerusalem",
    "Pain, healing, duration, candidacy and keloids.",
    simple_page("en", "FAQ", "Questions", [
        ("faq", [
            ("Does this erase a scar?", "No. Structure stays. Contrast drops, so the eye moves on."),
            ("Who should wait?", "Pregnancy, nursing, uncontrolled diabetes, keloid tendency, fresh scars, active skin disease."),
            ("What does it cost?", "Depends on size, site and sessions. You get an estimate at consult."),
        ]),
    ]),
)

PAGES[("en", "book.html")] = (
    "Book a medical tattoo consult in Jerusalem | Sara Scalp",
    "WhatsApp or call 050-812-8665. Hamor 1, Jerusalem.",
    simple_page("en", "Book a visit", "No obligation first consult", [
        ("text", ["The form opens WhatsApp with your details. You can also call or visit Hamor 1 by appointment."]),
        ("form", form_en),
    ]),
)

PAGES[("en", "privacy.html")] = (
    "Privacy | Sara Scalp",
    "How we handle enquiry details and photos.",
    simple_page("en", "Privacy", "Privacy", [
        ("text", ["Form and WhatsApp details are used only to reply and book.", "Before/after photos go online only with written consent.", "Contact: sara@sarascalpjerusalem.com · 050-812-8665."]),
    ]),
)

PAGES[("en", "accessibility.html")] = (
    "Accessibility | Sara Scalp",
    "Accessibility statement.",
    simple_page("en", "Accessibility", "Access", [
        ("text", ["The site uses semantic HTML, skip links and image alt text. If something blocks you, call 050-812-8665."]),
    ]),
)

PAGES[("en", "terms.html")] = (
    "Terms | Sara Scalp",
    "Website terms.",
    simple_page("en", "Terms of use", "Terms", [
        ("text", ["Content is general and not a personal medical opinion. Results vary. Full scar erasure is not promised."]),
    ]),
)


def write_page(lang, slug, title, desc, body):
    html = page(lang, slug, title, desc, body)
    if lang == "he":
        path = ROOT / slug
    else:
        path = ROOT / "en" / slug
    path.write_text(html, encoding="utf-8")


def main():
    write_page("he", "index.html", "הסוואת צלקות וקעקוע רפואי בירושלים | Sara Scalp",
               "קליניקה להסוואת צלקות, כוויות, סימני מתיחה והדמיית שיער SMP בירושלים. המור 1.", home_he())
    write_page("en", "index.html", "Scar camouflage & medical tattoo Jerusalem | Sara Scalp",
               "Medical tattoo clinic in Jerusalem for scar camouflage, burns, stretch marks and SMP. Hamor 1.", home_en())
    for (lang, slug), (title, desc, body) in PAGES.items():
        write_page(lang, slug, title, desc, body)

    slugs = ["index.html"] + sorted({s for l, s in PAGES})
    urls = []
    for s in slugs:
        loc = "" if s == "index.html" else s
        urls.append(f"  <url><loc>https://YOUR-USER.github.io/sara-scalp/{loc}</loc><changefreq>monthly</changefreq></url>")
        urls.append(f"  <url><loc>https://YOUR-USER.github.io/sara-scalp/en/{loc}</loc><changefreq>monthly</changefreq></url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls) + "\n</urlset>\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://YOUR-USER.github.io/sara-scalp/sitemap.xml\n", encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("built", len(list(ROOT.glob('*.html'))) + len(list((ROOT/'en').glob('*.html'))), "html files")


if __name__ == "__main__":
    main()
