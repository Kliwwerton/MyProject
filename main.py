
from kivy.config import Config

Config.set('graphics', 'width', 420)
Config.set('graphics', 'height', 800)
Config.set('kivy', 'keyboard_mode', 'systemanddock')
# Config.set('kivy', 'window_icon', 'Images/Logo.png')

from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SwapTransition, FadeTransition, FallOutTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from variables import PRESS_PARAMETERS
from variables import VALUES
from MyPopups import SelectionOptionPopup, choice_popup, \
    RessetPopup, ClosePopup, MistakePopup


# from kivymd.theming import ThemeManager

# Screens
Builder.load_file('First.kv')
Builder.load_file('Second.kv')
Builder.load_file('Third.kv')
Builder.load_file('Fourth.kv')

# Popups
Builder.load_file('MyPopups.kv')

# Shapes
Builder.load_file('Tube.kv')
Builder.load_file('Trapezoid.kv')
Builder.load_file('Rectangle.kv')
Builder.load_file('Ribbed.kv')
Builder.load_file('Shaped.kv')
Builder.load_file('Fason.kv')

# Another buttons
Builder.load_file('References.kv')
Builder.load_file('Gost_standards.kv')

# The game
Builder.load_file('Cows_and_bulls.kv')


def open_OptionPopup():
    if not VALUES:
        SelectionOptionPopup().open()

    elif VALUES['gost'] and VALUES['number'] and VALUES['weight'] and \
            VALUES['volume'] and VALUES['square'] and VALUES['size']:
        choice_popup(gost=VALUES['gost'],
                     number=VALUES['number'],
                     weight=VALUES['weight'],
                     volume=VALUES['volume'],
                     square=VALUES['square'],
                     size=VALUES['size']
                     )

    elif VALUES['gost'] and VALUES['number'] and VALUES['size'] and VALUES['weight']:
        choice_popup(gost=VALUES['gost'],
                     number=VALUES['number'],
                     size=VALUES['size'],
                     weight=VALUES['weight']
                     )

    elif VALUES['gost'] and VALUES['number'] and VALUES['size']:
        choice_popup(gost=VALUES['gost'],
                     number=VALUES['number'],
                     size=VALUES['size']
                     )

    elif VALUES['gost'] and VALUES['number'] and VALUES['weight'] and VALUES['volume']:
        choice_popup(gost=VALUES['gost'],
                     number=VALUES['number'],
                     weight=VALUES['weight'],
                     volume=VALUES['volume']
                     )

    elif VALUES['gost'] and VALUES['number'] and VALUES['square'] and VALUES['volume']:
        choice_popup(gost=VALUES['gost'],
                     number=VALUES['number'],
                     square=VALUES['square'],
                     volume=VALUES['volume']
                     )

    elif VALUES['gost'] and VALUES['number'] and VALUES['weight'] and VALUES['square']:
        choice_popup(gost=VALUES['gost'],
                     number=VALUES['number'],
                     weight=VALUES['weight'],
                     square=VALUES['square']
                     )

    elif VALUES['gost'] and VALUES['number'] and VALUES['weight']:
        choice_popup(gost=VALUES['gost'],
                     number=VALUES['number'],
                     weight=VALUES['weight'],
                     )

    elif VALUES['gost'] and VALUES['number'] and VALUES['volume']:
        choice_popup(gost=VALUES['gost'],
                     number=VALUES['number'],
                     volume=VALUES['volume']
                     )

    elif VALUES['gost'] and VALUES['number'] and VALUES['square']:
        choice_popup(gost=VALUES['gost'],
                     number=VALUES['number'],
                     square=VALUES['square']
                     )

    # elif VALUES['gost'] and VALUES['number']:
    #     choice_popup(gost=VALUES['gost'],
    #                  number=VALUES['number'],
    #                  )

    else:
        SelectionOptionPopup().open()


def return_mistake(value):
    popup = MistakePopup()
    popup.ids.text_mistake.text = value
    if value == 'Превышено количество компонентов!':
        popup.ids.text_label.text = ''
    popup.open()


class Container(ScreenManager):
    """Main Widget"""
    pass


class References(Screen):
    """Window of references"""
    def __init__(self):
        super().__init__()
        self.name = 'References'


