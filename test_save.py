from schedule_class import Event, Busy
import datetime as dt
from PyQt5 import QtCore

# importing the required libraries

from PyQt5.QtWidgets import QLabel, QPushButton, QMainWindow, QApplication, QVBoxLayout, QFrame, QGridLayout, QSpacerItem
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.s = self
		self.setWindowTitle("Динамический label")
		self.setGeometry(0, 0, 400, 300)
		self.button = QPushButton("создать label", self)
		self.button.clicked.connect(self.run)
		self.button.setGeometry(200, 100, 100, 20)
		self.panel = QVBoxLayout(self)
		#self.panel.addWidget(self.button)

		self.frame = QFrame(self)
		self.frame.setMinimumSize(200, 300)
		self.frame.setFrameStyle(QFrame.Box)
		self.frame.setLayout(self.panel)

		#self.panel.setGeometry(self.rect())
		#self.setLayout(self.panel)
		#self.run()

	def run(self):
		spacerItem = QSpacerItem(20, 55)
		self.panel.insertSpacerItem(0, spacerItem)
		label = QLabel('This is label')
		#label.setGeometry(100, 100, 100, 20)
		#self.panel.addWidget(spacerItem)
		self.panel.addWidget(label)
		#self.panel.insertWidget(1, label)
		self.panel.addStretch()


App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())

#now = QtCore.QDateTime.currentDateTime()
#now = QtCore.QDate(2021, 1, 5)
#print(now)
#d = now.toPyDate()
#print(d)
#d = dt.datetime.strptime("12.01.2020", '%d.%m.%Y')
#print(d)

#b = Busy()
#b.load()


#b.add_event(Event("Программы ИВТ", "25.12.2021", "nosu.ru", [1, 2], "Вика"))
#b.add_event(Event("Яндекс куб", "11.01.2021"))
#a = b.get_today("11.01.2021")
#b.save()
#print(b)
