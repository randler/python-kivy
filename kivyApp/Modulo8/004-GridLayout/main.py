from kivy.app import App
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '580')
#Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'fullscreen', '0')

janela = None
glayout = None

class JanelaApp(App):
    ...

janela = JanelaApp()
ji = InteractiveLauncher(janela)
ji.run()