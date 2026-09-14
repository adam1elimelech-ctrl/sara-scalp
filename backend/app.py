#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sara Scalp backend: leads, photo upload, calendar, admin."""
import os, sqlite3, smtplib, secrets, datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from functools import wraps
from flask import (
    Flask, request, jsonify, send_from_directory, session, redirect, render_template_string
)
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

ROOT = Path(__file__).parent
DB = ROOT / "sara.db"
UPLOADS = ROOT / "uploads"
UPLOADS.mkdir(exist_ok=True)

ADMIN_USER = os.environ.get("ADMIN_USER", "sara")
ADMIN_PASS = os.environ.get("ADMIN_PASS", "scalp2026")
SECRET = os.environ.get("SECRET_KEY", "change-me-sara-scalp")
NOTIFY_EMAIL = "sarascalp@gmail.com"
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASS = os.environ.get("SMTP_PASS", "")

app = Flask(__name__)
app.secret_key = SECRET
CORS(app, supports_credentials=True)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024
ALLOWED = {".jpg", ".jpeg", ".png", ".webp"}


def db():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def init():
    con = db()
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS leads (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          created TEXT,
          name TEXT, phone TEXT, email TEXT,
          service TEXT, message TEXT, photo TEXT,
          slot_date TEXT, slot_time TEXT,
          status TEXT DEFAULT 'new'
        );
        CREATE TABLE IF NOT EXISTS slots (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          day TEXT, time TEXT, taken INTEGER DEFAULT 0
        );
        """
    )
    if con.execute("SELECT COUNT(*) c FROM slots").fetchone()["c"] == 0:
        times = ["09:00", "10:30", "12:00", "14:00", "16:00"]
        start = datetime.date.today()
        for i in range(1, 22):
            d = start + datetime.timedelta(days=i)
            if d.weekday() == 5:  # Saturday closed
                continue
            for t in times:
                if d.weekday() == 4 and t >= "14:00":  # Friday until 14
                    continue
                con.execute("INSERT INTO slots(day,time,taken) VALUES(?,?,0)", (d.isoformat(), t))
    con.commit()
    con.close()


def mail_notify(lead):
    body = (
        f"פנייה חדשה מאתר שרה סקאלפ\n\n"
        f"שם: {lead['name']}\nטלפון: {lead['phone']}\nמייל: {lead.get('email')}\n"
        f"טיפול: {lead['service']}\nמועד: {lead.get('slot_date')} {lead.get('slot_time')}\n"
        f"הודעה: {lead['message']}\nתמונה: {lead.get('photo')}\n"
    )
    if not SMTP_USER or not SMTP_PASS:
        (ROOT / "last-notify.txt").write_text(body, encoding="utf-8")
        return False
    msg = MIMEMultipart()
    msg["Subject"] = f"פנייה חדשה: {lead['name']} — {lead['service']}"
    msg["From"] = SMTP_USER
    msg["To"] = NOTIFY_EMAIL
    msg.attach(MIMEText(body, "plain", "utf-8"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, [NOTIFY_EMAIL], msg.as_string())
    return True


@app.get("/api/health")
def health():
    return {"ok": True}


@app.get("/api/slots")
def slots():
    con = db()
    rows = con.execute(
        "SELECT day, time FROM slots WHERE taken=0 AND day>=? ORDER BY day,time LIMIT 80",
        (datetime.date.today().isoformat(),),
    ).fetchall()
    con.close()
    out = {}
    for r in rows:
        out.setdefault(r["day"], []).append(r["time"])
    return jsonify(out)


@app.post("/api/leads")
def create_lead():
    name = (request.form.get("name") or "").strip()
    phone = (request.form.get("phone") or "").strip()
    if not name or not phone:
        return jsonify({"error": "name and phone required"}), 400
    email = (request.form.get("email") or "").strip()
    service = (request.form.get("service") or "").strip()
    message = (request.form.get("message") or "").strip()
    slot_date = (request.form.get("slot_date") or "").strip()
    slot_time = (request.form.get("slot_time") or "").strip()
    photo_name = ""
    f = request.files.get("photo")
    if f and f.filename:
        ext = Path(f.filename).suffix.lower()
        if ext not in ALLOWED:
            return jsonify({"error": "file type not allowed"}), 400
        photo_name = secrets.token_hex(8) + ext
        f.save(UPLOADS / photo_name)
    con = db()
    if slot_date and slot_time:
        row = con.execute(
            "SELECT id,taken FROM slots WHERE day=? AND time=?", (slot_date, slot_time)
        ).fetchone()
        if not row or row["taken"]:
            con.close()
            return jsonify({"error": "slot taken"}), 409
        con.execute("UPDATE slots SET taken=1 WHERE id=?", (row["id"],))
    con.execute(
        """INSERT INTO leads(created,name,phone,email,service,message,photo,slot_date,slot_time)
           VALUES(?,?,?,?,?,?,?,?,?)""",
        (
            datetime.datetime.now().isoformat(timespec="minutes"),
            name, phone, email, service, message, photo_name, slot_date, slot_time,
        ),
    )
    con.commit()
    con.close()
    lead = {
        "name": name, "phone": phone, "email": email, "service": service,
        "message": message, "photo": photo_name, "slot_date": slot_date, "slot_time": slot_time,
    }
    try:
        mail_notify(lead)
    except Exception as e:
        (ROOT / "mail-error.txt").write_text(str(e), encoding="utf-8")
    wa = "https://wa.me/972508128665?text=" + (
        f"שלום שרה סקאלפ, שמי {name}. טלפון: {phone}. טיפול: {service}. "
        f"מועד: {slot_date} {slot_time}. {message}"
    ).replace(" ", "%20")
    return jsonify({"ok": True, "whatsapp": wa})


def login_required(fn):
    @wraps(fn)
    def wrap(*a, **k):
        if not session.get("admin"):
            return redirect("/admin/login")
        return fn(*a, **k)
    return wrap


LOGIN_HTML = """
<!doctype html><html lang="he" dir="rtl"><meta charset="utf-8">
<title>כניסת ניהול</title>
<style>body{font-family:Assistant,sans-serif;background:#F6F1E8;display:grid;place-items:center;min-height:100vh}
form{background:#fff;padding:28px;border-radius:18px;width:min(360px,90vw);display:grid;gap:10px}
input,button{padding:10px;border-radius:10px;border:1px solid #ddd;font:inherit}
button{background:#C4A574;border:0;font-weight:700}</style>
<form method="post"><h2>ניהול שרה סקאלפ</h2>
<input name="user" placeholder="שם משתמש" required>
<input name="password" type="password" placeholder="סיסמה" required>
<button>כניסה</button></form></html>
"""

ADMIN_HTML = """
<!doctype html><html lang="he" dir="rtl"><meta charset="utf-8">
<title>פניות</title>
<style>
body{font-family:Assistant,sans-serif;background:#F6F1E8;margin:0;color:#1A1714}
header{background:#161310;color:#fff;padding:16px 24px;display:flex;justify-content:space-between}
table{width:100%;border-collapse:collapse;background:#fff}
th,td{border-bottom:1px solid #eee;padding:10px 12px;text-align:right;font-size:14px;vertical-align:top}
img{max-width:90px;border-radius:8px}
a{color:#9A7B4F}
.wrap{padding:20px}
select{padding:6px}
</style>
<header><strong>אזור ניהול · פניות</strong>
<div><a href="/admin/logout" style="color:#E3D2B0">יציאה</a></div></header>
<div class="wrap">
<p>{{n}} פניות</p>
<table>
<tr><th>#</th><th>תאריך</th><th>שם</th><th>טלפון</th><th>טיפול</th><th>מועד</th><th>הודעה</th><th>תמונה</th><th>סטטוס</th></tr>
{% for r in rows %}
<tr>
<td>{{r.id}}</td><td>{{r.created}}</td><td>{{r.name}}</td>
<td><a href="https://wa.me/972{{r.phone|replace('-','')|replace(' ','')}}">{{r.phone}}</a></td>
<td>{{r.service}}</td><td>{{r.slot_date}} {{r.slot_time}}</td>
<td>{{r.message}}</td>
<td>{% if r.photo %}<a href="/uploads/{{r.photo}}" target="_blank"><img src="/uploads/{{r.photo}}"></a>{% endif %}</td>
<td>
<form method="post" action="/admin/status">
<input type="hidden" name="id" value="{{r.id}}">
<select name="status" onchange="this.form.submit()">
<option {% if r.status=='new' %}selected{% endif %}>new</option>
<option {% if r.status=='contacted' %}selected{% endif %}>contacted</option>
<option {% if r.status=='booked' %}selected{% endif %}>booked</option>
<option {% if r.status=='done' %}selected{% endif %}>done</option>
</select>
</form>
</td></tr>
{% endfor %}
</table></div></html>
"""


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        if request.form.get("user") == ADMIN_USER and request.form.get("password") == ADMIN_PASS:
            session["admin"] = True
            return redirect("/admin")
        return "סיסמה שגויה", 401
    return LOGIN_HTML


@app.get("/admin/logout")
def admin_logout():
    session.clear()
    return redirect("/admin/login")


@app.get("/admin")
@login_required
def admin():
    from flask import render_template_string as rts
    con = db()
    rows = con.execute("SELECT * FROM leads ORDER BY id DESC").fetchall()
    con.close()
    return rts(ADMIN_HTML, rows=rows, n=len(rows))


@app.post("/admin/status")
@login_required
def admin_status():
    con = db()
    con.execute("UPDATE leads SET status=? WHERE id=?", (request.form.get("status"), request.form.get("id")))
    con.commit()
    con.close()
    return redirect("/admin")


@app.get("/uploads/<path:name>")
@login_required
def upload(name):
    return send_from_directory(UPLOADS, name)


if __name__ == "__main__":
    init()
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port, debug=False)
