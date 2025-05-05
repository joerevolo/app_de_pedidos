import requests
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from os.path import dirname, join

# Cargar el archivo .kv
Builder.load_file(join(dirname(__file__), 'login.kv'))

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.usuario_guardado = ''
        self.clave_guardada = ''

    def on_kv_post(self, base_widget):
        # Asociar botones con sus métodos correspondientes
        self.ids.boton_registrar.bind(on_press=self.registrar)
        self.ids.boton_login.bind(on_press=self.iniciar_sesion)  # Cambiado a iniciar_sesion

    def registrar(self, instance):
        # Enviar datos al servidor Flask
        datos = {
            "usuario": self.ids.usuario.text,
            "clave": self.ids.clave.text
        }

        try:
            r = requests.post("http://127.0.0.1:5000/registrar", json=datos)
            r.raise_for_status()  # Lanza error si status_code != 200
            mensaje = r.json().get("mensaje", "Registro exitoso")
        except requests.exceptions.ConnectionError:
            mensaje = "❌ No se pudo conectar al servidor"
        except requests.exceptions.JSONDecodeError:
            mensaje = "❌ Respuesta inválida del servidor"
        except Exception as e:
            mensaje = f"🚫 Error: {str(e)}"

        self.ids.mensaje.text = mensaje

    def iniciar_sesion(self, instance):
        # Enviar credenciales al backend Flask
        datos = {
            "correo": self.ids.usuario.text,  # Aquí usamos los mismos campos de texto
            "contrasena": self.ids.clave.text
        }

        try:
            r = requests.post("http://127.0.0.1:5000/login", json=datos)
            r.raise_for_status()
            respuesta = r.json()

            if respuesta.get("mensaje") == "OK":
                self.manager.current = "catalogo"
            else:
                self.ids.mensaje.text = respuesta.get("mensaje", "Error desconocido")
        except requests.exceptions.ConnectionError:
            self.ids.mensaje.text = "❌ No se pudo conectar al servidor"
        except requests.exceptions.JSONDecodeError:
            self.ids.mensaje.text = "❌ Respuesta inválida del servidor"
        except Exception as e:
            self.ids.mensaje.text = f"🚫 Error: {str(e)}"