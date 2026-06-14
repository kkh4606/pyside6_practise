from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        slider = QSlider(Qt.Orientation.Horizontal)

        slider.valueChanged.connect(self.value_changed)
        slider.sliderMoved.connect(self.slider_postition)

        slider.sliderPressed.connect(self.slider_pressed)
        slider.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(slider)

    def value_changed(self, value):
        print("value changed: ", value)

    def slider_postition(self, position):
        print(position)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


app = QApplication([])
window = MainWindow()
window.show()

app.exec()
