import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

from Lessons.basic.dialogs_2 import CustomDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        btn = QPushButton("Press me for a dialog")
        btn.clicked.connect(self.btn_clicked)

        self.setCentralWidget(btn)

    def btn_clicked(self, s):

        dlg = CustomDialog(self)
        dlg.exec()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
