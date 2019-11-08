from PyQt5 import QtWidgets as widget
import Records


class GameOver(widget.QWidget):
    def __init__(self, game, rec):
        super().__init__()
        # инициализация
        self.game_name = game
        self.rec = rec
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Game Over!')
        #установка интерфейса
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
        #запись рекорда в зависимости от игры
        if self.game_name == "Змейка":
            Records.set_rec(
                self.game_name, self.input_name.text(),  self.rec)
        elif self.game_name == 'Ним':
            Records.set_rec(
                self.game_name, self.input_name.text(),  self.rec)
        self.hide()
        
