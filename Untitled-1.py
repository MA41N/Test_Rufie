from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.animation import Animation
 
 
class MainScreen(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        pink = (.87, .54, .8, 1)
        Window.clearcolor = pink


        ar1 = AnchorLayout(padding=[100, 200, 0, 400])
        lb1 = Label(
            text='Данное приложение позволит вам с помощью теста Руфье\n провести первичную диагностику вашего здоровья.')
 
        ar1.add_widget(lb1)
        self.add_widget(ar1)
 
        ar2 = AnchorLayout(padding=[0, 200, 400, 0])
        lb2 = Label(text='Введите имя:')
        ar2.add_widget(lb2)
        self.add_widget(ar2)
 
        ar3 = AnchorLayout(padding=[0, 300, 400, 0])
        lb3 = Label(text='Введите возраст')
        ar3.add_widget(lb3)
        self.add_widget(ar3)
 
        ar4 = AnchorLayout(padding=[300, 390, 200, 180])
        self.ti = TextInput(text='')
        # ti.bind(text = self.save)
        ar4.add_widget(self.ti)
        self.add_widget(ar4)
 
        ar5 = AnchorLayout(padding=[300, 435, 200, 135])
        self.ti2 = TextInput(text='')
        ar5.add_widget(self.ti2)
        self.add_widget(ar5)
 
        ar6 = AnchorLayout(padding=[300, 500, 300, 0])
        btstart = Button(text='Начать', background_color=(0, 1, 0))
        btstart.on_press = self.next
        ar6.add_widget(btstart)
        self.add_widget(ar6)

        blue = (0,.75,1,1)
        btstart.background_color = blue
 
 
    def next(self):
        global name
        name = self.ti.text
        if name == '':
            name = 'user'
            self.ti.text = name
 
        global age
        age = self.save_age(self.ti2.text)
        if age < 7 or age == False:
            age = 'Введите целое число >=7'
            self.ti2.text = age
            self.ti2.foreground_color = (1, 0, 0)
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'first'
 
 
    def save_age(self, insntance):
        try:
            return int(insntance)
        except:
            return False
 
 
class FirstScreen(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
 
        self.current = 0
        self.totall = 15
 
        bl = BoxLayout(padding=[400, 280, 300, 460])
        lb = Label(text='Замерьте пульс за 15 секунд. \n Результат запишите в соответсвующее поле.')
        bl.add_widget(lb)
        self.add_widget(bl)
 
        bl2 = BoxLayout(padding=[300, 390, 200, 180])
        lb2 = Label(text='Введите результат:')
        self.txt = TextInput(text='')

        txt = '[color=#db0000]' + 'Введите имя:' + '[/color]'
        lbl = Label(text=txt, markup= True)
 
        # txt.bind(text = self.value1)
        bl2.add_widget(lb2)
        bl2.add_widget(self.txt)
        self.add_widget(bl2)
 
        bl1 = BoxLayout(padding=[300, 500, 300, 0])
        btstart = Button(text='Продолжить', background_color=(0, 1, 0))
        btstart.on_press = self.next
        bl1.add_widget(btstart)
        self.add_widget(bl1)
 
        bltimer = BoxLayout(padding=[250, 250])
        self.labtimer = Label(text='Прошло времени:')
        buttimer = Button(text='Start')
        buttimer.on_press = self.time
        bltimer.add_widget(self.labtimer)
        bltimer.add_widget(buttimer)
        self.add_widget(bltimer)
 
    def todo(self, dt):
        self.current += 1
        self.labtimer.text = f'Прошло времени: {str(self.current)}'
        if self.current >= self.totall:
            self.labtimer.text = 'Время вышло'
            return False
 
 
    def time(self):
        Clock.schedule_interval(self.todo, 1)
 
    def next(self):
        global t
        t = self.integer_text(self.txt.text)
        if t == False:
            t = 'Ошибка'
            self.txt.text = t
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'second'
 
    def integer_text(self, text):
        try:
            return int(text)
        except:
            return False
 
 
class SecondScreen(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
 
        self.current = 0
        self.totall = 45
 
        bl1 = BoxLayout(padding=[300, 500, 300, 0])
        btstart = Button(text='Продолжить', background_color=(0, 1, 0))
        btstart.on_press = self.next
        bl1.add_widget(btstart)
        self.add_widget(bl1)
 
        bl2 = BoxLayout(padding=[0, 0, 0, 150])
        lb = Label(text='Выполнить 30 приседаний за 45.')
        bl2.add_widget(lb)
        self.add_widget(bl2)
 
 
        bl_timer = BoxLayout(padding=[200,290,200,200])
        self.label_timer = Label(text='Время:')
        start_button = Button(text='Начать')
        start_button.on_press = self.time
        bl_timer.add_widget(self.label_timer)
        bl_timer.add_widget(start_button)
        self.add_widget(bl_timer)
 
    def todo(self, td):
        self.current += 1
        self.label_timer.text = f'Время: {str(self.current)}'
        if self.current >= self.totall:
            return False
 
    def time(self):
        Clock.schedule_interval(self.todo, 1)
 
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'three'
 
 
class ThriedScreen(Screen):
    def __init__(self, name='three'):
        super().__init__(name=name)
 
        self.current = 0
        self.totall = 60
        self.first_stop = 16
        self.breaks = 45
 
        lb = Label(
            text='В течение минуты замерьте пульс два раза:\n за первые 15 секунд минуты, затем последние 15 секунд.\n Результаты запишите в соответсвующие поля.')
 
        bl1 = BoxLayout(padding=[300, 500, 300, 0])
        bl2 = BoxLayout(padding=[0, 0, 0, 250])
        bl3 = BoxLayout(padding=[300, 390, 200, 180])
        bl4 = BoxLayout(padding=[300, 435, 200, 135])
        bl5 = BoxLayout(padding=[0, 200, 400, 0])
        bl6 = BoxLayout(padding=[0, 300, 400, 0])
 
        lb2 = Label(text='Результат:')
        lb3 = Label(text='Результат после отдыха:')
 
        self.ti = TextInput(text='0')
        self.ti2 = TextInput(text='0')
 
        bl5.add_widget(lb2)
        bl3.add_widget(self.ti)
        bl6.add_widget(lb3)
        bl4.add_widget(self.ti2)
 
        self.add_widget(bl5)
        self.add_widget(bl6)
        self.add_widget(bl3)
        self.add_widget(bl4)
 
        btstart = Button(text='Завершить', background_color=(0, 1, 0))
        btstart.on_press = self.next
 
        bl2.add_widget(lb)
        bl1.add_widget(btstart)
 
        self.add_widget(bl2)
        self.add_widget(bl1)
 
        timer_boxlayout = BoxLayout(padding=[200,290,300,300])
        button_start = Button(text='start')
        self.text_timer = Label(text='Время: ')
        button_start.on_press = self.time
        timer_boxlayout.add_widget(self.text_timer)
        timer_boxlayout.add_widget(button_start)
        self.add_widget(timer_boxlayout)
 
    def todo(self, td):
        self.current += 1
        self.text_timer.text = f'Время: {str(self.current)}'
 
        if self.current >= self.first_stop and self.current <= self.breaks:
            self.text_timer.text = f'Перерыв'
 
        if self.current >= self.totall:
            self.text_timer.text = 'Время вышло'
            return False
 
    def time(self):
        Clock.schedule_interval(self.todo, 1)
 
 
 
    def next(self):
        global Ti
 
        Ti = self.integer_text(self.ti.text)
        if Ti == False:
            Ti = 'Ошибка'
            self.ti.text = Ti
        global Ti2
        Ti2 = self.integer_text(self.ti2.text)
        if Ti2 == False:
            Ti2 = 'Ошибка'
            self.ti2.text = Ti2
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'final'
 
    def integer_text(self, text):
        try:
            return int(text)
        except:
            return False
 
 
class FinalScreen(Screen):
    def __init__(self, name='final'):
        super().__init__(name=name)
 
        #count = (4 * (p1 + p2 + p3) - 200) / 10
 
        bl = BoxLayout(padding=[200, 200, 200, 200])
        lb = Label(text=f'Иван\nВаш индекс Руфье:\nРаботоспособность сердца:низкая.\nСрочно обратитесь к врачу!')
        bl.add_widget(lb)
        self.add_widget(bl)
 
 
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen())
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())
        sm.add_widget(ThriedScreen())
        sm.add_widget(FinalScreen())
 
        return sm
 
MyApp().run()
