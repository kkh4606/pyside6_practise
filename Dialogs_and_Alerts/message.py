import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QMessageBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        btn = QPushButton("Press me for a dialog!")
        btn.clicked.connect(self.btn_clicked)

        self.setCentralWidget(btn)

    def btn_clicked(self):

        button = QMessageBox.critical(
            self,
            "Question dialog",
            "The longer message",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )

        if button == QMessageBox.Yes:
            print("Yes")
        else:
            print("No")

        # dlg = QMessageBox(self)
        #
        # dlg.setWindowTitle("I have a question!")
        # dlg.setText("This is a simple dialog")
        # dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # dlg.setIcon(QMessageBox.Warning)
        #
        # dlg.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
