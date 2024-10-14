import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()  # initializes the main window like in the previous one
        # window = QMainWindow()
        self.title = "PyQt Button"
        self.left = 200  # or left
        self.top = 200  # or top
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('chopper.ico.png'))

        # In GUI Python, these buttons, textboxes, labels are called Widgets
        self.button = QPushButton('click me!', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(100, 70)  # button.move(x,y)

        self.button2 = QPushButton('Register', self)
        self.button2.setToolTip("this button does nothing.. yet..")
        self.button2.move(100, 100)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())