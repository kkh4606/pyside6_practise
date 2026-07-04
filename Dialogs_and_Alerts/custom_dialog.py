from PySide6.QtWidgets import (
    QDialog,
    QLineEdit,
    QDialogButtonBox,
    QVBoxLayout,
    QListWidgetItem,
)


from PySide6.QtCore import Qt


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.add_todo)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        self.todo = QLineEdit()
        layout.addWidget(self.todo)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def add_todo(self):
        task = self.todo.text()
        #
        # try:
        #
        #     cur.execute(
        #         f"INSERT INTO todos (todo,is_completed) VALUES (?,?)", (task, 0)
        #     )
        #
        #     all_todos = cur.fetchall()
        #     print(all_todos)
        #
        #     conn.commit()
        #     conn.close()
        #
        # except Exception as e:
        #     print(e)
        # else:
        #     print("success")
