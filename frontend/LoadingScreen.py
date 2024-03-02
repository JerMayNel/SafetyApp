from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 600)


class LoadingScreen(MDApp):
    i = 0
    def build(self):
        Clock.schedule_interval(self.loader, 0.5)
        return Builder.load_file("Loading.kv")

    def loader(self, *args):
        try:
            self.i += 10
            self.root.ids.progress_bar.value = self.i
        except:
            Clock.unschedule(self.loader)

if __name__ == "__main__":
    LoadingScreen().run()
