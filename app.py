from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from pantallas.login import LoginScreen
from pantallas.catalogo import CatalogoScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
<<<<<<< HEAD
        sm.add_widget(CatalogoScreen(name='catalogo'))
        return sm

if __name__ == '__main__':
    MyApp().run()
=======
        sm.add_widget(CatalogoScreen(name='catalogo'))  # ✅ Registro correcto
        return sm

if __name__ == '__main__':
    MyApp().run()
>>>>>>> a957099d2a0cd302a4bd626cf706ecaaac1c13b9
