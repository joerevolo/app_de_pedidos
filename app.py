from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from pantallas.login import LoginScreen
from pantallas.catalogo import CatalogoScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(CatalogoScreen(name='catalogo'))  # ✅ Registro correcto
        return sm

if __name__ == '__main__':
    MyApp().run()
