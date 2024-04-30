from kivy.app import App
from kivy.uix.video import Video

class MinhaApp(App):
    def build(self):
        return Video(source='../app-kivy/img/vide.html')
    
if __name__=="__main__": 
    MinhaApp().run()    