from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 81, 251))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 120, 81, 251))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 120, 81, 251))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 120, 81, 251))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 120, 81, 251))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 120, 81, 251))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(500, 120, 81, 251))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(70, 120, 51, 161))
        self.pushButton_9.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(150, 120, 51, 161))
        self.pushButton_10.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(310, 120, 51, 161))
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(400, 120, 51, 161))
        self.pushButton_12.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(470, 120, 51, 161))
        self.pushButton_13.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

import sys
from untitled import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(950, 500, 950, 500)
        self.setWindowTitle('Пианинко')

        btn = QPushButton('До', self)
        btn.resize(100, 300)
        btn.move(100, 100)

        btn1 = QPushButton('Ре', self)
        btn1.resize(100, 300)
        btn1.move(200, 100)

        btn2 = QPushButton('Ми', self)
        btn2.resize(100, 300)
        btn2.move(300, 100)

        btn3 = QPushButton('Фа', self)
        btn3.resize(100, 300)
        btn3.move(400, 100)

        btn4 = QPushButton('Соль', self)
        btn4.resize(100, 300)
        btn4.move(500, 100)

        btn5 = QPushButton('Ля', self)
        btn5.resize(100, 300)
        btn5.move(600, 100)

        btn6 = QPushButton('Си', self)
        btn6.resize(100, 300)
        btn6.move(700, 100)

        btn8 = QPushButton(self)
        btn8.resize(50, 180)
        btn8.move(175, 100)

        btn9 = QPushButton(self)
        btn9.resize(50, 180)
        btn9.move(275, 100)

        btn10 = QPushButton(self)
        btn10.resize(50, 180)
        btn10.move(475, 100)

        btn11 = QPushButton(self)
        btn11.resize(50, 180)
        btn11.move(575, 100)

        btn12 = QPushButton(self)
        btn12.resize(50, 180)
        btn12.move(675, 100)



class Dyrdom(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dyrdom()
    ex.show()
    sys.exit(app.exec())
