from kivy.uix.popup import Popup

from variables import GOST_STANDARDS, PARAMS, FORMS
from variables import VALUES, RECTANGLES, TUBE, TRAPEZOID, TUBE_1, FASON, \
    TRAPEZOID_1, RIBBED, RIBBED_1, RIBBED_2, RIBBED_3, END_WEDGE, END_WEDGE_2, SHAPED

from math import pi


def choice_popup(gost, number=None, size=None, weight='', volume='', square='', dad=None):
    """Opening new shape popup"""

    if gost in RECTANGLES and number in RECTANGLES[gost]:
        popup = Rectangle(dad)

    elif gost in TRAPEZOID and number in TRAPEZOID[gost]:
        popup = Trapezoid(dad)
        popup.chose_values.append(TRAPEZOID['Image'])
        popup.ids.length_label.text = 'Ширина(L), мм:'
        popup.ids.width_label.text = 'Длина(S), мм:'
        popup.ids.width_label_2.text = 'Длина(S[sub]1[/sub]), мм:'

    elif gost in TRAPEZOID_1 and number in TRAPEZOID_1[gost]:
        popup = Trapezoid(dad)
        popup.chose_values.append(TRAPEZOID_1['Image'])

    elif gost in RIBBED and number in RIBBED[gost]:
        popup = Ribbed(dad)
        popup.chose_values.append(RIBBED['Image'])

    elif gost in RIBBED_1 and number in RIBBED_1[gost]:
        popup = Ribbed(dad)
        popup.chose_values.append(RIBBED_1['Image'])

    elif gost in RIBBED_2 and number in RIBBED_2[gost]:
        popup = Ribbed(dad)
        popup.chose_values.append(RIBBED_2['Image'])
        popup.ids.width_label_H.text = 'Ширина(S), мм:'
        popup.ids.thickness_label_S.text = 'Толщина(H), мм:'
        popup.ids.thickness_label_S1.text = 'Ширина(S[sub]1[/sub]), мм:'

    elif gost in RIBBED_3 and number in RIBBED_3[gost]:
        popup = Ribbed(dad)
        popup.chose_values.append(RIBBED_3['Image'])
        popup.ids.length_label_L.text = 'Ширина(в), мм'
        popup.ids.width_label_H.text = 'Длина(б), мм:'
        popup.ids.thickness_label_S.text = 'Толщина(а), мм:'
        popup.ids.thickness_label_S1.text = 'Толщина(а[sub]1[/sub]), мм:'

    elif gost in END_WEDGE and number in END_WEDGE[gost]:
        popup = Ribbed(dad)
        popup.chose_values.append(END_WEDGE['Image'])
        popup.ids.length_label_L.text = 'Длина(в), мм'
        popup.ids.width_label_H.text = 'Ширина(б), мм:'
        popup.ids.thickness_label_S.text = 'Толщина(а), мм:'
        popup.ids.thickness_label_S1.text = 'Толщина(а[sub]1[/sub]), мм:'
        popup.title = 'Расчёт площади торцового клина'

    elif gost in END_WEDGE_2 and number in END_WEDGE_2[gost]:
        popup = Ribbed(dad)
        popup.chose_values.append(END_WEDGE_2['Image'])
        popup.title = 'Расчёт площади торцового клина'

    elif gost in SHAPED and number in SHAPED[gost]:
        popup = Shaped(dad)
        popup.chose_values.append(SHAPED['Image'])

    elif gost in TUBE and number in TUBE[gost]:
        popup = Tube(dad)
        popup.chose_values.append(TUBE['Image'])

    elif gost in TUBE_1 and number in TUBE_1[gost]:
        popup = Tube(dad)
        popup.chose_values.append(TUBE_1['Image'])

    elif gost in FASON and number in FASON[gost]:
        popup = Fason(dad)

    else:
        popup = WrongPopup()

    popup.chose_values.insert(0, gost)
    popup.chose_values.insert(1, number)
    popup.weight = weight
    if VALUES['volume_weight']:
        popup.volume_weight = VALUES['volume_weight']

    if size:
        popup.product_size = size
    if volume:
        popup.volume = volume
    if square:
        popup.square = square

    popup.open()


