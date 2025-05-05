from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios = []

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.get_json()
    usuarios.append({
        "correo": data.get("usuario"),      # ✅ Cambia a "usuario" si es el campo en Kivy
        "contrasena": data.get("clave")
    })
    return jsonify({"mensaje": "Registrado correctamente"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('correo')
    contrasena = data.get('contrasena')

    if not correo or not contrasena:
        return jsonify({"mensaje": "Faltan credenciales"}), 400

    for usuario in usuarios:
        if usuario.get('correo') == correo and usuario.get('contrasena') == contrasena:
            return jsonify({"mensaje": "OK", "redirect": "catalogo"})
    
    return jsonify({"mensaje": "Correo o contraseña incorrectos"}), 401

if __name__ == '__main__':
    app.run(debug=True)