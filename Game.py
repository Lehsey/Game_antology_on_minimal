# import sys
from PyQt5 import QtWidgets as widget


class GameOver(widget.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.setWindowTitle('Game!')
        
        self.setupInputName()
        self.setupButtons()
        self.setupGrid()
        
        self.setFixedSize(self.sizeHint())
    
    def setupInputName(self):
        self.input_name_text = widget.QLabel('Введите имя:', self)
        self.input_name = widget.QLineEdit(self)
    
    def setupButtons(self):
        self.set_record = widget.QPushButton('Продолжить')
        self.set_record.clicked.connect(self.setRecord)
        
        self.cancel_button = widget.QPushButton('Отмена')
        self.cancel_button.clicked.connect(self.close)
    
    def setupGrid(self):
        self.grid = widget.QVBoxLayout(self)
        
        self.input_name_frame = widget.QWidget(self)
        self.input_name_layout = widget.QHBoxLayout(self.input_name_frame)
        self.input_name_layout.addWidget(self.input_name_text, 0)
        self.input_name_layout.addWidget(self.input_name, 1)
        
        self.buttons_frame = widget.QWidget(self)
        self.buttons_layout = widget.QHBoxLayout(self.buttons_frame)
        self.buttons_layout.addWidget(self.set_record)
        self.buttons_layout.addWidget(self.cancel_button)
        
        self.grid.addWidget(self.input_name_frame)
        self.grid.addWidget(self.buttons_frame)
        
        self.setLayout(self.grid)
    
    def setRecord(self):
        print('works')


# check!
# app = widget.QApplication(sys.argv)
# game = GameOver()
# game.show()
# sys.exit(app.exec())
