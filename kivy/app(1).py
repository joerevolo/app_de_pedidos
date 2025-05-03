from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from pantallas.login import LoginScreen
from pantallas.catalogo import CatalogoScreen

# Cambiar color del fondo de la ventana principal a un color claro (crema)
Window.clearcolor = (0.95, 0.95, 0.9, 1)  # fondo crema claro

class MyApp(App):
    def build(self):
        # Forzar color de texto negro por defecto (si se usa por widgets personalizados)
        from kivy.utils import get_color_from_hex
        from kivy.uix.label import Label
        Label.color = get_color_from_hex("#000000")  # letras negras por defecto

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(CatalogoScreen(name='catalogo'))
        return sm

if __name__ == '__main__':
    MyApp().run()
