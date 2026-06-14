# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo_app_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 196)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.task_input = QLineEdit(self.centralwidget)
        self.task_input.setObjectName(u"task_input")
        self.task_input.setGeometry(QRect(10, 10, 550, 30))
        self.add_task_btn = QPushButton(self.centralwidget)
        self.add_task_btn.setObjectName(u"add_task_btn")
        self.add_task_btn.setGeometry(QRect(10, 45, 75, 24))
        self.main_layout_vertical = QWidget(self.centralwidget)
        self.main_layout_vertical.setObjectName(u"main_layout_vertical")
        self.main_layout_vertical.setGeometry(QRect(10, 90, 551, 71))
        self.verticalLayout = QVBoxLayout(self.main_layout_vertical)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.task_layout = QWidget(self.main_layout_vertical)
        self.task_layout.setObjectName(u"task_layout")
        self.horizontalLayout = QHBoxLayout(self.task_layout)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.task_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_task_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

