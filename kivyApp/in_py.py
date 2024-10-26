import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Tela1(BoxLayout):

    def on_press_button(self):
        janela.root_window.remove_widget(janela.root_window)
        janela.root_window.add_widget(Tela2())

    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs)
        self.orientation = 'vertical'
        bt1 = Button(text='bt1')
        bt2 = Button(text='bt2')
        bt3 = Button(text='bt2')
        bt1.on_press =self.on_press_button
        self.add_widget(bt1)
        self.add_widget(bt2)
        self.add_widget(bt3)
        
class Tela2(BoxLayout):

    def on_press_button(self):
        janela.root_window.remove_widget(janela.root_window)
        janela.root_window.add_widget(Tela1())

    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)
        self.orientation = 'vertical'
        bt = Button(text='clique')
        bt.on_press = self.on_press_button
        self.add_widget(bt)

class KvVsPy(App):
    def build(self):
        return Tela1()
    
janela = KvVsPy()
janela.run()