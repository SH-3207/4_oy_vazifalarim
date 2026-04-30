import json
from PyQt5.QtWidgets import *

app = QApplication([])

win = QWidget()
win.setWindowTitle("Form App")
win.setFixedSize(350, 400)

layout = QVBoxLayout()

name = QLineEdit()
name.setPlaceholderText("Name")

second = QLineEdit()
second.setPlaceholderText("Second")

age = QLineEdit()
age.setPlaceholderText("Age")

layout.addWidget(name)
layout.addWidget(second)
layout.addWidget(age)

city = QComboBox()
city.addItems(["Tashkent", "Samarqand", "Buxoro"])

layout.addWidget(QLabel("Shahar"))
layout.addWidget(city)

village = QComboBox()
layout.addWidget(QLabel("Tuman"))
layout.addWidget(village)


data = {
    "Tashkent": ["Zangiota", "Qibray", "Yangibozor"],
    "Samarqand": ["Urgut", "Toyloq", "Bulung‘ur"],
    "Buxoro": ["G‘ijduvon", "Romitan", "Vobkent"]
}

def update_village():
    village.clear()
    tanlangan = city.currentText()
    if tanlangan in data:
        village.addItems(data[tanlangan])

city.currentIndexChanged.connect(update_village)
update_village()

def submit():
    if not name.text() or not second.text() or not age.text():
        QMessageBox.warning(win, "Xatolik", "Barcha maydonlarni to‘ldiring!")
        return

    user_data = {
        "name": name.text(),
        "second": second.text(),
        "age": age.text(),
        "city": city.currentText(),
        "village": village.currentText()
    }

    try:
        with open("data.json", "r") as f:
            data_list = json.load(f)
    except:
        data_list = []

    data_list.append(user_data)

    with open("data.json", "a") as f:
        json.dump(data_list, f, indent=4)

    QMessageBox.information(win, "Success", "Muvaffaqiyatli qo‘shildi!")

    name.clear()
    second.clear()
    age.clear()

btn_submit = QPushButton("Submit")
btn_exit = QPushButton("Exit")

btn_submit.clicked.connect(submit)
btn_exit.clicked.connect(app.quit)

btn_layout = QHBoxLayout()
btn_layout.addWidget(btn_submit)
btn_layout.addWidget(btn_exit)

layout.addLayout(btn_layout)

win.setLayout(layout)

win.show()
app.exec_()