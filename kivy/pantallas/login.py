from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# Cargar el archivo .kv
from os.path import dirname, join
Builder.load_file(join(dirname(__file__), 'login.kv'))

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.usuario_guardado = ''
        self.clave_guardada = ''

    def on_kv_post(self, base_widget):
        self.ids.boton_registrar.bind(on_press=self.registrar)
        self.ids.boton_login.bind(on_press=self.login)

    def registrar(self, instance):
        self.usuario_guardado = self.ids.usuario.text
        self.clave_guardada = self.ids.clave.text
        self.ids.mensaje.text = "¡Registrado!"

    def login(self, instance):
        if (self.ids.usuario.text == self.usuario_guardado and
                self.ids.clave.text == self.clave_guardada):
            self.manager.current = 'catalogo'
        else:
            self.ids.mensaje.text = "Usuario o contraseña incorrectos"