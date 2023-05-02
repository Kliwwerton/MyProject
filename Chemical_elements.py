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
        self.mixture = {}
        # if args:
        #     for i in args:
        #         if isinstance(i, MixtureComponent):
        #             self.mixture.append(i)
        #             self.name += i.name + ':'
        self.content = None

    def __str__(self):
        return f'{self.name}, {self.mixture}'


class AddComponent(Popup):
    """Popup for adding Chemical element for composition of mixture"""

    def __init__(self, fourth, widget, **kwargs):
        super().__init__(**kwargs)
        self.component = MixtureComponent()
        self.ELEMENTS = deepcopy(CHEMICAL_ELEMENTS)
        self.dad = fourth
        self.widget = widget
        print(self.component.name)
        print(self.component.chemical_composition)

    def build(self):
        """Creates Chemical element"""
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
                box2 = Box2()
                box2.ids.wid_id.add_widget(but)
                self.ids.grid_box.add_widget(box2)

                if len(self.component.chemical_composition) >= 4:
                    self.size_hint = [0.8, 0.55]
                    self.ids.box_grid.size_hint = [1, 0.44]

                else:
                    self.size_hint = [0.8, 0.45]
                    self.ids.box_grid.size_hint = [1, 0.22]

            else:
                pass

    def clear_grid(self):
        """Removes chemical elements that inside the Box class"""
        print(self.ids.grid_box.children)

        if self.ids.grid_box.children:
            self.ids.grid_box.clear_widgets()

    def add_component(self):
        """Add new component to the Screen Fourth`s Composition
        Upgrades the received Widget"""
        if self.component.name and not self.ids.content_value.text:
            mistake = MistakePopup()
            mistake.ids.text_label.text = 'Не указано процентное'
            mistake.ids.text_mistake.text = 'содержание компонента в шихте!'
            mistake.open()

        elif self.component.name and self.ids.content_value.text:
            self.dad.composition.mixture[self.component] = self.ids.content_value.text
            _box = Box()
            _box.ids.name_element.text = self.component.name
            _box.ids.value_element.text = self.ids.content_value.text
            self.widget.add_widget(_box)

            print(self.component.name)
            print(self.component.chemical_composition)
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

            self.instance.component.chemical_composition[self.ids.spinner_element.text] = str(
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
