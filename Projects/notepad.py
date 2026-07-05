import sys


from PySide6.QtGui import QAction, QIcon, QKeySequence, QGuiApplication, QTextCursor
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QFileDialog,
    QMessageBox,
    QWidget,
    QPushButton,
    QVBoxLayout,
)
from pathlib import Path

from Projects.find_dialog import FindDialog
from Projects.replace_dialgo import ReplaceDialog


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
        self.default_font_size = 18
        self.selected_text = ""
        self.f_dialog = FindDialog()
        self.r_dialog = ReplaceDialog()

        self.search_input = self.f_dialog.input
        self.search_btn = self.f_dialog.find_btn

        self.search_btn.clicked.connect(self.search_text)

        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("""font:14px;""")

        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        format_menu = menu_bar.addMenu("Format")
        view_menu = menu_bar.addMenu("View")
        help_menu = menu_bar.addMenu("Help")

        # file menu
        new_file = QAction("New", self)
        new_file.setShortcut(QKeySequence("Ctrl+N"))
        new_file.triggered.connect(self.new_file)
        file_menu.addAction(new_file)
        new_window = QAction("New Window", self)
        new_window.setShortcut(QKeySequence("Ctrl+Shift+N"))

        file_menu.addAction(new_window)
        open_file = QAction("Open", self)
        open_file.setShortcut(QKeySequence("Ctrl+O"))
        open_file.triggered.connect(self.open_file)
        file_menu.addAction(open_file)
        save = QAction("Save", self)
        save.setShortcut(QKeySequence("Ctrl+S"))
        save.triggered.connect(self.save_file)
        file_menu.addAction(save)
        save_as = QAction("Save As", self)
        save_as.setShortcut(QKeySequence("Ctrl+Shift+N"))
        save_as.triggered.connect(self.save_as_file)
        file_menu.addAction(save_as)

        file_menu.addSeparator()

        exit_window = QAction(QIcon(""), "Exit", self)
        exit_window.triggered.connect(self.exit_app)
        file_menu.addAction(exit_window)

        # edit menu

        undo = QAction("Undo", self)
        undo.setShortcut(QKeySequence("Ctrl+Shift+Z"))
        undo.triggered.connect(lambda: self.text_box.undo())
        edit_menu.addAction(undo)

        redo = QAction("Redo", self)
        redo.setShortcut(QKeySequence("Ctrl+Z"))
        redo.triggered.connect(lambda: self.text_box.redo())
        edit_menu.addAction(redo)
        self.cut = QAction("Cut", self)

        self.cut.setShortcut(QKeySequence("Ctrl+X"))
        self.cut.triggered.connect(lambda: self.text_box.cut())
        edit_menu.addAction(self.cut)
        self.copy = QAction("Copy", self)
        self.copy.setDisabled(True)
        self.copy.setShortcut(QKeySequence("Ctrl+C"))
        self.copy.triggered.connect(lambda: self.text_box.copy())
        edit_menu.addAction(self.copy)
        paste = QAction("Paste", self)
        paste.setShortcut(QKeySequence("Ctrl+V"))
        paste.triggered.connect(lambda: self.text_box.paste())
        edit_menu.addAction(paste)
        self.delete = QAction("Delete", self)
        self.delete.setDisabled(True)
        self.delete.triggered.connect(
            lambda: self.text_box.setText(
                self.text_box.toPlainText().replace(self.selected_text, "")
            )
        )
        self.delete.setShortcut(QKeySequence("Del"))
        edit_menu.addAction(self.delete)

        edit_menu.addSeparator()

        self.find = QAction("Find", self)
        self.find.setDisabled(True)

        self.find.triggered.connect(self.show_f_dialog)
        edit_menu.addAction(self.find)
        find_next = QAction("Find Next", self)
        edit_menu.addAction(find_next)
        find_parev = QAction("Find Previous", self)
        edit_menu.addAction(find_parev)
        replace = QAction("Replace", self)
        replace.triggered.connect(self.show_r_dialog)
        edit_menu.addAction(replace)
        go_to = QAction("Go To", self)
        edit_menu.addAction(go_to)

        edit_menu.addSeparator()

        select_all = QAction("Select All", self)
        edit_menu.addAction(select_all)

        time_date = QAction("Time/Date", self)
        edit_menu.addAction(time_date)

        # format menu
        font = QAction("Font", self)
        format_menu.addAction(font)

        # view menu
        zoom = view_menu.addMenu("Zoom")

        zoom_in = QAction("Zoom in", self)
        zoom_in.triggered.connect(self.zoom_in)

        zoom_in.setShortcut(QKeySequence("Ctrl+-"))

        zoom_out = QAction("Zoom out", self)
        zoom_out.triggered.connect(self.zoom_out)

        zoom_out.setShortcut(QKeySequence("Ctrl+="))
        default = QAction("Restore Default Zoom", self)
        default.triggered.connect(self.default_zoom)
        default.setShortcut(QKeySequence("Ctrl+0"))
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
        self.text_box.setStyleSheet(f"font:{self.default_font_size}px;")
        self.text_box.textChanged.connect(self.text_changed)
        self.text_box.selectionChanged.connect(self.selection_changed)

        self.setCentralWidget(self.text_box)

    def show_f_dialog(self):

        self.f_dialog.show()

    def show_r_dialog(self):

        self.r_dialog.show()

    def search_text(self):
        text = self.search_input.text().lower()

        if text in self.text_box.toPlainText().lower():

            start = self.text_box.toPlainText().lower().index(text)

            end = None

            if len(text) == 0:
                return

            if len(text) == 1:
                end = start + 1

            if len(text) > 1:
                end = start + len(text)

            cursor = self.text_box.textCursor()

            cursor.setPosition(start)

            cursor.setPosition(end, QTextCursor.MoveMode.KeepAnchor)

            self.text_box.setTextCursor(cursor)

            self.search_input.setText("")

    def zoom_in(self):
        self.default_font_size -= 2
        self.text_box.setStyleSheet(f"font:{self.default_font_size}px;")

    def zoom_out(self):
        self.default_font_size += 2
        self.text_box.setStyleSheet(f"font:{self.default_font_size}px;")

    def default_zoom(self):
        self.default_font_size = 18
        self.text_box.setStyleSheet(f"font:{self.default_font_size}px;")

    def text_changed(self):
        self.changed = True

        if self.text_box.toPlainText():
            self.find.setDisabled(False)
        else:
            self.find.setDisabled(True)

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

    def show_new_window(self):

        self.new_window.show()

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
                    pass

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
            return

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
            dlg.setText("Do you want to save Changes to Untitled ?")
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
                    return

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

    def selection_changed(self):
        text = self.text_box.textCursor().selectedText()
        self.selected_text = text

        for action in [self.copy, self.cut, self.delete]:
            if text:
                action.setDisabled(False)
            else:
                action.setDisabled(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
