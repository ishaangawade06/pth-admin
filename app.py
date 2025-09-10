from flask import Flask, request, render_template, redirect, url_for, flash
import os, requests

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "supersecretlocal")

# Config
BACKEND_URL = os.environ.get("BACKEND_URL", "https://protraderhack.onrender.com").rstrip("/")
OWNER_KEY   = os.environ.get("OWNER_KEY", "supersecret")

@app.route("/")
def index():
    return render_template("admin_index.html")

@app.route("/api/add-key", methods=["POST"])
def add_key():
    key = request.form.get("key")
    role = request.form.get("role", "user")
    days = request.form.get("days", None)

    if not key:
        flash("❌ Missing key", "error")
        return redirect(url_for("index"))

    try:
        payload = {"key": key, "role": role}
        if days:
            payload["days"] = int(days)

        r = requests.post(
            f"{BACKEND_URL}/owner/add-key",
            json=payload,
            headers={"X-OWNER-KEY": OWNER_KEY},
            timeout=15
        )

        if r.status_code == 200:
            flash(f"✅ Key '{key}' added successfully", "success")
        else:
            flash(f"❌ Failed to add key: {r.text}", "error")
    except Exception as e:
        flash(f"❌ Error: {str(e)}", "error")

    return redirect(url_for("index"))

@app.route("/api/delete-key", methods=["POST"])
def delete_key():
    key = request.form.get("key")
    if not key:
        flash("❌ Missing key", "error")
        return redirect(url_for("index"))

    try:
        r = requests.post(
            f"{BACKEND_URL}/owner/delete-key",
            params={"key": key},
            headers={"X-OWNER-KEY": OWNER_KEY},
            timeout=15
        )
        if r.status_code == 200:
            flash(f"✅ Key '{key}' deleted successfully", "success")
        else:
            flash(f"❌ Failed to delete key: {r.text}", "error")
    except Exception as e:
        flash(f"❌ Error: {str(e)}", "error")

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
