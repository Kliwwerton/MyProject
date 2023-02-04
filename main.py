
from kivy.config import Config
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput


class Container(ScreenManager):
    def press(self):
        if self.name == 'First':
            self.button_1.text = "Нажата"
            self.Screen = 'Second'


class EngineerApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    EngineerApp().run()
