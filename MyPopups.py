from kivy.uix.popup import Popup
from variables import GOST_STANDARDS
from variables import VALUES, RECTANGLES, TUBE, TRAPEZOID, \
    TRAPEZOID_1, RIBBED, RIBBED_1, RIBBED_2, RIBBED_3, END_WEDGE, END_WEDGE_2, SHAPED
from math import pi

# TODO reformat this function (Вынести все значения в модуль variables, оставить цикл
def choice_popup(gost, number=None, size=None, weight=''):
    if gost in RECTANGLES and number in RECTANGLES[gost]:
        popup = Rectangle()

    elif gost in TRAPEZOID and number in TRAPEZOID[gost]:
        popup = Trapezoid()
        popup.chose_values.append(TRAPEZOID['Image'])
        popup.ids.length_label.text = 'Ширина(L), мм:'
        popup.ids.width_label.text = 'Длина(S), мм:'
        popup.ids.width_label_2.text = 'Длина(S[sub]1[/sub]), мм:'

    elif gost in TRAPEZOID_1 and number in TRAPEZOID_1[gost]:
        popup = Trapezoid()
        popup.chose_values.append(TRAPEZOID_1['Image'])

    elif gost in RIBBED and number in RIBBED[gost]:
        popup = Ribbed()
        popup.chose_values.append(RIBBED['Image'])

    elif gost in RIBBED_1 and number in RIBBED_1[gost]:
        popup = Ribbed()
        popup.chose_values.append(RIBBED_1['Image'])

    elif gost in RIBBED_2 and number in RIBBED_2[gost]:
        popup = Ribbed()
        popup.chose_values.append(RIBBED_2['Image'])
        popup.ids.width_label_H.text = 'Ширина(S), мм:'
        popup.ids.thickness_label_S.text = 'Толщина(H), мм:'
        popup.ids.thickness_label_S1.text = 'Ширина(S[sub]1[/sub]), мм:'

    elif gost in RIBBED_3 and number in RIBBED_3[gost]:
        popup = Ribbed()
        popup.chose_values.append(RIBBED_3['Image'])
        popup.ids.length_label_L.text = 'Ширина(в), мм'
        popup.ids.width_label_H.text = 'Длина(б), мм:'
        popup.ids.thickness_label_S.text = 'Толщина(а), мм:'
        popup.ids.thickness_label_S1.text = 'Толщина(а[sub]1[/sub]), мм:'

    elif gost in END_WEDGE and number in END_WEDGE[gost]:
        popup = Ribbed()
        popup.chose_values.append(END_WEDGE['Image'])
        popup.ids.length_label_L.text = 'Длина(в), мм'
        popup.ids.width_label_H.text = 'Ширина(б), мм:'
        popup.ids.thickness_label_S.text = 'Толщина(а), мм:'
        popup.ids.thickness_label_S1.text = 'Толщина(а[sub]1[/sub]), мм:'
        popup.title = 'Расчёт площади торцового клина'

    elif gost in END_WEDGE_2 and number in END_WEDGE_2[gost]:
        popup = Ribbed()
        popup.chose_values.append(END_WEDGE_2['Image'])
        popup.title = 'Расчёт площади торцового клина'

    elif gost in SHAPED and number in SHAPED[gost]:
        popup = CalculationsAreaOfShaped()

    elif gost in TUBE and number in TUBE[gost]:
        popup = Tube()
        popup.chose_values.append(TUBE['Image'])

    else:
        popup = WrongPopup()

    popup.chose_values.insert(0, gost)
    popup.chose_values.insert(1, number)
    popup.weight = weight
    if size:
        popup.product_size = size

    popup.open()


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
        choice_popup(gost=self.ids.gost_number.text,
                     number=self.ids.product_numbers.text)


class ChoosingShapeProduct(Popup):

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def choose_window(self):
        popup = None
        if self.ids.spin_choose_window.text == 'Прямоугольник':
            popup = Rectangle()
        elif self.ids.spin_choose_window.text == 'Трапецеидальный клин':
            popup = Trapezoid()
            popup.chose_values.append(TRAPEZOID_1['Image'])
        elif self.ids.spin_choose_window.text == 'Ребровый клин':
            popup = Ribbed()
            popup.chose_values.append(RIBBED['Image'])
        elif self.ids.spin_choose_window.text == 'Трубка':
            popup = Tube()
            popup.chose_values.append(TUBE['Image'])

        popup.chose_values.insert(0, self.ids.spin_choose_window.text)
        popup.open()


