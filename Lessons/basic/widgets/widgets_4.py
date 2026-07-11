from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        widget = QComboBox()

        widget.setEditable(True)
        widget.addItems(["C", "B", "A"])

        widget.setInsertPolicy(QComboBox.InsertAlphabetically)

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, index):
        print("index: ", index)

    def text_changed(self, item):
        print("item: ", item)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
