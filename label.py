from kivy.app import App
from kivy.uix.label import Label

class minhaApp(App):
    def build(self):
        return Label(text='Olá SENAI!',font_size=200, font_name='Arial')
    
if __name__=='__main__':
    minhaApp().run()    