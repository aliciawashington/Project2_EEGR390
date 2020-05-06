import random

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


red = [1,0,0,1]
green = [0,1,0,1]
blue=[0,0,1,1]
purple=[1,0,1,1]

class ButtonApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello!",
                  font_size=150
                  )
        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__=="__main__":
    ButtonApp().run()