def change_text(dad):
    """Changing text Textinput after calculate"""

    if not VALUES:
        pass
    elif not dad:
        pass

    elif VALUES:
        if VALUES['square']:
            dad.ids.label_S_pressing_value.text = str(VALUES['square'])
        else:
            dad.ids.label_S_pressing_value.text = ''

        if VALUES['volume']:
            dad.ids.volume_label.text = 'Объём изделия: '
            dad.ids.volume_value.text = str(VALUES['volume']) + ' см[sup]3[/sup]'
        else:
            dad.ids.volume_label.text = ''
            dad.ids.volume_value.text = ''

        if VALUES['gost'] in ('Прямоугольник', 'Трапецеидальный клин',
                              'Ребровый клин', 'Кольцо', 'Фасонное изделие'):
            dad.ids.gost_text.text = VALUES['gost']
        elif VALUES['gost']:
            dad.ids.gost_text.text = 'Размеры по: ' + VALUES['gost']
        else:
            dad.ids.gost_text.text = ''

        if VALUES['number']:
            dad.ids.stamp_text.text = 'Номер изделия: '
            dad.ids.stamp_label.text = VALUES['number']
        else:
            dad.ids.stamp_text.text = ''
            dad.ids.stamp_label.text = ''

        if VALUES['volume_weight']:
            dad.ids.volume_weight.text = 'Объёмный вес: ' + VALUES['volume_weight'] + ' г/см[sup]3[/sup]'
        else:
            dad.ids.volume_weight.text = ''

        if VALUES['weight']:
            dad.ids.weight_value.text = 'Вес изделия: ' + VALUES['weight'] + 'грамм'


class SelectionOptionPopup(Popup):
    """The window of chose open popup. On gost or another shape."""

    def __init__(self, dad):
        super().__init__()
        self.dad = dad
        for i in PARAMS:
            if i not in VALUES:
                VALUES[i] = None

    def choosing_a_product_number(self):
        numbers = []
        if self.ids.gost_number.text:
            for i in GOST_STANDARDS[self.ids.gost_number.text]:
                numbers.append(str(i))
            self.ids.spin_choose_window.text = 'Номер изделия'
            self.ids.spin_choose_window.values = numbers

    def choose_window(self):
        popup = None
        if self.ids.spin_choose_window.text == 'Прямоугольник':
            popup = Rectangle(self.dad)

        elif self.ids.spin_choose_window.text == 'Трапецеидальный клин':
            popup = Trapezoid(self.dad)
            popup.chose_values.append(TRAPEZOID_1['Image'])

        elif self.ids.spin_choose_window.text == 'Ребровый клин':
            popup = Ribbed(self.dad)
            popup.chose_values.append(RIBBED['Image'])

        elif self.ids.spin_choose_window.text == 'Трубка':
            popup = Tube(self.dad)
            popup.chose_values.append(TUBE['Image'])

        elif self.ids.spin_choose_window.text == 'Произвольное':
            popup = Fason(self.dad)

        else:
            if self.ids.spin_choose_window.text != 'Номер изделия':
                choice_popup(gost=self.ids.gost_number.text,
                             number=self.ids.spin_choose_window.text, dad=self.dad)
                self.dismiss()
            else:
                pass

        if popup:
            popup.chose_values.insert(0, self.ids.spin_choose_window.text)
            popup.open()
            self.dismiss()


class WrongPopup(Popup):
    def __init__(self):
        super().__init__()
        self.chose_values = []

    def build_instance(self):
        self.ids.label_wrong.text = 'В базе пока нет изделия под № ' + \
                                    self.chose_values[1]


class RessetPopup(Popup):
    def __init__(self, instance):
        super().__init__()
        self.instance = instance

    def reset_all(self):
        self.instance.reset()


class ClosePopup(Popup):
    pass


class MistakePopup(Popup):
    pass


