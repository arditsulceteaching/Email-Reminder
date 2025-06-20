from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QDateTimeEdit, QLineEdit, QTextEdit,
                             QSpacerItem, QSizePolicy, QHBoxLayout,
                             QPushButton, QMessageBox)
from PyQt6.QtCore import QDateTime
import sys, requests

class ReminderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Reminder")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Event date and time
        self.datetime_label = QLabel("Event Date and Time:")
        self.datetime_picker = QDateTimeEdit()
        self.datetime_picker.setDateTime(QDateTime.currentDateTime())
        self.datetime_picker.setCalendarPopup(True)
        layout.addWidget(self.datetime_label)
        layout.addWidget(self.datetime_picker)

        # Email
        self.email_label = QLabel("Email: ")
        self.email_input = QLineEdit("app11flask@gmail.com")
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        # Reminder
        self.reminder_label = QLabel("Reminder: ")
        self.reminder_input = QTextEdit()
        layout.addWidget(self.reminder_label)
        layout.addWidget(self.reminder_input)

        # Repeat interval
        self.repeat_label = QLabel("Repeat Interval: ")
        self.repeat_input = QLineEdit()
        self.repeat_input.setPlaceholderText("e.g., 1d, 2w, 3m")
        layout.addWidget(self.repeat_label)
        layout.addWidget(self.repeat_input)

        # Buttons layout
        button_layout = QHBoxLayout()
        self.submit_button = QPushButton("Add Reminder")
        self.submit_button.clicked.connect(self.submit_reminder)
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.close_button)
        layout.addLayout(button_layout)

        layout.addSpacerItem(QSpacerItem(20, 40,
                                         QSizePolicy.Policy.Minimum,
                                         QSizePolicy.Policy.Expanding))
        self.setLayout(layout)

    def submit_reminder(self):
        datetime = self.datetime_picker.dateTime().toString("yyyy-MM-dd HH:mm")
        date, time = datetime.split(" ")
        data = {"date": date,
                "time": time,
                "email": self.email_input.text(),
                "message": self.reminder_input.toPlainText(),
                "repeat_interval": self.repeat_input.text()}

        response = requests.post(
            "http://realworldpython.pythonanywhere.com/add",
            json=data)

        if response.status_code == 200:
            QMessageBox.information(self, "Success", "Reminder added successfully!")
            self.reminder_input.clear()
            self.repeat_input.clear()


app = QApplication(sys.argv)
window = ReminderApp()
window.show()
sys.exit(app.exec())