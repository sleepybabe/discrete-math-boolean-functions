from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 40, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 110, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 180, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 280, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 180, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 350, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 230, 231, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 250, 451, 31))
        self.label_4.setObjectName("label_4")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "ДНФ"))
        self.pushButton.setText(_translate("MainWindow", "Выдать вектор"))
        self.label.setText(_translate("MainWindow", "Введите ДНФ:"))
        self.pushButton_2.setText(_translate("MainWindow", "Проверить"))
        self.label_3.setText(_translate("MainWindow", "Запишите без пробелов, соблюдая правила:  "))
        self.label_4.setText(_translate("MainWindow", "имена переменных: x,y,z; знак отрицания: ~; знак конъюнкции: &; знак дизъюнкции: v"))

    def add_functions(self):
        self.pushButton.clicked.connect(self.showVector)
        self.pushButton_2.clicked.connect(self.showResult)

    def showVector(self):
        self.lineEdit.clear()
        s=''
        v=[]
        n=8
        def createF():
            for i in range(n):
                v.append(random.randint(0, 1))
            return v
        vector=createF()
        s=" ".join(str(x) for x in vector)
        s=s.replace(' ', '')
        self.lineEdit.setText(str(s))

    def showResult(self):
        str=self.lineEdit_2.text()
        k=''
        minus=0
        userdnf=[]
        nab = ['000', '001', '010', '011', '100', '101', '110', '111']
        vnab = []
        strvec = self.lineEdit.text()
        v = list(strvec)
        v = [int(i) for i in v]
        for i in range(len(v)):
            if v[i] == 1:
                vnab.append((nab[i]))

        for i in range(len(str)):
            if str[i] == '&':
                continue
            if str[i] == 'v':
                userdnf.append(k)
                k = ''
                continue
            if str[i] == '~':
                minus = 1
                continue
            if str[i] == 'x':
                if minus == 0:
                    k = k + '1'
                else:
                    k = k + '0'
                    minus = 0
                continue
            elif len(k) == 0:
                k = k + '*'
            if str[i] == 'y':
                if minus == 0:
                    k = k + '1'
                else:
                    k = k + '0'
                    minus = 0
                continue
            elif len(k) == 1:
                k = k + '*'
            if str[i] == 'z':
                if minus == 0:
                    k = k + '1'
                else:
                    k = k + '0'
                    minus = 0
                continue
        userdnf.append(k)

        for i in range(len(userdnf)):
            if len(userdnf[i]) < 3:
                while len(userdnf[i]) != 3:
                    userdnf[i] = userdnf[i] + '*'
            userdnf.append(userdnf[i].replace('*', '0'))
            userdnf.append(userdnf[i].replace('*', '1'))
            userdnf[i] = userdnf[i].replace('*', '')

        res=[]
        for i in range(len(userdnf)):
            if len(userdnf[i]) == 3:
                res.append(userdnf[i])

        res=set(res)
        res=list(res)
        res.sort()
        vnab.sort()
        if res==vnab:
            self.label_2.setText('Правильно!')
        else:
            self.label_2.setText('Неверно!')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
