#mainpage i tasarlayıp login ile birleştireceğim
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

Window.size = (400, 500)

#bu değişkeni dosyadan alsın.
db_wants_execute_order = True
db_execute_time = None

class MainPagesMenu(TabbedPanel):
    this_buttons_text = StringProperty("Enabled" if db_wants_execute_order else "Disabled")
    def execute_button_click(self):
        global db_wants_execute_order
        if db_wants_execute_order:
            db_wants_execute_order = False
            print('\n\n\n###Execute order set to: False')
            self.ids.wants_execute.text = "Disabled"
        else:
            db_wants_execute_order = True
            print('\n\n\n###Execute order set to: True')
            self.ids.wants_execute.text = "Enabled"


 
        
class Buildingmainpage(App):
    
    def build(self):
        return MainPagesMenu()
        



if __name__ == '__main__':
    Buildingmainpage().run()

 