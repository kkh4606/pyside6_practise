import sys

import PySide6.QtWidgets
from PySide6.QtWidgets import QApplication, QPushButton, QWidget
from ui_widget import Ui_Form


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 455, 300, 350)
        self.setMaximumHeight(450)

        self.btn_0.clicked.connect(self.on_button_click)
        self.btn_1.clicked.connect(self.on_button_click)
        self.btn_2.clicked.connect(self.on_button_click)
        self.btn_3.clicked.connect(self.on_button_click)
        self.btn_4.clicked.connect(self.on_button_click)
        self.btn_5.clicked.connect(self.on_button_click)
        self.btn_6.clicked.connect(self.on_button_click)
        self.btn_7.clicked.connect(self.on_button_click)
        self.btn_8.clicked.connect(self.on_button_click)
        self.btn_9.clicked.connect(self.on_button_click)
        self.btn_float.clicked.connect(self.on_button_click)

        self.btn_add.clicked.connect(self.on_button_click)
        self.btn_sub.clicked.connect(self.on_button_click)
        self.btn_mul.clicked.connect(self.on_button_click)
        self.btn_div.clicked.connect(self.on_button_click)

        self.btn_cls.clicked.connect(self.on_button_click)
        self.btn_equal.clicked.connect(self.on_button_click)

    def on_button_click(self):
        btn = self.sender()

        print(btn.text())

        current_text = self.d.text()

        if current_text == "0":
            current_text = ""
        if btn.text() == "=":
            try:
                result = str(eval(current_text))
                self.d.setText(result)
            except ZeroDivisionError:
                self.d.setText("Can't divide by zero")
            except Exception as e:
                self.d.setText(("Error: Invalid expression"))
        else:

            if (
                len(current_text) > 0
                and btn.text() in "+-*/."
                and current_text[-1] in "+-*/."
            ):
                return
            self.d.setText(current_text + btn.text())

        if btn.text() == "C":
            self.d.setText("0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()

    app.exec()
