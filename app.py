from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "IA Gamer Online!"

@app.route("/command", methods=["POST"])
def command():
    data = request.json

    print(data)

    return jsonify({
        "action": "tap",
        "x": 500,
        "y": 800
    })

app.run(host="0.0.0.0", port=10000)