class Addition(Popup):

    def __init__(self, instance):
        super().__init__()
        self.instance = instance

    def write_average_value(self):
        values = []
        if self.ids.length_first.text:
            values.append(float(self.ids.length_first.text))
        if self.ids.length_second.text:
            values.append(float(self.ids.length_second.text))
        if self.ids.length_third.text:
            values.append(float(self.ids.length_third.text))

        if values:
            summ = 0
            for i in values:
                summ += i
            equals = round(summ / len(values), 1)

            self.instance.text = str(equals)


class Rectangle(Popup):
    """Shape of rectangle"""

    def __init__(self, dad):
        super().__init__()
        self.chose_values = []
        self.product_size = []
        self.weight = ''
        self.volume_weight = ''
        self.dad = dad

    def build_instance(self):
        if self.chose_values and self.product_size:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            self.ids.length_value.text = self.product_size[0]
            self.ids.width_value.text = self.product_size[1]
            if len(self.product_size) == 3:
                self.ids.thickness_value.text = self.product_size[2]
                volume = (float(self.product_size[0]) * float(self.product_size[1]) *
                          float(self.product_size[2]) / 1000)
                VALUES['volume'] = round(float(volume), 2)
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = self.chose_values[1]

        elif len(self.chose_values) > 1:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]

            if self.chose_values[0] in FORMS:
                pass
            else:
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
        if self.volume_weight:
            self.ids.volume_weight_product.text = self.volume_weight

    def return_beck(self):
        SelectionOptionPopup(self.dad).open()

    @staticmethod
    def open_calculation_average_popup(instance):
        Addition(instance).open()

    def calculation(self):

        if self.ids.length_value.text and self.ids.width_value.text:
            square = float(self.ids.length_value.text) * float(self.ids.width_value.text)
            VALUES['square'] = (round(square / 100, 1))
            VALUES['size'] = []
            VALUES['size'].append(self.ids.length_value.text)
            VALUES['size'].append(self.ids.width_value.text)

            if self.ids.thickness_value.text:
                volume = round((square * float(self.ids.thickness_value.text)) / 1000, 2)
                VALUES['volume'] = volume
                VALUES['size'].append(self.ids.thickness_value.text)

                if self.ids.weight_product.text:

                    if float(self.ids.weight_product.text) != float(VALUES['weight']):
                        volume_weight = round(float(self.ids.weight_product.text) / volume, 2)
                        VALUES['volume_weight'] = str(volume_weight)
                        self.ids.volume_weight_product.text = str(volume_weight)
                        VALUES['weight'] = self.ids.weight_product.text
                    else:
                        pass
                else:
                    VALUES['weight'] = 0

                if self.ids.volume_weight_product.text:

                    if float(self.ids.volume_weight_product.text) != float(VALUES['volume_weight']):
                        self.calculation_weight_product()
                    else:
                        pass

                else:
                    VALUES['volume_weight'] = 0

            else:
                VALUES['volume'] = 0
                VALUES['volume_weight'] = 0
                VALUES['weight'] = 0

        else:
            VALUES['square'] = 0
            VALUES['size'] = 0
            VALUES['volume'] = 0
            VALUES['volume_weight'] = 0
            VALUES['weight'] = 0

    def calculation_weight_product(self):
        if self.ids.length_value.text and self.ids.width_value.text and \
                self.ids.thickness_value.text and self.ids.volume_weight_product.text:
            l, h, s, vw = float(self.ids.length_value.text), float(self.ids.width_value.text), \
                float(self.ids.thickness_value.text), float(self.ids.volume_weight_product.text)
            volume = (l * h * s) / 1000
            var = round(vw * volume)
            self.ids.weight_product.text = str(var)
            VALUES['weight'] = str(var)
            VALUES['volume'] = volume
            VALUES['volume_weight'] = self.ids.volume_weight_product.text
            VALUES['size'] = []
            VALUES['size'].append(self.ids.length_value.text)
            VALUES['size'].append(self.ids.width_value.text)
            VALUES['size'].append(self.ids.thickness_value.text)

    def check_value(self, var):

        text = None

        def check():
            if not self.ids.length_value.text:
                _text = 'Укажите длину изделия!'
            elif not self.ids.width_value.text:
                _text = 'Укажите ширину изделия!'
            elif not self.ids.thickness_value.text:
                _text = 'Укажите толщину изделия!'
            else:
                _text = None
            return _text

        if var == 1:
            if not self.ids.weight_product.text:
                text = 'Укажите вес изделия!'
            else:
                text = check()

        elif var == 2:
            if not self.ids.volume_weight_product.text:
                text = 'Укажите объёмный вес!'
            else:
                text = check()

        if text:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = text
            mistake.open()

    def change_text_weight_product(self):
        if VALUES['weight']:
            self.ids.weight_product.text = VALUES['weight']

    def change_text(self):
        change_text(self.dad)


