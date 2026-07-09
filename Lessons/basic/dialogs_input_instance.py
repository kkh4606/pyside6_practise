import sys
from PySide6.QtWidgets import (
    QApplication,
    QInputDialog,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
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

        dlg = QInputDialog()
        dlg.setWindowTitle(title)
        dlg.setLabelText(label)

        dlg.setIntValue(0)
        dlg.setIntMinimum(-3)
        dlg.setIntMaximum(3)

        ok = dlg.exec()

        if dlg.intValue() and ok:
            print(dlg.intValue())

    def get_a_float(self):

        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter a float")
        dialog.setLabelText("Type your float here")
        dialog.setDoubleValue(0.1)
        dialog.setDoubleMinimum(-5.3)
        dialog.setDoubleMaximum(5.7)
        dialog.setDoubleStep(1.4)
        dialog.setDoubleDecimals(2)

        ok = dialog.exec()

        print("Result:", ok, dialog.doubleValue())

    def get_a_str_from_a_list(self):
        dlg = QInputDialog()
        dlg.setWindowTitle("Select a string")
        dlg.setLabelText("Select a fruit from the list")
        dlg.setComboBoxItems(["apple", "banana", "orange", "mango"])
        dlg.setTextValue("orange")
        dlg.setComboBoxEditable(False)

        ok = dlg.exec()
        if dlg.textValue() and ok:
            print(dlg.textValue())

    def get_a_str(self):
        dlg = QInputDialog()
        dlg.setWindowTitle("Enter your password")
        dlg.setLabelText("Type your password here")
        dlg.setTextValue("My secret password")
        dlg.setTextEchoMode(QLineEdit.Password)

        ok = dlg.exec()

        if dlg.textValue() and ok:
            print(dlg.textValue())

    def get_text(self):
        dlg = QInputDialog()
        dlg.setWindowTitle("Get your text")
        dlg.setLabelText("Enter your text here")
        dlg.setTextValue("Once upon a time ...")

        dlg.setOption(QInputDialog.UsePlainTextEditForTextInput, True)

        ok = dlg.exec()

        if dlg.textValue() and ok:
            print(dlg.textValue())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
