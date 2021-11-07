# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Main.ui'
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
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 652)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setMaximumSize(QSize(1100, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(202, 199, 195);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 50))
        self.topBar.setMaximumSize(QSize(16777215, 50))
        self.topBar.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.topBar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMinimumSize(QSize(0, 50))
        self.frame_toggle.setMaximumSize(QSize(70, 50))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(30, 30, 40);\n"
"\n"
"")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toggle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.button_toggle = QPushButton(self.frame_toggle)
        self.button_toggle.setObjectName(u"button_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_toggle.sizePolicy().hasHeightForWidth())
        self.button_toggle.setSizePolicy(sizePolicy)
        self.button_toggle.setMinimumSize(QSize(24, 0))
        self.button_toggle.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.button_toggle.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.button_toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.topBar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 50))
        self.frame_top.setStyleSheet(u"	background-color: rgb(30, 30, 40);\n"
"")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_top)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 151, 31))
        font = QFont()
        font.setFamilies([u"Monotype Corsiva"])
        font.setPointSize(16)
        font.setItalic(True)
        self.label.setFont(font)
        self.hintbox = QLabel(self.frame_top)
        self.hintbox.setObjectName(u"hintbox")
        self.hintbox.setGeometry(QRect(190, 10, 831, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.hintbox.setFont(font1)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.topBar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"	background-color: rgb(30, 30, 40);\n"
"")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.button_page_search = QPushButton(self.frame_top_menus)
        self.button_page_search.setObjectName(u"button_page_search")
        self.button_page_search.setMinimumSize(QSize(0, 55))
        self.button_page_search.setMaximumSize(QSize(16777215, 55))
        self.button_page_search.setStyleSheet(u"QPushButton{\n"
"    border: 0px solid;\n"
"	color: rgb(250, 250, 250);\n"
"	background-color: rgb(30, 30, 40);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    border: 0px solid;\n"
"	color: rgb(250, 250, 250);\n"
"	background-color: rgb(50, 50, 50);;\n"
"\n"
"\n"
"}")

        self.verticalLayout_4.addWidget(self.button_page_search)

        self.button_page_schedule = QPushButton(self.frame_top_menus)
        self.button_page_schedule.setObjectName(u"button_page_schedule")
        self.button_page_schedule.setMinimumSize(QSize(0, 55))
        self.button_page_schedule.setMaximumSize(QSize(16777215, 55))
        self.button_page_schedule.setStyleSheet(u"QPushButton{\n"
"    border: 0px solid;\n"
"	color: rgb(250, 250, 250);\n"
"	background-color: rgb(30, 30, 40);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 0px solid;\n"
"	color: rgb(250, 250, 250);\n"
"	background-color: rgb(50, 50, 50);;\n"
"\n"
"}")

        self.verticalLayout_4.addWidget(self.button_page_schedule)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.button_page_setting = QPushButton(self.frame_left_menu)
        self.button_page_setting.setObjectName(u"button_page_setting")
        self.button_page_setting.setMinimumSize(QSize(0, 40))
        self.button_page_setting.setMaximumSize(QSize(16777215, 40))
        self.button_page_setting.setStyleSheet(u"QPushButton{\n"
"    border: 0px solid;\n"
"	color: rgb(250, 250, 250);\n"
"	background-color: rgb(30, 30, 40);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    border: 0px solid;\n"
"    color: rgb(250, 250, 250);\n"
"	background-color: rgb(50, 50, 50);\n"
"}")

        self.verticalLayout_3.addWidget(self.button_page_setting)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"background-color: rgb(147, 147, 147);")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(1030, 444))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.verticalLayout_5 = QVBoxLayout(self.page_search)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_search)
        self.frame.setObjectName(u"frame")
        font2 = QFont()
        font2.setPointSize(10)
        self.frame.setFont(font2)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(160, 20, 761, 61))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.search_input = QLineEdit(self.frame_2)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(16)
        self.search_input.setFont(font3)
        self.search_input.setStyleSheet(u"QLineEdit{\n"
" border: 1px solid #A0A0A0;\n"
" border-radius: 10px;\n"
"border-color: rgb(255, 255, 255);\n"
" selection-color: #F2F2F2;\n"
"}\n"
"QLineEdit:hover{\n"
" border: 1px solid rgb(19, 23, 255);.\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
" border-radius: 10px;\n"
" color: #F2F2F2;\n"
" selection-color: #F2F2F2\n"
"}")

        self.horizontalLayout_4.addWidget(self.search_input)

        self.search_button = QPushButton(self.frame_2)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(120, 40))
        self.search_button.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_4.addWidget(self.search_button)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 90, 1011, 481))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.search_listwidget_information = QListWidget(self.frame_3)
        QListWidgetItem(self.search_listwidget_information)
        QListWidgetItem(self.search_listwidget_information)
        QListWidgetItem(self.search_listwidget_information)
        QListWidgetItem(self.search_listwidget_information)
        QListWidgetItem(self.search_listwidget_information)
        QListWidgetItem(self.search_listwidget_information)
        QListWidgetItem(self.search_listwidget_information)
        QListWidgetItem(self.search_listwidget_information)
        self.search_listwidget_information.setObjectName(u"search_listwidget_information")
        self.search_listwidget_information.setMinimumSize(QSize(430, 0))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.search_listwidget_information.setFont(font4)
        self.search_listwidget_information.setStyleSheet(u" border: 3px solid #A0A0A0;\n"
"\n"
"border-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.search_listwidget_information)

        self.search_picture = QLabel(self.frame_3)
        self.search_picture.setObjectName(u"search_picture")
        self.search_picture.setMinimumSize(QSize(250, 350))

        self.horizontalLayout_5.addWidget(self.search_picture)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(250, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, -1)
        self.search_listwidget_all = QListWidget(self.frame_8)
        self.search_listwidget_all.setObjectName(u"search_listwidget_all")

        self.verticalLayout_7.addWidget(self.search_listwidget_all)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.search_download_all = QPushButton(self.frame_11)
        self.search_download_all.setObjectName(u"search_download_all")
        self.search_download_all.setMinimumSize(QSize(0, 30))
        self.search_download_all.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_10.addWidget(self.search_download_all)

        self.search_download_select = QPushButton(self.frame_11)
        self.search_download_select.setObjectName(u"search_download_select")
        self.search_download_select.setMinimumSize(QSize(0, 30))
        self.search_download_select.setStyleSheet(u"QPushButton{\n"
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
        self.search_download_select.setAutoDefault(False)

        self.horizontalLayout_10.addWidget(self.search_download_select)


        self.verticalLayout_7.addWidget(self.frame_11)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_5.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_search)
        self.page_schedule = QWidget()
        self.page_schedule.setObjectName(u"page_schedule")
        self.label_2 = QLabel(self.page_schedule)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 151, 51))
        self.label_2.setFont(font3)
        self.downloadlist = QListWidget(self.page_schedule)
        self.downloadlist.setObjectName(u"downloadlist")
        self.downloadlist.setGeometry(QRect(10, 70, 1001, 511))
        self.stackedWidget.addWidget(self.page_schedule)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.frame_4 = QFrame(self.page_setting)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(50, 50, 921, 281))
        self.frame_4.setStyleSheet(u"font: 12pt \"Consolas\";")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.setting_button_Download = QPushButton(self.frame_7)
        self.setting_button_Download.setObjectName(u"setting_button_Download")
        self.setting_button_Download.setMinimumSize(QSize(150, 40))
        self.setting_button_Download.setMaximumSize(QSize(150, 16777215))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        self.setting_button_Download.setFont(font5)
        self.setting_button_Download.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_6.addWidget(self.setting_button_Download)

        self.setting_label_Download = QLabel(self.frame_7)
        self.setting_label_Download.setObjectName(u"setting_label_Download")
        font6 = QFont()
        font6.setFamilies([u"Consolas"])
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        self.setting_label_Download.setFont(font6)

        self.horizontalLayout_6.addWidget(self.setting_label_Download)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.setting_button_FFMPEG = QPushButton(self.frame_5)
        self.setting_button_FFMPEG.setObjectName(u"setting_button_FFMPEG")
        self.setting_button_FFMPEG.setMinimumSize(QSize(150, 40))
        self.setting_button_FFMPEG.setMaximumSize(QSize(150, 16777215))
        self.setting_button_FFMPEG.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_7.addWidget(self.setting_button_FFMPEG)

        self.setting_label_FFMPEG = QLabel(self.frame_5)
        self.setting_label_FFMPEG.setObjectName(u"setting_label_FFMPEG")

        self.horizontalLayout_7.addWidget(self.setting_label_FFMPEG)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.setting_button_DownloadLog = QPushButton(self.frame_9)
        self.setting_button_DownloadLog.setObjectName(u"setting_button_DownloadLog")
        self.setting_button_DownloadLog.setMinimumSize(QSize(150, 40))
        self.setting_button_DownloadLog.setMaximumSize(QSize(150, 40))
        self.setting_button_DownloadLog.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_8.addWidget(self.setting_button_DownloadLog)

        self.setting_label_DownloadLog = QLabel(self.frame_9)
        self.setting_label_DownloadLog.setObjectName(u"setting_label_DownloadLog")

        self.horizontalLayout_8.addWidget(self.setting_label_DownloadLog)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.setting_button_MyselfLog = QPushButton(self.frame_6)
        self.setting_button_MyselfLog.setObjectName(u"setting_button_MyselfLog")
        self.setting_button_MyselfLog.setMinimumSize(QSize(150, 40))
        self.setting_button_MyselfLog.setMaximumSize(QSize(150, 40))
        self.setting_button_MyselfLog.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_9.addWidget(self.setting_button_MyselfLog)

        self.setting_label_MyselfLog = QLabel(self.frame_6)
        self.setting_label_MyselfLog.setObjectName(u"setting_label_MyselfLog")

        self.horizontalLayout_9.addWidget(self.setting_label_MyselfLog)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.button_exit = QPushButton(self.page_setting)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setGeometry(QRect(780, 510, 200, 50))
        self.button_exit.setMinimumSize(QSize(200, 50))
        self.button_exit.setMaximumSize(QSize(200, 50))
        font7 = QFont()
        font7.setPointSize(15)
        self.button_exit.setFont(font7)
        self.button_exit.setStyleSheet(u"QPushButton{\n"
"	border-style :outset;\n"
"	border-color: rgb(255, 83, 83);\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style :outset;\n"
"	border-color: rgb(26, 120, 179);\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"	color: rgb(102, 102, 102);\n"
"	background-color: rgb(255, 83, 83);\n"
"}")
        self.stackedWidget.addWidget(self.page_setting)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.label_4 = QLabel(self.frame_pages)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 12))
        self.label_4.setMaximumSize(QSize(16777215, 11))
        font8 = QFont()
        font8.setFamilies([u"Consolas"])
        self.label_4.setFont(font8)
        self.label_4.setStyleSheet(u"	background-color: rgb(107, 103, 125);")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.frame_pages)

        self.frame_pages.raise_()
        self.frame_left_menu.raise_()

        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_toggle.setText(QCoreApplication.translate("MainWindow", u"\u9078\u55ae", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">MyselfDownloader</span></p></body></html>", None))
        self.hintbox.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.button_page_search.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9801", None))
        self.button_page_schedule.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f09", None))
        self.button_page_setting.setText(QCoreApplication.translate("MainWindow", u"\u8a2d\u5b9a", None))
        self.search_input.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f38\u5165\u7db2\u5740\u6216ID", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"\u641c\u5c0b", None))

        __sortingEnabled = self.search_listwidget_information.isSortingEnabled()
        self.search_listwidget_information.setSortingEnabled(False)
        ___qlistwidgetitem = self.search_listwidget_information.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u540d\u7a31", None));
        ___qlistwidgetitem1 = self.search_listwidget_information.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u54c1\u985e\u578b", None));
        ___qlistwidgetitem2 = self.search_listwidget_information.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u9996\u64ad\u65e5\u671f", None));
        ___qlistwidgetitem3 = self.search_listwidget_information.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u51fa\u96c6\u6578", None));
        ___qlistwidgetitem4 = self.search_listwidget_information.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u539f\u8457\u4f5c\u8005", None));
        ___qlistwidgetitem5 = self.search_listwidget_information.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u5b98\u65b9\u7db2\u7ad9", None));
        ___qlistwidgetitem6 = self.search_listwidget_information.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u5099\u8a3b", None));
        ___qlistwidgetitem7 = self.search_listwidget_information.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u4ecb\u7d39", None));
        self.search_listwidget_information.setSortingEnabled(__sortingEnabled)

        self.search_picture.setText("")
        self.search_download_all.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u4e0b\u8f09", None))
        self.search_download_select.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f09\u9078\u53d6\u7684\u96c6\u6578", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f09\u6e05\u55ae", None))
        self.setting_button_Download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.setting_label_Download.setText("")
        self.setting_button_FFMPEG.setText(QCoreApplication.translate("MainWindow", u"FFMPEG", None))
        self.setting_label_FFMPEG.setText("")
        self.setting_button_DownloadLog.setText(QCoreApplication.translate("MainWindow", u"DownloadLog", None))
        self.setting_label_DownloadLog.setText("")
        self.setting_button_MyselfLog.setText(QCoreApplication.translate("MainWindow", u"MyselfLog", None))
        self.setting_label_MyselfLog.setText("")
        self.button_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7a0b\u5f0f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Registered by Patrickk | Please contact me if there is a bug | Discord: Patrickuuuu#0922", None))
    # retranslateUi

