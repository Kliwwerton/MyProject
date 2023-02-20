from kivy.uix.popup import Popup
from variables import GOST_STANDARDS
from variables import SQUARE


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
            self.ids.product_number.values = numbers

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def opening_calculation_window(self):
        popup = CalculationsAreaOfRectangle()
        popup.chose_values.append(self.ids.gost_number.text)
        popup.chose_values.append(self.ids.product_number.text)
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
            value = round(float(self.ids.length_value.text) * float(self.ids.width_value.text), 2)
            print(value)
            SQUARE.append(value)


class CalculationsAreaOfTrapezoid(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []


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
