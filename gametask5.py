from PyQt5 import QtCore, QtGui, QtWidgets
import random

v=[]
def fict(arg,v):
    hii=0
    j=int(len(v)/(2**arg))
    ii=0
    for ex in range(0,2**(arg-1)):
        for i in range(ii,j):
            if v[i] != v[j]:
                return 1
            j=j+1
            ii=ii+1
            hii=hii+1
        ii=ii+hii
        j=j+hii
        hii=0
    return 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(290, 30, 71, 31))
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 290, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 380, 231, 41))
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 90, 251, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 160, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(480, 220, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Существенные и фиктивные переменные"))
        self.label.setText(_translate("MainWindow", "Выберите количество переменных:"))
        self.pushButton.setText(_translate("MainWindow", "Выдать вектор"))
        self.label_2.setText(_translate("MainWindow", "Запишите порядковый номер существенных переменных через запятую:"))
        self.label_3.setText(_translate("MainWindow", "Запишите порядковый номер фиктивных переменных через запятую:"))
        self.pushButton_2.setText(_translate("MainWindow", "Проверить"))

    def add_functions(self):
        self.pushButton.clicked.connect(self.showVector)
        self.pushButton_2.clicked.connect(self.showResult)

    def showVector(self):
        self.lineEdit.clear()
        s=''
        v=[]
        n=self.spinBox.value()
        n=2**n
        def createF():
            for i in range(n):
                v.append(random.randint(0, 1))
            return v
        vector=createF()
        s=" ".join(str(x) for x in vector)
        s=s.replace(' ', '')
        self.lineEdit.setText(str(s))

    def showResult(self):
        ss=''
        ff=''
        strvec=self.lineEdit.text()
        v=list(strvec)
        v=[int(i) for i in v]
        per=self.spinBox.value()
        self.label_4.clear()
        sushvec = []
        fictvec = []
        res=-1
        ss=self.lineEdit_2.text()
        ff=self.lineEdit_3.text()
        k=''
        for i in ss:
            if i==' ':
                continue
            if i==',':
                sushvec.append(int(k))
                k=''
                continue
            k=k+i
            if(i>'0')&(i<'9'):
                if (int(k)<1)|(int(k)>per):
                    self.label_4.setText('Введите правильно!')
                    return
            else:
                self.label_4.setText('Введите правильно!')
                return

        if k!='':
            sushvec.append(int(k))
        k=''
        for i in ff:
            if i == ' ':
                continue
            if i == ',':
                fictvec.append(int(k))
                k = ''
                continue
            k = k + i
            if (i > '0') & (i < '9'):
                if (int(k) < 1) | (int(k) > per):
                    self.label_4.setText('Введите правильно!')
                    return
            else:
                self.label_4.setText('Введите правильно!')
                return
        if k!='':
            fictvec.append(int(k))

        for i in range(len(sushvec)):
            res=fict(sushvec[i],v)
            if res==0:
                self.label_4.setText('Ошибка!')
                return
        for i in range(len(fictvec)):
            res=fict(fictvec[i],v)
            if res==1:
                self.label_4.setText('Ошибка!')
                return
        if res!=-1:
            self.label_4.setText('Правильно!')
        else:
            self.label_4.setText('Введите переменные!')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


