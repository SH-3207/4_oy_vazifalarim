import json
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SH_3207.ilovasi")

        self.v_main_lay=QVBoxLayout()
        self.h_main_lay=QHBoxLayout()

        self.setStyleSheet("background:lightgreen")

        self.setFixedSize(450, 350)

        self.nomi=QLineEdit()
        self.nomi.setPlaceholderText("Film nomi ")
        self.v_main_lay.addWidget(self.nomi)

        self.Rejissor=QLineEdit()
        self.Rejissor.setPlaceholderText("Rejissor")
        self.v_main_lay.addWidget(self.Rejissor)

        self.yili=QLineEdit()
        self.yili.setPlaceholderText(" Yili- ")
        self.v_main_lay.addWidget(self.yili) 

        self.janr=QLineEdit()
        self.janr.setPlaceholderText(" Janri -")
        self.v_main_lay.addWidget(self.janr)     

        self.btn_qoshish=QPushButton("Qoshish ➕ ")
        self.btn_qoshish.clicked.connect(self.add)

        self.btn_exit=QPushButton(" Chiqish ❌")
        self.btn_exit.clicked.connect(exit)

        self.h_main_lay.addWidget(self.btn_qoshish)
        self.h_main_lay.addWidget(self.btn_exit)

        self.v_main_lay.addLayout(self.h_main_lay)
        
        self.setLayout(self.v_main_lay)

    def add(self):
        nomi=self.nomi.text()
        rejissor=self.Rejissor.text()
        yil=self.yili.text()
        janr=self.janr.text()


        if nomi and rejissor and yil and janr:

            try:
                yil=int(yil)
                self.nomi.clear()
                self.Rejissor.clear()
                self.janr.clear()
                self.yili.clear()

                QMessageBox().information(self, "Succses 👌", "Ajoyib Film Muvaffaqiyatli Qoshildi ✔️")
                with open("movies.json", "a")as f:
                  data={
                  "title":nomi,
                  "director":rejissor,
                  "year":int(yil),
                  "genre":janr
              }
                  json.dump(data, f, indent=4)
                  
            except ValueError:
                QMessageBox().warning(self,"ERROR 😡", "Yili- int Type da bolishi kerak ! 🤦")

        else:
            QMessageBox().warning(self,"ERROR 😡","Barcha Maydonlarni 👆 Toldirsh Shart !✍️")


app=QApplication([])
win=MyWindow()
win.show()
app.exec_()
