import sys
import re
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QHBoxLayout,
)


def check_file_names(file_name: str) -> bool:
    if re.fullmatch(r"FIFA 12.part\d+\.rar$", file_name, flags=re.IGNORECASE):
        return True
    return False


def rename_invalid_files(file_name: str) -> str | None:
    if not check_file_names(file_name):
        return re.sub(r"(\s\(\d\))", "", file_name)
    return None


class FileValidator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Validator V1.0")

        self.label = QLabel("Validate Rar Files")
        self.label.setStyleSheet("""font-size: 20px;""")

        self.label.move(100, 40)

        btn = QPushButton("open folder")

        btn.setFixedSize(90, 30)

        btn_validate = QPushButton("check validation")

        btn_validate.setFixedSize(100, 30)

        btn.clicked.connect(self.open_folder)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn)
        btn_layout.addWidget(btn_validate)

        self.setLayout(btn_layout)

    def open_folder(self):

        file_path = QFileDialog.getExistingDirectory(
            self, caption="Select folder", dir="."
        )

        base_dir = Path(file_path)

        rar_files = list(base_dir.glob("*.rar"))
        found_invalid = False

        for file in rar_files:

            try:
                if not check_file_names(file.name):
                    found_invalid = True
                    valid_name = rename_invalid_files(file.name)
                    file.rename(base_dir / valid_name)
                    print(f"{file.name} successfully renamed to {valid_name}")

            except Exception as e:
                print("Error {e} occurred")
        if rar_files and not found_invalid:
            print("All files have valid file names")


app = QApplication(sys.argv)

window = FileValidator()


window.show()

app.exec()
