import sys

from PySide6.QtCore import Qt, QSize

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QCheckBox,
    QFormLayout,
    QDialog,
)


class ReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Replace")

        self.setFixedSize(QSize(400, 200))

        self.s_input = QLineEdit()
        self.r_input = QLineEdit()

        form_layout = QFormLayout()
        form_layout.addRow(QLabel("Find what"), self.s_input)
        form_layout.addRow(QLabel("Replace with"), self.r_input)

        self.find_btn = QPushButton("Find Next")
        self.r_btn = QPushButton("Replace")

        self.r_all_btn = QPushButton("Replace All")
        self.cancel_btn = QPushButton("Cancel")

        btn_layout = QVBoxLayout()
        btn_layout.addWidget(self.find_btn)
        btn_layout.addWidget(self.r_btn)
        btn_layout.addWidget(self.r_all_btn)
        btn_layout.addWidget(self.cancel_btn)

        match_case_btn = QCheckBox("Match case")
        match_case_btn.setChecked(True)
        wrap_around_btn = QCheckBox("Wrap around")

        check_layout = QVBoxLayout()
        check_layout.addWidget(match_case_btn)
        check_layout.addWidget(wrap_around_btn)

        layout = QGridLayout()

        layout.addLayout(
            form_layout,
            0,
            0,
        )
        layout.addLayout(btn_layout, 0, 3)

        layout.addLayout(check_layout, 2, 0)

        self.setLayout(layout)
