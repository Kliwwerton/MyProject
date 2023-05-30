from copy import deepcopy

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from variables import CHEMICAL_COMPONENTS, CHEMICAL_ELEMENTS
from MyPopups import MistakePopup


class Box(BoxLayout):

    def __init__(self, instance):
        super().__init__()
        self.instance = instance

    def change_value(self):
        if self.ids.value_element.text == self.instance.COMPONENTS[self.instance.component.name][self.ids.name_element.text]:
            pass
        else:
            self.instance.COMPONENTS[self.instance.component.name][self.ids.name_element.text] = self.ids.value_element.text


class Box2(BoxLayout):
    pass


class Box3(BoxLayout):
    pass


class BigBox(BoxLayout):
    pass


class BigBoxResult(BoxLayout):
    pass


class ResetButton(Button):
    pass


class CalcButton(Button):
    pass


class ButtonAddElement(Button):
    """Button for add new chemical element to component"""

    def __init__(self, instance):
        super().__init__()
        self.instance = instance

    def add_element(self):
        element = NewElement(self.instance)
        element.open()


class MixtureComponent:
    """Class Chemical_element. Creating chemical element, which has some attributes"""

    def __init__(self, name='', chemical_composition=None):
        if chemical_composition is None:
            chemical_composition = {}
        self.name = name
        self.chemical_composition = chemical_composition


class Composition(MixtureComponent):
    """Composition of Chemical_elements"""

    def __init__(self, *args):
        super().__init__()
        self.mixture = {}
        self.names = []
        self.ratio = ''
        self.content = None

    def __str__(self):
        return f'{self.name}, {self.ratio}, {self.names}, {self.mixture}'


