from kivy.app import App 
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):
        return AsyncImage(source='https://miro.medium.com/v2/resize:fit:828/format:webp/0*qdHImq1G588SB9Ii.jpg')
    
if __name__ =="__main__":
    MinhaApp().run()    