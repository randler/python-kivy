from kivy.uix.boxlayout import BoxLayout
import kivy
kivy.require('1.9.1')

from kivy.app import App

class MinhaTela(BoxLayout):
    
    def click(self):
        print('Botão clicado!')
        self.ids.lb1.text = 'Botão clicado!'
        self.ids.lb2.text = 'Clicado'

class Estudo4App(App):
    ...

janela = Estudo4App()
janela.run()