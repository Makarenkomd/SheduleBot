from schedule_class import Busy, Event
from form_day_UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import  QColor

import sys

class FormDay(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calendarWidget.clicked.connect(self.chooseDay)
        self.calendar = Busy()
        self.calendar.load()

    def chooseDay(self, d):
        self.add_events(self.calendar.get_today(d))


app = QApplication(sys.argv)
form = FormDay()
form.show()
sys.exit(app.exec_())

