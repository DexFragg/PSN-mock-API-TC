from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return {'message': 'PSNP Flask API is live!'}

@app.route('/api/trophies/<username>')
def get_trophies(username):
    return jsonify({
        "user": username,
        "level": 350,
        "xp_progress": 73,
        "games": [
            {
                "title": "God of War Ragnarok",
                "cover": "https://image.example.com/gowr.jpg",
                "progress": 85,
                "trophies": {
                    "platinum": 1,
                    "gold": 5,
                    "silver": 10,
                    "bronze": 20
                },
                "rarity": {
                    "Ultra Rare": 2,
                    "Rare": 8,
                    "Common": 26
                }
            }
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)