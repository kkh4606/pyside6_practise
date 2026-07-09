from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hello")

        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        print(type(btn))

        self.btn_box = QDialogButtonBox(btn)
        self.btn_box.accepted.connect(self.accept)
        self.btn_box.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK ?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.btn_box)

        self.setLayout(self.layout)
