import sys
import MainMenu

app = Main_menu.QApplication(sys.argv)
main_window = MainMenu.MainMenu()
main_window.show()
sys.exit(app.exec())
