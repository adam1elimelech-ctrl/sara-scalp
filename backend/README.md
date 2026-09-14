# Backend שרה סקאלפ

שומר פניות + תמונות + יומן תורים + אזור ניהול.

## הרצה מקומית

```
cd backend
pip install -r requirements.txt
python app.py
```

השרת עולה על http://127.0.0.1:5050  
ניהול: http://127.0.0.1:5050/admin  
משתמש ברירת מחדל: `sara`  
סיסמה ברירת מחדל: `scalp2026`  
שנו מיד עם משתני סביבה.

## מייל ל־sarascalp@gmail.com

צרו בגוגל **סיסמת אפליקציה** (לא הסיסמה הרגילה של ג׳ימייל) והריצו:

```
set ADMIN_USER=sara
set ADMIN_PASS=סיסמה-חזקה
set SMTP_USER=sarascalp@gmail.com
set SMTP_PASS=סיסמת-האפליקציה
set SECRET_KEY=מחרוזת-סודית
python app.py
```

בלי SMTP הפנייה עדיין נשמרת במסד ובקובץ `last-notify.txt`. וואטסאפ נפתח תמיד ל־050-812-8665.

## חיבור לאתר ב־GitHub Pages

ב־`assets/js/config.js` שנו לכתובת השרת אחרי העלאה ל־Render:

```
window.SARA_API = "https://YOUR-SERVICE.onrender.com";
```

ב־Render: New Web Service, root `backend`, start command `python app.py`.

GitHub Pages לא מריץ שרת. האתר הסטטי נשאר ב-Pages, הניהול רץ בנפרד.
