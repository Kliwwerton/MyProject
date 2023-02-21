from kivy.config import Config

Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 800)
Config.set('kivy', 'keyboard_mode', 'systemanddock')
# Config.set('kivy', 'window_icon', 'Images/Logo.png')

from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

from variables import PRESS_PARAMETERS
from variables import SQUARE
from MyPopups import SelectionOptionPopup, CalculationsAreaOfRectangle


# from kivymd.theming import ThemeManager

Builder.load_file('Engineer.kv')
Builder.load_file('Second.kv')
Builder.load_file('Third.kv')
Builder.load_file('MyPopups.kv')
Builder.load_file('Ring.kv')
Builder.load_file('Trapezoid.kv')
Builder.load_file('Rectangle.kv')


class Container(ScreenManager):
    """Main Widget"""
    pass


class First(Screen):
    """First screen for the app"""
    pass


class Second(Screen):
    """Second Screen for the app"""
    sound = SoundLoader.load('sounds/sound.wav')
    sound_reset = SoundLoader.load('sounds/sound_reset.mp3')

    def return_mistake(self, data):
        """returning wrong enter"""
        self.ids.label_P_pressing_text.text = 'НЕХВАТАЕТ ДАННЫХ!!!'
        self.ids.label_P_pressing_value.text = data

    def calculate_pressure(self):
        """Calculating pressing pressure"""
        self.sound.play()
        if self.ids.spinner_press_mark.text == 'Выберите пресс':
            self.return_mistake('УКАЖИТЕ МАРКУ ПРЕССА')

        elif not self.ids.label_S_pressing_value.text:
            self.return_mistake('УКАЖИТЕ ПЛОЩАДЬ ИЗДЕЛИЯ')

        elif self.ids.spinner_quantity_stamps.text == '0':
            self.return_mistake('УКАЖИТЕ КОЛИЧЕТВО ШТАМПОВ')

        elif not self.ids.specific_pressure.text:
            self.return_mistake('УКАЖИТЕ УДЕЛЬНОЕ ДАВЛЕНИЕ')

        else:
            press_mark = self.ids.spinner_press_mark.text
            square_pressing = float(self.ids.label_S_pressing_value.text)
            quantity_stamps = int(self.ids.spinner_quantity_stamps.text)
            specific_pressure = int(self.ids.specific_pressure.text)
            data = (square_pressing * quantity_stamps * PRESS_PARAMETERS[press_mark][1] *
                    (specific_pressure / 1000)) / PRESS_PARAMETERS[press_mark][0]

            if data > PRESS_PARAMETERS[press_mark][1]:
                data = 'ПРЕСС СТОЛЬКО НЕ ПОТЯНЕТ!!!'

            else:
                data = str(round(data, 2)) + ' ' + PRESS_PARAMETERS[press_mark][2]

            self.ids.label_P_pressing_text.text = 'Давление прессования:'
            self.ids.label_P_pressing_value.text = str(data)

    def reset(self):
        """reset all parameters"""
        self.ids.label_P_pressing_text.text = ''
        self.ids.label_P_pressing_value.text = ''
        self.ids.spinner_quantity_stamps.text = '0'
        self.ids.spinner_press_mark.text = 'Выберите пресс'
        self.ids.specific_pressure.text = ''
        self.ids.label_S_pressing_value.text = ''
        SQUARE.clear()
        self.sound_reset.play()

    def open_SelectionOptionPopup(self):
        """opening popup window Selection Option"""
        if SQUARE:
            self.ids.label_S_pressing_value.text = str(SQUARE[0])
        elif self.ids.label_S_pressing_value.text == '':
            SelectionOptionPopup().open()

    def change_text(self):
        if SQUARE:
            self.ids.label_S_pressing_value.text = str(SQUARE[0])


class Third(Screen):
    sound = SoundLoader.load('sounds/sound.wav')
    sound_reset = SoundLoader.load('sounds/sound_reset.mp3')

    def calculate(self):
        self.sound.play()
        if self.ids.spinner_press_mark.text == 'Выберите пресс':
            self.return_mistake('УКАЖИТЕ МАРКУ ПРЕССА')

        elif not self.ids.S_pressing_value.text:
            self.return_mistake('УКАЖИТЕ ПЛОЩАДЬ ИЗДЕЛИЯ')

        elif self.ids.spinner_quantity_stamps.text == '0':
            self.return_mistake('УКАЖИТЕ КОЛИЧЕТВО ШТАМПОВ')

        elif not self.ids.pressure.text:
            self.return_mistake('УКАЖИТЕ ПРЕССОВОЕ ДАВЛЕНИЕ')

        else:
            press = self.ids.spinner_press_mark.text
            square_pressing = float(self.ids.S_pressing_value.text)
            quantity_stamps = int(self.ids.spinner_quantity_stamps.text)
            pressure = float(self.ids.pressure.text)
            if pressure > PRESS_PARAMETERS[press][1]:
                data = 'ДАВЛЕНИЕ ПРЕССА ПРЕВЫШЕНО!!!'
            else:
                data = round((pressure * PRESS_PARAMETERS[press][0]) /
                             (square_pressing * quantity_stamps * PRESS_PARAMETERS[press][1]) * 1000)

            if isinstance(data, str):
                self.ids.label_P_pressing_text.text = data
                self.ids.label_P_specific_pressure_value.text = ''
            else:
                self.ids.label_P_pressing_text.text = 'Удельное давление:'
                self.ids.label_P_specific_pressure_value.text = str(data) + ' ' + 'кг/см[sup]2[/sup]'

    def return_mistake(self, data):
        self.ids.label_P_pressing_text.text = 'НЕХВАТАЕТ ДАННЫХ!!!'
        self.ids.label_P_specific_pressure_value.text = data

    def reset(self):
        """Reset all parameters and labels text"""
        self.ids.label_P_pressing_text.text = ''
        self.ids.label_P_specific_pressure_value.text = ''
        self.ids.spinner_quantity_stamps.text = '0'
        self.ids.spinner_press_mark.text = 'Выберите пресс'
        self.ids.pressure.text = ''
        SQUARE.clear()
        self.ids.S_pressing_value.text = ''
        self.sound_reset.play()

    def change_label(self):
        """changing label unit of press parameters"""
        if self.ids.spinner_press_mark.text == 'Выберите пресс':
            self.ids.pressure_unit.text = ''
        else:
            self.ids.pressure_unit.text = PRESS_PARAMETERS[self.ids.spinner_press_mark.text][2]

    def open_SelectionOptionPopup(self):
        if SQUARE:
            self.ids.S_pressing_value.text = str(SQUARE[0])
        elif self.ids.S_pressing_value.text == '':
            SelectionOptionPopup().open()

    def change_text(self):
        if SQUARE:
            self.ids.S_pressing_value.text = str(SQUARE[0])


class EngineerApp(App):
    """MAIN APP ENGINEER"""

    def __init__(self):
        super().__init__()
        self.title = 'ИНЖЕНЕР НА ВСЮ ГОЛОВУ!'
        self.icon = 'Images/Logo.png'
        self.SQUARE = []
        self.First = First()
        self.Second = Second()
        self.Third = Third()

    def build(self):
        Window.clearcolor = (232 / 255, 184 / 255, 1, 1)
        container = Container()
        container.add_widget(self.First)
        container.add_widget(self.Second)
        container.add_widget(self.Third)
        return container


if __name__ == '__main__':
    EngineerApp().run()
