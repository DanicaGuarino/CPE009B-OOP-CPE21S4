import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()  # initializes the main window like in the previous one
        self.title = "Pyqt Line Edit"
        self.left = 200  # or left
        self.top = 200  # or top
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('chopper.ico.png'))

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        self.textbox.setText("Set this text value")

        self.button = QPushButton('Submit', self)
        self.button.setToolTip("Click to submit text")
        self.button.move(100, 100)


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
