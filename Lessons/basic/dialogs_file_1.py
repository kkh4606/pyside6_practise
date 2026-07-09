import sys
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
)
from pathlib import Path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        open_btn = QPushButton("Open file")
        open_btn.clicked.connect(self.get_filename)

        self.setCentralWidget(open_btn)

    def get_filename(self, s):

        file_filters = [
            "Portable Network Graphics files (*.png)",
            "Text files (*.txt)",
            "Comma Separated Values (*.csv)",
            "All files (*.*)",
        ]

        initial_filter = file_filters[1]

        filters = ";;".join(file_filters)
        filename, selected_filter = QFileDialog.getOpenFileName(
            self, "select a text file", filter=filters, selectedFilter=initial_filter
        )

        print(filename)
        print(selected_filter)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
