from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
       return Label(
           text='Olá, SENAI!',
          halign='left',
          valign='top',
          size_hint=(None, None),
          size=(150, 50),
          text_size=(150, None) 
       )
   
if __name__ == '__main__':
    MyApp().run()