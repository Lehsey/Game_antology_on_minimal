from PyQt5 import uic
from PyQt5.QtWidgets import *

class Main_menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('User_int/main_menu.ui', self)

