# Sara Scalp Jerusalem

אתר סטטי דו־לשוני (עברית + English) לקליניקת קעקוע רפואי בירושלים.  
מוכן ל־**GitHub Pages** בריפו `sara-scalp`.

## מה בפנים

- 18 עמודים בעברית בשורש
- 18 עמודים באנגלית בתיקייה `en/`
- עיצוב שמנת/זהב, אנימציות עדינות, וואטסאפ צף
- תמונות WebP קלות + JPG גיבוי
- Schema מסוג MedicalBusiness
- טופס שפותח וואטסאפ עם הפרטים
- מדיניות פרטיות, נגישות, תנאי שימוש

## העלאה ל־GitHub Desktop (הריפו sara-scalp)

1. ב־GitHub Desktop בחרו את הריפו **sara-scalp** (או File → Add local repository).
2. אם הריפו ריק, העתיקו לתוכו **את כל התוכן של התיקייה הזו** (לא את התיקייה עצמה כעטיפה כפולה):

```
index.html
about.html
...
en/
assets/
README.md
robots.txt
sitemap.xml
.nojekyll
404.html
```

3. Commit message לדוגמה: `Launch Sara Scalp bilingual clinic site`
4. Push origin.
5. באתר GitHub: Settings → Pages → Source: **Deploy from a branch** → branch `main` → folder `/ (root)` → Save.
6. האתר יעלה ל־`https://YOUR-USERNAME.github.io/sara-scalp/`

### דומיין עצמאי

Settings → Pages → Custom domain, למשל `sarascalp.co.il`.  
אצל רשם הדומיין הוסיפו רשומת A/CNAME לפי ההוראות של GitHub.  
עדכנו ב־`sitemap.xml` ו־`robots.txt` את הכתובת במקום `YOUR-USER.github.io/sara-scalp`.

## החלפת תמונות אמיתיות

שימו קבצים ב־`assets/img/` באותם שמות:

| קובץ | מה לשים |
|---|---|
| `hero-clinic.jpg` + `.webp` | קבלה / קליניקה |
| `treatment-room.jpg` | חדר טיפול |
| `pigment.jpg` | ערבוב פיגמנט |
| `skin.jpg` | תקריב עור / צלקת מוסווית |
| `smp.jpg` | תקריב SMP |
| `freckles.jpg` | נמשים |
| `cheeks.jpg` | סומק |
| `jerusalem.jpg` | אווירת הקליניקה |

ב־`gallery.html` החליפו בזוגות לפני/אחרי עם הסכמת מטופלים.

## בניה מחדש אחרי שינוי טקסט

```
python3 build.py
```

## פרטי קשר שמוטמעים באתר

- טלפון / וואטסאפ: 050-812-8665
- כתובת: המור 1, ירושלים
- מייל: sara@sarascalpjerusalem.com
- שעות: א׳–ה׳ 09:00–18:00 · ו׳ וערבי חג 09:00–14:00
