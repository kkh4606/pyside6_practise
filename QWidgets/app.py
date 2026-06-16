import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QSlider,
    QSpinBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        #
        # label = QLabel()
        #
        # label.setPixmap(QPixmap("Gotje.jpg"))
        #
        # label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #
        # label.setScaledContents(True)

        checkbox = QCheckBox("This is checkbox")
        checkbox.setCheckState(Qt.CheckState.Checked)

        checkbox.stateChanged.connect(self.show_state)

        self.setCentralWidget(checkbox)

    def show_state(self, state):
        print(state == Qt.CheckState.Checked.value)


app = QApplication(sys.argv)

window = MainWindow()

window.show()


app.exec()
