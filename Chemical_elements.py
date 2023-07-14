from copy import deepcopy

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader

from variables import CHEMICAL_COMPONENTS, CHEMICAL_ELEMENTS
from MyPopups import MistakePopup, RessetPopup


class Box(BoxLayout):

    def __init__(self, instance):
        super().__init__()
        self.instance = instance

    def change_value(self):
        if self.ids.value_element.text == \
                self.instance.COMPONENTS[self.instance.component.name][self.ids.name_element.text]:
            pass
        else:
            self.instance.COMPONENTS[self.instance.component.name][self.ids.name_element.text] = \
                self.ids.value_element.text


class Box2(BoxLayout):
    pass


class Box3(BoxLayout):
    pass


class BigBox(BoxLayout):

    """big box for output information about chemical element,
    kv version Located in Element_info.kv file"""

    pass


class BigBoxResult(BoxLayout):
    pass


class BoxForElement(BoxLayout):

    """Class includes all widgets for displays parameters component:
     component.name
     component.chemical_composition
     KV code located in Chemical_element.kv file"""

    sound_wrong = SoundLoader.load('sounds/sound_wrong.mp3')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.component = None
        self.dad = None

    def open_component(self):
        try:

            if self.component:
                self.dad.ids.box_result.clear_widgets()

                CHEMICAL_COMPONENTS[self.component.name] = self.component.chemical_composition
                if self.dad.color:
                    element = AddComponent(self.dad, self, number_component=self.number_component, color=self.dad.color)
                else:
                    element = AddComponent(self.dad, self, number_component=self.number_component)
                element.component = self.component
                element.title = 'Корректировка компонента'
                element.ids.spinner_component.text = self.component.name
                element.ids.spinner_component.values = self.dad.components_for_spinner
                element.ids.content_value.text = self.dad.composition.mixture[self.component]
                element.ids.btn_add.text = 'Внести корректировку'

                element.ids.box_id.add_widget(MyAnchor(element))
                element.ids.btn_id.size_hint = [0.6, 0.8]
                self.dad.sound_open_component.play()

                element.open()
            else:
                self.sound_wrong.play()

        except AttributeError:
            print('Ошибка!!!')
            self.sound_wrong.play()


class MyAnchor(AnchorLayout):
    """Class includes button 'Удалить элемент'
     KV code located in Chemical_element.kv file"""
    def __init__(self, element):
        super().__init__()
        self.element = element

    def dell_component(self):

        """Calling RessetPopup"""

        reset_popup = RessetPopup(self)
        reset_popup.title = 'Подтвердите удаление элемента'
        reset_popup.ids.btn_res.text = 'УДАЛИТЬ!!!'
        reset_popup.ids.warning_text.text = 'При подтверждении будет удалён \nкомпонент из состава!'
        reset_popup.open()

    def reset(self):

        del self.element.dad.composition.mixture[self.element.component]
        self.element.widget.component = None

        self.element.widget.clear_widgets()
        k = 0
        for i in self.element.dad.composition.mixture:
            if k == 0:
                self.element.dad.composition.name = i.name
                self.element.dad.composition.ratio = str(self.element.dad.composition.mixture[i])
                k += 1
            else:
                self.element.dad.composition.name += ':' + i.name
                self.element.dad.composition.ratio += ':' + str(self.element.dad.composition.mixture[i])

        self.element.dad.sound_del_component.play()
        self.element.dismiss()


class ResetButton(Button):
    pass


class CalcButton(Button):
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
        self.names = []
        self.ratio = ''
        self.content = None

    def __str__(self):
        return f'{self.name}, {self.ratio}, {self.names}, {self.mixture}'


