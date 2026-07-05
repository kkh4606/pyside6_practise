import sys

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QHBoxLayout,
    QCheckBox,
    QRadioButton,
    QApplication,
    QFormLayout,
    QMainWindow,
    QTextEdit,
)


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Replace")

        self.textedit = QTextEdit()

        main_layout = QVBoxLayout()

        form_layout = QFormLayout()

        s_lineedit = QLineEdit()
        r_lineedit = QLineEdit()

        form_layout.addRow(QLabel("Find what"), s_lineedit)
        form_layout.addRow(QLabel("Replace with"), r_lineedit)

        # main_layout.addLayout(v_layout)

        self.setLayout(form_layout)


app = QApplication(sys.argv)

window = Test()
window.show()

app.exec()
