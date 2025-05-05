from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from os.path import dirname, join

# Carga el archivo KV asociado a esta pantalla
Builder.load_file(join(dirname(__file__), 'catalogo.kv'))

class CatalogoScreen(Screen):
    def volver_login(self):
        self.manager.current = 'login'