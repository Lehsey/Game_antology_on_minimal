import sys
import MainMenu

app = MainMenu.widget.QApplication(sys.argv)
main_window = MainMenu.MainMenu()
main_window.show()
sys.exit(app.exec())
