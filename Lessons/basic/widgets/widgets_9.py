import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDial, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        widget = QDial()

        widget.setRange(-10, 100)

        self.setCentralWidget(widget)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_relased)

    def value_changed(self, i):
        print("value", i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("pressed")

    def slider_relased(self):
        print("released")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
