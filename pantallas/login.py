import requests
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from os.path import dirname, join
from kivy.clock import Clock
import re

# Cargar el archivo KV
Builder.load_file(join(dirname(__file__), 'login.kv'))

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        Clock.schedule_once(self.get_ids, 0)

    def get_ids(self, dt):
        try:
            self.usuario_input = self.ids.usuario
            self.email_input = self.ids.email
            self.clave_input = self.ids.clave
            self.mensaje_label = self.ids.mensaje
        except KeyError as e:
            print(f"Error al obtener IDs: {e}. Reintentando...")
            Clock.schedule_once(self.get_ids, 0.2)
        except Exception as e:
            print(f"Error inesperado: {e}")

    def validar_correo(self, correo):
        """Valida el formato de correo electrónico"""
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(patron, correo) is not None

    def registrar(self, instance):
        if not hasattr(self, 'usuario_input') or not hasattr(self, 'email_input') or not hasattr(self, 'clave_input'):
            print("Error: Los IDs no están asignados aún.")
            return

        nombre = self.usuario_input.text.strip()
        correo = self.email_input.text.strip()
        clave = self.clave_input.text.strip()

        if not nombre or not correo or not clave:
            self.mensaje_label.text = "Todos los campos son obligatorios"
            return

        if not self.validar_correo(correo):
            self.mensaje_label.text = "Correo electrónico inválido"
            return

        datos = {
            "nombre": nombre,
            "email": correo,
            "clave": clave
        }

        try:
            r = requests.post("http://127.0.0.1:5000/registro", json=datos)
            mensaje = r.json().get("mensaje", "Error desconocido")
        except requests.exceptions.JSONDecodeError:
            mensaje = "❌ Respuesta inválida del servidor"
        except Exception as e:
            mensaje = f"🚫 Error: {str(e)}"

        if hasattr(self, 'mensaje_label'):
            self.mensaje_label.text = mensaje

    def iniciar_sesion(self, instance):
        datos = {
            "correo": self.email_input.text.strip(),
            "contrasena": self.clave_input.text.strip()
        }

        try:
            r = requests.post("http://127.0.0.1:5000/login", json=datos)
            respuesta = r.json()
            if respuesta.get("mensaje") == "OK":
                self.manager.current = "catalogo"
            else:
                self.mensaje_label.text = respuesta.get("mensaje", "Error desconocido")
        except Exception as e:
            self.mensaje_label.text = f"🚫 Error: {str(e)}"