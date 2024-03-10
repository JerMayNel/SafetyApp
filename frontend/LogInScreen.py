# import pyrebase
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (300, 600)

"""
    firebaseConfig = {
    'apiKey': "AIzaSyDF5SAD9euJbbsUEz3yQY6W3LgvA-0bM8U",
    'authDomain': "finalproject-8b6b4.firebaseapp.com",
    'projectId': "finalproject-8b6b4",
    'databaseURL': "https://finalproject-8b6b4-default-rtdb.firebaseio.com",
    'storageBucket': "finalproject-8b6b4.appspot.com",
    'messagingSenderId': "29231288442",
    'appId': "1:29231288442:web:03f8123760578266e2abc3",
    'measurementId': "G-SR5YY8FEGW"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
"""


class LoginScreen(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.primary_hue = "500"  # Corresponding to the RGB components, since Cyan is a shade of Teal.
        self.theme_cls.accent_hue = "400"  # Adjust as needed, based on your color preferences.
        return Builder.load_file("loginscreen.kv")


class LogInScreen(Screen):
    pass


class SignUpScreen(Screen):
    """
    def create_account(self, email, password):
        emailpy = email
        passwordpy = password
        auth.create_user_with_email_and_password(emailpy, passwordpy)
    """
    pass


class AddTrustedContactsScreen(Screen):
    pass


class AskLocationScreen(Screen):
    pass


class ForgotPasswordScreen(Screen):
    pass


class PinScreen(Screen):
    pass


screen_manager = ScreenManager()
screen_manager.add_widget(LogInScreen(name='LogIn'))
screen_manager.add_widget(SignUpScreen(name='SignUp'))
screen_manager.add_widget(AddTrustedContactsScreen(name='AddTrustedContacts'))
screen_manager.add_widget(AskLocationScreen(name='AskLocation'))
screen_manager.add_widget(ForgotPasswordScreen(name='ForgotPassword'))
screen_manager.add_widget(PinScreen(name='Pin'))

if __name__ == "__main__":
    LoginScreen().run()
