from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (300, 600)


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
    pass


screen_manager = ScreenManager()
screen_manager.add_widget(LogInScreen(name='LogIn'))
screen_manager.add_widget(SignUpScreen(name='SignUp'))

if __name__ == "__main__":
    LoginScreen().run()
