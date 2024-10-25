from kivy.app import App
from kivy.core.window import Window

from kivy.utils import get_color_from_hex as ColorHex

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '580')
#Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'fullscreen', '0')

Window.clearcolor = ColorHex('#FFFFFF')

janela = None
glayout = None

class JanelaApp(App):
    ...

janela = JanelaApp()
janela.run()