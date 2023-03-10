from kivy.uix.popup import Popup
from variables import GOST_STANDARDS
from variables import SQUARE, RECTANGLES, RING, TRAPEZOID, \
    TRAPEZOID_1, RIBBED, RIBBED_1, RIBBED_2, RIBBED_3, END_WEDGE, END_WEDGE_2, SHAPED
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

        elif self.ids.gost_number.text in TRAPEZOID \
                and self.ids.product_numbers.text in TRAPEZOID[self.ids.gost_number.text]:
            popup = CalculationsAreaOfTrapezoid()
            popup.chose_values.append(TRAPEZOID['Image'])

        elif self.ids.gost_number.text in TRAPEZOID_1 \
                and self.ids.product_numbers.text in TRAPEZOID_1[self.ids.gost_number.text]:
            popup = CalculationsAreaOfTrapezoid()
            popup.chose_values.append(TRAPEZOID_1['Image'])

        elif self.ids.gost_number.text in RIBBED \
                and self.ids.product_numbers.text in RIBBED[self.ids.gost_number.text]:
            popup = CalculationsAreaOfRibbed()
            popup.chose_values.append(RIBBED['Image'])

        elif self.ids.gost_number.text in RIBBED_1 \
                and self.ids.product_numbers.text in RIBBED_1[self.ids.gost_number.text]:
            popup = CalculationsAreaOfRibbed()
            popup.chose_values.append(RIBBED_1['Image'])

        elif self.ids.gost_number.text in RIBBED_2 \
                and self.ids.product_numbers.text in RIBBED_2[self.ids.gost_number.text]:
            popup = CalculationsAreaOfRibbed()
            popup.chose_values.append(RIBBED_2['Image'])
            popup.ids.width_label_H.text = 'Ширина(S):'
            popup.ids.thickness_label_S.text = 'Толщина(H)[sup][size=20]*[/size][sup]):'
            popup.ids.width_label_S1.text = 'Ширина(S[sub]1[/sub])[sup][size=20]*[/size][/sup]:'

        elif self.ids.gost_number.text in RIBBED_3 \
                and self.ids.product_numbers.text in RIBBED_3[self.ids.gost_number.text]:
            popup = CalculationsAreaOfRibbed()
            popup.chose_values.append(RIBBED_3['Image'])
            popup.ids.length_label_L.text = 'Ширина(в)'
            popup.ids.width_label_H.text = 'Длина(б):'
            popup.ids.thickness_label_S.text = 'Толщина(а)[sup][size=20]*[/size][sup]):'
            popup.ids.width_label_S1.text = 'Толщина(а[sub]1[/sub])[sup][size=20]*[/size][/sup]:'

        elif self.ids.gost_number.text in END_WEDGE \
                and self.ids.product_numbers.text in END_WEDGE[self.ids.gost_number.text]:
            popup = CalculationsAreaOfRibbed()
            popup.chose_values.append(END_WEDGE['Image'])
            popup.ids.length_label_L.text = 'Длина(в)'
            popup.ids.width_label_H.text = 'Ширина(б):'
            popup.ids.thickness_label_S.text = 'Толщина(а)[sup][size=20]*[/size][sup]):'
            popup.ids.width_label_S1.text = 'Толщина(а[sub]1[/sub])[sup][size=20]*[/size][/sup]:'
            popup.title = 'Расчёт площади торцового клина'

        elif self.ids.gost_number.text in SHAPED \
                and self.ids.product_numbers.text in SHAPED[self.ids.gost_number.text]:
            popup = CalculationsAreaOfShaped()
            popup.chose_values.append(SHAPED['Image'])
            popup.ids.length_label.text = 'Длина(L)'
            popup.ids.width_label.text = 'Ширина(H):'
            popup.ids.width_label_2.text = 'Ширина(H[sub]1[/sub]):'
            popup.ids.thickness_label_S.text = 'Толщина(S[sub]1[/sub])[sup][size=20]*[/size][/sup]:'
            popup.title = 'Расчёт площади фасонного изделия'

        elif self.ids.gost_number.text in END_WEDGE_2 \
                and self.ids.product_numbers.text in END_WEDGE_2[self.ids.gost_number.text]:
            popup = CalculationsAreaOfRibbed()
            popup.chose_values.append(END_WEDGE_2['Image'])
            popup.title = 'Расчёт площади торцового клина'

        elif self.ids.gost_number.text in RING \
                and self.ids.product_numbers.text in RING[self.ids.gost_number.text]:
            popup = CalculationsAreaOfRing()

        else:
            popup = WrongPopup()

        popup.chose_values.insert(0, self.ids.gost_number.text)
        popup.chose_values.insert(1, self.ids.product_numbers.text)
        popup.open()


