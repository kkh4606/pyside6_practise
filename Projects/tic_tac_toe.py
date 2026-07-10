import sys

from PySide6.QtCore import qIsNaN
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
)

MAX_HEIGHT = 140
MAX_WIDTH = 170
FONT_SIZE = 30


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setMaximumHeight(300)

        main_layout = QVBoxLayout()

        gird_layout = QGridLayout()
        gird_layout.setContentsMargins(20, 20, 20, 20)
        gird_layout.setSpacing(0)

        bottom_layout = QHBoxLayout()

        self.btn_0 = QPushButton()
        self.btn_0.clicked.connect(lambda: self.btn_click(self.btn_0, 0))
        self.btn_0.setMinimumHeight(MAX_HEIGHT)
        self.btn_0.setMinimumWidth(MAX_WIDTH)
        self.btn_0.setStyleSheet(
            f"border:2px solid grey;border-left: none;border-top:none;font:{FONT_SIZE}px;"
        )

        self.btn_1 = QPushButton()
        self.btn_1.clicked.connect(lambda: self.btn_click(self.btn_1, 1))
        self.btn_1.setMinimumHeight(MAX_HEIGHT)
        self.btn_1.setMinimumWidth(MAX_WIDTH)
        self.btn_1.setStyleSheet(
            f"border:2px solid grey;border-left: none;border-top:none;font:{FONT_SIZE}px;"
        )

        self.btn_2 = QPushButton()
        self.btn_2.clicked.connect(lambda: self.btn_click(self.btn_2, 2))
        self.btn_2.setMinimumHeight(MAX_HEIGHT)
        self.btn_2.setMinimumWidth(MAX_WIDTH)
        self.btn_2.setStyleSheet(
            f"border:2px solid grey;border-left: none;border-top:none;border-right:none;font:{FONT_SIZE}px;"
        )

        self.btn_3 = QPushButton()
        self.btn_3.clicked.connect(lambda: self.btn_click(self.btn_3, 3))
        self.btn_3.setMinimumHeight(MAX_HEIGHT)
        self.btn_3.setMinimumWidth(MAX_WIDTH)
        self.btn_3.setStyleSheet(
            f"border:2px solid grey;border-left: none;border-top:none;font:{FONT_SIZE}px;"
        )

        self.btn_4 = QPushButton()
        self.btn_4.clicked.connect(lambda: self.btn_click(self.btn_4, 4))
        self.btn_4.setMinimumHeight(MAX_HEIGHT)
        self.btn_4.setMinimumWidth(MAX_WIDTH)
        self.btn_4.setStyleSheet(
            f"border:2px solid grey;border-left: none;border-top:none;font:{FONT_SIZE}px;"
        )

        self.btn_5 = QPushButton()
        self.btn_5.clicked.connect(lambda: self.btn_click(self.btn_5, 5))
        self.btn_5.setMinimumHeight(MAX_HEIGHT)
        self.btn_5.setMinimumWidth(MAX_WIDTH)
        self.btn_5.setStyleSheet(
            f"border:2px solid grey;border-left: none;border-top:none;border-right:none;font:{FONT_SIZE}px;"
        )

        self.btn_6 = QPushButton()
        self.btn_6.clicked.connect(lambda: self.btn_click(self.btn_6, 6))
        self.btn_6.setMinimumHeight(MAX_HEIGHT)
        self.btn_6.setMinimumWidth(MAX_WIDTH)
        self.btn_6.setStyleSheet(
            f"border:2px solid grey;border-left: none;border-top:none;border-bottom:none;font:{FONT_SIZE}px;"
        )

        self.btn_7 = QPushButton()
        self.btn_7.clicked.connect(lambda: self.btn_click(self.btn_7, 7))
        self.btn_7.setMinimumHeight(MAX_HEIGHT)
        self.btn_7.setMinimumWidth(MAX_WIDTH)
        self.btn_7.setStyleSheet(
            f"border:2px solid grey;border-left: none;border-top:none;border-bottom:none;font:{FONT_SIZE}px;"
        )

        self.btn_8 = QPushButton()
        self.btn_8.clicked.connect(lambda: self.btn_click(self.btn_8, 8))
        self.btn_8.setMinimumHeight(MAX_HEIGHT)
        self.btn_8.setMinimumWidth(MAX_WIDTH)
        self.btn_8.setStyleSheet(
            f"border:2px solid grey;border-left: none;border-top:none;border-bottom:none;border-right:none;font:{FONT_SIZE}px;"
        )

        btn_restart = QPushButton("Restart")
        btn_restart.clicked.connect(self.restart)
        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.close)

        gird_layout.addWidget(self.btn_0, 0, 0)
        gird_layout.addWidget(self.btn_1, 0, 1)
        gird_layout.addWidget(self.btn_2, 0, 2)

        gird_layout.addWidget(self.btn_3, 1, 0)
        gird_layout.addWidget(self.btn_4, 1, 1)
        gird_layout.addWidget(self.btn_5, 1, 2)

        gird_layout.addWidget(self.btn_6, 2, 0)
        gird_layout.addWidget(self.btn_7, 2, 1)
        gird_layout.addWidget(self.btn_8, 2, 2)

        bottom_layout.addWidget(btn_restart)
        bottom_layout.addWidget(btn_exit)

        main_layout.addLayout(gird_layout)
        main_layout.addLayout(bottom_layout)

        container_widget = QWidget()
        container_widget.setLayout(main_layout)

        self.setCentralWidget(container_widget)

        self.p1_turn = True
        self.p2_turn = False
        self.times = 0
        self.tie = False

        self.board = ["", "", "", "", "", "", "", "", ""]

        self.all_buttons = [
            self.btn_0,
            self.btn_1,
            self.btn_2,
            self.btn_3,
            self.btn_4,
            self.btn_5,
            self.btn_6,
            self.btn_7,
            self.btn_8,
        ]

    def restart(self):

        self.board = ["", "", "", "", "", "", "", "", ""]

        for button in self.all_buttons:
            button.setEnabled(True)
            button.setText("")

    def btn_click(self, btn: QPushButton, pos: int):

        if self.p1_turn:

            if not btn.text():
                self.board[pos] = "X"
                btn.setText("X")

                self.p2_turn, self.p1_turn = self.p1_turn, self.p2_turn
                self.times += 1
        else:

            if not btn.text():
                self.board[pos] = "O"
                btn.setText("O")

                self.p1_turn, self.p2_turn = self.p2_turn, self.p1_turn

                self.times += 1

        winner = self.check_winner()

        if winner:

            for button in self.all_buttons:
                button.setEnabled(False)
            QMessageBox.information(self, "result", f"{winner} win!")

    def check_winner(self):

        if self.board[0] == self.board[1] == self.board[2]:
            return self.board[0]
        elif self.board[3] == self.board[4] == self.board[5]:
            return self.board[3]
        elif self.board[0] == self.board[3] == self.board[6]:
            return self.board[0]
        elif self.board[1] == self.board[4] == self.board[7]:
            return self.board[1]

        elif self.board[2] == self.board[5] == self.board[6]:
            return self.board[2]
        elif self.board[0] == self.board[4] == self.board[8]:
            return self.board[0]

        return False


app = QApplication(sys.argv)
window = TicTacToe()
window.show()
app.exec()
