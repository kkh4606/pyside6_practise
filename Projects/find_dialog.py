import sys

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QHBoxLayout,
    QCheckBox,
    QRadioButton,
    QDialog,
)


class FindDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Find")

        self.setMaximumHeight(100)
        self.setMaximumWidth(400)

        label = QLabel("Find what")
        self.input = QLineEdit()

        input_layout = QHBoxLayout()
        input_layout.addWidget(label)
        input_layout.addWidget(self.input)

        self.find_btn = QPushButton("Find Next")

        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.clicked.connect(self.close)

        btn_layout = QVBoxLayout()
        btn_layout.addWidget(self.find_btn)
        btn_layout.addWidget(self.cancel_btn)

        up_radio = QRadioButton("Up")
        up_radio.setChecked(True)
        down_radio = QRadioButton("Down")

        raido_layout = QHBoxLayout()
        raido_layout.addWidget(up_radio)
        raido_layout.addWidget(down_radio)

        match_case_btn = QCheckBox("Match case")
        match_case_btn.setChecked(True)
        wrap_around_btn = QCheckBox("Wrap around")

        check_layout = QVBoxLayout()
        check_layout.addWidget(match_case_btn)
        check_layout.addWidget(wrap_around_btn)

        layout = QGridLayout()

        layout.addLayout(input_layout, 0, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addLayout(btn_layout, 0, 3)
        layout.addLayout(raido_layout, 1, 2)
        layout.addLayout(check_layout, 2, 0)

        self.setLayout(layout)
