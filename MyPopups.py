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
        # elif self.ids.gost_number.text == 'ГОСТ 5341-2016 (Ковшевой)':
        #     for i in GOST_STANDARDS[self.ids.gost_number.text]:

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    @staticmethod
    def opening_calculation_window(self):
        CalculationsAreaOfRectangle().open()


class CalculationsAreaOfRectangle(Popup):
    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()