class Trapezoid(Popup):
    """Shape of trapezoid"""

    def __init__(self, dad):
        super().__init__()
        self.chose_values = []
        self.product_size = []
        self.weight = ''
        self.volume_weight = ''
        self.dad = dad

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
            if self.chose_values[0] in FORMS:
                self.ids.image.source = self.chose_values[2]
            else:
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
        if self.volume_weight:
            self.ids.volume_weight_product.text = self.volume_weight

    def return_beck(self):
        SelectionOptionPopup(self.dad).open()

    @staticmethod
    def open_calculation_average_popup(instance):
        Addition(instance).open()

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
                volume = round((square * float(self.ids.thickness_value.text)) / 1000, 2)
                VALUES['volume'] = volume
                VALUES['size'].append(self.ids.thickness_value.text)

                if self.ids.weight_product.text:

                    if float(self.ids.weight_product.text) != float(VALUES['weight']):
                        volume_weight = round(float(self.ids.weight_product.text) / volume, 2)
                        self.ids.volume_weight_product.text = str(volume_weight)
                        VALUES['volume_weight'] = str(volume_weight)
                        VALUES['weight'] = self.ids.weight_product.text

                    else:
                        pass
                else:
                    VALUES['weight'] = 0

                if self.ids.volume_weight_product.text:

                    if float(self.ids.volume_weight_product.text) != VALUES['volume_weight']:
                        self.calculation_weight_product()
                    else:
                        pass

                else:
                    VALUES['volume_weight'] = 0

            else:
                VALUES['volume'] = 0
                VALUES['volume_weight'] = 0
                VALUES['weight'] = 0

        else:
            VALUES['square'] = 0
            VALUES['size'] = 0
            VALUES['volume'] = 0
            VALUES['volume_weight'] = 0
            VALUES['weight'] = 0

    def calculation_weight_product(self):

        if self.ids.length_value.text and self.ids.width_value_1.text and \
                self.ids.width_value_2.text and self.ids.thickness_value.text and self.ids.volume_weight_product.text:
            l, s, s_1, h, v = float(self.ids.length_value.text), \
                float(self.ids.width_value_1.text), \
                float(self.ids.width_value_2.text), \
                float(self.ids.thickness_value.text), \
                float(self.ids.volume_weight_product.text)
            volume = round(((l * ((s + s_1) / 2)) * h) / 1000, 2)
            var = round(v * volume)
            self.ids.weight_product.text = str(var)
            VALUES['weight'] = str(var)
            VALUES['volume'] = volume
            VALUES['volume_weight'] = self.ids.volume_weight_product.text
            VALUES['size'] = []
            VALUES['size'].append(self.ids.length_value.text)
            VALUES['size'].append(self.ids.width_value_1.text)
            VALUES['size'].append(self.ids.width_value_2.text)
            VALUES['size'].append(self.ids.thickness_value.text)

    def check_value(self, var):

        text = ''

        def check():
            if not self.ids.length_value.text:
                _text = 'Укажите длину(L)!'
            elif not self.ids.width_value_1.text:
                _text = 'Укажите ширину(S)!'
            elif not self.ids.width_value_2.text:
                _text = 'Укажите ширину(S[sub]1[/sub])!'
            elif not self.ids.thickness_value.text:
                _text = 'Укажите толщину(H)!'
            else:
                _text = ''
            return _text

        if var == 1:
            if not self.ids.weight_product.text:
                text = 'Укажите вес изделия!'
            else:
                text = check()

        elif var == 2:
            if not self.ids.volume_weight_product.text:
                text = 'Укажите объёмный вес!'
            else:
                text = check()

        if text:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = text
            mistake.open()

    def change_text(self):
        change_text(self.dad)


