# основной цикл, главное окно
from itertools import product

import sys
from PyQt5 import QtWidgets as widget

from tabe import table
from text_games.Nim3 import Nim3
from Graph_game.Snake_py import Snake_game


class MainMenu(widget.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Python Game Antology vol.0')

        # Инициализация
        self.setupTextGames()
        self.setupGraphicGames()
        self.setupGamesGroup()
        self.setupButtons()
        self.setupGrid()

        self.setFixedSize(self.sizeHint())

    # Текстовые игры
    def setupTextGames(self):
        self.text_games = widget.QWidget()
        self.text_games_grid = widget.QVBoxLayout(self.text_games)

        self.nim = widget.QRadioButton('Ним')

        self.text_games_grid.addWidget(self.nim)

    # Графические игры
    def setupGraphicGames(self):
        self.graphic_games = widget.QWidget()
        self.graphic_games_grid = widget.QVBoxLayout(self.graphic_games)

        self.snake = widget.QRadioButton('Змейка')

        self.graphic_games_grid.addWidget(self.snake)

    # Инициализация кнопок
    def setupButtons(self):
        self.records_button = widget.QPushButton('Рекорды', self)
        self.records_button.clicked.connect(self.records)

        self.play_button = widget.QPushButton('Играть')
        self.play_button.clicked.connect(self.run)

    # Группировка кнопок
    def setupGamesGroup(self):
        self.games = widget.QButtonGroup(self)
        self.games.addButton(self.nim)
        self.games.addButton(self.snake)

    # Инициализация сетки
    def setupGrid(self):
        self.grid = widget.QVBoxLayout()

        self.text_layout = widget.QWidget()
        self.text_grid = widget.QHBoxLayout(self.text_layout)
        self.text_grid.addWidget(widget.QLabel('Текстровые:'))
        self.text_grid.addWidget(widget.QLabel('Графические:'))

        self.games_layout = widget.QWidget()
        self.games_grid = widget.QHBoxLayout(self.games_layout)
        self.games_grid.addWidget(self.text_games)
        self.games_grid.addWidget(self.graphic_games)

        self.buttons_layout = widget.QWidget()
        self.buttons_grid = widget.QHBoxLayout(self.buttons_layout)
        self.buttons_grid.addWidget(self.records_button)
        self.buttons_grid.addWidget(self.play_button)

        self.grid.addWidget(self.text_layout)
        self.grid.addWidget(self.games_layout)
        self.grid.addWidget(self.buttons_layout)

        self.setLayout(self.grid)

    # Запуск игры
    def run(self):
        game = self.games.checkedButton()
        if game:
            game = game.text()
            if game == 'Ним':
                self.game = Nim3(game)
                self.game.show()
            elif game == 'Змейка':
                self.game = Snake_game(game)

    # Рекорды
    def records(self):
        game = self.games.checkedButton()
        if game:
            game = game.text()
            self.t = table(game)
            self.t.show()


app = widget.QApplication(sys.argv)
game = MainMenu()
game.show()
sys.exit(app.exec_())


