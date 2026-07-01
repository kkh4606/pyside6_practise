class OpenFile:
    def __init__(self):
        self.is_open = True

        file = QFileDialog.getOpenFileName(self, "Open", "*.txt", "Text Files (*.txt)")

        file_path = Path(file[0])

        self.setWindowTitle(f"{file_path.name}-Notepad")

        with open(file_path, "r", encoding="UTF-8") as f:
            text = f.read()

        self.text_box.setText(text)

        self.file_path = file_path
        self.text_value = text
