# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 580)
        MainWindow.setMinimumSize(QSize(400, 580))
        MainWindow.setMaximumSize(QSize(400, 580))
        MainWindow.setStyleSheet(u"background-color: rgb(88, 88, 88);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{	\n"
"    border-style :outset;\n"
"	border-color:#ffffff;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"}")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        self.logo.setGeometry(QRect(90, 50, 221, 110))
        self.logo.setStyleSheet(u"QLabel{\n"
"    border-style :outset;\n"
"	border-color: rgb(26, 120, 179);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"}")
        self.logo.setAlignment(Qt.AlignCenter)
        self.Account = QLineEdit(self.centralwidget)
        self.Account.setObjectName(u"Account")
        self.Account.setGeometry(QRect(40, 280, 321, 31))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)
        self.Account.setFont(font)
        self.Account.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Account.setStyleSheet(u"QLineEdit{\n"
" border: 1px solid #A0A0A0;\n"
" border-radius: 3px;\n"
"color: rgb(222, 222, 222);\n"
" selection-color: #F2F2F2;\n"
"}\n"
"QLineEdit:hover{\n"
" border: 1px solid rgb(19, 23, 255);.\n"
" border-radius: 3px;\n"
" color: #F2F2F2;\n"
" selection-color: #F2F2F2\n"
"}")
        self.Account.setText(u"")
        self.Account.setEchoMode(QLineEdit.Normal)
        self.Account.setReadOnly(False)
        self.Account.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.Account.setClearButtonEnabled(True)
        self.Password = QLineEdit(self.centralwidget)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(40, 370, 321, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.Password.setFont(font1)
        self.Password.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Password.setStyleSheet(u"QLineEdit{\n"
" border: 1px solid #A0A0A0;\n"
" border-radius: 3px;\n"
"color: rgb(222, 222, 222);\n"
" selection-color: #F2F2F2;\n"
"}\n"
"QLineEdit:hover{\n"
" border: 1px solid rgb(19, 23, 255);.\n"
" border-radius: 3px;\n"
" color: #F2F2F2;\n"
" selection-color: #F2F2F2\n"
"}")
        self.Password.setText(u"")
        self.Password.setEchoMode(QLineEdit.Password)
        self.Password.setReadOnly(False)
        self.Password.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.Password.setClearButtonEnabled(False)
        self.loginAccount = QPushButton(self.centralwidget)
        self.loginAccount.setObjectName(u"loginAccount")
        self.loginAccount.setEnabled(True)
        self.loginAccount.setGeometry(QRect(210, 490, 151, 41))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.loginAccount.setFont(font2)
        self.loginAccount.setCursor(QCursor(Qt.ArrowCursor))
        self.loginAccount.setStyleSheet(u"QPushButton{\n"
"	border-style :outset;\n"
"	border-color: rgb(26, 120, 179);\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"	color: rgb(250, 250, 250);\n"
"	background-color: rgb(102, 102, 102);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style :outset;\n"
"	border-color: rgb(26, 120, 179);\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"	color: rgb(102, 102, 102);\n"
"	background-color: rgb(250, 250, 250);\n"
"}")
        self.loginAccount.setCheckable(False)
        self.loginAccount.setChecked(False)
        self.loginAccount.setFlat(False)
        self.loginVisitor = QPushButton(self.centralwidget)
        self.loginVisitor.setObjectName(u"loginVisitor")
        self.loginVisitor.setGeometry(QRect(40, 490, 151, 41))
        self.loginVisitor.setFont(font2)
        self.loginVisitor.setStyleSheet(u"QPushButton{\n"
"	border-style :outset;\n"
"	border-color: rgb(26, 120, 179);\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"	color: rgb(250, 250, 250);\n"
"	background-color: rgb(102, 102, 102);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style :outset;\n"
"	border-color: rgb(26, 120, 179);\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"	color: rgb(102, 102, 102);\n"
"	background-color: rgb(250, 250, 250);\n"
"}")
        self.loginSuggestion = QLabel(self.centralwidget)
        self.loginSuggestion.setObjectName(u"loginSuggestion")
        self.loginSuggestion.setGeometry(QRect(50, 440, 301, 31))
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.loginSuggestion.setFont(font3)
        self.loginSuggestion.setStyleSheet(u"QLabel{\n"
" border: 0px solid #A0A0A0;\n"
" border-radius: 0px;\n"
"	color: rgb(223, 79, 53);\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.loginAccount.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.Account.setInputMask("")
        self.Account.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Myself Account", None))
        self.Password.setInputMask("")
        self.Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginAccount.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.loginVisitor.setText(QCoreApplication.translate("MainWindow", u"Visitor", None))
        self.loginSuggestion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:16pt;\"><br/></span></p></body></html>", None))
    # retranslateUi