class Ribbed(Popup):
    """Shape of ribbed"""

    def __init__(self, dad):
        super().__init__()
        self.chose_values = []
        self.product_size = []
        self.weight = ''
        self.volume_weight = ''
        self.dad = dad

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
            if self.chose_values[0] in FORMS:
                self.ids.image.source = self.chose_values[2]
            else:
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
        if self.volume_weight:
            self.ids.volume_weight_product.text = self.volume_weight

    def return_beck(self):
        SelectionOptionPopup(self.dad).open()

    @staticmethod
    def open_calculation_average_popup(instance):
        Addition(instance).open()

    def calculation(self):
        if self.ids.length_value.text and self.ids.width_value.text:
            square = (float(self.ids.length_value.text) * float(self.ids.width_value.text))
            VALUES['square'] = (round(square / 100, 1))
            VALUES['size'] = []
            VALUES['size'].append(self.ids.length_value.text)
            VALUES['size'].append(self.ids.width_value.text)

            if self.ids.thickness_value_1.text and self.ids.thickness_value_2.text:
                volume = round((square * ((float(self.ids.thickness_value_1.text) +
                                           float(self.ids.thickness_value_2.text)) / 2)) / 1000, 2)
                VALUES['volume'] = volume
                VALUES['size'].append(self.ids.thickness_value_1.text)
                VALUES['size'].append(self.ids.thickness_value_2.text)

                if self.ids.weight_product.text:

                    if float(self.ids.weight_product.text) != float(VALUES['weight']):
                        volume_weight = round(float(self.ids.weight_product.text) / volume, 2)
                        self.ids.volume_weight_product.text = str(volume_weight)
                        VALUES['volume_weight'] = str(volume_weight)
                        VALUES['weight'] = self.ids.weight_product.text
                    else:
                        pass
                else:
                    VALUES['weight'] = 0

                if self.ids.volume_weight_product.text:

                    if float(self.ids.volume_weight_product.text) != float(VALUES['volume_weight']):
                        self.calculation_weight_product()
                    else:
                        pass
                else:
                    VALUES['volume_weight'] = 0

            else:
                VALUES['volume'] = 0
                VALUES['volume_weight'] = 0
                VALUES['weight'] = 0

        else:
            VALUES['square'] = 0
            VALUES['size'] = 0
            VALUES['volume'] = 0
            VALUES['volume_weight'] = 0
            VALUES['weight'] = 0

    def calculation_weight_product(self):

        if self.ids.length_value.text and self.ids.width_value.text and \
                self.ids.thickness_value_1.text and self.ids.thickness_value_2.text and \
                self.ids.volume_weight_product.text:
            l, h, s, s_1, v = float(self.ids.length_value.text), \
                float(self.ids.width_value.text), \
                float(self.ids.thickness_value_1.text), \
                float(self.ids.thickness_value_2.text), \
                float(self.ids.volume_weight_product.text)
            volume = round(((l * h) * ((s + s_1) / 2)) / 1000, 2)
            var = round(v * volume)
            self.ids.weight_product.text = str(var)
            VALUES['weight'] = str(var)
            VALUES['volume'] = volume
            VALUES['volume_weight'] = self.ids.volume_weight_product.text
            VALUES['size'] = []
            VALUES['size'].append(self.ids.length_value.text)
            VALUES['size'].append(self.ids.width_value.text)
            VALUES['size'].append(self.ids.thickness_value_1.text)
            VALUES['size'].append(self.ids.thickness_value_2.text)

    def check_value(self, var):

        text = None

        def check():
            if not self.ids.length_value.text:
                _text = 'Укажите длину(L)!'
            elif not self.ids.width_value.text:
                _text = 'Укажите ширину(H)!'
            elif not self.ids.thickness_value_1.text:
                _text = 'Укажите толщину(S)!'
            elif not self.ids.thickness_value_2.text:
                _text = 'Укажите толщину(S[sub]1[/sub])!'
            else:
                _text = None
            return _text

        if var == 1:
            if not self.ids.weight_product.text:
                text = 'Укажите вес изделия!'
            else:
                text = check()

        elif var == 2:
            if not self.ids.volume_weight_product.text:
                text = 'Укажите объёмный вес!'
            else:
                text = check()

        if text:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = text
            mistake.open()

    def change_text(self):
        change_text(self.dad)


