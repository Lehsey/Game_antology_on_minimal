import sys
import MainMenu
# сновной файл запуска

app = MainMenu.widget.QApplication(sys.argv)
main_window = MainMenu.MainMenu()
main_window.show()
sys.exit(app.exec_())
