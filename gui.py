from PyQt6.QtWidgets import (QApplication, QWidget, QLabel)
import sys

class ReminderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Reminder")


app = QApplication(sys.argv)
window = ReminderApp()
window.show()
sys.exit(app.exec())