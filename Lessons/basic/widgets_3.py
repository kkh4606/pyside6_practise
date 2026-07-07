import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        check_box = QCheckBox("This is a checkbox")
        check_box.setCheckState(Qt.CheckState.Checked)

        check_box.stateChanged.connect(self.show_state)

        self.setCentralWidget(check_box)

    def show_state(self, s):
        print(s)

        # print(s == Qt.CheckState)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
