import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
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


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
