from kivy.uix.popup import Popup
from variables import GOST_STANDARDS


class SelectionOptionPopup(Popup):
    def open_next_popup(self):
        if self.ids.option_selection.text == 'Размеры по ГОСТ':
            SelectionGostPopup().open()


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
        self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
        product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
        self.ids.length_value.text = str(product_size[0])
        self.ids.width_value.text = str(product_size[1])
        self.ids.thickness_value.text = str(product_size[2])

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()
