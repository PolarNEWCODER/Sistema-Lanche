from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# "Banco fake" em memória
produtos = []
vendas = []

# TESTE
@app.route('/')
def home():
    return jsonify({"msg": "API rodando"})

# CADASTRAR PRODUTO
@app.route('/produto', methods=['POST'])
def cadastrar_produto():
    dados = request.json
    produtos.append(dados)
    return jsonify({"msg": "Produto cadastrado", "produtos": produtos})

# LISTAR PRODUTOS
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

# REALIZAR VENDA
@app.route('/venda', methods=['POST'])
def venda():
    dados = request.json
    vendas.append(dados)
    return jsonify({"msg": "Venda realizada", "vendas": vendas})

app.run(debug=True)