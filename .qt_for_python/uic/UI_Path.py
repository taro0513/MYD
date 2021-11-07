# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Path.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 267)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 521, 271))
        self.frame.setStyleSheet(u"background-color: rgb(88, 88, 88);\n"
"border-radius: 3px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name = QLabel(self.frame)
        self.name.setObjectName(u"name")
        font = QFont()
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.name)

        self.path = QLabel(self.frame)
        self.path.setObjectName(u"path")
        font1 = QFont()
        font1.setFamilies([u"Microsoft JhengHei UI"])
        font1.setPointSize(11)
        self.path.setFont(font1)
        self.path.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.path)

        self.folder_input = QLineEdit(self.frame)
        self.folder_input.setObjectName(u"folder_input")
        self.folder_input.setMinimumSize(QSize(0, 30))
        self.folder_input.setStyleSheet(u"QLineEdit{\n"
"	font: 11pt \"Microsoft JhengHei UI\";\n"
" border: 1px solid ;\n"
"	color: rgb(222, 222, 222);\n"
"\n"
" border-radius: 10px;\n"
"border-color: rgb(255, 255, 255);\n"
" selection-color: #F2F2F2;\n"
"}\n"
"QLineEdit:hover{\n"
"	font: 11pt \"Microsoft JhengHei UI\";\n"
"\n"
" border: 1px solid rgb(19, 23, 255);.\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
" border-radius: 10px;\n"
"color: rgb(222, 222, 222);\n"
" selection-color: #F2F2F2\n"
"}")

        self.verticalLayout.addWidget(self.folder_input)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cancel = QPushButton(self.frame_2)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(0, 40))
        self.cancel.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.cancel)

        self.confirm = QPushButton(self.frame_2)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setMinimumSize(QSize(0, 40))
        self.confirm.setStyleSheet(u"QPushButton{\n"
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
        self.confirm.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.confirm)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u52d5\u6f2b\u540d\u7a31", None))
        self.path.setText(QCoreApplication.translate("MainWindow", u"Path: ", None))
        self.folder_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u65b0\u8cc7\u6599\u593e\u540d\u7a31", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.confirm.setText(QCoreApplication.translate("MainWindow", u"\u78ba\u8a8d\u8cc7\u6599\u593e\u540d\u7a31", None))
    # retranslateUi

