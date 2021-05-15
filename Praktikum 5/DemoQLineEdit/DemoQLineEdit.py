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
        self.resize(400, 200)
        self.move(300, 300)
        self.setWindowTitle('Demo QLabel, QLineEdit, dan QPushButton')
        self.label1 = QLabel()
        self.label1.setText('Bilangan pertama')
        self.numberEdit1 = QLineEdit()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.numberEdit1)
        self.label2 = QLabel()
        self.label2.setText('Bilangan kedua')
        self.numberEdit2 = QLineEdit()
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.numberEdit2)
        self.label3 = QLabel()
        self.label3.setText('Hasil Perhitungan')
        self.resultEdit = QLineEdit()
        self.resultEdit.setReadOnly(True)
        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.label3)
        vbox3.addWidget(self.resultEdit)
        vbox4 = QVBoxLayout()
        vbox4.addLayout(vbox1)
        vbox4.addLayout(vbox2)
        vbox4.addLayout(vbox3)
        vbox4.addStretch()
        self.addButton = QPushButton('&Tambah')
        self.substractButton = QPushButton('&Kurang')
        self.mulButton = QPushButton('K&ali')
        self.divButton = QPushButton('&Bagi')
        vbox5 = QVBoxLayout()
        vbox5.addWidget(self.addButton)
        vbox5.addWidget(self.substractButton)
        vbox5.addWidget(self.mulButton)
        vbox5.addWidget(self.divButton)
        vbox5.addStretch()
        layout = QHBoxLayout()
        layout.addLayout(vbox4)
        verticalLine = QFrame();
        verticalLine.setFrameShape(QFrame.VLine)
        verticalLine.setFrameShadow(QFrame.Sunken)
        layout.addWidget(verticalLine)
        layout.addLayout(vbox5)
        self.setLayout(layout)
        self.addButton.clicked.connect(self.addButtonClick)
        self.substractButton.clicked.connect(self.substractButtonClick)
        self.mulButton.clicked.connect(self.mulButtonClick)
        self.divButton.clicked.connect(self.divButtonClick)
    def calculate(self, operator):
        a = float(self.numberEdit1.text())
        b = float(self.numberEdit2.text())
        if operator == '+': c = a + b
        elif operator == '-': c = a - b
        elif operator == '*': c = a * b
        else: c = a / b
        self.resultEdit.setText(str(c))
    def addButtonClick(self):
        self.calculate('+')
    def substractButtonClick(self):
        self.calculate('-')
    def mulButtonClick(self):
        self.calculate('*')
    def divButtonClick(self):
        self.calculate('/')
