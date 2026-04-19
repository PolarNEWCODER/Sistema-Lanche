from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"msg": "API rodando"})

@app.route('/produto', methods=['POST'])
def produto():
    dados = request.json
    return jsonify({"msg": "Produto cadastrado", "dados": dados})

app.run(debug=True)