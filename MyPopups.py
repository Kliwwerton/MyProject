from kivy.uix.popup import Popup
from variables import GOST_STANDARDS
from variables import SQUARE, RECTANGLES, RING, TRAPEZOID
from math import pi


class SelectionOptionPopup(Popup):
    def open_next_popup(self):
        if self.ids.option_selection.text == 'Размеры по ГОСТ':
            SelectionGostPopup().open()
        else:
            ChoosingShapeProduct().open()


class SelectionGostPopup(Popup):
    def choosing_a_product_number(self):
        numbers = []
        if self.ids.gost_number.text:
            for i in GOST_STANDARDS[self.ids.gost_number.text]:
                numbers.append(str(i))
            self.ids.product_numbers.values = numbers

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def opening_calculation_window(self):
        if self.ids.gost_number.text in RECTANGLES \
                and self.ids.product_numbers.text in RECTANGLES[self.ids.gost_number.text]:
            popup = CalculationsAreaOfRectangle()
            popup.chose_values.append(self.ids.gost_number.text)
            popup.chose_values.append(self.ids.product_numbers.text)
            popup.open()
        elif self.ids.gost_number.text in TRAPEZOID \
                and self.ids.product_numbers.text in TRAPEZOID[self.ids.gost_number.text]:
            popup = CalculationsAreaOfTrapezoid()
            popup.chose_values.append(self.ids.gost_number.text)
            popup.chose_values.append(self.ids.product_numbers.text)
            popup.open()
        elif self.ids.gost_number.text in RING \
                and self.ids.product_numbers.text in RING[self.ids.gost_number.text]:
            popup = CalculationsAreaOfRing()
            popup.chose_values.append(self.ids.gost_number.text)
            popup.chose_values.append(self.ids.product_numbers.text)
            popup.open()


class CalculationsAreaOfRectangle(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []

    def build_instance(self):
        if len(self.chose_values) > 1:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
            self.ids.length_value.text = str(product_size[0])
            self.ids.width_value.text = str(product_size[1])
            self.ids.thickness_value.text = str(product_size[2])
        else:
            self.ids.label_gost_number.text = self.chose_values[0]

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def calculation_square(self):
        if self.ids.length_value.text and self.ids.width_value.text:
            value = (float(self.ids.length_value.text) * float(self.ids.width_value.text)/100)
            SQUARE.append(round(value, 1))


class CalculationsAreaOfTrapezoid(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []

    def build_instance(self):
        if len(self.chose_values) > 1:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
            self.ids.length_value.text = str(product_size[0])
            self.ids.width_value_1.text = str(product_size[1])
            self.ids.width_value_2.text = str(product_size[2])
            self.ids.thickness_value.text = str(product_size[3])
        else:
            self.ids.label_gost_number.text = self.chose_values[0]

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def calculation_square(self):
        if self.ids.length_value.text and self.ids.width_value_1.text and self.ids.width_value_2.text:
            value = (float(self.ids.length_value.text) *\
                    ((float(self.ids.width_value_1.text) + float(self.ids.width_value_2.text)) / 2)/100)
            print(value)
            SQUARE.append(round(value, 1))


class CalculationsAreaOfRing(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []

    def build_instance(self):
        if len(self.chose_values) > 1:
            self.ids.label_gost_number.text = self.chose_values[0] + ' ' + self.chose_values[1]
            product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
            self.ids.outer_diameter_D.text = str(product_size[0])
            self.ids.inner_diameter_d.text = str(product_size[1])
            self.ids.length_value.text = str(product_size[2])
        else:
            self.ids.label_gost_number.text = self.chose_values[0]

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def calculation_square(self):
        if self.ids.outer_diameter_D.text and self.ids.inner_diameter_d.text:
            _D = float(self.ids.outer_diameter_D.text)
            d = float(self.ids.inner_diameter_d.text)
            value = (((pi * _D ** 2) / 4) - ((pi * d ** 2) / 4) / 100)
            print(value)
            SQUARE.append(round(value, 1))


class ChoosingShapeProduct(Popup):

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def choose_window(self):
        if self.ids.spin_choose_window.text == 'Прямоугольник':
            popup = CalculationsAreaOfRectangle()
            popup.chose_values.append(self.ids.spin_choose_window.text)
            popup.open()

        elif self.ids.spin_choose_window.text == 'Трапецеидальный клин':
            popup = CalculationsAreaOfTrapezoid()
            popup.chose_values.append(self.ids.spin_choose_window.text)
            popup.open()

        elif self.ids.spin_choose_window.text == 'Кольцо':
            popup = CalculationsAreaOfRing()
            popup.chose_values.append(self.ids.spin_choose_window.text)
            popup.open()
