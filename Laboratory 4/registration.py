import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Registration(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Account Registration System"
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)
        self.setWindowIcon(QIcon('chopper.ico.png'))
        self.center()

        # Create program title
        self.program_title = QLabel("Account Registration", self)
        self.program_title.setAlignment(Qt.AlignCenter)
        self.program_title.setGeometry(0, 10, self.width, 30)

        self.label_first_name = QLabel("First Name", self)
        self.label_first_name.move(30, 50)
        self.textbox_first_name = QLineEdit(self)
        self.textbox_first_name.move(150, 50)
        self.textbox_first_name.resize(200, 30)

        self.label_Surname = QLabel("Surname", self)
        self.label_Surname.move(30, 90)
        self.textbox_Surname = QLineEdit(self)
        self.textbox_Surname.move(150, 90)
        self.textbox_Surname.resize(200, 30)

        self.label_username = QLabel("Username:", self)
        self.label_username.move(30, 130)
        self.textbox_username = QLineEdit(self)
        self.textbox_username.move(150, 130)
        self.textbox_username.resize(200, 30)

        self.label_password = QLabel("Password:", self)
        self.label_password.move(30, 170)
        self.textbox_password = QLineEdit(self)
        self.textbox_password.move(150, 170)
        self.textbox_password.resize(200, 30)

        self.label_Email_Address= QLabel("Email Address:", self)
        self.label_Email_Address.move(30, 210)
        self.textbox_Email_Address = QLineEdit(self)
        self.textbox_Email_Address.move(150, 210)
        self.textbox_Email_Address.resize(200, 30)

        self.label_contact_number = QLabel("Contact Number:", self)
        self.label_contact_number.move(30, 210)
        self.textbox_contact_number = QLineEdit(self)
        self.textbox_contact_number.move(150, 210)
        self.textbox_contact_number.resize(200, 30)


        self.submit_button = QPushButton("Submit", self)
        self.submit_button.move(100, y_position)
        self.clear_button = QPushButton("Clear", self)
        self.clear_button.move(200, y_position)

        self.show()