class WrongPopup(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []

    def build_instance(self):
        self.ids.label_wrong.text = 'В базе пока нет изделия под № ' + \
                                    self.chose_values[1]


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
        if len(self.chose_values) > 2:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
            self.ids.length_value.text = str(product_size[0])
            self.ids.width_value_1.text = str(product_size[1])
            self.ids.width_value_2.text = str(product_size[2])
            self.ids.thickness_value.text = str(product_size[3])
            self.ids.image.source = self.chose_values[2]
        else:
            self.ids.label_gost_number.text = self.chose_values[0]
            self.ids.image.source = self.chose_values[1]

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def calculation_square(self):
        if self.ids.length_value.text and self.ids.width_value_1.text and self.ids.width_value_2.text:
            value = (float(self.ids.length_value.text) *
                     ((float(self.ids.width_value_1.text) + float(self.ids.width_value_2.text)) / 2)/100)
            SQUARE.append(round(value, 1))


class CalculationsAreaOfRibbed(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []

    def build_instance(self):
        if len(self.chose_values) > 2:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
            self.ids.length_value.text = str(product_size[0])
            self.ids.width_value_1.text = str(product_size[1])
            self.ids.width_value_2.text = str(product_size[2])
            self.ids.thickness_value.text = str(product_size[3])
            self.ids.image.source = self.chose_values[2]
        else:
            self.ids.label_gost_number.text = self.chose_values[0]
            self.ids.image.source = self.chose_values[1]

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def calculation_square(self):
        if self.ids.length_value.text and self.ids.width_value_1.text:
            value = (float(self.ids.length_value.text) * float(self.ids.width_value_1.text)) / 100
            SQUARE.append(round(value, 1))


class CalculationsAreaOfShaped(Popup):

    def __init__(self):
        super().__init__()
        self.chose_values = []

    def build_instance(self):
        if len(self.chose_values) > 2:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
            self.ids.length_value.text = str(product_size[0])
            self.ids.width_value_1.text = str(product_size[1])
            self.ids.width_value_2.text = str(product_size[2])
            self.ids.thickness_value.text = str(product_size[3])
            self.ids.image.source = self.chose_values[2]
        else:
            self.ids.label_gost_number.text = self.chose_values[0]
            self.ids.image.source = self.chose_values[1]

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def calculation_square(self):
        if self.ids.length_value.text and self.ids.width_value_1.text:
            value = (float(self.ids.length_value.text) * float(self.ids.width_value_1.text)) / 100
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
            value = (((pi * _D ** 2) / 4) - ((pi * d ** 2) / 4)) / 100
            SQUARE.append(round(value, 1))


class ChoosingShapeProduct(Popup):

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def choose_window(self):
        popup = None
        if self.ids.spin_choose_window.text == 'Прямоугольник':
            popup = CalculationsAreaOfRectangle()
        elif self.ids.spin_choose_window.text == 'Трапецеидальный клин':
            popup = CalculationsAreaOfTrapezoid()
            popup.chose_values.append(TRAPEZOID_1['Image'])
        elif self.ids.spin_choose_window.text == 'Ребровый клин':
            popup = CalculationsAreaOfRibbed()
            popup.chose_values.append(RIBBED['Image'])
        elif self.ids.spin_choose_window.text == 'Кольцо':
            popup = CalculationsAreaOfRing()

        popup.chose_values.insert(0, self.ids.spin_choose_window.text)
        popup.open()
