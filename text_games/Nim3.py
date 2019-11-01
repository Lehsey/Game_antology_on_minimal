#import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt


class Nim3(QWidget):
    from random import choice
    def __init__(self):
        super().__init__()
        self.heap = []
        self.Rocks = False
        self.Winner = 0
        self.side = 0 # 0 - ИИ/ 1 - Игрок 
        self.Win = False
        self.initUI()

    def initUI(self):
        uic.loadUi('User_int\\Nim3.ui', self)
        self.setWindowTitle('Ним')
        #self.setWindowIcon(QtGui.QIcon('icon\\rock.png'))
        self.Choice.clicked.connect(self.chek)

    def chek(self):
        if self.Win:
            pass
        else:
            if not self.Rocks:
                if self.Inp.text() == '':
                    pass
                else:
                    self.heap.extend(int(el) for el in self.Inp.text().split())
                    self.peat_cond()
                    self.Rocks = True
                    self.Inp.clear()
                    self.AI()
            else:
                if self.side == 0:
                    self.AI()
                else:
                    if self.man_t == 0:
                        self.whichHeap = int(self.Inp.text())
                        if self.whichHeap > len(self.heap) or self.whichHeap <= 0:
                            self.Cmd.appendPlainText("Ты ошибся дружок-пирожок, попробуй снова \n")
                            self.Inp.clear()
                        else:
                            self.Cmd.appendPlainText("Введите колчество камней, которые возьмёте:")
                            self.Inp.clear()
                            self.man_t = 1
                    else:
                        self.takeStones = int(self.Inp.text())
                        if self.takeStones > self.heap[self.whichHeap - 1] or self.takeStones <= 0:
                            self.Cmd.appendPlainText("Ты ошибся дружок-пирожок, попробуй снова\n")
                            self.Inp.clear()
                        else:
                            self.heap[self.whichHeap - 1] -= self.takeStones
                            self.Inp.clear()
                            self.Winner = "вы"
                            self.peat_cond()
                            if self.Win:
                                pass
                            else:
                                self.side = 0
                                self.AI()


    def AI(self):
        self.Cmd.appendPlainText("ИИ сделал ход")
        if max(self.heap) ^ min(self.heap) != 0:
            self.heap.insert(self.heap.index(max(self.heap)), min(self.heap))
            self.heap.remove(max(self.heap))
        else: 
            self.heap.insert(self.heap.index(self.choice(self.heap)), max(self.heap) - 1)
            self.heap.remove(max(self.heap))
    
        self.Winner = "ИИ"
        self.side = 1
        self.peat_cond()
        self.Cmd.appendPlainText("Теперь ваш ход")
        self.Cmd.appendPlainText("Введите кучу, в которой хотите играть цифрой, например: 1")
        self.man_t = 0 #0 ввод кучи/ 1 ввод кол-ва камней


    def peat_cond(self):
        while 0 in self.heap:
            self.heap.remove(0)
            self.Cmd.appendPlainText("Куч стало на одну меньше")
        if self.heap:
            self.Cmd.appendPlainText('')
            self.Cmd.appendPlainText('Состояние куч:')
            self.Cmd.appendPlainText(' '.join(str(el) for el in self.heap))
            for el in self.heap:
                self.Cmd.appendPlainText(''.join('*' for i in range(el)))
        else:
            self.Cmd.clear()
            self.Cmd.appendPlainText(f"Победитель {self.Winner}")
            self.Win = True
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.chek()



#app = QApplication(sys.argv)
#nim = Nim3()
#nim.show()
#sys.exit(app.exec_())