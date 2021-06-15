import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class DemoIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(400, 100)
        self.move(300, 300)
        self.setWindowTitle('Latihan Icon')
        self.label = QLabel()
        self.label.setText('<b>ALAMBUH BODOAMAAT</b>')
        icon1 = QIcon('delete-icon.png')

        self.button1 = QPushButton('\tHAPUS SI KUDU')
        self.button1.setIcon(icon1)
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0 , 1, 5)
        layout.addWidget(self.button1, 1, 0)
        self.setLayout(layout)

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = DemoIcon()
    form.show()
    a.exec_()