const BACKEND_URL = "https://your-backend.onrender.com"; // replace later with your actual Render URL
let OWNER_KEY = "";

// Login
document.getElementById("loginBtn").addEventListener("click", () => {
  OWNER_KEY = document.getElementById("ownerKey").value.trim();
  if (OWNER_KEY) {
    document.getElementById("login-section").style.display = "none";
    document.getElementById("admin-section").style.display = "block";
    loadKeys();
  }
});

// Add Key
document.getElementById("addKeyBtn").addEventListener("click", async () => {
  const key = document.getElementById("newKey").value.trim();
  const role = document.getElementById("role").value;
  const days = document.getElementById("days").value.trim();

  const res = await fetch(`${BACKEND_URL}/owner/add-key`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-APP-KEY": OWNER_KEY
    },
    body: JSON.stringify({ key, role, days: days ? parseInt(days) : null })
  });

  const data = await res.json();
  alert(JSON.stringify(data));
  loadKeys();
});

// Load Keys
async function loadKeys() {
  const res = await fetch(`${BACKEND_URL}/owner/list-keys`, {
    headers: { "X-APP-KEY": OWNER_KEY }
  });
  const data = await res.json();
  const list = document.getElementById("keyList");
  list.innerHTML = "";
  if (data.keys) {
    data.keys.forEach(k => {
      const li = document.createElement("li");
      li.className = "list-group-item bg-secondary text-light d-flex justify-content-between align-items-center";
      li.textContent = `${k.key} (${k.role}) exp: ${k.expiry || "never"}`;
      list.appendChild(li);
    });
  }
}
