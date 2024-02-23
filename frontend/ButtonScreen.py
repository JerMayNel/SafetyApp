from kivy.lang import Builder

from kivymd.app import MDApp


class SafetyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan" # Fix
        self.theme_cls.primary_hue = "600"  # Corresponding to the RGB components, since Cyan is a shade of Teal.
        self.theme_cls.accent_hue = "400"  # Adjust as needed, based on your color preferences.
        return Builder.load_file('bbar.kv')


SafetyApp().run()