class AddComponent(Popup):
    """Popup for adding Chemical element for composition of mixture"""

    def __init__(self, fourth, widget, number_component=None, color=None, **kwargs):
        super().__init__(**kwargs)
        self.component = MixtureComponent()
        self.COMPONENTS = deepcopy(CHEMICAL_COMPONENTS)
        self.dad = fourth
        self.widget = widget
        self.number_component = number_component
        self.color = color

    def build(self):
        """Creates Chemical element"""
        if self.ids.spinner_component.text in self.COMPONENTS:

            if len(self.ids.spinner_component.text) > 32:
                self.ids.spinner_component.font_size = '10sp'
            else:
                self.ids.spinner_component.font_size = '15sp'

            self.component.name = self.ids.spinner_component.text
            self.component.chemical_composition = self.COMPONENTS[self.component.name]

            for i, j in self.component.chemical_composition.items():
                box = Box(self)
                box.ids.name_element.text = i
                if isinstance(j, float):
                    box.ids.value_element.text = str(round(j, 2))
                else:
                    box.ids.value_element.text = j
                self.ids.grid_box.add_widget(box)

            self.create_button()

        elif self.ids.spinner_component.text != 'Выберите компонент':
            self.component.name = self.ids.spinner_component.text
            self.component.chemical_composition = {}
            self.COMPONENTS[self.component.name] = {}

            if len(self.ids.spinner_component.text) > 32:
                self.ids.spinner_component.font_size = '10sp'
            else:
                self.ids.spinner_component.font_size = '15sp'

            self.create_button()

    def clear_grid(self):
        """Removes chemical elements that inside the Box class"""

        if self.ids.grid_box.children:
            self.ids.grid_box.clear_widgets()

    def check_name(self):
        """checks the selected name for entry into the list """

        if self.ids.spinner_component.text == 'Новый компонент':

            if 'Компонент 1' not in self.dad.composition.names:
                self.ids.spinner_component.text = 'Компонент 1'
            elif 'Компонент 2' not in self.dad.composition.names:
                self.ids.spinner_component.text = 'Компонент 2'
            elif 'Компонент 3' not in self.dad.composition.names:
                self.ids.spinner_component.text = 'Компонент 3'
            elif 'Компонент 4' not in self.dad.composition.names:
                self.ids.spinner_component.text = 'Компонент 4'
            elif 'Компонент 5' not in self.dad.composition.names:
                self.ids.spinner_component.text = 'Компонент 5'

            else:
                mistake = MistakePopup()
                mistake.ids.text_label.text = 'От куда столько'
                mistake.ids.text_mistake.text = 'НОВЫХ КОМПОНЕНТОВ!!!'
                mistake.open()
                self.ids.spinner_component.text = 'Выберите компонент'

        elif self.ids.spinner_component.text == 'СОБРАТЬ СМЕСЬ':
            new_popup = AddComponents(self)
            new_popup.open()

        elif self.widget.component:
            self.clear_grid()
            self.build()

        elif self.dad.composition.mixture:

            for i in self.dad.composition.mixture:

                if i.name == self.ids.spinner_component.text:
                    mistake = MistakePopup()
                    mistake.ids.text_label.text = 'Такой компонент'
                    mistake.ids.text_mistake.text = 'УЖЕ ДОБАВЛЕН В ШИХТУ!!!'
                    mistake.open()
                    self.ids.spinner_component.text = 'Выберите компонент'

                else:
                    self.clear_grid()
                    self.build()
        else:
            self.clear_grid()
            self.build()

    def create_button(self):
        """Creates new button for add new element"""
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

    def check_values(self):
        """Checks presence for the entered date"""

        if self.component.name and not self.ids.content_value.text:
            mistake = MistakePopup()
            mistake.ids.text_label.text = 'Не указано процентное'
            mistake.ids.text_mistake.text = 'содержание компонента в шихте!'
            mistake.open()

        elif self.component.name and self.ids.content_value.text:

            if not self.component.chemical_composition:
                mistake = MistakePopup()
                mistake.ids.text_label.text = 'НЕ ДОБАВЛЕНО НИ ОДНОГО'
                mistake.ids.text_mistake.text = 'ХИМИЧЕСКОГО ЭЛЕМЕНТА!!!'
                self.ids.content_value.text = ''
                mistake.open()

            elif self.dad.composition.mixture:
                if self.widget.component in self.dad.composition.mixture:
                    del self.dad.composition.mixture[self.widget.component]
                    if self.widget.component.name in self.dad.composition.names:
                        self.dad.composition.names.remove(self.widget.component.name)
                    self.widget.clear_widgets()
                summ = 0

                for i in self.dad.composition.mixture:
                    summ += float(self.dad.composition.mixture[i])
                summ += float(self.ids.content_value.text)

                if summ > 100:
                    mistake = MistakePopup()
                    mistake.ids.text_label.text = 'КОЛИЧЕСТВО КОМПОНЕНТОВ'
                    mistake.ids.text_mistake.text = 'ПРЕВЫСИЛО 100%!!!'
                    self.ids.content_value.text = ''
                    mistake.open()

                else:
                    self.add_component()

            elif float(self.ids.content_value.text) > 100:
                mistake = MistakePopup()
                mistake.ids.text_label.text = 'КОЛИЧЕСТВО КОМПОНЕНТОВ'
                mistake.ids.text_mistake.text = 'ПРЕВЫСИЛО 100%!!!'
                self.ids.content_value.text = ''
                mistake.open()

            else:
                self.add_component()
        else:
            mistake = MistakePopup()
            mistake.ids.text_mistake.text = 'Не выбран компонент!'
            mistake.open()

    def add_component(self):
        """Add new component to the Screen Fourth`s Composition
        Upgrades the received Widget"""

        self.dad.composition.mixture[self.component] = self.ids.content_value.text
        self.widget.component = self.component
        self.dad.composition.names.append(self.component.name)

        k = 0
        for i in self.dad.composition.mixture:
            if k == 0:
                self.dad.composition.name = i.name
                # print(self.dad.composition.mixture)
                self.dad.composition.ratio = str(self.dad.composition.mixture[i])
                k += 1
            else:
                self.dad.composition.name += ':' + i.name
                self.dad.composition.ratio += ':' + str(self.dad.composition.mixture[i])

        _box = BigBox()
        _box.ids.number_component.text = 'Компонент № ' + str(self.number_component)
        _box.ids.components_name.text = self.component.name

        if '(' in self.component.name:
            if len(self.component.name) > 32:
                _box.ids.components_name.font_size = '10sp'
            else:
                _box.ids.components_name.font_size = '15sp'

        _box.ids.lab_lab.text = '% в шихте'
        _box.ids.lab_value_element.text = self.ids.content_value.text

        if self.color:
            _box.ids.number_component.color = self.color
            _box.ids.components_name.color = self.color
            _box.ids.lab_lab.color = self.color
            _box.ids.lab_lab.text = '% в смеси'
            _box.ids.lab_value_element.color = self.color

        for i, j in self.component.chemical_composition.items():
            box = Box3()
            box.ids.lab_1.text = i
            if isinstance(j, float):
                box.ids.lab_2.text = str(round(j, 2))
            else:
                box.ids.lab_2.text = j
            if self.color:
                box.ids.lab_1.color = self.color
                box.ids.lab_2.color = self.color
            _box.ids.box_for_elements.add_widget(box)

        self.widget.name = self.component.name
        self.widget.dad = self.dad
        self.widget.add_widget(_box)
        self.widget.number_component = self.number_component
        self.dad.add_buttons()
        CHEMICAL_COMPONENTS[self.component.name] = self.component.chemical_composition

        self.dismiss()

    def close(self):
        del self.component


