import sys
from PyQt5 import QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fortep.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 41, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 30, 41, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 30, 41, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 30, 41, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 30, 41, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 30, 41, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 30, 41, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 30, 41, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(170, 30, 41, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 30, 41, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 90, 351, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фортепиано"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "10"))
        self.pushButton_4.setText(_translate("MainWindow", "8"))
        self.pushButton_5.setText(_translate("MainWindow", "7"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_8.setText(_translate("MainWindow", "9"))
        self.pushButton_9.setText(_translate("MainWindow", "4"))
        self.pushButton_10.setText(_translate("MainWindow", "3"))
        self.label.setText(_translate("MainWindow", "Кнопки на клавиатуре соответствуют названиям кнопок"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.player = QtMultimedia.QMediaPlayer()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.song)
        self.pushButton_2.clicked.connect(self.song)
        self.pushButton_3.clicked.connect(self.song)
        self.pushButton_4.clicked.connect(self.song)
        self.pushButton_5.clicked.connect(self.song)
        self.pushButton_6.clicked.connect(self.song)
        self.pushButton_7.clicked.connect(self.song)
        self.pushButton_8.clicked.connect(self.song)
        self.pushButton_9.clicked.connect(self.song)
        self.pushButton_10.clicked.connect(self.song)

    def song(self, n=None):
        songs = ['guitar/g1.mp3', 'guitar/g2.mp3', 'guitar/g3.mp3', 'guitar/g4.mp3', 'guitar/g5.mp3', 'guitar/g6.mp3',
                 'guitar/g7.mp3', 'guitar/g8.mp3', 'guitar/g9.mp3', 'guitar/g10.mp3']
        if n:
            index = n - 1
        else:
            index = int(self.sender().text()) - 1
        self.load_mp3(songs[index])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.song(1)
        if event.key() == Qt.Key_2:
            self.song(2)
        if event.key() == Qt.Key_3:
            self.song(3)
        if event.key() == Qt.Key_4:
            self.song(4)
        if event.key() == Qt.Key_5:
            self.song(5)
        if event.key() == Qt.Key_6:
            self.song(6)
        if event.key() == Qt.Key_7:
            self.song(7)
        if event.key() == Qt.Key_8:
            self.song(8)
        if event.key() == Qt.Key_9:
            self.song(9)
        if event.key() == Qt.Key_0:
            self.song(10)

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player.setMedia(content)
        self.player.play()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
