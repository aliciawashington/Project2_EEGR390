from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

import psycopg2

#Establish a Connection with the data base
#conn = psycopg2.connect(
   # host="localhost",
    #database="test",
    #user="pi",
    #password="henny")

#Cursor for database interactions
#cur = conn.cursor()

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
        ##Establish a connection with server
        ##Create the Cursor for executions
        ##Do some logic to check if the space is available at the time of fetch
        ##like so maybe only fetch the most recent time stamped line
        ##everytime this method is called via the button on the home screen
        self.root.ids.screen_manager.current = "screen2"
        ## In this method is where the function will call to the database
    def refresh_reservation(self):
        self.root.ids.screen_manager.current = "screen2"
    def goback(self):
        self.root.ids.screen_manager.current = "screen1"


if __name__ == "__main__":
    NavDrawerAndScreenManagerApp().run()


#Closes the connection with the database
#cur.close()