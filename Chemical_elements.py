from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from variables import CHEMICAL_ELEMENTS


class ChemicalElement:
    """Class Chemical_element. Creating chemical element, which has some attributes"""

    def __init__(self, name='', chemical_composition=None):
        if chemical_composition is None:
            chemical_composition = {}
        self.name = name
        self.chemical_composition = chemical_composition


class Composition(ChemicalElement):
    """Composition of Chemical_elements"""

    def __init__(self, *args):
        super().__init__()
        self.composition = []
        if args:
            for i in args:
                if isinstance(i, ChemicalElement):
                    self.composition.append(i)
                    self.name += i.name + ':'

    def __str__(self):
        return f'{self.name}, {self.composition}'


class Element(Popup):
    """Popup for adding Chemical element for composition of mixture"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.element = ChemicalElement()
        self.chemical_elements = []

    def build(self):
        if self.ids.spinner_element.text in CHEMICAL_ELEMENTS:
            self.element.name = self.ids.spinner_element.text
            self.element.chemical_composition = CHEMICAL_ELEMENTS[self.element.name]

            for i, j in self.element.chemical_composition.items():
                box = Box()
                box.ids.name_element.text = i
                box.ids.value_element.text = j
                self.ids.grid_box.add_widget(box)
                self.chemical_elements.append(box)

    def check_value(self):
        if self.chemical_elements:
            for i in self.chemical_elements:
                self.ids.grid_box.remove_widget(i)

    def add_element(self):
        if len(self.chemical_elements) < 5:
            pass

class Box(BoxLayout):
    pass


if __name__ == '__main__':

    first = ChemicalElement(name='ПГНУ-2', chemical_composition={'Al':32, 'Fe':2.6})
    second = ChemicalElement(name='АРО-40', chemical_composition={'Al':40, 'Fe':1.8})

    composition = Composition(first, second)

    print(composition.name)
