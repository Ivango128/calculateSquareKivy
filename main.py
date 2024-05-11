import math

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lable_a = Label(text='Введите a', halign='right')
        self.lable_b = Label(text='Введите b:', halign='right')
        self.lable_c = Label(text='Введите c:', halign='right')
        self.input_a = TextInput(multiline=False)
        self.input_b = TextInput(multiline=False)
        self.input_c = TextInput(multiline=False)
        self.main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.line_a = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.line_b = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.line_c = BoxLayout(size_hint=(0.8, None), height='30sp')

        self.eqution = Label(text=f'Пример:', halign='center')
        self.answer = Label(text=f'Ответ', halign='center')

        self.btn = Button(text='Расчитать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = (0.98, 0.31, 0.8, 1)
        self.btn.on_press = self.next


        self.line_a.add_widget(self.lable_a)
        self.line_a.add_widget(self.input_a)
        self.line_b.add_widget(self.lable_b)
        self.line_b.add_widget(self.input_b)
        self.line_c.add_widget(self.lable_c)
        self.line_c.add_widget(self.input_c)

        self.main_line.add_widget(self.line_a)
        self.main_line.add_widget(self.line_b)
        self.main_line.add_widget(self.line_c)

        self.main_line.add_widget(self.eqution)
        self.main_line.add_widget(self.answer)
        self.main_line.add_widget(self.btn)

        self.add_widget(self.main_line)

    def next(self):
        try:
            a = int(self.input_a.text)
            b = int(self.input_b.text)
            c = int(self.input_c.text)
            if b > 0:
                if c > 0:
                    self.eqution.text = f'{a}x²+{b}x+{c}=0'
                else:
                    self.eqution.text = f'{a}x²+{b}x{c}=0'
            else:
                if c > 0:
                    self.eqution.text = f'{a}x²{b}x+{c}=0'
                else:
                    self.eqution.text = f'{a}x²{b}x{c}=0'

            D = b ** 2 - 4 * a * c
            if D < 0:
                self.answer.text = f'Ответ: Корней нет!'
            elif D == 0:
                x = -b / (2 * a)
                self.answer.text = f'Ответ: x = {x}'
            elif D > 0:
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)
                self.answer.text = f'Ответ: x₁ = {x1}\n           x₂ = {x2}'
        except:
            self.answer.text = 'Error'
class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='oneScreen'))
        return sm


app = HeartCheck()
app.run()