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
        self.setWindowTitle('Demo QTextEdit')
        self.label1 = QLabel()
        self.label1.setText('No. HP')
        self.phoneEdit = QLineEdit()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.phoneEdit)
        self.label2 = QLabel()
        self.label2.setText('Pesan')
        self.messageEdit = QTextEdit()
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.messageEdit)
        vbox3 = QVBoxLayout()
        vbox3.addLayout(vbox1)
        vbox3.addLayout(vbox2)
        self.sendButton = QPushButton('&Kirim SMS')
        self.cancelButton = QPushButton('&Batal')
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.sendButton)
        hbox.addWidget(self.cancelButton)
        layout = QVBoxLayout()
        layout.addLayout(vbox3)
        horizontalLine = QFrame();
        horizontalLine.setFrameShape(QFrame.HLine)
        horizontalLine.setFrameShadow(QFrame.Sunken)
        layout.addWidget(horizontalLine)
        layout.addLayout(hbox)
        self.setLayout(layout)
#  Copyright (c) 2021.This code was written by Rohman Beny R (19104060)
