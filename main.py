# version.regex
# __version__ = 0.5.6

from kivy.config import Config

Config.set('graphics', 'width', 420)
Config.set('graphics', 'height', 800)
Config.set('kivy', 'keyboard_mode', 'systemanddock')
# Config.set('kivy', 'window_icon', 'Images/Logo.png')

from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FallOutTransition
from kivy.uix.label import Label

from variables import PRESS_PARAMETERS, CHEMICAL_COMPONENTS
from variables import VALUES
from MyPopups import SelectionOptionPopup, choice_popup, RessetPopup, ClosePopup, MistakePopup

from Chemical_elements import AddComponent, Composition, Box3, BigBoxResult, ResetButton, CalcButton

# Screens
Builder.load_file('First.kv')
Builder.load_file('Second.kv')
Builder.load_file('Third.kv')
Builder.load_file('Fourth.kv')
Builder.load_file('Fifth.kv')

# Popups
Builder.load_file('MyPopups.kv')

# Shapes
Builder.load_file('Tube.kv')
Builder.load_file('Trapezoid.kv')
Builder.load_file('Rectangle.kv')
Builder.load_file('Ribbed.kv')
Builder.load_file('Shaped.kv')
Builder.load_file('Fason.kv')

# Chemical_element
Builder.load_file('Chemical_element.kv')
Builder.load_file('Element_info.kv')

# Another buttons
Builder.load_file('References.kv')
Builder.load_file('Gost_standards.kv')

# The game
Builder.load_file('Cows_and_bulls.kv')


def open_option_popup():
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

    else:
        SelectionOptionPopup().open()


def return_mistake(value):
    popup = MistakePopup()
    popup.ids.text_mistake.text = value
    if value == 'Превышено количество компонентов!':
        popup.ids.text_label.text = ''
    popup.open()


class References(Screen):
    """Window of references"""

    def __init__(self):
        super().__init__()
        self.name = 'References'


