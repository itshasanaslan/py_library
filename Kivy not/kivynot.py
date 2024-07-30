import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from functools import partial

class Menu(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='HASAN ASLAN')) #size_hint=(.25,.10), pos = (230,230)
        self.add_widget(Label(text=''))

        self.add_widget(Label(text='Name:'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='Surname:'))
        self.surname = TextInput(multiline=False)
        self.add_widget(self.surname)

        self.add_widget(Label(text='E-mail:'))
        self.email = TextInput()
        self.add_widget(self.email)

        self.add_widget(Label(text='Phone:'))
        self.phone = TextInput()
        self.add_widget(self.phone)

        self.add_widget(Button(text='Send'))


class MyApp(App):
    def build(self):
        return Menu()


if __name__ == '__main__':
    MyApp().run()

^^^^^^^^^^^^^^^^^^^^^^^^^Buton çalıştırma^^^^^^^^^^3333

class Kivy(App):
    def disable(self,instance,*args):
        instance.disabled = True

    def update(self,instance,*args):
        instance.text = 'I am disabled!'

    def build(self):
        mybtn = Button(text= 'Click me to disable.',size_hint = (.25,.10))
        mybtn.bind(on_press=partial(self.disable,mybtn))
        mybtn.bind(on_press=partial(self.update,mybtn))
        return mybtn

Kivy().run()

^^^^^^^^^^^^^^^^^^^^^^^^^

class Tutorial(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Hello! Drag me with your mouse!')

        f.add_widget(s)
        s.add_widget(l)
        return f


if __name__ =='__main__':
    Tutorial().run()

padding = "widgetlar arasındaki boşluk"
# kv dosyası olustururken ana classımın adını vermeli ve her harfi kücük yazmalıyım.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
class MainPage(inherit):
	this_buttons_text = StringProperty("Enabled" if db_wants_execute_order else "Disabled")
#kv dosyasında alakalı butonda:
text: root.this_buttons_text #yazıyorum.















