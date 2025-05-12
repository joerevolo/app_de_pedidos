from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from os.path import dirname, join
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.widget import Widget
import requests

# Cargar el archivo KV
Builder.load_file(join(dirname(__file__), 'catalogo.kv'))

class CatalogoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "catalogo"
        self.cargar_productos()

    def cargar_productos(self):
        try:
            response = requests.get("http://127.0.0.1:5000/productos")
            response.raise_for_status()
            productos = response.json()
            self.mostrar_productos(productos)
        except requests.exceptions.RequestException as e:
            print(f"Error al cargar productos: {e}")
            self.mostrar_error("No se pudieron cargar los productos.")
        except ValueError:
            print("Respuesta del servidor no es JSON válido")
            self.mostrar_error("Error al procesar los datos del servidor")

    def mostrar_productos(self, productos):
        try:
            container = self.ids.productos_container
            container.clear_widgets()
            
            for producto in productos:
                layout = BoxLayout(
                    orientation='horizontal',
                    size_hint_y=None,
                    height=80,
                    padding=10,
                    spacing=10
                )
                
                info = BoxLayout(orientation='vertical')
                nombre = Label(
                    text=producto.get('nombre', 'Sin nombre'),
                    font_size=18,
                    bold=True
                )
                precio = Label(
                    text=f"${producto.get('precio', '0')}",
                    font_size=16,
                    color=(0, 0.5, 0, 1)
                )
                info.add_widget(nombre)
                info.add_widget(precio)
                
                layout.add_widget(info)
                container.add_widget(layout)
        except KeyError:
            self.mostrar_error("Error en la interfaz: contenedor no encontrado")

    def mostrar_error(self, mensaje):
        try:
            container = self.ids.productos_container
            container.clear_widgets()
            container.add_widget(Label(
                text=mensaje,
                color=(1, 0, 0, 1),
                font_size=18,
                halign='center'
            ))
        except Exception as e:
            print(f"No se pudo mostrar el mensaje de error: {e}")

    def volver_login(self):
        try:
            if 'login' in self.manager.screen_names:
                self.manager.current = 'login'
            else:
                print("La pantalla 'login' no existe")
        except Exception as e:
            print(f"Error al cambiar de pantalla: {e}")