class Tube(Popup):
    """Shape of tube"""

    def __init__(self, dad):
        super().__init__()
        self.chose_values = []
        self.product_size = []
        self.weight = ''
        self.volume_weight = ''
        self.dad = dad

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
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            if self.chose_values[0] in FORMS:
                self.ids.image.source = self.chose_values[2]
            else:
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

        if self.volume_weight:
            self.ids.volume_weight_product.text = self.volume_weight

    def return_beck(self):
        SelectionOptionPopup(self.dad).open()

    @staticmethod
    def open_calculation_average_popup(instance):
        Addition(instance).open()

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
                volume = round((square * float(self.ids.length_value.text)) / 1000, 2)
                VALUES['volume'] = volume
                VALUES['size'].append(self.ids.length_value.text)

                if self.ids.weight_product.text:

                    volume_weight = round(float(self.ids.weight_product.text) / volume, 2)
                    VALUES['volume_weight'] = str(volume_weight)
                    VALUES['weight'] = self.ids.weight_product.text
                    self.ids.volume_weight_product.text = str(volume_weight)
                elif self.ids.volume_weight_product.text:
                    VALUES['volume_weight'] = self.ids.volume_weight_product.text
                    VALUES['weight'] = None
                else:
                    VALUES['volume_weight'] = None
                    VALUES['weight'] = None

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

    def calculation_weight_product(self):
        pass
        if self.ids.outer_diameter_D.text and self.ids.inner_diameter_d.text and \
                self.ids.length_value.text and self.ids.volume_weight_product.text:
            _d, d, l, v = float(self.ids.outer_diameter_D.text), float(self.ids.inner_diameter_d.text), \
                float(self.ids.length_value.text), float(self.ids.volume_weight_product.text)
            volume = round((((pi * (_d / 2) ** 2) - (pi * (d / 2) ** 2)) * l) / 1000, 2)
            var = round(v * volume)
            self.ids.weight_product.text = str(var)
            VALUES['weight'] = str(var)
            VALUES['volume'] = volume
            VALUES['volume_weight'] = self.ids.volume_weight_product.text
            VALUES['size'] = []
            VALUES['size'].append(self.ids.outer_diameter_D.text)
            VALUES['size'].append(self.ids.inner_diameter_d.text)
            VALUES['size'].append(self.ids.length_value.text)

    def check_value(self, var):

        text = None

        def check():
            if not self.ids.outer_diameter_D.text:
                _text = 'Укажите наружный диаметр!'
            elif not self.ids.inner_diameter_d.text:
                _text = 'Укажите внутренний диаметр!'
            elif not self.ids.length_value.text:
                _text = 'Укажите высоту изделия!'
            else:
                _text = None
            return _text

        if var == 1:
            if not self.ids.weight_product.text:
                text = 'Укажите вес изделия!'
            else:
                text = check()

        elif var == 2:
            if not self.ids.volume_weight_product.text:
                text = 'Укажите объёмный вес!'
            else:
                text = check()

        if text:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = text
            mistake.open()

    def change_text(self):
        change_text(self.dad)


