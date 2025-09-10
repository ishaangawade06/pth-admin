from flask import Flask, request, render_template, jsonify
import os, requests

app = Flask(__name__)

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
        return jsonify({"error": "missing key"}), 400

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
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/delete-key", methods=["POST"])
def delete_key():
    key = request.form.get("key")
    if not key:
        return jsonify({"error": "missing key"}), 400
    try:
        r = requests.post(
            f"{BACKEND_URL}/owner/delete-key",
            params={"key": key},
            headers={"X-OWNER-KEY": OWNER_KEY},
            timeout=15
        )
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
