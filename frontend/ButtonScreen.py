from kivy.lang import Builder
from kivy.garden.mapview import MapMarker, MapSource
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (400, 600)  # For phone size development only


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
    """ Sample getting data for now, printing datas on the screen.
     IMPORTANT: for backend soon!
     Create a backend code to create a card / gui for new contacts, based on the database inputted by
     text fields, ensure that the cards has a delete option to delete cards.
    """
    def get_data(self):
        phone_number_text = self.ids.phone_number.text
        name_text = self.ids.name.text
        email_text = self.ids.email.text

        print("Phone Number:", phone_number_text)
        print("Name:", name_text)
        print("Email:", email_text)

        self.manager.current = 'Main'
        self.ids.phone_number.text = ""
        self.ids.name.text = ""
        self.ids.email.text = ""


screen_manager = ScreenManager()
screen_manager.add_widget(MainScreen(name='Main'))
screen_manager.add_widget(AddContactsScreen(name='AddContacts'))

SafetyApp().run()
