import sys


from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QWidget,
    QListWidget,
    QTabWidget,
    QListWidgetItem,
    QInputDialog,
)


import sqlite3


class ToDo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo App")
        self.setGeometry(100, 100, 600, 400)

        self.theme = "day_mode"

        self.layout = QGridLayout()

        self.conn = sqlite3.connect("todo.db")

        self.cur = self.conn.cursor()

        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY ,todo TEXT,is_completed INTEGER NOT NULL DEFAULT 0)"""
        )

        self.cur = self.conn.cursor()

        self.cur.execute("SELECT * FROM todos")

        self.all_todos = self.cur.fetchall()

        self.todos = QListWidget()
        self.todos.setStyleSheet("""font: 25px;""")

        for i in range(len(self.all_todos)):

            todo_item = QListWidgetItem(self.all_todos[i][1])

            if self.all_todos[i][2] == 0:
                todo_item.setCheckState(Qt.CheckState.Unchecked)
            else:
                todo_item.setCheckState(Qt.CheckState.Checked)

            self.todos.addItem(todo_item)

        self.todos.itemPressed.connect(self.pressed_todo)

        self.todos_completed = QListWidget()

        self.todos_completed.setStyleSheet("""font: 25px;""")

        self.todos_uncompleted = QListWidget()
        self.todos_uncompleted.setStyleSheet("""font: 25px;""")

        self.todos_tab = QTabWidget()

        self.todos_tab.setStyleSheet("""color: black;""")

        self.todos_tab.setTabPosition(QTabWidget.North)

        self.todos_tab.addTab(self.todos, "ALL")
        self.todos_tab.addTab(self.todos_completed, "COMPLETED")
        self.todos_tab.addTab(self.todos_uncompleted, "UNCOMPLETED")

        self.completed_todos = QListWidget()

        self.search_box = QLineEdit()
        self.search_box.setFixedSize(QSize(500, 32))
        self.search_box.setStyleSheet("""padding: 0 0 0 8px;""")

        self.search_box.textChanged.connect(self.filter_items)

        self.search_btn = QPushButton("Search")
        self.search_btn.setFixedSize(QSize(70, 32))

        self.btn_toggle = QPushButton()
        self.btn_toggle.setStyleSheet("""border: none;""")

        self.btn_toggle.setIcon(QIcon("images/day.png"))
        self.btn_toggle.setFixedSize(QSize(32, 32))
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.btn_toggle.clicked.connect(self.toggle_theme)

        self.btn_delete = QPushButton("Delete")
        self.btn_delete.clicked.connect(self.delete_todo)

        self.btn_update = QPushButton("Update")
        self.btn_update.clicked.connect(self.update_todo)
        self.btn_update.setFixedSize(QSize(70, 30))

        self.btn_add = QPushButton("+")
        self.btn_add.clicked.connect(self.add_todo)

        self.btn_delete.setFixedSize(QSize(70, 30))

        self.layout.addWidget(self.search_box, 0, 0, 1, 4)
        self.layout.addWidget(self.search_btn, 0, 4)
        self.layout.addWidget(self.btn_toggle, 0, 5)
        self.layout.addWidget(self.todos_tab, 2, 0, 1, 5)
        self.layout.addWidget(self.btn_delete, 7, 0)
        self.layout.addWidget(self.btn_update, 7, 1)
        self.layout.addWidget(self.btn_add, 7, 4)

        container_widget = QWidget()
        container_widget.setLayout(self.layout)

        self.setCentralWidget(container_widget)

    def pressed_todo(self):

        self.update_todo()

    def filter_items(self):

        for i in range(self.todos.count()):
            item = self.todos.item(i)

            if (
                self.search_box.text() == ""
                or self.search_box.text().lower() in item.text().lower()
            ):
                self.todos.setRowHidden(i, False)
            else:
                self.todos.setRowHidden(i, True)

    def add_todo(self):
        task, ok = QInputDialog.getText(
            self,
            "Add a task",
            "",
        )

        if task and task.strip(" ") != "" and ok:

            todo_item = QListWidgetItem(task)
            todo_item.setCheckState(Qt.CheckState.Unchecked)

            self.todos.addItem(todo_item)

            with self.conn:

                self.cur.execute(
                    f"INSERT INTO todos (todo,is_completed) VALUES (?,?)", (task, 0)
                )

                self.conn.commit()

    def update_todo(self):

        if not self.todos.count() > 0:
            return

        current_row = self.todos.currentRow()
        old_todos = self.todos.currentItem()

        if old_todos is None:
            return

        update_dil = QInputDialog()

        update_todos, ok = update_dil.getText(
            self, "update", "", QLineEdit.Normal, old_todos.text()
        )

        if update_todos and update_todos.strip(" ") != "" and ok:

            self.todos.takeItem(current_row)
            update_item = QListWidgetItem(update_todos)

            if old_todos.checkState() == Qt.CheckState.Unchecked:
                update_item.setCheckState(Qt.CheckState.Unchecked)
            else:
                update_item.setCheckState(Qt.CheckState.Checked)
            self.todos.insertItem(current_row, update_item)

            with self.conn:

                self.cur.execute(
                    "UPDATE todos SET todo=(?), is_completed=(?)",
                    (
                        update_todos,
                        0 if old_todos.checkState() == Qt.CheckState.Unchecked else 1,
                    ),
                )

                self.conn.commit()

    def delete_todo(self):
        current_item = self.todos.currentRow()

        item = self.todos.currentItem()

        if item:

            with self.conn:

                self.cur.execute("DELETE FROM todos WHERE todo=(?)", (item.text(),))

                self.conn.commit()

        if current_item >= 0:
            self.todos.takeItem(current_item)
        del current_item

    def toggle_theme(self):
        if self.theme == "day_mode":
            self.btn_toggle.setIcon(QIcon("images/night.png"))
            self.theme = "night_mode"

        else:
            self.btn_toggle.setIcon(QIcon("images/day.png"))
            self.theme = "day_mode"

        self.setStyleSheet(
            f"""background-color: {'#36454F' if self.theme == 'night_mode' else 'white'};color: {'white' if self.theme == 'night_mode' else '#36454F'}"""
        )

        self.search_box.setStyleSheet(
            f"""padding: 8px;background-color: {'#36454F' if self.theme == 'night_mode' else 'white'};color: {'white' if self.theme == 'night_mode' else 'black'};"""
        )

        self.todos.setStyleSheet(
            f"""font: 25px;background-color: {'#36454F' if self.theme == 'night_mode' else 'white'};color: {'white' if self.theme == 'night_mode' else 'black'};"""
        )
        self.btn_add.setStyleSheet(
            f"""background-color: {'#36454F' if self.theme == 'night_mode' else 'white'};color: {'white' if self.theme == 'night_mode' else 'black'}"""
        )


app = QApplication(sys.argv)
window = ToDo()
window.show()
app.exec()
