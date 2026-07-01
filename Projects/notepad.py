import sys

from PySide6.QtCore import QEvent
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTextEdit,
    QFileDialog,
    QMessageBox,
    QDialogButtonBox,
)
from pathlib import Path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Untitled-Notepad")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("images/notepad.png"))

        self.save = False
        self.file_path = None
        self.text_value = ""
        self.is_new = False
        self.is_open = False
        self.changed = False

        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("""font:16px;""")

        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        format_menu = menu_bar.addMenu("Format")
        view_menu = menu_bar.addMenu("View")
        help_menu = menu_bar.addMenu("Help")

        # file menu
        new_file = QAction("New", self)
        new_file.triggered.connect(self.new_file)
        file_menu.addAction(new_file)
        new_window = QAction("New Window", self)
        file_menu.addAction(new_window)
        open_file = QAction("Open", self)
        open_file.triggered.connect(self.open_file)
        file_menu.addAction(open_file)
        save = QAction("Save", self)
        save.triggered.connect(self.save_file)
        file_menu.addAction(save)
        save_as = QAction("Save As", self)
        save_as.triggered.connect(self.save_as_file)
        file_menu.addAction(save_as)

        file_menu.addSeparator()

        exit_window = QAction(QIcon(""), "Exit", self)
        exit_window.triggered.connect(self.exit_app)
        file_menu.addAction(exit_window)

        # edit menu

        undo = QAction("Undo", self)
        edit_menu.addAction(undo)
        cut = QAction("Cut", self)
        edit_menu.addAction(cut)
        copy = QAction("Copy", self)
        edit_menu.addAction(copy)
        paste = QAction("Paste", self)
        edit_menu.addAction(paste)
        delete = QAction("Delete", self)
        edit_menu.addAction(delete)

        edit_menu.addSeparator()

        find = QAction("Find", self)
        edit_menu.addAction(find)
        find_next = QAction("Find Next", self)
        edit_menu.addAction(find_next)
        find_parev = QAction("Find Previous", self)
        edit_menu.addAction(find_parev)
        replace = QAction("Replace", self)
        edit_menu.addAction(replace)
        go_to = QAction("Go To", self)
        edit_menu.addAction(go_to)

        edit_menu.addSeparator()

        select_all = QAction(QIcon(""), "Select All", self)
        edit_menu.addAction(select_all)

        time_date = QAction(QIcon(""), "Time/Date", self)
        edit_menu.addAction(time_date)

        # format menu
        font = QAction(QIcon(""), "Font", self)
        format_menu.addAction(font)

        # view menu
        zoom = view_menu.addMenu("Zoom")

        zoom_in = QAction("Zoom in", self)
        zoom_out = QAction("Zoom out", self)
        default = QAction("Restore Default Zoom", self)
        zoom.addAction(zoom_in)
        zoom.addAction(zoom_out)
        zoom.addAction(default)

        # help menu
        view_help = QAction("View Help", self)
        s_feedback = QAction("Send Feedback", self)
        about = QAction("About Notepad", self)

        help_menu.addAction(view_help)
        help_menu.addAction(s_feedback)

        help_menu.addSeparator()

        help_menu.addAction(about)

        self.text_box = QTextEdit()
        self.text_box.setStyleSheet("""font:18px;""")
        self.text_box.textChanged.connect(self.text_changed)

        self.setCentralWidget(self.text_box)

    def text_changed(self):
        self.changed = True

        window_title = self.windowTitle()
        if window_title == "Untitled-Notepad":
            if self.text_box.toPlainText():
                self.setWindowTitle("*Untitled-Notepad")

        elif window_title == "*Untitled-Notepad":
            if not self.text_box.toPlainText():
                self.setWindowTitle("Untitled-Notepad")
        else:
            if self.file_path is not None:
                if not self.text_value:
                    return
                if self.text_box.toPlainText() == self.text_value:
                    self.setWindowTitle(f"{self.file_path.name}-Notepad")
                else:

                    self.setWindowTitle(f"*{self.file_path.name}-Notepad")

    def new_file(self):

        if self.text_box.toPlainText() != "":

            msgBox = QMessageBox(self)
            msgBox.setWindowTitle("Notepad")
            msgBox.setInformativeText("Do you want to save changes to Untitled?")
            msgBox.setStandardButtons(
                QMessageBox.Save
                | QMessageBox.Discard
                | QMessageBox.StandardButton.Cancel
            )
            msgBox.setDefaultButton(QMessageBox.Save)

            msgBox.exec()
        self.text_box.setText("")
        self.setWindowTitle("Untitled-Notepad")

    def open_file(self):

        if self.text_box.toPlainText() != "":

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Notepad")
            dlg.setText("Do you want to save Changes to  Untitled ?")
            dlg.setStandardButtons(
                QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Close
            )

            btn = dlg.exec()

            if btn == QMessageBox.Ok:

                try:

                    if self.file_path:

                        with open(self.file_path, "w", encoding="UTF-8") as f:
                            f.write(self.text_box.toPlainText())
                    else:
                        self.save_file()

                except PermissionError:
                    QMessageBox.critical(
                        self,
                        "Error",
                        "No permission to save this file",
                        QMessageBox.Ok,
                    )
            elif btn == QMessageBox.Cancel:
                self.open()
            else:
                dlg.destroy()
        else:

            self.open()

    def open(self):

        self.is_open = True

        try:

            file = QFileDialog.getOpenFileName(
                self, "Open", "*.txt", "Text Files (*.txt)"
            )

            file_path = Path(file[0])

            if file_path.name == "":
                self.setWindowTitle("Untitled-Notepad")
                self.file_path = None
            else:

                self.setWindowTitle(f"{file_path.name}-Notepad")
            self.file_path = file_path

            with open(file_path, "r", encoding="UTF-8") as f:
                text = f.read()

            self.text_box.setText(text)
            self.changed = True

            self.file_path = file_path
            self.text_value = text

        except PermissionError:

            self.file_path = None

    def save_file(self):

        try:

            if not self.save and not self.file_path:

                file = QFileDialog.getSaveFileName(
                    self, "Save", "*.txt", "Text Files (*.txt"
                )

                self.file_path = Path(file[0])

                self.text_value = self.text_box.toPlainText()

                with open(self.file_path, "w", encoding="UTF-8") as f:
                    f.write(self.text_value)
                self.save = True
                self.setWindowTitle(f"*{self.file_path.name}-Notepad")

            else:

                with open(self.file_path, "w", encoding="UTF-8") as f:
                    f.write(self.text_box.toPlainText())
        except PermissionError:

            msg_box = QMessageBox(self)

            msg_box.critical(
                self,
                "Permission Error",
                "No permission to perform requested action",
                QMessageBox.Ok,
            )

    def save_as_file(self):

        try:
            save_dir = self.file_path if self.file_path else Path.home() / "Documents"

            file = QFileDialog.getSaveFileName(
                self, "Save", str(save_dir.parent), "Text Files (*.txt"
            )

            self.file_path = Path(file[0])

            self.text_value = self.text_box.toPlainText()

            with open(self.file_path, "w", encoding="UTF-8") as f:
                f.write(self.text_value)
            self.save = True
            self.setWindowTitle(f"{self.file_path.name}-Notepad")

        except PermissionError:
            self.file_path = None

    def exit_app(self):
        if self.changed and self.file_path:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Notepad")
            dlg.setText("Do you want to save Changes to  Untitled ?")
            dlg.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)

            btn = dlg.exec()

            if btn == QMessageBox.Save:

                try:

                    if self.file_path:

                        with open(self.file_path, "w", encoding="UTF-8") as f:
                            f.write(self.text_box.toPlainText())
                    else:
                        self.save_file()

                except PermissionError:
                    QMessageBox.critical(
                        self,
                        "Error",
                        "No permission to save this file",
                        QMessageBox.Ok,
                    )
            elif btn == QMessageBox.Cancel:
                self.close()
        else:
            if self.text_box.toPlainText():
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Notepad")
                dlg.setText("Do you want to save Changes to  Untitled ?")
                dlg.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)

                btn = dlg.exec()

                if btn == QMessageBox.Save:

                    self.save_as_file()
                    self.close()
                else:
                    self.close()
            else:
                self.close()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