class Shaped(Popup):
    """Shape of shaped"""

    def __init__(self, dad):
        super().__init__()
        self.chose_values = []
        self.product_size = []
        self.weight = ''
        self.volume_weight = ''
        self.dad = dad

    def build_instance(self):

        if self.chose_values and self.product_size:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            self.ids.length_value.text = self.product_size[0]
            self.ids.width_value_1.text = self.product_size[1]
            self.ids.width_value_2.text = self.product_size[2]

            if len(self.product_size) == 7:
                self.ids.thickness_value_S.text = self.product_size[3]
                self.ids.thickness_value_S1.text = self.product_size[4]
                self.ids.thickness_value_S2.text = self.product_size[5]
                self.ids.thickness_value_S3.text = self.product_size[6]
            self.ids.image.source = self.chose_values[2]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = self.chose_values[1]

        elif len(self.chose_values) > 2:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            if self.chose_values[0] in FORMS:
                self.ids.image.source = self.chose_values[2]
            else:
                product_size = GOST_STANDARDS[self.chose_values[0]][self.chose_values[1]]
                self.ids.length_value.text = str(product_size[0])
                self.ids.width_value_1.text = str(product_size[1])
                self.ids.width_value_2.text = str(product_size[2])
                self.ids.thickness_value_S.text = str(product_size[3])
                self.ids.thickness_value_S1.text = str(product_size[4])
                self.ids.thickness_value_S2.text = str(product_size[5])
                self.ids.thickness_value_S3.text = str(product_size[6])
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
        if self.volume_weight:
            self.ids.volume_weight_product.text = self.volume_weight

    def return_beck(self):
        SelectionOptionPopup(self.dad).open()

    @staticmethod
    def open_calculation_average_popup(instance):
        Addition(instance).open()

    def calculation(self):
        if self.ids.length_value.text and self.ids.width_value_1.text and self.ids.width_value_1.text:
            square = (float(self.ids.length_value.text) *
                      ((float(self.ids.width_value_1.text) + float(self.ids.width_value_2.text)) / 2))
            VALUES['square'] = (round(square / 100, 1))
            VALUES['size'] = []
            VALUES['size'].append(self.ids.length_value.text)
            VALUES['size'].append(self.ids.width_value_1.text)
            VALUES['size'].append(self.ids.width_value_2.text)

            if self.ids.thickness_value_S.text and self.ids.thickness_value_S1.text \
                    and self.ids.thickness_value_S2.text and self.ids.thickness_value_S3.text:
                average_value = (float(self.ids.thickness_value_S.text)
                                 + float(self.ids.thickness_value_S1.text)
                                 + float(self.ids.thickness_value_S2.text)
                                 + float(self.ids.thickness_value_S3.text)) / 4
                volume = (square * average_value) / 1000
                VALUES['volume'] = (round(volume, 2))
                VALUES['size'].append(self.ids.thickness_value_S.text)
                VALUES['size'].append(self.ids.thickness_value_S1.text)
                VALUES['size'].append(self.ids.thickness_value_S2.text)
                VALUES['size'].append(self.ids.thickness_value_S3.text)

                if self.ids.weight_product.text:
                    volume_weight = round(float(self.ids.weight_product.text) / volume, 2)
                    self.ids.volume_weight_product.text = str(volume_weight)
                    VALUES['volume_weight'] = str(volume_weight)
                    VALUES['weight'] = self.ids.weight_product.text
                else:
                    VALUES['volume_weight'] = None
                    VALUES['weight'] = None

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

    def calculation_weight_product(self):
        if self.ids.length_value.text and self.ids.width_value_1.text and \
                self.ids.width_value_2.text and \
                self.ids.thickness_value_S.text and self.ids.thickness_value_S1.text \
                and self.ids.thickness_value_S2.text and self.ids.thickness_value_S3.text:
            l, h, h_1, s, s_1, s_2, s_3, v = float(self.ids.length_value.text), \
                float(self.ids.width_value_1.text), \
                float(self.ids.width_value_2.text), \
                float(self.ids.thickness_value_S.text), \
                float(self.ids.thickness_value_S1.text),\
                float(self.ids.thickness_value_S2.text),\
                float(self.ids.thickness_value_S3.text),\
                float(self.ids.volume_weight_product.text)
            volume = round((l * ((h + h_1) / 2) * ((s + s_1 + s_2 + s_3) / 4)) / 1000, 2)
            var = round(v * volume)
            self.ids.weight_product.text = str(var)
            VALUES['weight'] = str(var)
            VALUES['volume'] = volume
            VALUES['volume_weight'] = self.ids.volume_weight_product.text
            VALUES['size'] = []
            VALUES['size'].append(self.ids.length_value.text)
            VALUES['size'].append(self.ids.width_value_1.text)
            VALUES['size'].append(self.ids.width_value_2.text)
            VALUES['size'].append(self.ids.thickness_value_S.text)
            VALUES['size'].append(self.ids.thickness_value_S1.text)
            VALUES['size'].append(self.ids.thickness_value_S2.text)
            VALUES['size'].append(self.ids.thickness_value_S3.text)

    def check_value(self, var):

        text = None

        def check():
            if not self.ids.length_value.text:
                _text = 'Укажите длину(L)!'
            elif not self.ids.width_value_1.text:
                _text = 'Укажите ширину(H)!'
            elif not self.ids.width_value_2.text:
                _text = 'Укажите ширину(H[sub]1[/sub])!'
            elif not self.ids.thickness_value_S.text:
                _text = 'Укажите толщину(S)!'
            elif not self.ids.thickness_value_S1.text:
                _text = 'Укажите толщину(S[sub]1[/sub])!'
            elif not self.ids.thickness_value_S2.text:
                _text = 'Укажите толщину(S[sub]2[/sub])!'
            elif not self.ids.thickness_value_S3.text:
                _text = 'Укажите толщину(S[sub]3[/sub])!'
            else:
                _text = None
            return _text

        if var == 1:
            if not self.ids.weight_product.text:
                text = 'Укажите вес изделия!'
            else:
                text = check()

        elif var == 2:
            if not self.ids.volume_weight_product.text:
                text = 'Укажите объёмный вес!'
            else:
                text = check()

        if text:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = text
            mistake.open()

    def change_text(self):
        change_text(self.dad)


