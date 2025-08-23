from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Conexão com a base de dados goodwe
def conectar():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="goodwe",
        user="postgres",
        password="sua_senha_aqui"  # substitua pela sua senha real
    )

@app.route("/cadastro", methods=["POST"])
def cadastrar_usuario():
    data = request.json

    nome = data.get("nome")
    idade = data.get("idade")
    usuario = data.get("usuario")
    email = data.get("email")
    senha = data.get("senha")

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO usuarios (email, usuario, nome, idade, senha)
            VALUES (%s, %s, %s, %s, %s)
        """, (email, usuario, nome, idade, senha))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