class WrongPopup(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []

    def build_instance(self):
        self.ids.label_wrong.text = 'В базе пока нет изделия под № ' + \
                                    self.chose_values[1]


class RessetPopup(Popup):
    pass


class Rectangle(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []
        self.product_size = []
        self.weight = ''

    def build_instance(self):
        if self.chose_values and self.product_size:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            self.ids.length_value.text = self.product_size[0]
            self.ids.width_value.text = self.product_size[1]
            self.ids.thickness_value.text = self.product_size[2]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = self.chose_values[1]

        elif len(self.chose_values) > 1:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
            self.ids.length_value.text = str(product_size[0])
            self.ids.width_value.text = str(product_size[1])
            self.ids.thickness_value.text = str(product_size[2])
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = self.chose_values[1]
        else:
            self.ids.label_gost_number.text = self.chose_values[0]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = 'Не определён.'

        if self.weight:
            self.ids.weight_product.text = self.weight

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def calculation(self):

        if self.ids.length_value.text and self.ids.width_value.text:
            square = float(self.ids.length_value.text) * float(self.ids.width_value.text)
            VALUES['square'] = (round(square / 100, 1))
            VALUES['size'] = []
            VALUES['size'].append(self.ids.length_value.text)
            VALUES['size'].append(self.ids.width_value.text)

            if self.ids.thickness_value.text:
                volume = (square * float(self.ids.thickness_value.text)) / 1000
                VALUES['volume'] = (round(volume, 2))
                VALUES['size'].append(self.ids.thickness_value.text)

                if self.ids.weight_product.text:
                    volume_weight = round((float(self.ids.weight_product.text) * 1000) / volume, 2)
                    VALUES['volume_weight'] = str(volume_weight)
                    VALUES['weight'] = self.ids.weight_product.text
                else:
                    VALUES['volume_weight'] = None
                    VALUES['weight'] = None
                print(VALUES)

            else:
                VALUES['volume'] = None
                VALUES['volume_weight'] = None
                VALUES['weight'] = None

        else:
            VALUES['square'] = 0
            VALUES['size'] = 0
            VALUES['volume'] = 0
            VALUES['volume_weight'] = None
            VALUES['weight'] = None


class Trapezoid(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []
        self.product_size = []
        self.weight = ''

    def build_instance(self):
        if self.chose_values and self.product_size:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            self.ids.length_value.text = self.product_size[0]
            self.ids.width_value_1.text = self.product_size[1]
            self.ids.width_value_2.text = self.product_size[2]
            if len(self.product_size) == 4:
                self.ids.thickness_value.text = self.product_size[3]
            self.ids.image.source = self.chose_values[2]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = self.chose_values[1]

        elif len(self.chose_values) > 2:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
            self.ids.length_value.text = str(product_size[0])
            self.ids.width_value_1.text = str(product_size[1])
            self.ids.width_value_2.text = str(product_size[2])
            self.ids.thickness_value.text = str(product_size[3])
            self.ids.image.source = self.chose_values[2]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = self.chose_values[1]
        else:
            self.ids.label_gost_number.text = self.chose_values[0]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = 'Не определён.'
            self.ids.image.source = self.chose_values[1]

        if self.weight:
            self.ids.weight_product.text = self.weight

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def calculation(self):
        if self.ids.length_value.text and self.ids.width_value_1.text and self.ids.width_value_2.text:
            square = (float(self.ids.length_value.text) *
                      ((float(self.ids.width_value_1.text) + float(self.ids.width_value_2.text)) / 2))
            VALUES['square'] = (round(square / 100, 1))
            VALUES['size'] = []
            VALUES['size'].append(self.ids.length_value.text)
            VALUES['size'].append(self.ids.width_value_1.text)
            VALUES['size'].append(self.ids.width_value_2.text)

            if self.ids.thickness_value.text:
                volume = (square * float(self.ids.thickness_value.text)) / 1000
                VALUES['volume'] = (round(volume, 2))
                VALUES['size'].append(self.ids.thickness_value.text)
                print(square, volume)

                if self.ids.weight_product.text:
                    volume_weight = round((float(self.ids.weight_product.text) * 1000) / volume, 2)
                    VALUES['volume_weight'] = str(volume_weight)
                    VALUES['weight'] = self.ids.weight_product.text
                else:
                    VALUES['volume_weight'] = None
                    VALUES['weight'] = None
                print(VALUES)

            else:
                VALUES['volume'] = None
                VALUES['volume_weight'] = None
                VALUES['weight'] = None

        else:
            VALUES['square'] = 0
            VALUES['size'] = 0
            VALUES['volume'] = 0
            VALUES['volume_weight'] = None
            VALUES['weight'] = None


class Ribbed(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []
        self.product_size = []
        self.weight = ''

    def build_instance(self):

        if self.chose_values and self.product_size:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            self.ids.length_value.text = self.product_size[0]
            self.ids.width_value.text = self.product_size[1]

            if len(self.product_size) == 4:
                self.ids.thickness_value_1.text = self.product_size[2]
                self.ids.thickness_value_2.text = self.product_size[3]
            self.ids.image.source = self.chose_values[2]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = self.chose_values[1]

        elif len(self.chose_values) > 2:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
            self.ids.length_value.text = str(product_size[0])
            self.ids.width_value.text = str(product_size[1])
            self.ids.thickness_value_1.text = str(product_size[2])
            self.ids.thickness_value_2.text = str(product_size[3])
            self.ids.image.source = self.chose_values[2]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = self.chose_values[1]

        else:
            self.ids.label_gost_number.text = self.chose_values[0]
            self.ids.image.source = self.chose_values[1]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = 'Не определён.'

        if self.weight:
            self.ids.weight_product.text = self.weight

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def calculation(self):
        if self.ids.length_value.text and self.ids.width_value.text:
            square = (float(self.ids.length_value.text) * float(self.ids.width_value.text))
            VALUES['square'] = (round(square / 100, 1))
            VALUES['size'] = []
            VALUES['size'].append(self.ids.length_value.text)
            VALUES['size'].append(self.ids.width_value.text)

            if self.ids.thickness_value_1.text and self.ids.thickness_value_2.text:
                volume = (square * ((float(self.ids.thickness_value_1.text) +
                                     float(self.ids.thickness_value_2.text)) / 2)) / 1000
                VALUES['volume'] = (round(volume, 2))
                VALUES['size'].append(self.ids.thickness_value_1.text)
                VALUES['size'].append(self.ids.thickness_value_2.text)
                print(square, volume)

                if self.ids.weight_product.text:
                    volume_weight = round((float(self.ids.weight_product.text) * 1000) / volume, 2)
                    VALUES['volume_weight'] = str(volume_weight)
                    VALUES['weight'] = self.ids.weight_product.text
                else:
                    VALUES['volume_weight'] = None
                    VALUES['weight'] = None
                print(VALUES)

            else:
                VALUES['volume'] = None
                VALUES['volume_weight'] = None
                VALUES['weight'] = None

        else:
            VALUES['square'] = 0
            VALUES['size'] = 0
            VALUES['volume'] = 0
            VALUES['volume_weight'] = None
            VALUES['weight'] = None


class Tube(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []
        self.product_size = []
        self.weight = ''

    def build_instance(self):

        if self.chose_values and self.product_size:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            self.ids.outer_diameter_D.text = self.product_size[0]
            self.ids.inner_diameter_d.text = self.product_size[1]

            if len(self.product_size) == 3:
                self.ids.length_value.text = self.product_size[2]
            self.ids.image.source = self.chose_values[2]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = self.chose_values[1]

        elif len(self.chose_values) > 2:
            self.ids.label_gost_number.text = self.chose_values[0] + ' ' + self.chose_values[1]
            product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
            self.ids.outer_diameter_D.text = str(product_size[0])
            self.ids.inner_diameter_d.text = str(product_size[1])
            self.ids.length_value.text = str(product_size[2])
            self.ids.image.source = self.chose_values[2]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = self.chose_values[1]

        else:
            self.ids.label_gost_number.text = self.chose_values[0]
            self.ids.image.source = self.chose_values[1]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = 'Не определён.'

        if self.weight:
            self.ids.weight_product.text = self.weight

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def calculation(self):
        if self.ids.outer_diameter_D.text and self.ids.inner_diameter_d.text:
            _D = float(self.ids.outer_diameter_D.text)
            d = float(self.ids.inner_diameter_d.text)
            square = ((pi * (_D / 2) ** 2) - (pi * (d / 2) ** 2))
            VALUES['square'] = (round(square / 100, 1))
            VALUES['size'] = []
            VALUES['size'].append(self.ids.outer_diameter_D.text)
            VALUES['size'].append(self.ids.inner_diameter_d.text)

            if self.ids.length_value.text:
                volume = (square * float(self.ids.length_value.text)) / 1000
                VALUES['volume'] = (round(volume, 2))
                VALUES['size'].append(self.ids.length_value.text)
                print(square, volume)

                if self.ids.weight_product.text:
                    volume_weight = round((float(self.ids.weight_product.text) * 1000) / volume, 2)
                    VALUES['volume_weight'] = str(volume_weight)
                    VALUES['weight'] = self.ids.weight_product.text
                else:
                    VALUES['volume_weight'] = None
                    VALUES['weight'] = None
                print(VALUES)

            else:
                VALUES['volume'] = None
                VALUES['volume_weight'] = None
                VALUES['weight'] = None

        else:
            VALUES['square'] = 0
            VALUES['size'] = 0
            VALUES['volume'] = 0
            VALUES['volume_weight'] = None
            VALUES['weight'] = None


class CalculationsAreaOfShaped(Popup):

    def __init__(self):
        super().__init__()
        self.chose_values = []

        self.weight = ''

    def build_instance(self):
        if len(self.chose_values) > 1:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
            self.ids.length_value.text = str(product_size[0])
            self.ids.width_value_1.text = str(product_size[1])
            self.ids.width_value_2.text = str(product_size[2])
            self.ids.thickness_value_S.text = str(product_size[3])
            self.ids.thickness_value_S1.text = str(product_size[4])
            self.ids.thickness_value_S2.text = str(product_size[5])
            self.ids.thickness_value_S3.text = str(product_size[6])
            # self.ids.image.source = self.chose_values[2]
        else:
            self.ids.label_gost_number.text = self.chose_values[0]
            # self.ids.image.source = self.chose_values[1]

    @staticmethod
    def return_beck():
        SelectionOptionPopup().open()

    def calculation_square(self):
        if self.ids.length_value.text and self.ids.width_value_1.text:
            value = (float(self.ids.length_value.text) * float(self.ids.width_value_1.text)) / 100
            VALUES['square'] = (round(value, 1))