class AddComponent(Popup):
    """Popup for adding Chemical element for composition of mixture"""

    def __init__(self, fourth, widget, number_component=None, color=None, **kwargs):
        super().__init__(**kwargs)
        self.component = MixtureComponent()
        self.COMPONENTS = deepcopy(CHEMICAL_COMPONENTS)
        self.dad = fourth
        self.widget = widget
        self.number_component = number_component
        self.color = color

    def build(self):
        """Creates Chemical element"""
        if self.ids.spinner_component.text in self.COMPONENTS:

            if len(self.ids.spinner_component.text) > 32:
                self.ids.spinner_component.font_size = '10sp'
            else:
                self.ids.spinner_component.font_size = '15sp'

            self.component.name = self.ids.spinner_component.text
            self.component.chemical_composition = self.COMPONENTS[self.component.name]

            for i, j in self.component.chemical_composition.items():
                box = Box(self)
                box.ids.name_element.text = i
                if isinstance(j, float):
                    box.ids.value_element.text = str(round(j, 2))
                else:
                    box.ids.value_element.text = j
                self.ids.grid_box.add_widget(box)

            self.create_button()

        elif self.ids.spinner_component.text != 'Выберите компонент':
            self.component.name = self.ids.spinner_component.text
            self.component.chemical_composition = {}
            self.COMPONENTS[self.component.name] = {}

            if len(self.ids.spinner_component.text) > 32:
                self.ids.spinner_component.font_size = '10sp'
            else:
                self.ids.spinner_component.font_size = '15sp'

            self.create_button()

    def clear_grid(self):
        """Removes chemical elements that inside the Box class"""

        if self.ids.grid_box.children:
            self.ids.grid_box.clear_widgets()

    def check_name(self):
        """checks the selected name for entry into the list """

        if self.ids.spinner_component.text == 'Новый компонент':
            if 'Компонент 1' not in self.dad.composition.names:
                self.ids.spinner_component.text = 'Компонент 1'
            elif 'Компонент 2' not in self.dad.composition.names:
                self.ids.spinner_component.text = 'Компонент 2'
            elif 'Компонент 3' not in self.dad.composition.names:
                self.ids.spinner_component.text = 'Компонент 3'
            elif 'Компонент 4' not in self.dad.composition.names:
                self.ids.spinner_component.text = 'Компонент 4'
            elif 'Компонент 5' not in self.dad.composition.names:
                self.ids.spinner_component.text = 'Компонент 5'

            else:
                mistake = MistakePopup()
                mistake.ids.text_label.text = 'От куда столько'
                mistake.ids.text_mistake.text = 'НОВЫХ КОМПОНЕНТОВ!!!'
                mistake.open()
                self.ids.spinner_component.text = 'Выберите компонент'

        elif self.ids.spinner_component.text == 'СОБРАТЬ СМЕСЬ':
            new_popup = AddComponents(self)
            new_popup.open()

        elif self.dad.composition.mixture:

            for i in self.dad.composition.mixture:

                if i.name == self.ids.spinner_component.text:
                    mistake = MistakePopup()
                    mistake.ids.text_label.text = 'Такой компонент'
                    mistake.ids.text_mistake.text = 'УЖЕ ДОБАВЛЕН В ШИХТУ!!!'
                    mistake.open()
                    self.ids.spinner_component.text = 'Выберите компонент'

                else:
                    self.clear_grid()
                    self.build()
        else:
            self.clear_grid()
            self.build()

    def create_button(self):
        """Creates new button for add new element"""
        if len(self.component.chemical_composition) < 8:
            but = ButtonAddElement(self)
            box2 = Box2()
            box2.ids.wid_id.add_widget(but)
            self.ids.grid_box.add_widget(box2)

            if len(self.component.chemical_composition) >= 4:
                self.size_hint = [0.8, 0.55]
                self.ids.box_grid.size_hint = [1, 0.44]

            else:
                self.size_hint = [0.8, 0.45]
                self.ids.box_grid.size_hint = [1, 0.22]

    def check_values(self):
        """Checks presence for the entered date"""

        if self.component.name and not self.ids.content_value.text:
            mistake = MistakePopup()
            mistake.ids.text_label.text = 'Не указано процентное'
            mistake.ids.text_mistake.text = 'содержание компонента в шихте!'
            mistake.open()

        elif self.component.name and self.ids.content_value.text:

            if not self.component.chemical_composition:
                mistake = MistakePopup()
                mistake.ids.text_label.text = 'НЕ ДОБАВЛЕНО НИ ОДНОГО'
                mistake.ids.text_mistake.text = 'ХИМИЧЕСКОГО ЭЛЕМЕНТА!!!'
                self.ids.content_value.text = ''
                mistake.open()

            elif self.dad.composition.mixture:
                summ = 0

                for i in self.dad.composition.mixture:
                    summ += float(self.dad.composition.mixture[i])
                summ += float(self.ids.content_value.text)

                if summ > 100:
                    mistake = MistakePopup()
                    mistake.ids.text_label.text = 'КОЛИЧЕСТВО КОМПОНЕНТОВ'
                    mistake.ids.text_mistake.text = 'ПРЕВЫСИЛО 100%!!!'
                    self.ids.content_value.text = ''
                    mistake.open()

                else:
                    self.add_component()

            elif float(self.ids.content_value.text) > 100:
                mistake = MistakePopup()
                mistake.ids.text_label.text = 'КОЛИЧЕСТВО КОМПОНЕНТОВ'
                mistake.ids.text_mistake.text = 'ПРЕВЫСИЛО 100%!!!'
                self.ids.content_value.text = ''
                mistake.open()

            else:
                self.add_component()
        else:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = 'Не выбран компонент!'
            mistake.open()

    def add_component(self):
        """Add new component to the Screen Fourth`s Composition
        Upgrades the received Widget"""

        self.dad.composition.mixture[self.component] = self.ids.content_value.text
        self.dad.composition.names.append(self.component.name)

        if self.dad.composition.name:
            self.dad.composition.name += ':' + self.component.name
            self.dad.composition.ratio += ':' + self.ids.content_value.text
        else:
            self.dad.composition.name += self.component.name
            self.dad.composition.ratio += self.ids.content_value.text

        _box = BigBox()
        _box.ids.number_component.text = 'Компонент № ' + str(self.number_component)
        _box.ids.components_name.text = self.component.name

        if '(' in self.component.name:
            if len(self.component.name) > 32:
                _box.ids.components_name.font_size = '10sp'
            else:
                _box.ids.components_name.font_size = '15sp'

        _box.ids.lab_lab.text = '% в шихте'
        _box.ids.lab_value_element.text = self.ids.content_value.text

        if self.color:
            _box.ids.number_component.color = self.color
            _box.ids.components_name.color = self.color
            _box.ids.lab_lab.color = self.color
            _box.ids.lab_lab.text = '% в смеси'
            _box.ids.lab_value_element.color = self.color

        for i, j in self.component.chemical_composition.items():
            box = Box3()
            box.ids.lab_1.text = i
            if isinstance(j, float):
                box.ids.lab_2.text = str(round(j, 2))
            else:
                box.ids.lab_2.text = j
            if self.color:
                box.ids.lab_1.color = self.color
                box.ids.lab_2.color = self.color
            _box.ids.box_for_elements.add_widget(box)

        self.widget.name = self.component.name
        self.widget.add_widget(_box)
        self.dad.add_buttons()

        self.dismiss()

    def close(self):
        del self.component


