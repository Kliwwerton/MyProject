from copy import deepcopy

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from variables import CHEMICAL_ELEMENTS
from MyPopups import MistakePopup


class Box(BoxLayout):
    pass

class Box2(BoxLayout):
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
        self.ELEMENTS = deepcopy(CHEMICAL_ELEMENTS)
        print(self.component.name)
        print(self.component.chemical_composition)

    def build(self):
        """Creates Chemical element"""
        print(CHEMICAL_ELEMENTS)
        if self.ids.spinner_component.text in self.ELEMENTS:
            self.component.name = self.ids.spinner_component.text
            self.component.chemical_composition = self.ELEMENTS[self.component.name]

            for i, j in self.component.chemical_composition.items():
                box = Box()
                box.ids.name_element.text = i
                box.ids.value_element.text = j
                self.ids.grid_box.add_widget(box)

            if len(self.component.chemical_composition) < 8:
                but = ButtonAddElement(self)
                box = Box2()
                # box.ids.wid_id = but
                box.ids.wid_id.add_widget(but)
                self.ids.grid_box.add_widget(box)

                if len(self.component.chemical_composition) >= 4:
                    self.size_hint = [0.8, 0.45]
                    self.ids.box_id.size_hint = [1, 0.5]
                    self.ids.spinner_component.size_hint = [0.8, 0.4]
                    self.ids.btn_add.size_hint = [0.8, 0.4]

            else:
                pass

    def clear_grid(self):
        """Removes chemical elements that inside the Box class"""
        print(self.ids.grid_box.children)

        if self.ids.grid_box.children:
            self.ids.grid_box.clear_widgets()

    def add_component(self):
        if self.component.name:
            pass
            self.dismiss()
        else:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = 'Не выбран компонент!'
            mistake.open()

    def close(self):
        del self.component


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

        elif self.ids.spinner_element.text in self.instance.component.chemical_composition:
                mistake = MistakePopup()
                mistake.ids.text_mistake.text = 'Такой элемент уже добавлен!'
                mistake.open()

        elif self.ids.spinner_element.text and self.ids.element_value.text:

            self.instance.component.chemical_composition[self.ids.spinner_element.text] = str(self.ids.element_value.text)

            self.instance.clear_grid()
            self.instance.build()
            self.dismiss()

        elif not self.ids.element_value.text:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = 'Укажите процентное содержание элемента!'
            mistake.open()

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
