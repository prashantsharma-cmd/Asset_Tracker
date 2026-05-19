from flask import Flask, jsonify, render_template
import requests, csv, io, os

app = Flask(__name__)

SHEET_URL = os.environ.get("SHEET_URL")  # set this in Render dashboard

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/scans")
def scans():
    resp = requests.get(SHEET_URL, timeout=10)
    reader = csv.DictReader(io.StringIO(resp.text))
    return jsonify(list(reader))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))