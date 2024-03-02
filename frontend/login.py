from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (300, 600)
class LoginScreen(MDApp):
    def build(self):
        return Builder.load_file("login.kv")


if __name__ == "__main__":
    LoginScreen().run()

