from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {'message': 'PSNP Flask API is live!'}

@app.route('/api/trophies/<username>')
def get_trophies(username):
    return jsonify({...})  # your trophy data here

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
