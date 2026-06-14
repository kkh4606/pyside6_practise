import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_widget import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("First Game")

        self.pushButton.clicked.connect(self.click)

    def click(self):
        print("you clicked")
        X_turn, O_turn = True, False

        if not self.pushButton.text():

            if X_turn:

                self.pushButton.setText("X")
                X_turn, O_turn = O_turn, X_turn
            else:
                self.pushButton.setText("O")
                X_turn, O_turn = O_turn, X_turn


app = QApplication([])

window = MainWindow()
window.show()

sys.exit(app.exec())
