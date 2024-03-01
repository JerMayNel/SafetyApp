from kivy.lang import Builder
from kivy.garden.mapview import MapMarker, MapSource
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager


class SafetyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"  # Fix
        self.theme_cls.primary_hue = "500"  # Corresponding to the RGB components, since Cyan is a shade of Teal.
        self.theme_cls.accent_hue = "400"  # Adjust as needed, based on your color preferences.
        return Builder.load_file('mainscreen.kv')


class MainScreen(Screen):
    pass


class AddContactsScreen(Screen):
    pass


screen_manager = ScreenManager()
screen_manager.add_widget(MainScreen(name='Main'))
screen_manager.add_widget(AddContactsScreen(name='AddContacts'))


SafetyApp().run()
