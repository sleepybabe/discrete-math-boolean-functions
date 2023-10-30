from PyQt5 import QtCore, QtGui, QtWidgets
import random
from array import *

def T0(v):
    if v[0]==0:
        return 1
    else:
        return 0

def T1(v):
    if v[len(v)-1]==1:
        return 1
    else:
        return 0

def S(v):
    k=0
    j=len(v)-1
    for i in range(int(len(v)/2)):
        if v[i]!=v[j]:
            k=k+1
        j=j-1
    if k==int(len(v)/2):
        return 1
    else:
        return 0

def M(arg,v):
    #сравниваются наборы через степень двойки, т.е. (смотря сколько переменных) сначала наборы 0 и 1 (2**0),
    #затем 0 и 2 (2**1), дальше 0 и 4 (2**2) и т.д. n раз, где n - количество переменных
    hii = 0
    j = int(len(v) / (2 ** arg))
    ii = 0
    lenarg=arg
    for m in range(lenarg):
        for ex in range(0, 2 ** (arg - 1)):
            for i in range(ii, j):
                if v[i] > v[j]:
                    return 0
                j=j+1
                ii=ii + 1
                hii=hii + 1
            ii=ii+hii
            j=j + hii
            hii= 0
        arg=arg-1
        hii = 0
        j = int(len(v) / (2 ** arg))
        ii = 0
    return 1

def zhegalkin(v):
    zh=[]
    vc=v.copy()
    res=[]
    res.append(vc[0])
    for i in range(len(v)-1):
        for j in range(len(vc)-1):
            zh.append((vc[j]+vc[j+1])%2)
        res.append(zh[0])
        vc=zh.copy()
        zh=[]
    return res

def L(v):
    res=zhegalkin(v)
    k=3
    t=1
    while k<len(v):
        for i in range(k, 2**t +k-1):
            if res[i]==1:
                return 0
        k=k+2**t
        t=t+1
    return 1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 55, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(150, 260, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(300, 260, 70, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(450, 260, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(225, 300, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(375, 300, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 340, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 390, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(210, 20, 42, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 20, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(580, 20, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setObjectName("spinBox_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(380, 160, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(380, 190, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 230, 631, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Полные системы"))
        self.pushButton.setText(_translate("MainWindow", "Выдать набор"))
        self.checkBox.setText(_translate("MainWindow", "T0"))
        self.checkBox_2.setText(_translate("MainWindow", "T1"))
        self.checkBox_3.setText(_translate("MainWindow", "S"))
        self.checkBox_4.setText(_translate("MainWindow", "M"))
        self.checkBox_5.setText(_translate("MainWindow", "L"))
        self.pushButton_2.setText(_translate("MainWindow", "Проверить"))
        self.label_2.setText(_translate("MainWindow", "Количество переменных:"))
        self.label_3.setText(_translate("MainWindow", "Количество функций:"))
        self.radioButton.setText(_translate("MainWindow", "Да, набор полный"))
        self.label_4.setText(_translate("MainWindow", "Выберите, является ли набор функций полным:"))
        self.radioButton_2.setText(_translate("MainWindow", "Нет, набор неполный"))
        self.label_5.setText(_translate("MainWindow", "Если набор неполный, то выберите замкнутый класс, к которому он принадлежит:"))

    def add_functions(self):
        self.pushButton.clicked.connect(self.showVector)
        self.pushButton_2.clicked.connect(self.showResult)

    def showVector(self):
        self.lineEdit.clear()
        s=''
        v=[]
        n=self.spinBox.value()
        nabors = self.spinBox_2.value()
        if n==0:
            return
        if nabors == 0:
            return
        n=2**n
        def createF(nab):
            ss = ''
            while nab>0:
                s=''
                v=[]
                for i in range(n):
                    v.append(random.randint(0, 1))
                s = " ".join(str(x) for x in v)
                s = s.replace(' ', '')
                nab = nab - 1
                if nab==0:
                    ss=ss+s
                else:
                    ss=ss+s+', '
            return ss
        s=createF(nabors)
        self.lineEdit.setText(str(s))

    def showResult(self):
        if self.lineEdit.text()=='':
            self.label.setText('Набор не выдан!')
            return
        if ((self.radioButton.isChecked()==False) & (self.radioButton_2.isChecked()==False)):
            self.label.setText('Выберите, полный или нет!')
            return
        if ((self.radioButton_2.isChecked()) & (self.checkBox.isChecked()==False) & (self.checkBox_2.isChecked()==False) &
        (self.checkBox_3.isChecked()==False) & (self.checkBox_4.isChecked()==False) & (self.checkBox_5.isChecked()==False)):
            self.label.setText('Выберите замкнутые классы!')
            return
        str = self.lineEdit.text()
        str = str.replace(', ', '')
        v = list(str)
        v = [int(i) for i in v]
        n = self.spinBox.value()
        nabors = self.spinBox_2.value()
        resvec=array('i',[0,0,0,0,0])
        nper=2**n
        k=0
        resdl=0
        while k<(nper*nabors):
            resvec[0]=resvec[0]+(T0(v[k:k+nper]))
            resvec[1]=resvec[1]+(T1(v[k:k+nper]))
            resvec[2]=resvec[2]+(S(v[k:k+nper]))
            resvec[3]=resvec[3]+(M(n, v[k:k+nper]))
            resvec[4]=resvec[4]+(L(v[k:k+nper]))
            k=k+nper
            resdl=resdl+5

        if self.radioButton.isChecked():
            for i in resvec:
                if i==nabors:
                    self.label.setText('Ошибка!')
                    return

        if self.radioButton_2.isChecked():
            if self.checkBox.isChecked():
                if resvec[0]!=nabors:
                    self.label.setText('Ошибка!')
                    return
            if self.checkBox_2.isChecked():
                if resvec[1]!=nabors:
                    self.label.setText('Ошибка!')
                    return
            if self.checkBox_3.isChecked():
                if resvec[2]!=nabors:
                    self.label.setText('Ошибка!')
                    return
            if self.checkBox_4.isChecked():
                if resvec[3]!=nabors:
                    self.label.setText('Ошибка!')
                    return
            if self.checkBox_5.isChecked():
                if resvec[4]!=nabors:
                    self.label.setText('Ошибка!')
                    return
        self.label.setText('Правильно!')
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
