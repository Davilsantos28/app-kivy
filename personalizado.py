from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image

class CarouselApp(App):
   def build(self):
      carousel = Carousel(direction='right')
      img1=Image(source='../app-kivy/img/sesi.png')
      carousel.add_widget(img1)
      img2=Image(source='../app-kivy/img/senai.png')
      carousel.add_widget(img2)
      img3=Image(source='../app-kivy/img/iel.png')
      carousel.add_widget(img3)
      return carousel
CarouselApp().run()