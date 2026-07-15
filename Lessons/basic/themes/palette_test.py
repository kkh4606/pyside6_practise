from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
import sys

app = QApplication(sys.argv)
app.setStyle("Fusion")

palette = QPalette()

palette.setColor(QPalette.Window, QColor(0, 128, 225))

palette.setColor(QPalette.WindowText, QColor(0, 0, 0))


app.setPalette(palette)

window = QLabel("Palette Test")
window.setAlignment(Qt.AlignmentFlag.AlignCenter)

font = window.font()
font.setPointSize(20)
window.setFont(font)
window.show()

app.exec()
