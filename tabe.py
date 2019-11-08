import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Tabel import Ui_Table_w


class table(QMainWindow, Ui_Table_w):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.setupUi(self)
        self.con = sqlite3.connect('Records.db')
        self.weiw()

    def weiw(self):
        cur = self.con.cursor()
        if self.game == 'Ним':
            result = cur.execute('SELECT * FROM Nim').fetchall()
        elif self.game == 'Змейка':
            result = cur.execute("SELECT * FROM Snake").fetchall()
        self.Table.setRowCount(len(result))
        self.Table.setColumnCount(len(result[0]))
        col_name_list = [el[0] for el in cur.description]
        self.Table.setHorizontalHeaderLabels(col_name_list)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.Table.setItem(i, j, QTableWidgetItem(str(val)))
