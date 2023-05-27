# from PySide6 import QtWidgets, QtUiTools, QtCore

# app = QtWidgets.QApplication([])
# ui_file = "C:/Users/saada/Desktop/scroll view.ui"

# # Load the UI file and create an instance of the UI class
# loader = QtUiTools.QUiLoader()
# ui_file = QtCore.QFile(ui_file)
# ui_file.open(QtCore.QFile.ReadOnly)
# ui = loader.load(ui_file)
# ui_file.close()

# ui.show()
# app.exec()



import sys

from PySide6.QtCore import QRegExp, Qt
from PySide6.QtGui import QRegExpValidator
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow,
                               QMessageBox, QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Validation Example")

        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(10, 10, 200, 30)

        button = QPushButton("Submit", self)
        button.setGeometry(10, 50, 80, 30)
        button.clicked.connect(self.process_data)

        self.setup_input_validation()

    def setup_input_validation(self):
        # Create a regular expression validator
        regex = QRegExp("[A-Za-z0-9]+")  # Only allow alphanumeric characters
        validator = QRegExpValidator(regex, self.line_edit)
        self.line_edit.setValidator(validator)

    def validate_input(self):
        input_text = self.line_edit.text().strip()  # Trim leading/trailing whitespace
        if not input_text:
            QMessageBox.warning(self, "Error", "Input cannot be empty.")
            return False
        return True

    def process_data(self):
        if self.validate_input():
            input_text = self.line_edit.text().strip()
            QMessageBox.information(self, "Success", f"Valid input: {input_text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