class Gost_standards(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Gost_standards'

    def open_gost_8691(self):
        pass


class Cows_and_bulls(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Cows_and_bulls'


class First(Screen):
    """First screen for the app"""
    @staticmethod
    def print():
        print(VALUES)


class Second(Screen):
    """Second Screen for the app"""
    sound = SoundLoader.load('sounds/sound.wav')
    sound_reset = SoundLoader.load('sounds/sound_reset.mp3')

    def calculate(self):
        """Calculating pressing pressure"""
        self.sound.play()
        if self.ids.spinner_press_mark.text == 'Выберите пресс':
            return_mistake('УКАЖИТЕ МАРКУ ПРЕССА')

        elif not self.ids.label_S_pressing_value.text:
            return_mistake('УКАЖИТЕ ПЛОЩАДЬ ИЗДЕЛИЯ')

        elif self.ids.spinner_quantity_stamps.text == '0':
            return_mistake('УКАЖИТЕ КОЛИЧЕТВО ШТАМПОВ')

        elif not self.ids.specific_pressure.text:
            return_mistake('УКАЖИТЕ УДЕЛЬНОЕ ДАВЛЕНИЕ')

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
        self.ids.volume_label.text = ''
        self.ids.volume_value.text = ''
        self.ids.gost_text.text = ''
        self.ids.stamp_text.text = ''
        self.ids.stamp_label.text = ''
        self.ids.volume_weight.text = ''
        VALUES.clear()
        self.sound_reset.play()

    def open_ressetPopup(self):
        RessetPopup(self).open()

    @staticmethod
    def open_SelectionOptionPopup():
        open_OptionPopup()

    def change_text(self):
        """Changing text Textinput after calculate"""
        if not VALUES:
            pass
        elif VALUES:
            if VALUES['square']:
                self.ids.label_S_pressing_value.text = str(VALUES['square'])
            else:
                self.ids.label_S_pressing_value.text = ''

            if VALUES['volume']:
                self.ids.volume_label.text = 'Объём изделия: '
                self.ids.volume_value.text = str(VALUES['volume']) + ' см[sup]3[/sup]'
            else:
                self.ids.volume_label.text = ''
                self.ids.volume_value.text = ''

            if VALUES['gost'] in ('Прямоугольник', 'Трапецеидальный клин',
                                  'Ребровый клин', 'Кольцо', 'Фасонное изделие'):
                self.ids.gost_text.text = VALUES['gost']
            elif VALUES['gost']:
                self.ids.gost_text.text = 'Размеры по: ' + VALUES['gost']
            else:
                self.ids.gost_text.text = ''

            if VALUES['number']:
                self.ids.stamp_text.text = 'Номер изделия: '
                self.ids.stamp_label.text = VALUES['number']
            else:
                self.ids.stamp_text.text = ''
                self.ids.stamp_label.text = ''

            if VALUES['volume_weight']:
                self.ids.volume_weight.text = 'Объёмный вес: ' + VALUES['volume_weight'] + ' г/см[sup]3[/sup]'
            else:
                self.ids.volume_weight.text = ''


class Third(Screen):
    sound = SoundLoader.load('sounds/sound.wav')
    sound_reset = SoundLoader.load('sounds/sound_reset.mp3')

    def calculate(self):
        self.sound.play()
        if self.ids.spinner_press_mark.text == 'Выберите пресс':
            return_mistake('УКАЖИТЕ МАРКУ ПРЕССА')

        elif not self.ids.label_S_pressing_value.text:
            return_mistake('УКАЖИТЕ ПЛОЩАДЬ ИЗДЕЛИЯ')

        elif self.ids.spinner_quantity_stamps.text == '0':
            return_mistake('УКАЖИТЕ КОЛИЧЕТВО ШТАМПОВ')

        elif not self.ids.pressure.text:
            return_mistake('УКАЖИТЕ ПРЕССОВОЕ ДАВЛЕНИЕ')

        else:
            press = self.ids.spinner_press_mark.text
            square_pressing = float(self.ids.label_S_pressing_value.text)
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

    def open_ressetPopup(self):
        RessetPopup(self).open()

    def reset(self):
        """Reset all parameters and labels text"""
        self.ids.label_P_pressing_text.text = ''
        self.ids.label_P_specific_pressure_value.text = ''
        self.ids.spinner_quantity_stamps.text = '0'
        self.ids.spinner_press_mark.text = 'Выберите пресс'
        self.ids.pressure.text = ''
        self.ids.label_S_pressing_value.text = ''
        self.ids.volume_label.text = ''
        self.ids.volume_value.text = ''
        self.ids.gost_text.text = ''
        self.ids.stamp_text.text = ''
        self.ids.stamp_label.text = ''
        self.ids.volume_weight.text = ''
        VALUES.clear()
        self.sound_reset.play()

    def change_label(self):
        """changing label unit of press parameters"""
        if self.ids.spinner_press_mark.text == 'Выберите пресс':
            self.ids.pressure_unit.text = ''
        else:
            self.ids.pressure_unit.text = PRESS_PARAMETERS[self.ids.spinner_press_mark.text][2]

    @staticmethod
    def open_SelectionOptionPopup():
        open_OptionPopup()

    def change_text(self):
        if not VALUES:
            pass
        elif VALUES:
            if VALUES['square']:
                self.ids.label_S_pressing_value.text = str(VALUES['square'])
            else:
                self.ids.label_S_pressing_value.text = ''

            if VALUES['volume']:
                self.ids.volume_label.text = 'Объём изделия: '
                self.ids.volume_value.text = str(VALUES['volume']) + ' см[sup]3[/sup]'
            else:
                self.ids.volume_label.text = ''
                self.ids.volume_value.text = ''

            if VALUES['gost'] in ('Прямоугольник', 'Трапецеидальный клин', 'Ребровый клин', 'Кольцо'):
                self.ids.gost_text.text = VALUES['gost']
            elif VALUES['gost']:
                self.ids.gost_text.text = 'Размеры по: ' + VALUES['gost']
            else:
                self.ids.gost_text.text = ''

            if VALUES['number']:
                self.ids.stamp_text.text = 'Номер изделия: '
                self.ids.stamp_label.text = VALUES['number']
            else:
                self.ids.stamp_text.text = ''
                self.ids.stamp_label.text = ''

            if VALUES['volume_weight']:
                self.ids.volume_weight.text = 'Объёмный вес: ' + VALUES['volume_weight'] + ' г/см[sup]3[/sup]'
            else:
                self.ids.volume_weight.text = ''


class MyBox(BoxLayout):
    pass


class Fourth(Screen):
    """Fourth Screen. Screen of calculation chemical composition."""
    def __init__(self):
        super().__init__()
        self.name = 'Fourth'
        self.component1 = MyBox()
        self.component2 = MyBox()
        self.component3 = MyBox()
        self.component4 = MyBox()
        self.component5 = MyBox()

    def open_ressetPopup(self):
        RessetPopup(self).open()

    def add_new_component(self):
        if not self.ids.first_box.children:
            self.ids.first_box.add_widget(self.component1)
            print(self.ids.first_box)
        elif not self.ids.second_box.children:
            self.ids.second_box.add_widget(self.component2)
        elif not self.ids.third_box.children:
            self.ids.third_box.add_widget(self.component3)
        elif not self.ids.fourth_box.children:
            self.ids.fourth_box.add_widget(self.component4)
        elif not self.ids.fifth_box.children:
            self.ids.fifth_box.add_widget(self.component5)
        else:
            return_mistake('Превышено количество компонентов!')

    def reset(self):
        self.ids.first_box.remove_widget(self.component1)
        self.ids.second_box.remove_widget(self.component2)
        self.ids.third_box.remove_widget(self.component3)
        self.ids.fourth_box.remove_widget(self.component4)
        self.ids.fifth_box.remove_widget(self.component5)


class EngineerApp(App):
    """MAIN APP ENGINEER"""

    def __init__(self):
        super().__init__()
        self.title = 'ИНЖЕНЕР НА ВСЮ ГОЛОВУ!'
        self.icon = 'Logo.png'
        self.container = Container(transition=FallOutTransition())
        self.First = First()
        self.Second = Second()
        self.Third = Third()
        self.Fourth = Fourth()
        self.References = References()
        self.Gost_standards = Gost_standards()
        self.Cows_and_bulls = Cows_and_bulls()

    def build(self):
        self.icon = 'Logo.png'
        self.bind(on_start=self.post_build_init)
        Window.clearcolor = (232 / 255, 184 / 255, 1, 1)
        # container = Container(transition=SwapTransition())
        self.container.add_widget(self.First)
        self.container.add_widget(self.Second)
        self.container.add_widget(self.Third)
        self.container.add_widget(self.Fourth)
        self.container.add_widget(self.References)
        self.container.add_widget(self.Gost_standards)
        self.container.add_widget(self.Cows_and_bulls)
        return self.container

    @staticmethod
    def close_app():
        ClosePopup().open()

    def post_build_init(self, ev):

        win = Window
        win.bind(on_keyboard=self.key_handler)

    def key_handler(self, window, keycode1, keycode2, text, modifiers):
        if keycode1 == 27 or keycode1 == 1001:

            if self.container.current == 'First':
                ClosePopup().open()
                return True

            elif self.container.current == 'Second' or 'Third':
                self.container.current = 'First'
                return True

            else:
                pass
        else:
            return False


if __name__ == '__main__':
    EngineerApp().run()
