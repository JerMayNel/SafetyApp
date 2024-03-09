from kivy.lang import Builder
from kivy.garden.mapview import MapMarker, MapSource
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

Window.size = (350, 600)  # For phone size development only


class SafetyApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"  # TODO: Fix DESIGN
        self.theme_cls.primary_hue = "500"  # Corresponding to the RGB components, since Cyan is a shade of Teal.
        self.theme_cls.accent_hue = "400"  # Adjust as needed, based on your color preferences.
        return Builder.load_file('mainscreen.kv')

    def logout_alert(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Log Out",
                text="Are you sure you want to log-out?",
                buttons=[
                    MDFlatButton(
                        text="No",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="Yes",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,  # TODO: Implement log-out function
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class MainScreen(Screen):
    pass


class AddContactsScreen(Screen):
    """ TODO: Sample getting data for now, printing datas on the screen.
     TODO: IMPORTANT: for backend soon!
     TODO: Create a backend code to create a card / list / gui for new contacts, based on the database inputted by
     TODO: -text fields, ensure that the cards has a delete option to delete cards.
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


class EditProfileScreen(Screen):
    pass


class AboutUsScreen(Screen):
    pass


screen_manager = ScreenManager()
screen_manager.add_widget(MainScreen(name='Main'))
screen_manager.add_widget(AddContactsScreen(name='AddContacts'))
screen_manager.add_widget(EditProfileScreen(name='EditProfile'))
screen_manager.add_widget(AboutUsScreen(name='AboutUs'))

SafetyApp().run()
