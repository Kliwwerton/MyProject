from kivy.config import Config

Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 800)
Config.set('kivy', 'keyboard_mode', 'systemanddock')
# Config.set('kivy', 'window_icon', 'Images/Logo.png')

from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
# from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager

from variables import PRESS_PARAMETERS
from MyPopups import SelectionOptionPopup, SelectionGostPopup
import MyPopups

# from kivymd.theming import ThemeManager

Builder.load_file('Engineer.kv')
Builder.load_file('Second.kv')
Builder.load_file('Third.kv')
Builder.load_file('MyPopups.kv')


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
        self.ids.label_P_pressing_value.text = data[0] + ' ' + data[1]

    def calculate_pressure(self):
        """Calculating pressing pressure"""
        self.sound.play()
        if self.ids.spinner_press_mark.text == 'Выберите пресс':
            data = ['УКАЖИТЕ МАРКУ', 'ПРЕССА']
            self.return_mistake(data)

        elif not self.ids.label_S_pressing_value.text:
            data = ['УКАЖИТЕ ПЛОЩАДЬ', 'ИЗДЕЛИЯ']
            self.return_mistake(data)

        elif self.ids.spinner_quantity_stamps.text == '0':
            data = ['УКАЖИТЕ КОЛИЧЕТВО', 'ШТАМПОВ']
            self.return_mistake(data)

        elif not self.ids.specific_pressure.text:
            data = ['УКАЖИТЕ УДЕЛЬНОЕ', 'ДАВЛЕНИЕ']
            self.return_mistake(data)

        else:
            press = self.ids.spinner_press_mark.text
            square_pressing = float(self.ids.label_S_pressing_value.text)
            quantity_stamps = int(self.ids.spinner_quantity_stamps.text)
            specific_pressure = int(self.ids.specific_pressure.text)


            pressure = (square_pressing * quantity_stamps * PRESS_PARAMETERS[press][1] *
                        (specific_pressure / 1000)) / PRESS_PARAMETERS[press][0]
            if pressure > PRESS_PARAMETERS[press][1]:
                data = ['ПРЕСС СТОЛЬКО', 'НЕ ПОТЯНЕТ!!!']
            else:
                data = [round(pressure, 2), PRESS_PARAMETERS[press][2]]

            self.ids.label_P_pressing_text.text = 'Давление прессования:'
            self.ids.label_P_pressing_value.text = str(data[0]) + ' ' + str(data[1])

    def reset(self):
        """reset all parameters"""
        self.ids.label_P_pressing_text.text = ''
        self.ids.label_P_pressing_value.text = ''
        self.ids.unit_of_measurement.text = ''
        self.ids.spinner_quantity_stamps.text = '0'
        self.ids.spinner_press_mark.text = 'Выберите пресс!'
        self.ids.specific_pressure.text = ''
        self.ids.label_S_pressing_value.text = ''
        self.sound_reset.play()

    def open_SelectionOptionPopup(self):
        """opening popup window Selection Option"""
        if self.ids.label_S_pressing_value.text == '':
            SelectionOptionPopup().open()


class Third(Screen):
    sound = SoundLoader.load('sounds/sound.wav')
    sound_reset = SoundLoader.load('sounds/sound_reset.mp3')

    def calculate(self):
        self.sound.play()
        if self.ids.spinner_quantity_stamps.text == '0':
            self.press()
        elif self.ids.spinner_press_mark.text == 'Выберите пресс':
            self.press()
        elif self.ids.spinner_press_mark.text \
                and self.ids.S_pressing_value.text \
                and self.ids.spinner_quantity_stamps.text != '0' \
                and self.ids.pressure.text:
            data = self.calculate_specific_pressure(press=self.ids.spinner_press_mark.text,
                                                    square_pressing=float(self.ids.S_pressing_value.text),
                                                    quantity_stamps=int(self.ids.spinner_quantity_stamps.text),
                                                    pressure=float(self.ids.pressure.text))
            if not data:
                self.press()
            elif isinstance(data, str):
                self.ids.label_P_pressing_text.text = data
                self.ids.label_P_specific_pressure_value.text = ''
                self.ids.unit_of_measurement.text = ''
            else:
                self.ids.label_P_pressing_text.text = 'Удельное давление:'
                self.ids.label_P_specific_pressure_value.text = str(data)
                self.ids.unit_of_measurement.text = 'кг/см[sup]2[/sup]'
        else:
            self.press()

    @staticmethod
    def calculate_specific_pressure(press, square_pressing, quantity_stamps, pressure):
        if pressure > PRESS_PARAMETERS[press][1]:
            return 'ДАВЛЕНИЕ ПРЕССА ПРЕВЫШЕНО!!!'
        else:
            specific_pressure = (pressure * PRESS_PARAMETERS[press][0]) / \
                                (square_pressing * quantity_stamps * PRESS_PARAMETERS[press][1])
            return round(specific_pressure * 1000, 2)

    def press(self):
        self.ids.label_P_pressing_text.text = 'НЕХВАТАЕТ ДАННЫХ!!!'
        self.ids.label_P_specific_pressure_value.text = ''
        self.ids.unit_of_measurement.text = ''

    def reset(self):
        """Reset all parameters and labels text"""
        self.ids.label_P_pressing_text.text = ''
        self.ids.label_P_specific_pressure_value.text = ''
        self.ids.unit_of_measurement.text = ''
        self.ids.spinner_quantity_stamps.text = '0'
        self.ids.spinner_press_mark.text = 'Выберите пресс'
        self.ids.pressure.text = ''
        self.ids.S_pressing_value.text = ''
        self.sound_reset.play()

    def change_label(self):
        """changing label unit of press parameters"""
        if self.ids.spinner_press_mark.text == 'Выберите пресс':
            self.ids.pressure_unit.text = ''
        else:
            self.ids.pressure_unit.text = PRESS_PARAMETERS[self.ids.spinner_press_mark.text][2]

    def open_SelectionOptionPopup(self):
        if self.ids.S_pressing_value.text == '':
            SelectionOptionPopup().open()

class EngineerApp(App):
    """MAIN APP ENGINEER"""
    def build(self):
        self.icon = 'Images/Logo.png'
        Window.clearcolor = (232 / 255, 184 / 255, 1, 1)
        container = Container()
        container.add_widget(First())
        container.add_widget(Second())
        container.add_widget(Third())
        return container


if __name__ == '__main__':
    EngineerApp(title='ИНЖЕНЕР НА ВСЮ ГОЛОВУ!').run()
