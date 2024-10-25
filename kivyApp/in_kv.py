import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Tela1(BoxLayout):

    def on_press_button(self):
        janela.root_window.remove_widget(janela.root_window)
        janela.root_window.add_widget(Tela2())

class Tela2(BoxLayout):

    def on_press_button(self):
        janela.root_window.remove_widget(janela.root_window)
        janela.root_window.add_widget(Tela1())


class KvVsPy2(App):
    ...
    # def build(self):
    #     return Tela1()
    
janela = KvVsPy2()
janela.run()