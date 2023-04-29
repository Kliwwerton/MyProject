from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from variables import CHEMICAL_ELEMENTS
from MyPopups import MistakePopup


class Box(BoxLayout):
    pass


class ButtonAddElement(Button):
    """Button for add new chemical element to component"""

    def __init__(self, instance):
        super().__init__()
        self.instance = instance

    def add_element(self):
        element = NewElement(self.instance)
        element.open()

        # if len(self.chemical_elements) < 5:
        #     element = NewElement(self)
        #     element.open()
        #     print('Hello')
        #
        # elif len(self.chemical_elements) < 8:
        #     element = NewElement(self)
        #     element.open()
        #
        #     # self.size_hint = [0.8, 0.45]
        #
        # else:
        #     mistake = MistakePopup()
        #     mistake.ids.text_mistake.text = 'Превышено количество элементов!'
        #     mistake.open()


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
        self.composition = []
        if args:
            for i in args:
                if isinstance(i, MixtureComponent):
                    self.composition.append(i)
                    self.name += i.name + ':'

    def __str__(self):
        return f'{self.name}, {self.composition}'


class AddComponent(Popup):
    """Popup for adding Chemical element for composition of mixture"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.component = MixtureComponent()
        self.chemical_elements = {}
        self.chemical_elements_box = []

    def build(self):
        """Creates Chemical element"""
        print('Hello there')
        if self.ids.spinner_component.text in CHEMICAL_ELEMENTS:
            self.component.name = self.ids.spinner_component.text
            self.component.chemical_composition = CHEMICAL_ELEMENTS[self.component.name]

            for i, j in self.component.chemical_composition.items():
                box = Box()
                box.ids.name_element.text = i
                box.ids.value_element.text = j
                self.ids.grid_box.add_widget(box)
                self.chemical_elements_box.append(box)
                self.chemical_elements[i] = j
            but = ButtonAddElement(self)
            self.ids.grid_box.add_widget(but)
            self.chemical_elements_box.append(but)
            if len(self.chemical_elements_box) > 4:
                self.size_hint = [0.8, 0.45]
            else:
                pass

    def check_value(self):
        """Removes chemical elements that inside the Box class"""

        if self.chemical_elements_box:
            for i in self.chemical_elements_box:
                self.ids.grid_box.remove_widget(i)
            self.chemical_elements = {}

    def change_value(self):
        for i, j in self.component.chemical_composition.items():
            box = Box()
            box.ids.name_element.text = i
            box.ids.value_element.text = j
            self.ids.grid_box.add_widget(box)
            self.chemical_elements_box.append(box)
            self.chemical_elements[i] = j
        but = ButtonAddElement(self)
        self.ids.grid_box.add_widget(but)
        self.chemical_elements_box.append(but)
        if len(self.chemical_elements_box) > 4:
            self.size_hint = [0.8, 0.45]
        else:
            pass

    def add_component(self):
        pass


class NewElement(Popup):
    """Adda new chemical element to the selected component"""

    def __init__(self, instance):
        super().__init__()
        self.instance = instance

    def build(self):
        pass

    def add_element(self):
        if self.ids.spinner_element.text == 'Выберите элемент':
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = 'Не указано название элемента!'
            mistake.open()

        elif self.ids.spinner_element.text and self.ids.element_value.text:
            if self.ids.spinner_element.text in self.instance.chemical_elements:
                mistake = MistakePopup()
                mistake.ids.text_mistake.text = 'Такой элемент уже добавлен!'
                mistake.open()
            else:
                box = Box()
                box.ids.name_element.text = self.ids.spinner_element.text
                box.ids.value_element.text = str(self.ids.element_value.text)
                self.instance.ids.grid_box.add_widget(box)
                self.instance.chemical_elements_box.append(box)
                self.instance.chemical_elements[self.ids.spinner_element.text] = str(self.ids.element_value.text)

                self.instance.check_value()
                self.instance.change_value()
                self.dismiss()


        elif self.ids.spinner_element.text:
            if self.ids.spinner_element.text in self.instance.chemical_elements:
                mistake = MistakePopup()
                mistake.ids.text_mistake.text = 'Такой элемент уже добавлен!'
                mistake.open()
            else:
                box = Box()
                box.ids.name_element.text = self.ids.spinner_element.text
                box.ids.value_element.text = ''
                self.instance.ids.grid_box.add_widget(box)
                self.instance.chemical_elements_box.append(box)
                self.instance.chemical_elements[self.ids.spinner_element.text] = str(self.ids.element_value.text)
                if len(self.instance.chemical_elements) > 4:
                    self.instance.size_hint = [0.8, 0.45]
                else:
                    self.instance.size_hint = [0.8, 0.3]
                self.dismiss()

        else:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = 'Не указано название элемента!'
            mistake.open()


if __name__ == '__main__':
    """Test"""

    first = MixtureComponent(name='ПГНУ-2', chemical_composition={'Al': 32, 'Fe': 2.6})
    second = MixtureComponent(name='АРО-40', chemical_composition={'Al': 40, 'Fe': 1.8})

    composition = Composition(first, second)

    print(composition.name)
