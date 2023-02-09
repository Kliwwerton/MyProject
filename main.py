from kivy.config import Config

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)
Config.set('kivy', 'keyboard_mode', 'systemanddock')

from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


Builder.load_file('Engineer.kv')

PRESS_PARAMETERS = {'LAEIS-1250': [1250, 11.98, 'N/см[sup]2[/sup]'],
                    'SACMI-1000': [990, 350, 'Бар'],
                    'SACMI-500': [500, 350, 'Бар'],
                    'YPR-2500': [2500, 28.9, 'kN'],
                    'ДО-542': [1600, 320, 'Атм'],
                    'ДА-2238(ЦИЧО)': [630, 320, 'Атм'],
                    'СМ-1085': [630, 90, 'Ампер'],
                    'ПЮ': [200, 90, 'Ампер'],
                    'ПД-476 (ЦИЧО)': [160, 320, 'Атм'],
                    'П-483 (ЦИЧО)': [63, 320, 'Атм'],
                    'П-474А (ЦИЧО)': [100, 320, 'Атм'],
                    'ИП-500М-АВТО': [50, 500, 'kN']}


def calculate_pressure(press, square_pressing, quantity_stamps, specific_pressure):
    if press in PRESS_PARAMETERS:
        pressure = (square_pressing * quantity_stamps * PRESS_PARAMETERS[press][1] *
                    (specific_pressure/1000)) / PRESS_PARAMETERS[press][0]
        values = [round(pressure, 2), PRESS_PARAMETERS[press][2]]
        return values
    else:
        pressure = False
        return pressure


class Container(ScreenManager):
    pass


class First(Screen):
    pass


class Second(Screen):
    sound = SoundLoader.load('sounds/sound.wav')
    sound_reset = SoundLoader.load('sounds/sound_reset.mp3')
    def press(self):
        self.ids.label_P_pressing_text.text = 'НЕХВАТАЕТ ДАННЫХ!!!'
        self.ids.label_P_pressing_value.text = ''
        self.ids.unit_of_measurement.text = ''

    def calculate(self):
        if self.ids.spinner_quantity_stamps.text == '0':
            self.press()
        elif self.ids.spinner_press_mark.text \
                and self.ids.label_S_pressing_value.text \
                and self.ids.spinner_quantity_stamps.text != '0' \
                and self.ids.specific_pressure.text:
            data = calculate_pressure(press=self.ids.spinner_press_mark.text,
                                      square_pressing=float(self.ids.label_S_pressing_value.text),
                                      quantity_stamps=int(self.ids.spinner_quantity_stamps.text),
                                      specific_pressure=int(self.ids.specific_pressure.text))
            if not data:
                self.press()
            else:
                self.ids.label_P_pressing_text.text = 'Давление прессования:'
                self.ids.label_P_pressing_value.text = str(data[0])
                self.ids.unit_of_measurement.text = str(data[1])
        else:
            self.press()

    def reset(self):
        self.ids.label_P_pressing_text.text = ''
        self.ids.label_P_pressing_value.text = ''
        self.ids.unit_of_measurement.text = ''
        self.ids.spinner_quantity_stamps.text = '0'
        self.ids.spinner_press_mark.text = 'Выберите пресс!'
        self.ids.specific_pressure.text = ''
        self.ids.label_S_pressing_value.text = ''


    def play_sound(self):
        self.sound.play()

    def play_sound_reset(self):
        self.sound_reset.play()


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
