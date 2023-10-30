from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(310, 120, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 120, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 180, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(375, 180, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 300, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Имя функции"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Конъюнкция"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Дизъюнкция"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Импликация"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Эквивалентность"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Сложение по модулю 2"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Стрелка Пирса"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Штрих Шеффера"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Коимпликация"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Обратная импликация"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Обратная коимпликация"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Инверсия 2-го аргумента"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Инверсия 1-го аргумента"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Постоянный 0"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Постоянная 1"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Тождественность 1-го аргумента"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Тождественность 2-го аргумента"))
        self.pushButton.setText(_translate("MainWindow", "Выдать вектор"))
        self.pushButton_2.setText(_translate("MainWindow", "Проверить"))

    def add_functions(self):
        self.pushButton.clicked.connect(self.showVector)
        self.pushButton_2.clicked.connect(self.showResult)

    def showVector(self):
        f_list = ["0000", "1111", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010",
                  "1011", "1100", "1101", "1110"]
        f = random.choices(f_list, k=1)
        f = ('').join(f)
        self.lineEdit.setText(str(f))

    def showResult(self):
        name=self.comboBox.currentText()
        f = self.lineEdit.text()
        if f == "0001":
            if name == "Конъюнкция":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "0111":
            if name == "Дизъюнкция":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "1101":
            if name == "Импликация":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "1001":
            if name == "Эквивалентность":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "0110":
            if name == "Сложение по модулю 2":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "1000":
            if name == "Стрелка Пирса":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "1110":
            if name == "Штрих Шеффера":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "0010":
            if name == "Коимпликация":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "1011":
            if name == "Обратная импликация":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "0100":
            if name == "Обратная коимпликация":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "1010":
            if name == "Инверсия 2-го аргумента":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "1100":
            if name == "Инверсия 1-го аргумента":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "0000":
            if name == "Постоянный 0":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "1111":
            if name == "Постоянная 1":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "0011":
            if name == "Тождественность 1-го аргумента":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return
        if f == "0101":
            if name == "Тождественность 2-го аргумента":
                self.label.setText('Правильно!')
                return
            else:
                self.label.setText('Неправильно!')
                return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
