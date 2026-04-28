from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout

app = QApplication([])

win = QWidget()
win.setWindowTitle("SH_3207.ilovasi")
win.setFixedSize(600, 700)

line = QLineEdit()
line.setStyleSheet("font-size:20px; padding:10px;")

grid = QGridLayout()
grid.addWidget(line, 0, 0, 1, 4)


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

def on_click(text):
    if text == "=":
        try:
            result = eval(line.text())
            line.setText(str(result))
        except:
            line.setText("Error")
    elif text == "C":
        line.clear()
    else:
        line.setText(line.text() + text)

for text, row, col in buttons:
    btn = QPushButton(text)
    btn.setStyleSheet("font-size:18px; height:50px;")
    btn.clicked.connect(lambda _, t=text: on_click(t))
    grid.addWidget(btn, row, col)

win.setLayout(grid)

win.show()
app.exec_()