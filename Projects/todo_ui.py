# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(508, 497)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.version = QLabel(self.centralwidget)
        self.version.setObjectName(u"version")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setItalic(False)
        self.version.setFont(font1)

        self.gridLayout.addWidget(self.version, 0, 2, 1, 1)

        self.todo_list_widget = QListWidget(self.centralwidget)
        self.todo_list_widget.setObjectName(u"todo_list_widget")
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(14)
        self.todo_list_widget.setFont(font2)
        self.todo_list_widget.setStyleSheet(u"background-color: #003366;\n"
"color: white")

        self.gridLayout.addWidget(self.todo_list_widget, 1, 0, 1, 3)

        self.input_box = QLineEdit(self.centralwidget)
        self.input_box.setObjectName(u"input_box")

        self.gridLayout.addWidget(self.input_box, 2, 0, 1, 2)

        self.add_btn = QPushButton(self.centralwidget)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setStyleSheet(u"background-color: rgb(0, 51, 102);\n"
"color: white;;")

        self.gridLayout.addWidget(self.add_btn, 2, 2, 1, 1)

        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")

        self.gridLayout.addWidget(self.exit_btn, 3, 2, 1, 1)

        self.toggle_btn = QPushButton(self.centralwidget)
        self.toggle_btn.setObjectName(u"toggle_btn")

        self.gridLayout.addWidget(self.toggle_btn, 3, 0, 1, 2)

        self.delete_btn = QPushButton(self.centralwidget)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.delete_btn, 4, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TODO APP", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MY TODO", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggle_btn.setText(QCoreApplication.translate("MainWindow", u"Toggle All", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

