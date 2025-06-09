import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout

class Calculator(QWidget):
    # define the Calculator constructor
    def __init__(self):
        # Qwidget constructor is called
        super().__init__()
        self.setWindowTitle("Calculator in PyQt")
        self.create_ui()
    
    def create_ui(self):
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(40)

        layout = QVBoxLayout()
        layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', 'C', '=', '+'),
        ]

        # enumerate returns a list of pairs i.e. (0, seq[0]), (1, seq[0])
        # seq[0] is a tuple

        # row = 0, rowValues = { buttons[0][0], buttons[0][1], buttons[0][2], buttons[0][3]}
        # row = 1, rowValues = { buttons[1][0], buttons[1][1], buttons[1][2], buttons[1][3]}
        # ...

        for row, row_values in enumerate(buttons):
            # col is the index and the value is the actual character there
            # (col = 0, '7'), (col = 1, '8'), (col = 2, '9'), (col = 3, '/')
            for col, value in enumerate(row_values):
                button = QPushButton(value)
                button.setFixedSize(50,50)
                #val=value capture the current value at the time the lamda is defined
                # o.w. you'd end up passing the last value in the loop to every button click
                button.clicked.connect(lambda _, val=value: self.on_button_click(val))
                grid.addWidget(button, row, col)

        #setup the layout
        layout.addLayout(grid)
        self.setLayout(layout)

    def on_button_click(self, value):
        if value == 'C':
            self.display.clear()
        elif value == '=':
            # prevent something like Division by Zero
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + value)

def main():
   # Setup the app 
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()