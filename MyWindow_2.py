import sys
import playsound

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_instruments()
        self.setupUi()

    def setupUi(self):
        self.resize(401, 267)
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.204, y1:0.773, x2:0.757548, y2:0, stop:0 rgba(43, 93, 184, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(self)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 120, 101, 51))
        self.pushButton.clicked.connect(self.perehod1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 120, 91, 51))
        self.pushButton_2.clicked.connect(self.perehod)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 20, 201, 61))
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 21))
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

    def init_instruments(self):
        self.piano = Piano(self)
        self.organ = Organ(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>лораве</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Орган"))
        self.pushButton_2.setText(_translate("MainWindow", "Фортепьяно"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-style:italic; text-decoration: underline; color:#0f0f0f;\">На чём бы вы хотели сыграть?</span></p></body></html>"))

    def perehod(self):
        self.piano.show()
        self.hide()

    def perehod1(self):
        self.organ.show()
        self.hide()


class Piano(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)

        conv_table = [1, 3, 5, 6, 8, 10, 12]
        for n in range(7):
            button = QtWidgets.QPushButton(self.centralwidget)
            button.setGeometry(QtCore.QRect(20 + 80 * n, 120, 81, 251))
            button.setStyleSheet("background-color: rgb(255, 255, 255)")
            button.clicked.connect(lambda void, ind=conv_table[n]: self.play_normal(ind))

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 120, 51, 161))
        self.pushButton_8.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_8.clicked.connect(self.play8)
        self.pushButton_8.setText("")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 120, 51, 161))
        self.pushButton_9.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_9.clicked.connect(self.play9)
        self.pushButton_9.setText("")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(310, 120, 51, 161))
        self.pushButton_10.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_10.clicked.connect(self.play10)
        self.pushButton_10.setText("")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(390, 120, 51, 161))
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_11.clicked.connect(self.play11)
        self.pushButton_11.setText("")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(470, 120, 51, 161))
        self.pushButton_12.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_12.clicked.connect(self.play12)
        self.pushButton_12.setText("")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    @staticmethod
    def play_normal(ind):
        playsound.playsound('ramsr-' + str(ind) + '.mp3', True)

    def play8(self):
        playsound.playsound('ramsran-2.2.mp3', True)
        # print(1)

    def play9(self):
        playsound.playsound('ramsr-4.mp3', True)
        # print(1)

    def play10(self):
        playsound.playsound('ramsr-7.mp3', True)
        # print(1)

    def play11(self):
        playsound.playsound('ramsr-9.mp3', True)
        # print(1)

    def play12(self):
        playsound.playsound('ramsr-11.mp3', True)
        # print(1)

    def closeEvent(self, event):
        self.parent.show()
        self.hide()
        event.ignore()


class Organ(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)

        conv_table = [1, 3, 5, 6, 8, 10, 12]
        for n in range(7):
            button = QtWidgets.QPushButton(self.centralwidget)
            button.setGeometry(QtCore.QRect(20 + 80 * n, 120, 81, 251))
            button.setStyleSheet("background-color: rgb(255, 255, 255)")
            button.clicked.connect(lambda void, ind=conv_table[n]: self.play_normal(ind))

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 120, 51, 161))
        self.pushButton_8.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_8.clicked.connect(self.play8)
        self.pushButton_8.setText("")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 120, 51, 161))
        self.pushButton_9.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_9.clicked.connect(self.play9)
        self.pushButton_9.setText("")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(310, 120, 51, 161))
        self.pushButton_10.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_10.clicked.connect(self.play10)
        self.pushButton_10.setText("")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(390, 120, 51, 161))
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_11.clicked.connect(self.play11)
        self.pushButton_11.setText("")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(470, 120, 51, 161))
        self.pushButton_12.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_12.clicked.connect(self.play12)
        self.pushButton_12.setText("")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    @staticmethod
    def play_normal(ind):
        playsound.playsound(str(ind) + '.mp3', True)

    def play8(self):
        playsound.playsound('2.mp3', True)
        # print(1)

    def play9(self):
        playsound.playsound('4.mp3', True)
        # print(1)

    def play10(self):
        playsound.playsound('7.mp3', True)
        # print(1)

    def play11(self):
        playsound.playsound('9.mp3', True)
        # print(1)

    def play12(self):
        playsound.playsound('11.mp3', True)
        # print(1)

    def closeEvent(self, event):
        self.parent.show()
        self.hide()
        event.ignore()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    main = MainWindow()  # Durdom()
    main.show()
    sys.exit(app.exec())
