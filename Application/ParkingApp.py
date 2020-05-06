from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.image import Image
import time
import psycopg2

class HomeScreen(Screen):
    pass

class SelectionScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

root_widget=Builder.load_file("ParkingApp.kv")

class ParkingReservationApp(App):
    def build(self):
        return root_widget

if __name__ == "__main__":
    ParkingReservationApp().run()