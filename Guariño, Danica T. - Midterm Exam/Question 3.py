import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, QPushButton, QGridLayout, QGroupBox, QHBoxLayout, QVBoxLayout, QTextEdit)
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt Login Screen"
        self.x = 200  # or left
        self.y = 200  # or top
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.createGridLayout()
        self.setLayout(self.layout)
        self.show()

    def createGridLayout(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(1, 2)
        self.textboxlbl = QLabel("Enter your fullname: ", self)
        self.textbox = QLineEdit(self)
        self.fullnamelbl = QPushButton("Click To display your Fullname: ", self)
        self.fullname = QLabel(self)

        self.fullnamelbl.clicked.connect(self.displayFullName)

        self.layout.addWidget(self.textboxlbl, 0, 1)
        self.layout.addWidget(self.textbox, 0, 2)
        self.layout.addWidget(self.fullnamelbl, 1, 1)
        self.layout.addWidget(self.fullname, 1, 2)

    def displayFullName(self):
        full_name = self.textbox.text()
        self.fullname.setText(full_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())