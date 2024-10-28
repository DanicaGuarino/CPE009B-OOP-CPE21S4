import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QFontDialog, QTextEdit, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.expression = ""

    def initUI(self):
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle('Calculator')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.display = QLineEdit(self)
        self.display.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.display)

        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'sin',
            '1', '2', '3', '-', 'cos',
            '0', '.', '=', '+', 'exp',
            '(', ')', 'log', 'sqrt', 'tan'
        ]

        positions = [(i, j) for i in range(5) for j in range(5)]

        for position, button in zip(positions, buttons):
            if button == '':
                continue
            btn = QPushButton(button)
            btn.clicked.connect(self.on_click)
            self.grid.addWidget(btn, *position)

    def on_click(self):
        sender = self.sender().text()
        current_text = self.display.text()

        if sender == 'C':
            self.display.clear()
            self.expression = ""
        elif sender == '=':
            try:
                result = str(eval(self.expression, {"__builtins__": None}, {"sin": math.sin, "cos": math.cos, "tan": math.tan, "log": math.log, "sqrt": math.sqrt, "exp": math.exp}))
                self.display.setText(result)
                self.save_to_file(self.expression + '=' + result)
                self.expression = result
            except Exception as e:
                self.display.setText('Error')
                self.expression = ""
        elif sender in ('sin', 'cos', 'tan', 'log', 'sqrt', 'exp'):
            function_expression = f"{sender}({current_text})"
            self.expression = function_expression
            self.display.setText(function_expression)
        else:
            self.expression += sender
            self.display.setText(current_text + sender)

    def save_to_file(self, text):
        with open('calc_history.txt', 'a') as file:
            file.write(text + '\n')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.calculator = Calculator()
        self.setCentralWidget(self.calculator)
        self.loadmenu()
        self.show()

    def loadmenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')

        saveButton = QAction('Save', self)
        saveButton.setShortcut('Ctrl+S')
        saveButton.triggered.connect(self.save_calculations)
        fileMenu.addAction(saveButton)

        openButton = QAction('Open', self)
        openButton.setShortcut('Ctrl+O')
        openButton.triggered.connect(self.open_calculations)
        fileMenu.addAction(openButton)

        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        editMenu = mainMenu.addMenu('Edit')
        clearButton = QAction('Clear', self)
        clearButton.setShortcut('Ctrl+M')
        clearButton.triggered.connect(self.clear_display)
        editMenu.addAction(clearButton)

        fontButton = QAction('Font', self)
        fontButton.setShortcut('Ctrl+D')
        fontButton.triggered.connect(self.show_font_dialog)
        editMenu.addAction(fontButton)

    def save_calculations(self):
        self.calculator.save_to_file(self.calculator.display.text())

    def open_calculations(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open calc history", "", "Text Files (*.txt);;All files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.calculator.display.setText(data)

    def clear_display(self):
        self.calculator.display.clear()

    def show_font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.calculator.display.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
