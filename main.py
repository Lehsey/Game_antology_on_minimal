import sys
from PyQt5.QtWidgets import QApplication

import MainMenu

app = QApplication(sys.argv)
main_window = MainMenu.MainMenu()
main_window.show()
sys.exit(app.exec())
