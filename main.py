import sys
import Main_menu

app = Main_menu.QApplication(sys.argv)
main_window = Main_menu.Main_menu()
main_window.show()
sys.exit(app.exec())