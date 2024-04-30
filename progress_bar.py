from kivy.app import App
from kivy.uix.progressbar import ProgressBar

class MinhaApp(App):
    def build(self):
        return ProgressBar(value=20)
    
if __name__ == '__main__':
    MinhaApp().run()    