class NewElement(Popup):
    """Adds new chemical element to the selected component"""

    def __init__(self, instance):
        super().__init__()
        self.instance = instance
        self.ids.spinner_element.values = CHEMICAL_ELEMENTS

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
            if self.instance.component.chemical_composition:
                summ = 0
                for i in self.instance.component.chemical_composition:
                    summ += float(self.instance.component.chemical_composition[i])
                else:
                    summ += float(self.ids.element_value.text)

                if summ > 100:
                    mistake = MistakePopup()
                    mistake.ids.text_label.text = 'НЕ МОЖЕТ БЫТЬ >100%!!!'
                    mistake.ids.text_mistake.text = 'Превышено содержание элементов!'
                    mistake.open()
                else:
                    self.instance.component.chemical_composition[self.ids.spinner_element.text] = str(
                        self.ids.element_value.text)
                    self.instance.clear_grid()
                    self.instance.build()
                    self.dismiss()
            else:
                if float(self.ids.element_value.text) > 99:
                    mistake = MistakePopup()
                    mistake.ids.text_label.text = 'НЕ МОЖЕТ БЫТЬ!!!'
                    mistake.ids.text_mistake.text = 'СТОЛЬКО НЕ БЫВАЕТ!!!'
                    mistake.open()
                else:
                    self.instance.component.chemical_composition[self.ids.spinner_element.text] = str(
                        self.ids.element_value.text)
                    self.instance.COMPONENTS[self.instance.component.name][self.ids.spinner_element.text] = str(
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


class AddComponents(Popup):
    """Popup for adding Chemical element for composition of mixture"""
    sound_open_component = SoundLoader.load('sounds/sound_open_element.mp3')
    sound_del_component = SoundLoader.load('sounds/del_component.mp3')

    def __init__(self, widget, **kwargs):
        super().__init__(**kwargs)
        self.widget = widget
        self.composition = Composition()
        self.components_for_spinner = ['Новый компонент']
        for i in CHEMICAL_COMPONENTS:
            self.components_for_spinner.append(i)
        self.color = [1, 1, 1, 1]

    def close(self):
        self.widget.ids.spinner_component.text = 'Выберите компонент'

    def add_buttons(self):
        pass

    def add_new_component(self):
        
        """Adds new component to mixture"""
        summ = 0
        for i in self.composition.mixture:
            summ += float(self.composition.mixture[i])

        if summ == 100:
            mistake = MistakePopup()
            mistake.size_hint = [0.8, 0.28]
            mistake.title = 'ПРЕДУПРЕЖДЕНИE!'
            mistake.ids.text_label.text = 'Сумма всех компонентов уже 100%'
            mistake.ids.text_mistake.text = 'БОЛЬШЕ НЕ ДОБАВИТЬ!!!'
            lab = Label()
            lab.text = 'Произведите корректировку содержания \nили создайте новую смесь!'
            lab.halign = 'center'
            lab.valign = 'middle'
            mistake.ids.text_mistake.size_hint = [1, 0.3]
            mistake.ids.text_label.size_hint = [1, 0.2]
            mistake.ids.mistake_box.size_hint = [1, 0.6]
            mistake.ids.mistake_box.add_widget(lab)
            mistake.ids.mistake_but.size_hint = [0.2, 0.2]
            mistake.open()
        else:

            if not self.ids.first_box.children:
                element = AddComponent(self, self.ids.first_box, number_component=1, color=self.color)
                element.ids.spinner_component.values = self.components_for_spinner
                element.open()

            elif not self.ids.second_box.children:
                element = AddComponent(self, self.ids.second_box, number_component=2, color=self.color)
                element.ids.spinner_component.values = self.components_for_spinner
                element.open()

            elif not self.ids.third_box.children:
                element = AddComponent(self, self.ids.third_box, number_component=3, color=self.color)
                element.ids.spinner_component.values = self.components_for_spinner
                element.open()

            else:
                popup = MistakePopup()
                popup.ids.text_mistake.text = 'Превышено количество компонентов'
                popup.open()

    def check_name(self):
        """Forms the name"""

        if self.composition.mixture:

            self.ids.box_result.clear_widgets()
            box = Box3()
            box.orientation = 'horizontal'

            if len(self.composition.name) > 34:
                box.ids.lab_1.font_size = '10sp'
                box.ids.lab_2.font_size = '15sp'
            elif len(self.composition.name) > 19:
                box.ids.lab_1.font_size = '15sp'
                box.ids.lab_2.font_size = '15sp'

            box.ids.lab_1.text = '(' + self.composition.name + ')'
            box.ids.lab_1.color = [1, 1, 1, 1]
            box.ids.lab_2.text = '(' + self.composition.ratio + ')'
            box.ids.lab_2.color = [1, 1, 1, 1]
            box.ids.lab_2.size_hint = [0.5, 1]
            self.ids.box_result.add_widget(box)
        else:
            pass

    def calculate_interim_result(self):
        self.ids.interim_result.clear_widgets()
        print(self.composition.mixture)
        box = Box3()

        interim_result = 0
        for i, k in self.composition.mixture.items():
            interim_result += float(k)

        if int(interim_result) == interim_result:
            interim_result = int(interim_result)

        box.ids.lab_1.font_size = '10sp'
        box.ids.lab_1.color = [1, 1, 1, 1]
        box.ids.lab_2.text = str(interim_result) + '%'
        box.ids.lab_2.font_sizer = '15sp'

        if interim_result != 100:
            box.ids.lab_1.text = 'Промежуточный \nитог:'
            box.ids.lab_2.color = [1, 0, 0, 1]
        else:
            box.ids.lab_1.text = 'Смесь \nукомплектована:'
            box.ids.lab_2.color = [1, 1, 1, 1]

        self.ids.interim_result.add_widget(box)

    # def build_label(self):
    #     """
    #     :rtype: object
    #
    #     """
    #     if self.composition.name:
    #         self.ids.box_result.clear_widgets()
    #
    #         _box = BigBoxResult()
    #         _box.ids.number_component.text = 'Состав шихты: '
    #         if len(self.composition.name) > 50:
    #             _box.ids.components_name.font_size = '10sp'
    #         _box.ids.components_name.text = self.composition.name
    #         _box.ids.ratio_composition.text = self.composition.ratio
    #
    #         for i, j in self.weight_value.items():
    #             box = Box3()
    #             box.ids.lab_1.text = i
    #             box.ids.lab_2.text = str(round(j, 2))
    #             _box.ids.box_for_elements.add_widget(box)
    #
    #         self.ids.box_result.add_widget(_box)

    def add_mixture(self):

        if self.composition.mixture:
            chemical_composition = {}
            for i, k in self.composition.mixture.items():  # i = component, k = % (содержание в шихте)

                for h, j in i.chemical_composition.items():  # h = element, j = % (количество элемента в компоненте)
                    n = (float(j) * float(k)) / 100

                    if h in chemical_composition:
                        chemical_composition[h] += n
                    else:
                        chemical_composition[h] = n

            self.composition.name = '(' + self.composition.name + '[sub](' + self.composition.ratio + ') [/sub]' + ')'
            self.widget.COMPONENTS[self.composition.name] = chemical_composition
            self.widget.ids.spinner_component.text = self.composition.name

            summ = 0
            if self.composition.mixture:

                for i in self.composition.mixture:
                    summ += float(self.composition.mixture[i])

                if summ < 100:
                    mistake = MistakePopup()
                    mistake.title = 'РЕКОМЕНДАЦИЯ'
                    mistake.ids.text_label.text = 'Для достоверного расчёта '
                    mistake.ids.text_mistake.text = 'состав смеси должен составлять 100%!!!'
                    mistake.open()
        else:
            self.widget.ids.spinner_component.text = 'Выберите компонент'
