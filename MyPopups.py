from kivy.uix.popup import Popup
from variables import GOST_NUMBERS


class SelectionOptionPopup(Popup):
    def open_next_popup(self):
        if self.ids.option_selection.text == 'Размеры по ГОСТ':
            SelectionGostPopup().open()


class SelectionGostPopup(Popup):
    def choosing_a_product_number(self):
        if self.ids.gost_number.text == 'ГОСТ 390-2018':
            numbers = []
            for i in GOST_NUMBERS[self.ids.gost_number.text]:
                numbers.append(str(i))
            self.ids.product_number.values = numbers

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()
