from PyQt5.QtWidgets import QWidget, QLabel

class MinimalForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(200, 100)
		self.move(300, 300)
		self.setWindowTitle('GUI Minimal')

		self.label = QLabel('Hello PyQt5')
		self.label.move(50, 40)
		self.label.setParent(self)
