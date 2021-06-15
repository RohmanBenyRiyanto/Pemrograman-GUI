import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 150)
        self.move(300, 300)
        self.setWindowTitle('Tugas QRadioButton')

        self.label1 = QLabel()
        self.label1.setText('Bilangan pertama')
        self.linepertama = QLineEdit()
        self.label2 = QLabel()
        self.label2.setText('Bilangan kedua')
        self.linekedua = QLineEdit()
        horizontalLine = QFrame();
        horizontalLine.setFrameShape(QFrame.HLine)
        horizontalLine.setFrameShadow(QFrame.Sunken)

        self.tambah = QRadioButton()
        self.tambah.setText('Tambah')
        self.kurang = QRadioButton()
        self.kurang.setText('Kurang')
        self.kali = QRadioButton()
        self.kali.setText('Kali')
        self.bagi = QRadioButton()
        self.bagi.setText('Bagi')

        self.myfont = QFont()
        self.myfont.setBold(True)
        self.hasil = QLabel()
        self.hasil.setFont(self.myfont)
        self.hasil.setText('Hasil')
        self.hitung = QPushButton()
        self.hitung.setText('Hitung')

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.linepertama, 0, 1, 1, 3)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.linekedua, 1, 1, 1, 3)
        layout.addWidget(self.tambah, 2, 0)
        layout.addWidget(self.kurang, 2, 1)
        layout.addWidget(self.kali, 2, 2)
        layout.addWidget(self.bagi, 2, 3)
        layout.addWidget(horizontalLine, 4, 0, 1, 4)
        layout.addWidget(self.hasil, 5, 0, 1, 2)
        layout.addWidget(self.hitung, 6, 0, 1, 4)

        self.hitung.clicked.connect(self.hitungan)
        self.setLayout(layout)

    def hitungan(self):
        a = float(self.linepertama.text())
        b = float(self.linekedua.text())

        if self.tambah.isChecked():
            jumlah = a + b
            self.hasil.setText('Hasil penjumlahan : ' + str(jumlah))
        elif self.kurang.isChecked():
            pengurangan = a - b
            self.hasil.setText('Hasil pengurangan : ' + str(pengurangan))
        elif self.kali.isChecked():
            perkalian = a * b
            self.hasil.setText('Hasil perkalian : ' + str(perkalian))
        elif self.bagi.isChecked():
            pembagian = a / b
            self.hasil.setText('Hasil pembagian : ' + str(pembagian))
        else:
            self.hasil.setText('Belum memilih operasi matematika')


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()