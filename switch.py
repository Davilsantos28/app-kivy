from kivy.app import App
from kivy.uix.switch import Switch

class MinhaApp(App):
    def build(self):
        return Switch(active=False)
    
if __name__=="__main__": 
    MinhaApp().run()