class GostStandards(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Gost_standards'

    def open_gost_8691(self):
        pass


class CowsAndBulls(Screen):
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

    def calculate(self):
        """Calculating pressing pressure"""

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
            EngineerApp.sound.play()

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
        EngineerApp.sound_reset.play()

    def open_resset_popup(self):
        RessetPopup(self).open()

    @staticmethod
    def open_selection_option_popup():
        open_option_popup()

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

    def calculate(self):
        """Calculates pressing pressure for any press"""

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
                EngineerApp.sound.play()

    def open_resset_popup(self):
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
        EngineerApp.sound_reset.play()

    def change_label(self):
        """changing label unit of press parameters"""
        if self.ids.spinner_press_mark.text == 'Выберите пресс':
            self.ids.pressure_unit.text = ''
        else:
            self.ids.pressure_unit.text = PRESS_PARAMETERS[self.ids.spinner_press_mark.text][2]

    @staticmethod
    def open_selection_option_popup():
        open_option_popup()

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


class Fourth(Screen):
    """Fourth Screen. Screen of calculation chemical composition."""

    def __init__(self):
        super().__init__()
        self.composition = Composition()
        self.name = 'Fourth'
        self.weight_value = {}
        self.components_for_spinner = ['Новый компонент', 'СОБРАТЬ СМЕСЬ']
        for i in CHEMICAL_COMPONENTS:
            self.components_for_spinner.append(i)

    # def on_touch_down(self, touch):
    #     print(touch, self.children)
    #     if touch.pos in self.ids.btn_add_component.pos:
    #         print('Hello world')

    def open_reset_popup(self):
        RessetPopup(self).open()

    def add_new_component(self):
        """Adds new component to mixture"""

        summ = 0
        for i in self.composition.mixture:
            summ += float(self.composition.mixture[i])

        if summ == 100:
            mistake = MistakePopup()
            mistake.size_hint = [0.8, 0.24]
            mistake.title = 'ПРЕДУПРЕЖДЕНИE!'
            mistake.ids.text_label.text = 'Сумма всех компонентов уже 100%'
            mistake.ids.text_mistake.text = 'БОЛЬШЕ НЕ ДОБАВИТЬ!!!'
            lab = Label()
            lab.text = 'ПРОИЗВЕДИТЕ СБРОС ДАННЫХ!'
            mistake.ids.mistake_box.add_widget(lab)
            mistake.ids.mistake_but.size_hint = [0.2, 0.3]
            mistake.open()
        else:
            self.ids.box_result.clear_widgets()

            if not self.ids.first_box.children:
                element = AddComponent(self, self.ids.first_box, number_component=1)
                element.ids.spinner_component.values = self.components_for_spinner
                element.open()

            elif not self.ids.second_box.children:
                element = AddComponent(self, self.ids.second_box, number_component=2)
                element.ids.spinner_component.values = self.components_for_spinner
                element.open()

            elif not self.ids.third_box.children:
                element = AddComponent(self, self.ids.third_box, number_component=3)
                element.ids.spinner_component.values = self.components_for_spinner
                element.open()

            elif not self.ids.fourth_box.children:
                element = AddComponent(self, self.ids.fourth_box, number_component=4)
                element.ids.spinner_component.values = self.components_for_spinner
                element.open()

            elif not self.ids.fifth_box.children:
                element = AddComponent(self, self.ids.fifth_box, number_component=5)
                element.ids.spinner_component.values = self.components_for_spinner
                element.open()

            else:
                return_mistake('Превышено количество компонентов!')

    def add_buttons(self):
        """Adds buttons: button1 RessetButton, button2 CalcButton"""
        if not self.ids.reset_but.children:
            reset_button = ResetButton()
            self.ids.reset_but.add_widget(reset_button)
            calc_button = CalcButton()
            self.ids.calc_but.add_widget(calc_button)

    def build_label(self):
        if self.composition.name:
            self.ids.box_result.clear_widgets()

            _box = BigBoxResult()
            _box.ids.number_component.text = 'Состав шихты: '

            if len(self.composition.name) > 50:
                _box.ids.components_name.font_size = '10sp'

            _box.ids.components_name.text = self.composition.name
            _box.ids.ratio_composition.text = self.composition.ratio

            for i, j in self.weight_value.items():
                box = Box3()
                box.ids.lab_1.text = i
                box.ids.lab_2.text = str(round(j, 2))
                _box.ids.box_for_elements.add_widget(box)

            self.ids.box_result.add_widget(_box)

    def calculate(self):

        self.weight_value = {}
        for i, k in self.composition.mixture.items():  # i = component, k = % (содержание в шихте)

            for h, j in i.chemical_composition.items():  # h = element, j = % (количество элемента в компоненте)
                n = (float(j) * float(k)) / 100

                if h in self.weight_value:
                    self.weight_value[h] += n
                else:
                    self.weight_value[h] = n

        self.build_label()
        EngineerApp.sound.play()

    def reset(self):
        self.ids.first_box.clear_widgets()
        self.ids.second_box.clear_widgets()
        self.ids.third_box.clear_widgets()
        self.ids.fourth_box.clear_widgets()
        self.ids.fifth_box.clear_widgets()
        self.ids.box_result.clear_widgets()
        self.ids.reset_but.clear_widgets()
        self.ids.calc_but.clear_widgets()

        self.composition = Composition()
        EngineerApp.sound_reset.play()

    def open_component(self, instance):
        try:
            if instance.component:
                element = AddComponent(self, instance, number_component=instance.number_component)
                element.ids.spinner_component.text = instance.component.name
                print(instance.component.name)
                element.ids.spinner_component.values = []
                element.open()

        except AttributeError:
            print('Перехвачена ошибка')


# class Fifth(Screen):
#     """Fourth Screen. Screen of calculation chemical composition."""
#     def __init__(self):
#         super().__init__()
#         self.composition = Composition()
#         self.name = 'Fifth'
#         self.weight_value = {}
#
#     def open_ressetPopup(self):
#         RessetPopup(self).open()
#
#     def add_new_component(self):
#         if not self.ids.first_box.children:
#             element = AddComponent(self, self.ids.first_box, number_component=1)
#             element.open()
#
#         elif not self.ids.second_box.children:
#             element = AddComponent(self, self.ids.second_box, number_component=2)
#             element.open()
#
#         elif not self.ids.third_box.children:
#             element = AddComponent(self, self.ids.third_box, number_component=3)
#             element.open()
#
#         elif not self.ids.fourth_box.children:
#             element = AddComponent(self, self.ids.fourth_box, number_component=4)
#             element.open()
#
#         elif not self.ids.fifth_box.children:
#             element = AddComponent(self, self.ids.fifth_box, number_component=5)
#             element.open()
#
#         else:
#             return_mistake('Превышено количество компонентов!')
#
#     def build_label(self):
#         if self.composition.name:
#             self.ids.box_result.clear_widgets()
#
#             _box = BigBoxResult()
#             _box.ids.number_component.text = 'Состав шихты: '
#             _box.ids.components_name.text = self.composition.name
#             _box.ids.ratio_composition.text = self.composition.ratio
#
#             for i, j in self.weight_value.items():
#                 box = Box3()
#                 box.ids.lab_1.text = i
#                 box.ids.lab_2.text = str(round(j, 2))
#                 _box.ids.box_for_elements.add_widget(box)
#
#             self.ids.box_result.add_widget(_box)
#
#     def calculate(self):
#
#         self.weight_value = {}
#         for i, k in self.composition.mixture.items():  # i = component, k = % (содержание в шихте)
#
#             for h, j in i.chemical_composition.items():  # h = element, j = % (количество элемента в компоненте)
#                 n = (float(j) * float(k)) / 100
#
#                 if h in self.weight_value:
#                     self.weight_value[h] += n
#                 else:
#                     self.weight_value[h] = n
#
#         self.build_label()
#
#     def reset(self):
#         self.ids.first_box.clear_widgets()
#         self.ids.second_box.clear_widgets()
#         self.ids.third_box.clear_widgets()
#         self.ids.fourth_box.clear_widgets()
#         self.ids.fifth_box.clear_widgets()
#         self.ids.box_result.clear_widgets()
#
#         self.composition = Composition()
#
#     def open_component(self, instance):
#         print(instance.name)
#         print(self.composition.mixture)


class EngineerApp(App):
    """MAIN APP ENGINEER"""
    sound = SoundLoader.load('sounds/sound_but.mp3')
    sound_reset = SoundLoader.load('sounds/sound_reset.mp3')

    def __init__(self):
        super().__init__()

        self.title = 'ИНЖЕНЕР НА ВСЮ ГОЛОВУ!'
        self.container = ScreenManager(transition=FallOutTransition())
        self.First = First()
        self.Second = Second()
        self.Third = Third()
        self.Fourth = Fourth()
        # self.Fifth = Fifth()
        self.References = References()
        self.Gost_standards = GostStandards()
        self.Cows_and_bulls = CowsAndBulls()

    def build(self):
        self.icon = 'Logo.png'
        self.bind(on_start=self.post_build_init)
        Window.clearcolor = (232 / 255, 184 / 255, 1, 1)
        # container = Container(transition=SwapTransition())
        self.container.add_widget(self.First)
        self.container.add_widget(self.Second)
        self.container.add_widget(self.Third)
        self.container.add_widget(self.Fourth)
        # self.container.add_widget(self.Fifth)
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

            elif self.container.current == 'Second' or 'Third' or 'Fourth':
                self.container.current = 'First'
                print('I`m here')
                return True

            else:
                pass
        else:
            return False


if __name__ == '__main__':
    EngineerApp().run()
