import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Account Registration System"
        self.width = 400
        self.height = 350
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)
        self.setWindowIcon(QIcon('chopper.ico.png'))
        self.center()

        self.program_title = QLabel("Account Registration", self)
        self.program_title.setAlignment(Qt.AlignCenter)
        self.program_title.setGeometry(0, 10, self.width, 30)

        self.label_first_name = QLabel("First Name", self)
        self.label_first_name.move(30, 50)
        self.textbox_first_name = QLineEdit(self)
        self.textbox_first_name.move(150, 50)
        self.textbox_first_name.resize(200, 30)

        self.label_surname = QLabel("Surname", self)
        self.label_surname.move(30, 90)
        self.textbox_surname = QLineEdit(self)
        self.textbox_surname.move(150, 90)
        self.textbox_surname.resize(200, 30)

        self.label_username = QLabel("Username", self)
        self.label_username.move(30, 130)
        self.textbox_username = QLineEdit(self)
        self.textbox_username.move(150, 130)
        self.textbox_username.resize(200, 30)

        self.label_password = QLabel("Password:", self)
        self.label_password.move(30, 170)
        self.textbox_password = QLineEdit(self)
        self.textbox_password.move(150, 170)
        self.textbox_password.resize(200, 30)

        self.label_email = QLabel("Email Address", self)
        self.label_email.move(30, 210)
        self.textbox_email = QLineEdit(self)
        self.textbox_email.move(150, 210)
        self.textbox_email.resize(200, 30)

        self.label_contact_number = QLabel("Contact Number", self)
        self.label_contact_number.move(30, 250)
        self.textbox_contact_number = QLineEdit(self)
        self.textbox_contact_number.move(150, 250)
        self.textbox_contact_number.resize(200, 30)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.move(100, 290)
        self.submit_button.clicked.connect(self.submit)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.move(200, 290)
        self.clear_button.clicked.connect(self.clear)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def submit(self):
        first_name = self.textbox_first_name.text()
        surname = self.textbox_surname.text()
        username = self.textbox_username.text()
        password = self.textbox_password.text()
        email = self.textbox_email.text()
        contact_number = self.textbox_contact_number.text()

        if not first_name or not surname or not username or not password or not email or not contact_number:
            QMessageBox.warning(self, "Input Error", "Please fill all fields", QMessageBox.Ok, QMessageBox.Ok)
            return

        # Save to a .txt file
        with open('registration_data.txt', 'a') as file:
            file.write(f"{first_name},{surname},{username},{password},{email},{contact_number}\n")

        QMessageBox.information(self, "Registration Successful", f"Welcome {first_name} {surname}!", QMessageBox.Ok,
                                QMessageBox.Ok)

        self.clear()

    def clear(self):
        self.textbox_first_name.clear()
        self.textbox_surname.clear()
        self.textbox_username.clear()
        self.textbox_password.clear()
        self.textbox_email.clear()
        self.textbox_contact_number.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registration()
    sys.exit(app.exec_())
