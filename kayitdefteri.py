import sys
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):
        self.setGeometry(200,350,800,200)
        self.setWindowTitle("Kayıt Formu")
        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()


        self.l1 = QtWidgets.QLabel("Name:")
        self.line1 = QtWidgets.QLineEdit()
        self.l2 = QtWidgets.QLabel("Address:")
        self.line2 = QtWidgets.QLineEdit()
        self.l3 = QtWidgets.QLabel("Phone:")
        self.line3 = QtWidgets.QLineEdit()
        self.l4 = QtWidgets.QLabel("Email:")
        self.line4 = QtWidgets.QLineEdit()
        self.save = QtWidgets.QPushButton("Save")
        self.clear = QtWidgets.QPushButton("Clear")
        self.exitt = QtWidgets.QPushButton("Exit")


        h_box.addWidget(self.l1)
        h_box.addWidget(self.line1)
        h_box.addWidget(self.l2)
        h_box.addWidget(self.line2)
        h_box.addWidget(self.l3)
        h_box.addWidget(self.line3)
        h_box.addWidget(self.l4)
        h_box.addWidget(self.line4)

        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()

        v_box.addWidget(self.save)
        v_box.addWidget(self.clear)
        v_box.addWidget(self.exitt)

        self.save.clicked.connect(self.click)
        self.clear.clicked.connect(self.click)
        self.exitt.clicked.connect(self.click)

        self.setLayout(v_box)
        self.show()

    def click(self):
        send = self.sender()

        if send.text() == "Save":
            file = open("ogrencino.txt", "a", encoding="utf-8")
            file.close()
            try:
                file = open("ogrencino.txt", "r", encoding="utf-8")
                bilgiler = "\n" + self.line1.text() + ":" + self.line2.text() + ":" + self.line3.text() + ":" + self.line4.text()
                bilgilerilk = self.line1.text() + ":" + self.line2.text() + ":" + self.line3.text() + ":" + self.line4.text()
                if file.readline() == "":
                    file.close()
                    file = open("ogrencino.txt", "a", encoding="utf-8")
                    file.write(bilgilerilk)
                    file.close()
                else:
                    file.close()
                    file = open("ogrencino.txt", "a", encoding="utf-8")
                    file.write(bilgiler)
                    file.close()
                print("Kayıt Başarılı")
            except FileNotFoundError:
                self.save.setText('Dosya yok')

        elif send.text() == "Clear":
            self.line1.setText("")
            self.line2.setText("")
            self.line3.setText("")
            self.line4.setText("")
        else:
            self.close()


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())