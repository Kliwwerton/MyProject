
from kivy.config import Config
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput


class Container(ScreenManager):

    pass


class First(Screen):
    def press(self):
        if self.ids.My_image.source == 'exit.png':
            self.ids.My_image.source = 'to_exit.png'
        else:
            self.ids.My_image.source = 'exit.png'


class Second(Screen):
    pass


class EngineerApp(App):
    def build(self):
        Window.clearcolor = (0.91,.72,.99,.5)
        container = Container()
        container.add_widget(First())
        container.add_widget(Second())
        return container


if __name__ == '__main__':
    EngineerApp(title='ИНЖЕНЕР НА ВСЮ ГОЛОВУ!',
                icon='Logo.png').run()
