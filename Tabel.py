# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Table_w(object):
    def setupUi(self, Table_w):
        Table_w.setObjectName("Table_w")
        Table_w.resize(799, 800)
        self.Table = QtWidgets.QTableWidget(Table_w)
        self.Table.setGeometry(QtCore.QRect(10, 10, 781, 781))
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(0)
        self.Table.setRowCount(0)

        self.retranslateUi(Table_w)
        QtCore.QMetaObject.connectSlotsByName(Table_w)

    def retranslateUi(self, Table_w):
        _translate = QtCore.QCoreApplication.translate
        Table_w.setWindowTitle(_translate("Table_w", "Таблица"))
