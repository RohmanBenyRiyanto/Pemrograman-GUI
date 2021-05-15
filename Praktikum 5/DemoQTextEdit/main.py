import sys
from PyQt5.QtWidgets import QApplication
from DemoQTextEdit import *

if __name__ == '__main__':
    a = QApplication(sys.argv)
    minform = MainForm()
    minform.show()
    a.exec()
