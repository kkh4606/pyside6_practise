import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")

        btn = QPushButton("Click me for dialog")
        btn.clicked.connect(self.button_clicked)

        self.setCentralWidget(btn)

    def button_clicked(self, s):

        button = QMessageBox.critical(
            self,
            "Question dialog",
            "This is a question dialog",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.NoAll,
        )

        # dlg = QMessageBox(self)
        # dlg.setWindowTitle("I have a question")
        # dlg.setText("This is a question dialog")
        # dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # dlg.setIcon(QMessageBox.Question)
        # button = dlg.exec()

        if button == QMessageBox.Discard:
            print("Discard")
        elif button == QMessageBox.NoToAll:
            print("NoToAll")
        else:
            print("Ignore")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
