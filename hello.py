from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="Hello World! This is my first program in kivy \n I'm a SESIANO Student, and I love my Teacher")
if __name__ == '__main__':
     MyApp().run()