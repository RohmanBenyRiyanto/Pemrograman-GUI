#  Copyright (c) 2021.This code was written by Rohman Beny R (19104060)

import sys
from PyQt5.QtWidgets import QApplication

from MainForm import *

if __name__ == '__main__':
	a = QApplication(sys.argv)

	form = MainForm()
	form.show()

	a.exec_()