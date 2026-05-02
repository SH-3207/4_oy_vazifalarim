from PyQt5.QtWidgets import *
import sys
import random

users = {}
current_user = ""
orders = []

STYLE = """
QWidget {
    background-color: #1e1e2f;
    color: white;
    font-size: 14px;
}
QPushButton {
    background-color: #3a86ff;
    border-radius: 10px;
    padding: 10px;
}
QPushButton:hover {
    background-color: #265df2;
}
"""

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ro'yxatdan o'tish")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.login = QLineEdit()
        self.login.setPlaceholderText("Login")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Parol")

        btn = QPushButton("Ro'yxatdan o'tish")
        btn.clicked.connect(self.register)

        back = QPushButton("Orqaga")
        back.clicked.connect(self.close)

        layout.addWidget(self.login)
        layout.addWidget(self.password)
        layout.addWidget(btn)
        layout.addWidget(back)

        self.setLayout(layout)

    def register(self):
        users[self.login.text()] = self.password.text()
        QMessageBox.information(self, "OK", "Ro'yxatdan o'tdingiz!")
        self.close()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.login = QLineEdit()
        self.login.setPlaceholderText("Login")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Parol")

        btn = QPushButton("Kirish")
        btn.clicked.connect(self.login_func)

        reg = QPushButton("Register")
        reg.clicked.connect(self.open_register)

        layout.addWidget(self.login)
        layout.addWidget(self.password)
        layout.addWidget(btn)
        layout.addWidget(reg)

        self.setLayout(layout)

    def login_func(self):
        global current_user
        if users.get(self.login.text()) == self.password.text():
            current_user = self.login.text()
            self.main = MainMenu()
            self.main.show()
            self.close()
        else:
            QMessageBox.warning(self, "Xato", "Login yoki parol noto‘g‘ri")

    def open_register(self):
        self.reg = RegisterWindow()
        self.reg.show()

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asosiy menyu")
        self.setFixedSize(300, 400)

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"Xush kelibsiz {current_user}"))

        btn1 = QPushButton("🍔 Menyu")
        btn1.clicked.connect(self.open_menu)

        btn2 = QPushButton("🧾 Buyurtmalar")
        btn2.clicked.connect(self.open_orders)

        btn3 = QPushButton("💰 Hisob")
        btn3.clicked.connect(self.open_payment)

        btn4 = QPushButton("🎁 Bonus o'yin")
        btn4.clicked.connect(self.open_bonus)

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)

        self.setLayout(layout)

    def open_menu(self):
        self.w = MenuWindow()
        self.w.show()

    def open_orders(self):
        self.w = OrderWindow()
        self.w.show()

    def open_payment(self):
        self.w = PaymentWindow()
        self.w.show()

    def open_bonus(self):
        self.w = BonusWindow()
        self.w.show()


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menyu")
        self.setFixedSize(300, 400)

        layout = QVBoxLayout()

        self.menu = {"Burger":25000,"Pizza":45000,"Cola":10000}
        self.boxes = []

        for i, p in self.menu.items():
            cb = QCheckBox(f"{i} - {p}")
            self.boxes.append(cb)
            layout.addWidget(cb)

        btn = QPushButton("Qo‘shish")
        btn.clicked.connect(self.add)

        back = QPushButton("Orqaga")
        back.clicked.connect(self.close)

        layout.addWidget(btn)
        layout.addWidget(back)

        self.setLayout(layout)

    def add(self):
        for cb in self.boxes:
            if cb.isChecked():
                name, price = cb.text().split("-")
                orders.append((name.strip(), int(price)))
        QMessageBox.information(self, "OK", "Qo‘shildi")

class OrderWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buyurtmalar")
        self.setFixedSize(300, 400)

        layout = QVBoxLayout()

        self.list = QListWidget()
        layout.addWidget(self.list)

        btn = QPushButton("Yangilash")
        btn.clicked.connect(self.load)

        back = QPushButton("Orqaga")
        back.clicked.connect(self.close)

        layout.addWidget(btn)
        layout.addWidget(back)

        self.setLayout(layout)

    def load(self):
        self.list.clear()
        for i,p in orders:
            self.list.addItem(f"{i} - {p}")


class PaymentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hisob")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.label = QLabel("0 so'm")
        layout.addWidget(self.label)

        btn = QPushButton("Hisoblash")
        btn.clicked.connect(self.calc)

        back = QPushButton("Orqaga")
        back.clicked.connect(self.close)

        layout.addWidget(btn)
        layout.addWidget(back)

        self.setLayout(layout)

    def calc(self):
        total = sum(p for _,p in orders)
        self.label.setText(f"{total} so'm")


class BonusWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bonus")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Tugmani bos va bonus ol!")
        layout.addWidget(self.label)

        btn = QPushButton("🎲 O‘yna")
        btn.clicked.connect(self.play)

        back = QPushButton("Orqaga")
        back.clicked.connect(self.close)

        layout.addWidget(btn)
        layout.addWidget(back)

        self.setLayout(layout)

    def play(self):
        discount = random.choice([0,5,10,20])
        self.label.setText(f"Siz {discount}% chegirma yutdingiz!")



app = QApplication(sys.argv)
app.setStyleSheet(STYLE)

win = LoginWindow()
win.show()

sys.exit(app.exec_())