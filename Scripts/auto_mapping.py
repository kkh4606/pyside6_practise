import sys
from pathlib import Path
import re


from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QFileDialog,
    QMessageBox,
    QErrorMessage,
    QListWidgetItem,
)
from mappepr_ui import Ui_Form


class AutoMapper(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Auto Map V1.0")

        self.list_widget.addItems(["1", "2", "3"])

        self.list_widget.currentItemChanged.connect(self.index_changed)

        self.list_widget.currentTextChanged.connect(self.text_changed)

        self.pushButton.clicked.connect(self.auto_assign_map)

    def index_changed(self, index: QListWidgetItem):
        print(index.text())

    def text_changed(self, text):
        print(text)

    def auto_assign_map(self) -> None:

        try:
            folder_dir = QFileDialog.getExistingDirectory()

            path = Path(folder_dir)

            regex = r"(\d+)"
            leagues = {}

            for league in path.iterdir():

                leagues[league.name] = {}

                if league.is_file():
                    continue

                for team in league.iterdir():

                    for kit in team.iterdir():
                        if kit.name == "g1":

                            for team_id in kit.iterdir():

                                match = re.search(regex, team_id.name)

                                if match:
                                    kit_team_format = f"{match.group().lstrip('0')}, {league.name}\\{team.name}\n"
                                    leagues[league.name][
                                        int(match.group())
                                    ] = kit_team_format
                                    break

            with open(path / "map.txt", "a", encoding="UTF-8") as f:

                for l, t in leagues.items():
                    f.write(f"#{l}\n")

                    print(f"assigning for {l}")
                    print("\033[1m" + f"Assigning for {l}" + "\033[0m")

                    for v in sorted(t.keys()):

                        f.write(f"{t[v]}")
                        print(f"success: {t[v]}")
                        print(f"success: {t[v]}", end="")
                    print()

                    f.write("\n")

        except PermissionError:
            print("No permission")
        except NotADirectoryError:
            print("Invalid directory")
        except Exception:
            print("error occurred")


app = QApplication(sys.argv)

window = AutoMapper()

window.show()
app.exec()
