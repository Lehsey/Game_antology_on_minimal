from PyQt5 import QtWidgets as widget


class MainMenu(widget.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.setWindowTitle('Python Game Antology vol.0')
        
        self.setupTextGames()
        self.setupGraphicGames()
        self.setupGamesGroup()
        self.setupButtons()
        self.setupGrid()
        
        self.setFixedSize(self.sizeHint())
    
    def setupTextGames(self):
        self.text_games = widget.QWidget()
        self.text_games_grid = widget.QVBoxLayout(self.text_games)
        
        self.nim = widget.QRadioButton('Ним')
        self.dungeon = widget.QRadioButton('Подземелье')
        
        self.text_games_grid.addWidget(self.nim)
        self.text_games_grid.addWidget(self.dungeon)
    
    def setupGraphicGames(self):
        self.graphic_games = widget.QWidget()
        self.graphic_games_grid = widget.QVBoxLayout(self.graphic_games)
        
        self.progress = widget.QRadioButton('In progress')
        
        self.graphic_games_grid.addWidget(self.progress)
    
    def setupGamesGroup(self):
        self.games = widget.QButtonGroup(self)
        self.games.addButton(self.nim)
        self.games.addButton(self.dungeon)
        self.games.addButton(self.progress)
    
    def setupButtons(self):
        self.records_button = widget.QPushButton('Рекорды', self)
        # self.records_button.clicked.connect(self.records)
        
        self.play_button = widget.QPushButton('Играть')
        # self.play_button.clicked.connect(self.close)
    
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
