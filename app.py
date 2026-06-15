from flask import Flask, request, jsonify
from flask_cors import CORS
from ytmusicapi import YTMusic

app = Flask(__name__)
CORS(app)

ytmusic = YTMusic()

@app.route("/")
def home():
    return {"status": "Sonix API running"}

@app.route("/search")
def search():
    q = request.args.get("q", "")
    results = ytmusic.search(q, filter="songs")
    return jsonify(results[:20])