from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class UI:
	app = QApplication(sys.argv)
	window = QMainWindow()
	window.setWindowTitle("Alice Assistant")


	def build_ui(self):
		button = QPushButton("Press Me!")
		self.window.setCentralWidget(button)


	def start(self):
		self.window.show()
		self.build_ui()
		self.app.exec()



if __name__ == "__main__":
	UI().start()