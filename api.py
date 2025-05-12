from flask import Flask, request, jsonify
<<<<<<< HEAD
from flask_mysqldb import MySQL
=======
>>>>>>> a957099d2a0cd302a4bd626cf706ecaaac1c13b9
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

<<<<<<< HEAD
# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Cambia si tu MySQL tiene contraseña
app.config['MYSQL_DB'] = 'prueba_db'
app.config['MYSQL_PORT'] = 3308  # Puerto de tu base de datos
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Ruta de login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        print("Datos recibidos:", data)  # ✅ Verificar datos

        correo = data.get('correo')
        contrasena = data.get('contrasena')

        if not correo or not contrasena:
            return jsonify({"mensaje": "Faltan credenciales"}), 400

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE email = %s", (correo,))
        usuario = cur.fetchone()
        cur.close()

        if usuario and usuario['contraseña'] == contrasena:
            return jsonify({"mensaje": "OK", "usuario": usuario['nombre']}), 200
        else:
            return jsonify({"mensaje": "Credenciales inválidas"}), 401

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"mensaje": "Error interno del servidor"}), 500

# Ruta de registro (sin encriptación)
@app.route('/registro', methods=['POST'])
def registro():
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        email = data.get('email')
        clave = data.get('clave')

        if not nombre or not email or not clave:
            return jsonify({"mensaje": "Faltan datos"}), 400

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios (nombre, email, contraseña) VALUES (%s, %s, %s)", 
                    (nombre, email, clave))
        mysql.connection.commit()
        cur.close()

        return jsonify({"mensaje": "Usuario registrado correctamente"}), 201

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"mensaje": "Error al registrar usuario"}), 500
@app.route('/productos', methods=['GET'])
def obtener_productos():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM producto")
        productos = cur.fetchall()
        cur.close()

        return jsonify([dict(producto) for producto in productos]), 200

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"mensaje": f"Error al obtener productos: {str(e)}"}), 500
    
=======
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

>>>>>>> a957099d2a0cd302a4bd626cf706ecaaac1c13b9
if __name__ == '__main__':
    app.run(debug=True)