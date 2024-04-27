from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RotuloApp(App):
    def buil(self):
        layout = BoxLayout(orientation='vertical')
        self.lab1 = Label(
            text='SENAI', color=[1, 0, 0, 1],
            font_size=40, bold=True
        )
        self.lab2 = Label(
            text='SESi', color=[0, 1, 0, 1],
            font_size=40, italac=True
        )
        self.lab3 = Label(
            text='ENEM', color=[0, 0, 1, 1],
            font_size=40, bold=True
        )
        layout.add_widget(self.lab1)
        layout.add_widget(self.lab2)
        layout.add_widget(self.lab3)

if __name__ == '__name__':
    RotuloApp().rum()