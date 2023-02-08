from kivy.config import Config

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)
Config.set('kivy', 'keyboard_mode', 'systemanddock')

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file('Engineer.kv')


class Container(ScreenManager):
    pass


class First(Screen):
    def press_exit(self):
        if self.ids.My_image.source == 'Images/exit.png':
            self.ids.My_image.source = 'Images/to_exit.png'
        else:
            self.ids.My_image.source = 'Images/exit.png'


class Second(Screen):
    def press(self):
        self.ids.label_P_pressing_text.text = 'Давление прессования: '

    def unpressed(self):
        pass

    def press_exit(self):
        if self.ids.My_image.source == 'Images/exit.png':
            self.ids.My_image.source = 'Images/to_exit.png'
        else:
            self.ids.My_image.source = 'Images/exit.png'


class EngineerApp(App):
    def build(self):
        Window.clearcolor = (0.91, .72, .99, .5)
        container = Container()
        container.add_widget(First())
        container.add_widget(Second())
        return container


if __name__ == '__main__':
    EngineerApp(title='ИНЖЕНЕР НА ВСЮ ГОЛОВУ!',
                icon='Images/Logo.png').run()
