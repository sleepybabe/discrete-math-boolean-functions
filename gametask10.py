from PyQt5 import QtCore, QtGui, QtWidgets
import random

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
        self.lineEdit.setGeometry(QtCore.QRect(210, 55, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(150, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(300, 170, 70, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(450, 170, 71, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(225, 240, 41, 31))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(375, 240, 41, 31))
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 290, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 360, 231, 41))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(400, 20, 42, 21))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 191, 41))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Замкнутые классы"))
        self.pushButton.setText(_translate("MainWindow", "Выдать вектор"))
        self.checkBox.setText(_translate("MainWindow", "T0"))
        self.checkBox_2.setText(_translate("MainWindow", "T1"))
        self.checkBox_3.setText(_translate("MainWindow", "S"))
        self.checkBox_4.setText(_translate("MainWindow", "M"))
        self.checkBox_5.setText(_translate("MainWindow", "L"))
        self.pushButton_2.setText(_translate("MainWindow", "Проверить"))
        self.label_2.setText(_translate("MainWindow", "Количество переменных:"))

    def add_functions(self):
        self.pushButton.clicked.connect(self.showVector)
        self.pushButton_2.clicked.connect(self.showResult)

    def showVector(self):
        self.lineEdit.clear()
        s=''
        v=[]
        n=self.spinBox.value()
        if n==0:
            return
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
        help=0
        strvec=self.lineEdit.text()
        v=list(strvec)
        v=[int(i) for i in v]
        per = self.spinBox.value()
        resvec=[]
        resvec.append(T0(v))
        resvec.append(T1(v))
        resvec.append(S(v))
        resvec.append(M(per,v))
        resvec.append(L(v))
        if self.checkBox.isChecked():
            help=1
            if resvec[0]==0:
                self.label.setText('Ошибка!')
                return
        if self.checkBox_2.isChecked():
            help=1
            if resvec[1]==0:
                self.label.setText('Ошибка!')
                return
        if self.checkBox_3.isChecked():
            help=1
            if resvec[2]==0:
                self.label.setText('Ошибка!')
                return
        if self.checkBox_4.isChecked():
            help=1
            if resvec[3]==0:
                self.label.setText('Ошибка!')
                return
        if self.checkBox_5.isChecked():
            help=1
            if resvec[4]==0:
                self.label.setText('Ошибка!')
                return
        k=0
        for i in range(len(resvec)):
            if resvec[i]==0:
                k=k+1

        if help==1:
            self.label.setText('Правильно!')
            return

        if k==5:
            self.label.setText('Правильно!')
            return
        else:
            self.label.setText('Ошибка!')
            return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
