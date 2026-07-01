import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

# from QtDesigner.dialog import Ui_Dialog

from PySide6.QtUiTools import QUiLoader

from QtDesigner.database import conn, cur

loader = QUiLoader()


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.btn = QPushButton("Employee...")

        self.name = None

        self.btn.clicked.connect(self.btn_clicked)
        self.setCentralWidget(self.btn)

    def btn_clicked(self):

        dlg = loader.load("dialog.ui", None)

        dlg.exec()

    # def onEmployeeClicked(self):
    #     dlg = EmployeeDlg(self)
    #
    #     dlg.exec()


# class EmployeeDlg(Ui_Dialog, QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)


# Create the application
app = QApplication(sys.argv)
# Create and show the application's main window
w = Window()
w.show()
# Run the application's main loop
app.exec()
