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

  document.querySelectorAll("[data-wa-form]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const name = data.get("name") || "";
      const phone = data.get("phone") || "";
      const service = data.get("service") || "";
      const msg = data.get("message") || "";
      const text = encodeURIComponent(
        `שלום שרה סקאלפ, שמי ${name}. טלפון: ${phone}. טיפול: ${service}. ${msg}`
      );
      window.open("https://wa.me/972508128665?text=" + text, "_blank");
    });
  });
})();
