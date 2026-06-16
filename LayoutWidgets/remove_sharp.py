import re

try:

    with open("Notes.txt", "r") as text:
        string = text.read()

        with open("Notes.txt", "w") as text:
            text.write(re.sub(" {4}", "", string))
except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("No permission")
except Exception as e:
    print(f"Error {e} occoured")
