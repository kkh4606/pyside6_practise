import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QLineEdit,
    QComboBox,
    QPushButton,
    QWidget,
    QListWidget,
    QListWidgetItem,
    QInputDialog,
)


class ToDo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo App")
        self.setGeometry(100, 100, 600, 400)

        self.theme = "day_mode"

        self.layout = QGridLayout()

        self.todos = QListWidget()
        self.todos.setStyleSheet("""font: 25px;""")

        self.search_box = QLineEdit("Search note...")
        self.search_box.setFixedSize(QSize(500, 32))

        self.combobox = QComboBox()
        self.combobox.setFixedSize(QSize(100, 32))

        self.combobox.addItem("ALL")
        self.combobox.addItem("COMPLETED")
        self.combobox.addItem("UNCOMPLETED")

        self.btn_toggle = QPushButton()
        self.btn_toggle.setStyleSheet("""border: none;""")

        self.btn_toggle.setIcon(QIcon("day.png"))
        self.btn_toggle.setFixedSize(QSize(32, 32))
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.btn_toggle.clicked.connect(self.toggle_theme)

        self.btn_add = QPushButton("+")
        self.btn_add.clicked.connect(self.add_todo)

        self.layout.addWidget(self.search_box, 0, 0)
        self.layout.addWidget(self.combobox, 0, 4)
        self.layout.addWidget(self.btn_toggle, 0, 5)
        self.layout.addWidget(self.todos, 2, 0, 1, 5)
        self.layout.addWidget(self.btn_add, 7, 4)

        container_widget = QWidget()
        container_widget.setLayout(self.layout)

        self.setCentralWidget(container_widget)

    def add_todo(self):

        todo_text, ok = QInputDialog.getText(
            self,
            "Add a task",
            "",
            QLineEdit.Normal,
        )

        if ok and todo_text.strip("") != "":

            todo = QListWidgetItem(todo_text)

            todo.setCheckState(Qt.CheckState.Unchecked)

            self.todos.addItem(todo)

    def toggle_theme(self):
        if self.theme == "day_mode":
            self.btn_toggle.setIcon(QIcon("night.png"))
            self.theme = "night_mode"

        else:
            self.btn_toggle.setIcon(QIcon("day.png"))
            self.theme = "day_mode"

        self.setStyleSheet(
            f"""background-color: {'white' if self.theme == 'day_mode' else '#36454F'};color: {'white' if self.theme == 'night_mode' else '#36454F'}"""
        )
        self.search_box.setStyleSheet(
            f"""background-color: {'white' if self.theme == 'night_mode' else '#36454F'};color: {'#36454F' if self.theme == 'night_mode' else 'white'}"""
        )
        self.combobox.setStyleSheet(
            f"""background-color: {'white' if self.theme == 'night_mode' else '#36454F'};color: {'#36454F' if self.theme == 'night_mode' else 'white'}"""
        )
        self.todos.setStyleSheet(
            f"""font: 25px;background-color: {'white' if self.theme == 'night_mode' else '#36454F'};color: {'#36454F' if self.theme == 'night_mode' else 'white'};"""
        )
        self.btn_add.setStyleSheet(
            f"""background-color: {'white' if self.theme == 'night_mode' else '#36454F'};color: {'#36454F' if self.theme == 'night_mode' else 'white'}"""
        )


app = QApplication(sys.argv)
window = ToDo()
window.show()
app.exec()
