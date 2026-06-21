import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QDialog,
    QLineEdit,
    QHBoxLayout,
    QGridLayout,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel,
)

from custom_dialog import CustomDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        btn = QPushButton("click me for a dialog")
        btn.clicked.connect(self.btn_clicked)
        self.setCentralWidget(btn)

    def btn_clicked(self, s):

        dlg = CustomDialog(self)

        if dlg.exec():
            print("success")
        else:
            print("cancel")
        # dlg = QDialog(self)
        # dlg.setWindowTitle("Hello")
        #
        # QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        #
        # self.btn_box = QDialogButtonBox(QBtn)
        # self.btn_box.accepted.connect(self.accept)
        # self.btn_box.rejected.connect((self.reject))
        #
        # layout = QVBoxLayout()
        #
        # message = QLabel("Something happened, is that OK?")
        # layout.addWidget(message)
        # layout.addWidget(self.btn_box)
        #
        # dlg.setLayout(layout)
        #
        # dlg.exec()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
