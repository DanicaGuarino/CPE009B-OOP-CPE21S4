import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()  # initializes the main window like in the previous one
        self.title = "PyQt Line Edit"
        self.left = 200  # or left
        self.top = 200  # or top
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textboxlbl = QLabel("Hello World!", self)
        self.textboxlbl.move(30, 25)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
