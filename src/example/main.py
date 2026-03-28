import sys
from PySide6 import QtUiTools
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel

from example.components.lexica import MyLexer
from example.components.parsers import ASTParser
from example.components.memory import Memory
from example.components.ui import Ui_MainWindow

class MainWindow(QMainWindow):

    # Do this for intellisense
    button_t:QPushButton
    button_f:QPushButton

    button_and:QPushButton
    button_or:QPushButton
    button_equal:QPushButton

    input_text:QLineEdit
  
    output_eval:QLabel # Evaluation ouput
    output_trans:QLabel # Translation ouput
    output_tree:QLabel # AST ouput

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #### Binding button to function ####
        # Method 2:
        self.ui.button_t.clicked.connect(lambda: self.push("t"))
        self.ui.button_f.clicked.connect(lambda: self.push("f"))
        self.ui.button_and.clicked.connect(lambda: self.push("∧"))
        self.ui.button_or.clicked.connect(lambda: self.push("∨"))

        self.ui.button_equal.clicked.connect(self.push_equal)

    # Method 2
    def push(self, text:str):
        current_text:str = self.ui.input_text.text()
        self.ui.input_text.setText(f"{current_text}{text}")
    
    def push_equal(self):
        print("Calculate")
        lexer = MyLexer()
        parser = ASTParser()
        memory = Memory()
        input_text = self.ui.input_text.text()
        result = parser.parse(lexer.tokenize(input_text))
        print(type(result))
        self.ui.label_eval.setText(str(result))
        self.ui.label_trans.setText(str(result))
        self.ui.label_tree.setText(str(result))
        # for debug
        print(memory)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())