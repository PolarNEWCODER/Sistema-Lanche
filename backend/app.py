from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"msg": "API funcionando"})

app.run(debug=True) 