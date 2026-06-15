from flask import Flask, request, jsonify
from ytmusicapi import YTMusic

app = Flask(__name__)
ytmusic = YTMusic()

@app.route("/")
def home():
    return {"status": "running"}

@app.route("/search")
def search():
    q = request.args.get("q", "")
    results = ytmusic.search(q, filter="songs")
    return jsonify(results[:20])