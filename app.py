from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/trophies/<username>')
def get_trophies(username):
    return jsonify({
        "user": username,
        "level": 421,
        "xp_progress": 92,
        "total_trophies": {
            "platinum": 12,
            "gold": 85,
            "silver": 232,
            "bronze": 894
        },
        "games": [
            {
                "title": "God of War Ragnarok",
                "cover": "https://image.api.playstation.com/vulcan/ap/rnd/202211/1615/yjqOyDjTDXFaX6CMvH7nWZ2Q.png",
                "progress": 87,
                "trophies": {
                    "platinum": 1,
                    "gold": 3,
                    "silver": 10,
                    "bronze": 22
                }
            },
            {
                "title": "Horizon Forbidden West",
                "cover": "https://image.api.playstation.com/vulcan/ap/rnd/202202/2316/NvJkD1RB0EpjYdYysaaN3VyD.png",
                "progress": 64,
                "trophies": {
                    "platinum": 0,
                    "gold": 4,
                    "silver": 12,
                    "bronze": 18
                }
            }
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)