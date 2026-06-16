# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auto_mapper_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(428, 380)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(18)
        font.setBold(True)
        Form.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, -10, 250, 60))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 10, 150, 30))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(15)
        font2.setBold(False)
        self.pushButton.setFont(font2)
        self.list_widget = QListWidget(Form)
        self.list_widget.setObjectName(u"list_widget")
        self.list_widget.setGeometry(QRect(10, 50, 411, 321))
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(8)
        font3.setBold(True)
        self.list_widget.setFont(font3)
        self.list_widget.setStyleSheet(u"background-color: black;\n"
"color: white")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"AutoMapper Kits ID", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"open folder", None))
    # retranslateUi

