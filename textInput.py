from kivy.app import App
from kivy.uix.textinput import TextInput

class MinhaApp(App):
    def build(self):
        return TextInput(text='Digite aqui!')
    
if __name__ == '__main__':
    MinhaApp().run() 