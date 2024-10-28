from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.app import App

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '580')
#Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'fullscreen', '0')

janela = None
glayout = None


class MyStack1(StackLayout):
    def click(self, bt):
        bt.text='on_press'
    
    def release(self, bt):
        bt.text='on_release'

class JanelaApp(App):
    ...

janela = JanelaApp()
janela.run()