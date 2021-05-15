#  Copyright (c) 2021.This code was written by Rohman Beny R (19104060)

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
        self.setWindowTitle('Demo QRadioButton')
        self.label1 = QLabel()
        self.label1.setText('Bilangan pertama')
        self.numberEdit1 = QLineEdit()
        self.label2 = QLabel()
        self.label2.setText('Bilangan kedua')
        self.numberEdit2 = QLineEdit()
        grid = QGridLayout()
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.numberEdit1, 0, 1)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.numberEdit2, 1, 1)
        self.addRadio = QRadioButton()
        self.addRadio.setText('&Tambah')
        self.addRadio.setChecked(True)
        self.substractRadio = QRadioButton()
        self.substractRadio.setText('&Kurang')
        self.mulRadio = QRadioButton()
        self.mulRadio.setText('K&ali')
        self.divRadio = QRadioButton()
        self.divRadio.setText('&Bagi')
        hbox = QHBoxLayout()
        hbox.addWidget(self.addRadio)
        hbox.addWidget(self.substractRadio)
        hbox.addWidget(self.mulRadio)
        hbox.addWidget(self.divRadio)
        self.resultLabel = QLabel('<b>Hasil penjumlahan: </b>')
        self.calculateButton = QPushButton('Hitung')
        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(hbox)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.calculateButton)
        layout.addStretch()
        self.setLayout(layout)
        self.addRadio.clicked.connect(
            lambda: self.resultLabel.setText('<b>Hasil penjumlahan: </b>'))
        self.substractRadio.clicked.connect(
            lambda: self.resultLabel.setText('<b>Hasil pengurangan: </b>'))
        self.mulRadio.clicked.connect(
            lambda: self.resultLabel.setText('<b>Hasil perkalian: </b>'))
        self.divRadio.clicked.connect(
            lambda: self.resultLabel.setText('<b>Hasil pembagian: </b>'))
        self.calculateButton.clicked.connect(self.calculateButtonClick)

    def calculateButtonClick(self):
        a = float(self.numberEdit1.text())
        b = float(self.numberEdit2.text())
        if self.addRadio.isChecked(): c = a + b
        elif self.substractRadio.isChecked(): c = a - b
        elif self.mulRadio.isChecked(): c = a * b
        else: c = a / b
        index = str(self.resultLabel.text()).index(':')
        s = str(self.resultLabel.text())[:index+1]
        self.resultLabel.setText('%s %.2f %s' % (s, c,
        '</b>'))
