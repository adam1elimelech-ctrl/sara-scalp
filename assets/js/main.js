(function () {
  const btn = document.querySelector("[data-menu]");
  const panel = document.querySelector("[data-panel]");
  if (btn && panel) {
    btn.addEventListener("click", () => {
      const open = panel.style.display === "block";
      panel.style.display = open ? "none" : "block";
      btn.setAttribute("aria-expanded", String(!open));
    });
  }

  const api = window.SARA_API || "";

  async function loadSlots(select) {
    if (!select || !api) return;
    try {
      const res = await fetch(api + "/api/slots");
      const data = await res.json();
      select.innerHTML = '<option value="">בחרו יום ושעה</option>';
      Object.keys(data).forEach((day) => {
        data[day].forEach((time) => {
          const opt = document.createElement("option");
          opt.value = day + "|" + time;
          opt.textContent = day + " · " + time;
          select.appendChild(opt);
        });
      });
    } catch (e) {
      select.innerHTML = '<option value="">היומן ייפתח אחרי חיבור השרת</option>';
    }
  }

  document.querySelectorAll("[data-slot]").forEach(loadSlots);

  document.querySelectorAll("[data-lead-form]").forEach((form) => {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const fd = new FormData(form);
      const slot = (fd.get("slot") || "").split("|");
      if (slot.length === 2) {
        fd.set("slot_date", slot[0]);
        fd.set("slot_time", slot[1]);
      }
      const name = fd.get("name") || "";
      const phone = fd.get("phone") || "";
      const service = fd.get("service") || "";
      const msg = fd.get("message") || "";
      const wa =
        "https://wa.me/972508128665?text=" +
        encodeURIComponent(
          "שלום שרה סקאלפ, שמי " + name + ". טלפון: " + phone + ". טיפול: " + service + ". " + msg
        );

      if (api) {
        try {
          const res = await fetch(api + "/api/leads", { method: "POST", body: fd });
          const json = await res.json();
          if (json.ok) {
            form.reset();
            alert("הפנייה נשמרה. נפתח וואטסאפ לאישור.");
            window.open(json.whatsapp || wa, "_blank");
            return;
          }
        } catch (err) {}
      }
      window.open(wa, "_blank");
    });
  });

  document.querySelectorAll("[data-wa-form]").forEach((form) => {
    if (form.hasAttribute("data-lead-form")) return;
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const text = encodeURIComponent(
        "שלום שרה סקאלפ, שמי " + (data.get("name") || "") + ". טלפון: " + (data.get("phone") || "") + ". טיפול: " + (data.get("service") || "") + ". " + (data.get("message") || "")
      );
      window.open("https://wa.me/972508128665?text=" + text, "_blank");
    });
  });
})();
