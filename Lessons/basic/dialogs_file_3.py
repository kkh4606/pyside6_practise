import sys
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)

FILE_FILTERS = [
    "Portable Network Graphics files (*.png)",
    "Text files (*.txt)",
    "Comma Separated Values (*.csv)",
    "All files (*)",
]


import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout = QVBoxLayout()
        button1 = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)
        button2 = QPushButton("Open files")
        button2.clicked.connect(self.get_filenames)
        layout.addWidget(button2)
        button3 = QPushButton("Save file")
        button3.clicked.connect(self.get_save_filename)
        layout.addWidget(button3)
        button4 = QPushButton("Select folder")
        button4.clicked.connect(self.get_folder)
        layout.addWidget(button4)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_filename(self):
        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)

        filename, selected_filter = QFileDialog.getOpenFileName(
            self, caption, initial_dir, filter=filters, selectedFilter=initial_filter
        )

        if filename:
            with open(filename, "r", encoding="UTF-8") as f:
                data = f.read()
            print(data)

    def get_filenames(self):

        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)

        filenames, selected_filter = QFileDialog.getOpenFileNames(
            self, caption, initial_dir, filter=filters, selectedFilter=initial_filter
        )

        print(filenames)

    def get_save_filename(self):
        flag = False
        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)

        filename, selected_filter = QFileDialog.getSaveFileName(
            self, caption, initial_dir, filter=filters, selectedFilter=initial_filter
        )

        if filename:
            if os.path.exists(filename):

                write_confirmed = QMessageBox.question(
                    self,
                    "Overwrite File?",
                    f"The file {filename} exists.Do you want to overwrite",
                )

                if write_confirmed == QMessageBox.Yes:
                    flag = True

            else:

                flag = True
            if flag:

                print("this code processed...")

                with open(filename, "w") as f:
                    f.write("File content new text testing v2 ...")

    def get_folder(self):
        pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
