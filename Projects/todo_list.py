import sys

from PySide6.QtCore import QFile, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
from todo_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.version.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.ui.add_btn.clicked.connect(self.add_todo)
        self.ui.toggle_btn.clicked.connect(self.toggle_todo)

        self.ui.delete_btn.clicked.connect(self.delete_todo)

    def add_todo(self):

        todo_text = self.ui.input_box.text()

        if not todo_text or todo_text.strip(" ") == "":
            return

        todo = QListWidgetItem(todo_text)
        todo.setCheckState(Qt.CheckState.Unchecked)

        self.ui.todo_list_widget.addItem(todo)

        self.ui.input_box.setText("")

    def delete_todo(self):

        current_index = self.ui.todo_list_widget.currentRow()

        if current_index >= 0:
            self.ui.todo_list_widget.takeItem(current_index)

    def toggle_todo(self):
        for i in range(self.ui.todo_list_widget.count()):
            item = self.ui.todo_list_widget.item(i)

            if item.checkState() == Qt.CheckState.Checked:
                item.setCheckState(Qt.CheckState.Unchecked)
            else:
                item.setCheckState(Qt.CheckState.Checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()
