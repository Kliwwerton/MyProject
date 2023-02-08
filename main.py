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
        self.ids.label_P_pressing_text.text = 'Давление прессования:'
        self.ids.label_P_pressing_value.text = 'VALUE'
        self.ids.unit_of_measurement.text = 'Пока NONE'

    def calculate(self):
        pass

    def press_exit(self):
        if self.ids.My_image.source == 'Images/exit.png':
            self.ids.My_image.source = 'Images/to_exit.png'
        else:
            self.ids.My_image.source = 'Images/exit.png'

    def reset(self):
        if self.ids.image_btn_reset.source == 'Images/reset.png':
            self.ids.image_btn_reset.source = 'Images/reset_2.png'
        else:
            self.ids.image_btn_reset.source = 'Images/reset.png'
        self.ids.label_P_pressing_text.text = ''
        self.ids.label_P_pressing_value.text = ''
        self.ids.unit_of_measurement.text = ''
        self.ids.spinner_quantity_stamps.text = '0'
        self.ids.spinner_id.text = 'Выбурите пресс!'
        self.ids.text_input_Pud.text = ''
        self.ids.label_S_pressing_value.text = ''

    def reset_2(self):
        self.ids.image_btn_reset.source = 'Images/reset.png'



class EngineerApp(App):
    def build(self):
        Window.clearcolor = (232/255, 184/255, 1, 1)
        container = Container()
        container.add_widget(First())
        container.add_widget(Second())
        return container


if __name__ == '__main__':
    EngineerApp(title='ИНЖЕНЕР НА ВСЮ ГОЛОВУ!',
                icon='Images/Logo.png').run()
