import sys
from PySide6.QtWidgets import (
    QApplication,
    QInputDialog,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QWidget,
    QLineEdit,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        btn1 = QPushButton("Integer")
        btn1.clicked.connect(self.get_an_int)

        btn2 = QPushButton("Float")
        btn2.clicked.connect(self.get_a_float)

        btn3 = QPushButton("String")
        btn3.clicked.connect(self.get_a_str_from_a_list)

        btn4 = QPushButton("Text")
        btn4.clicked.connect(self.get_a_str)

        btn5 = QPushButton("multiple text")
        btn5.clicked.connect(self.get_text)

        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)

        container_widget = QWidget()
        container_widget.setLayout(layout)

        self.setCentralWidget(container_widget)

    def get_an_int(self):
        title = "Get an integer"
        label = "Enter a number"

        my_int_value, ok = QInputDialog.getInt(
            self, title, label, value=0, minValue=-5, maxValue=5, step=1
        )

        if my_int_value and ok:
            print(my_int_value)

    def get_a_float(self):

        title = "Get an Float"
        label = "Type your float here"

        my_float_value, ok = QInputDialog.getDouble(
            self, title, label, value=0, minValue=-5.3, maxValue=5.7, decimals=2
        )

        if my_float_value and ok:
            print(my_float_value)

    def get_a_str_from_a_list(self):
        title = "Select a string"
        label = "Select a fruit from the list"
        items = ["apple", "pear", "orange", "grape"]
        initial_selection = 2

        my_selected_str, ok = QInputDialog.getItem(
            self,
            title,
            label,
            items,
            initial_selection,
            editable=True,
        )

        if my_selected_str and ok:
            print(my_selected_str)

    def get_a_str(self):
        title = "Enter a string"
        label = "Type your password"
        text = "my secret password"

        mode = QLineEdit.Password

        my_selected_str, ok = QInputDialog.getText(self, title, label, mode, text)

        if my_selected_str and ok:
            print(my_selected_str)

    def get_text(self):
        title = "Enter text"
        label = "Type your novel here"

        text = "Once upon a time..."
        my_selected_str, ok = QInputDialog.getMultiLineText(self, title, label, text)

        if my_selected_str and ok:
            print(my_selected_str)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
