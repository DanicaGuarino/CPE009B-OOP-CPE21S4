import sys
from PyQt5.QtWidgets import QApplication
from registration import Registration

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Registration()
    sys.exit(app.exec_())