from flask import Flask, jsonify, request

app = Flask(__name__)


# usuarios
usuarios = [
    {"id": 1, "nome": "Alice"},
    {"id": 2, "nome": "Bob"},
    {"id": 3, "nome": "Carol"}
]

#usuarios
@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios/<int:user_id>", methods=["GET"])
def get_usuario(user_id):
    # procurar o usuario
    usuario = None

    for item_usuario in usuarios:
        if user_id == item_usuario["id"]:
            usuario = item_usuario
            break

    if usuario:
        return jsonify(usuario)
    
    return jsonify({"mensagem": "Usuário não encontrado"}), 404

@app.route("/usuarios", methods=["POST"])
def adicionar_usuario():
    dados = request.get_json()

    if not "nome" in dados:
        return jsonify({"mensagem": "Dados inválidos"}), 400

    novo_usuario = {"id": len(usuarios) + 1, "nome": dados["nome"]}
    usuarios.append(novo_usuario)
    return jsonify({"mensagem": "Usuário cadastrado com sucesso"}), 201

if __name__ == "__main__":
    app.run(debug=True)