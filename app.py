from flask import Flask, request, jsonify
from flask_cors import CORS
from ytmusicapi import YTMusic
from yt_dlp import YoutubeDL

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

@app.route("/audio")
def get_audio():

    video_id = request.args.get("videoId")

    if not video_id:
        return jsonify({
            "error": "videoId required"
        }), 400

    try:

        url = f"https://www.youtube.com/watch?v={video_id}"

        ydl_opts = {
            "format": "bestaudio",
            "quiet": True,
            "noplaylist": True
        }

        with YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                url,
                download=False
            )

            return jsonify({
                "audioUrl": info["url"]
            })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
        
if __name__ == "__main__":
    app.run(debug=True)