class Fason(Popup):
    def __init__(self, dad):
        super().__init__()
        self.chose_values = []
        self.product_size = []
        self.weight = ''
        self.volume = ''
        self.square = ''
        self.dad = dad

    def build_instance(self):

        if self.volume:
            self.ids.volume_product.text = self.volume

        if self.weight:
            self.ids.weight_product.text = self.weight

        if self.square:
            self.ids.square_product.text = self.square

        if len(self.chose_values) > 1:
            self.ids.label_gost_number.text = self.chose_values[0] + ' № ' + self.chose_values[1]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = self.chose_values[1]
        else:
            self.ids.label_gost_number.text = self.chose_values[0]
            VALUES['gost'] = self.chose_values[0]
            VALUES['number'] = 'Не определён.'

    def return_beck(self):
        SelectionOptionPopup(self.dad).open()

    def calculation(self):
        if self.ids.square_product.text:
            VALUES['square'] = self.ids.square_product.text
        else:
            VALUES['square'] = 0

        if self.ids.volume_product.text and self.ids.weight_product.text:
            volume_weight = round(float(self.ids.weight_product.text)
                                  / float(self.ids.volume_product.text), 2)
            VALUES['volume'] = self.ids.volume_product.text
            VALUES['volume_weight'] = str(volume_weight)
            VALUES['weight'] = self.ids.weight_product.text

        else:
            VALUES['volume_weight'] = None
            VALUES['weight'] = None
            VALUES['volume'] = None

        if self.ids.volume_product.text:
            VALUES['volume'] = self.ids.volume_product.text
        else:
            VALUES['volume'] = None

        if self.ids.weight_product.text:
            VALUES['weight'] = self.ids.weight_product.text
        else:
            VALUES['weight'] = None

        VALUES['size'] = 0

    def change_text(self):
        change_text(self.dad)
