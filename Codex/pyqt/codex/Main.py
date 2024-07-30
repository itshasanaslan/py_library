from PyQt5 import QtWidgets
import sys
from design import Ui_Codex
from codex import CodeX
from colorama import Fore,Style,init
from os import system

system('title About...')

init()

class MyApp(QtWidgets.QMainWindow,CodeX):

    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_Codex()
        self.ui.setupUi(self)
    

       

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())






print(Fore.RED+Style.BRIGHT,'''\n
		You can contact me;
		
		***Twitter: Gepettolyon***
		
		***Instagram: hasanaslan7***

		***Mail: aslanhassan98@gmail.com***

		***Reddit: hasanaslan***


This app generates random key and encrypts your text simply.
In order to decrypt your text, just use the same encryption key.

	''')




app()