class NewElement(Popup):
    """Adds new chemical element to the selected component"""

    def __init__(self, instance):
        super().__init__()
        self.instance = instance
        self.ids.spinner_element.values = CHEMICAL_ELEMENTS

    def build(self):
        pass

    def add_element(self):
        """Adds new chemical element to the current component"""
        if self.ids.spinner_element.text == 'Выберите элемент':
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = 'Не указано название элемента!'
            mistake.open()

        elif self.ids.spinner_element.text in self.instance.component.chemical_composition:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = 'Такой элемент уже добавлен!'
            mistake.open()

        elif self.ids.spinner_element.text and self.ids.element_value.text:
            if self.instance.component.chemical_composition:
                summ = 0
                for i in self.instance.component.chemical_composition:
                    summ += float(self.instance.component.chemical_composition[i])
                else:
                    summ += float(self.ids.element_value.text)

                if summ > 100:
                    mistake = MistakePopup()
                    mistake.ids.text_label.text = 'НЕ МОЖЕТ БЫТЬ >100%!!!'
                    mistake.ids.text_mistake.text = 'Превышено содержание элементов!'
                    mistake.open()
                else:
                    self.instance.component.chemical_composition[self.ids.spinner_element.text] = str(
                        self.ids.element_value.text)
                    self.instance.clear_grid()
                    self.instance.build()
                    self.dismiss()
            else:
                if float(self.ids.element_value.text) > 99:
                    mistake = MistakePopup()
                    mistake.ids.text_label.text = 'НЕ МОЖЕТ БЫТЬ!!!'
                    mistake.ids.text_mistake.text = 'СТОЛЬКО НЕ БЫВАЕТ!!!'
                    mistake.open()
                else:
                    self.instance.component.chemical_composition[self.ids.spinner_element.text] = str(
                        self.ids.element_value.text)
                    self.instance.COMPONENTS[self.instance.component.name][self.ids.spinner_element.text] = str(
                        self.ids.element_value.text)
                    self.instance.clear_grid()
                    self.instance.build()
                    self.dismiss()

        elif not self.ids.element_value.text:
            mistake = MistakePopup()
            mistake.ids.text_label.text = 'Укажите процентное'
            mistake.ids.text_mistake.text = 'содержание элемента!'
            mistake.open()

        else:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = 'Не указано название элемента!'
            mistake.open()


class AddComponents(Popup):
    """Popup for adding Chemical element for composition of mixture"""

    def __init__(self, widget, **kwargs):
        super().__init__(**kwargs)
        self.widget = widget
        self.composition = Composition()

    def close(self):
        self.widget.ids.spinner_component.text = 'Выберите компонент'

    def add_new_component(self):

        values = ['Новый компонент']
        for i in CHEMICAL_COMPONENTS:
            values.append(i)

        if not self.ids.first_box.children:
            element = AddComponent(self, self.ids.first_box, number_component=1, color=[1, 1, 1, 1])
            element.ids.spinner_component.values = values
            element.open()

        elif not self.ids.second_box.children:
            element = AddComponent(self, self.ids.second_box, number_component=2, color=[1, 1, 1, 1])
            element.ids.spinner_component.values = values
            element.open()

        elif not self.ids.third_box.children:
            element = AddComponent(self, self.ids.third_box, number_component=3, color=[1, 1, 1, 1])
            element.ids.spinner_component.values = values
            element.open()

        else:
            popup = MistakePopup()
            popup.ids.text_mistake.text = 'Превышено количество компонентов'
            popup.open()

    def add_name(self):
        """Forms the name"""
        self.ids.box_result.clear_widgets()
        box = Box3()
        box.orientation = 'horizontal'

        # print(len(self.composition.name))

        if len(self.composition.name) > 34:
            box.ids.lab_1.font_size = '10sp'
            box.ids.lab_2.font_size = '15sp'
        elif len(self.composition.name) > 19:
            box.ids.lab_1.font_size = '15sp'
            box.ids.lab_2.font_size = '15sp'

        box.ids.lab_1.text = '(' + self.composition.name + ')'
        box.ids.lab_1.color = [1, 1, 1, 1]
        box.ids.lab_2.text = '(' + self.composition.ratio + ')'
        box.ids.lab_2.color = [1, 1, 1, 1]
        box.ids.lab_2.size_hint = [0.5, 1]
        self.ids.box_result.add_widget(box)

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

    def add_mixture(self):

        chemical_composition = {}
        for i, k in self.composition.mixture.items():  # i = component, k = % (содержание в шихте)

            for h, j in i.chemical_composition.items():  # h = element, j = % (количество элемента в компоненте)
                n = (float(j) * float(k)) / 100

                if h in chemical_composition:
                    chemical_composition[h] += n
                else:
                    chemical_composition[h] = n

        self.composition.name = '(' + self.composition.name + '[sub](' + self.composition.ratio + ') [/sub]' + ')'
        self.widget.COMPONENTS[self.composition.name] = chemical_composition
        self.widget.ids.spinner_component.text = self.composition.name

        summ = 0
        if self.composition.mixture:

            for i in self.composition.mixture:
                summ += float(self.composition.mixture[i])

            if summ < 100:
                mistake = MistakePopup()
                mistake.title = 'РЕКОМЕНДАЦИЯ'
                mistake.ids.text_label.text = 'Для достоверного расчёта '
                mistake.ids.text_mistake.text = 'состав смеси должен составлять 100%!!!'
                mistake.open()

