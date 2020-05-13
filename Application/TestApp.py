from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from gpiozero import DistanceSensor, LED, Button
import time

def parking_sensor():
    # Initializaiton of variables
    TRIG = 17
    ECHO = 27
    redled = LED(2)
    yellowled = LED(3)
    greenled = LED(4)
    state = Button(22)
    sensor = DistanceSensor(ECHO, TRIG)
    try:
        while True:
            if state.value == False:  # The parking space is not reserved (Green LED should be HIGH)
                greenled.on()
                yellowled.off()
                redled.off()
                if sensor.distance <= 0.1:
                    redled.on()
                    greenled.off()
                    yellowled.off()
            if state.value == True:  # The parking space is reserved (Yellow LED should be HIGH)
                greenled.off()
                yellowled.on()
                redled.off()
                if sensor.distance <= 0.1:
                    redled.on()
                    greenled.off()
                    yellowled.off()
            print('Distance to nearest object is ', sensor.distance * 100, 'cm')
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        redled.close()
        greenled.close()
        yellowled.close()


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    target = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class NavDrawerAndScreenManagerApp(MDApp):

    def build(self):
        return Builder.load_file("main.kv")

    def openScreen(self, itemdrawer):
        self.openScreenName(itemdrawer.target)
        self.root.ids.nav_drawer.set_state("close")

    def openScreenName(self, screenName):
        self.root.ids.screen_manager.current = screenName

    def on_start(self):
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(target="screen1", text="Home",
                       icon="home-circle-outline",
                       on_release=self.openScreen)
        )
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(target="screen2", text="Reserve Your Parking",
                       icon="parking",
                       on_release=self.openScreen)
        )
    def start_reservation(self):
        self.root.ids.screen_manager.current = "screen2"

    def refresh_reservation(self):
        self.root.ids.screen_manager.current = "screen2"

    def goback(self):
        self.root.ids.screen_manager.current = "screen1"


if __name__ == "__main__":
    parking_sensor()
    NavDrawerAndScreenManagerApp().run()

