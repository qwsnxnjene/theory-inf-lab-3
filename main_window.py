# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1508, 850)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textOriginal = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textOriginal.setGeometry(QtCore.QRect(40, 60, 641, 321))
        self.textOriginal.setObjectName("textOriginal")
        self.textCoded = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textCoded.setGeometry(QtCore.QRect(890, 60, 591, 321))
        self.textCoded.setObjectName("textCoded")
        self.openFileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(720, 90, 131, 41))
        self.openFileButton.setObjectName("openFileButton")
        self.codeTextButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.codeTextButton.setEnabled(False)
        self.codeTextButton.setGeometry(QtCore.QRect(720, 160, 131, 41))
        self.codeTextButton.setObjectName("codeTextButton")
        self.saveCodedTextButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saveCodedTextButton.setEnabled(False)
        self.saveCodedTextButton.setGeometry(QtCore.QRect(686, 230, 201, 41))
        self.saveCodedTextButton.setObjectName("saveCodedTextButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(900, 30, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 420, 131, 16))
        self.label_3.setObjectName("label_3")
        self.textCoded_2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textCoded_2.setGeometry(QtCore.QRect(890, 450, 591, 321))
        self.textCoded_2.setObjectName("textCoded_2")
        self.decodeTextButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.decodeTextButton.setEnabled(False)
        self.decodeTextButton.setGeometry(QtCore.QRect(720, 550, 131, 41))
        self.decodeTextButton.setObjectName("decodeTextButton")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(900, 420, 161, 16))
        self.label_4.setObjectName("label_4")
        self.textOriginal_2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textOriginal_2.setGeometry(QtCore.QRect(40, 450, 641, 321))
        self.textOriginal_2.setObjectName("textOriginal_2")
        self.openCodedFileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.openCodedFileButton.setGeometry(QtCore.QRect(720, 480, 131, 41))
        self.openCodedFileButton.setObjectName("openCodedFileButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1508, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа 3"))
        self.openFileButton.setText(_translate("MainWindow", "Открыть файл"))
        self.codeTextButton.setText(_translate("MainWindow", "Закодировать текст"))
        self.saveCodedTextButton.setText(_translate("MainWindow", "Сохранить закодированный текст"))
        self.label.setText(_translate("MainWindow", "Исходный текст:"))
        self.label_2.setText(_translate("MainWindow", "Закодированный текст:"))
        self.label_3.setText(_translate("MainWindow", "Исходный код:"))
        self.decodeTextButton.setText(_translate("MainWindow", "Декодировать текст"))
        self.label_4.setText(_translate("MainWindow", "Декодированный текст:"))
        self.openCodedFileButton.setText(_translate("MainWindow", "Открыть файл"))
