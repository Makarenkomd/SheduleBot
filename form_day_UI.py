# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_day_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem
import schedule_class

class Ui_MainWindow(object):
    widthSlot = 280
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 370, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 321, 371))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAutoScrollMargin(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("событие")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(280)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 319, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        # фрейм для отображения событий
        self.panelEvents = QVBoxLayout(self)
        self.panelEvents.setContentsMargins(0, 0, 0, 0)
        self.panelEvents

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.new_event()
        frame = QFrame(self)
        #frame.setGeometry(self.tableWidget.x() + self.tableWidget.verticalHeaderItem(0), self.tableWidget.y(), self.tableWidget.rect().width()                  self.tableWidget.rect().height())
        # frame.setMinimumSize(self.tableWidget.rect().width(), self.tableWidget.rect().height() - self.tableWidget.verticalHeader().width())
        frame.setGeometry(33, 66, Ui_MainWindow.widthSlot, 325)
        frame.setFrameStyle(QFrame.Box)
        frame.setLayout(self.panelEvents)
        #frame.setStyleSheet("background-color: cyan;")
        frame.setContentsMargins(0, 0, 0, 0)
        frame.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored))
        # ширина слота в один минуту
        self.oneMinSlot = (325 - 66) / (10 * 60)

    def new_event(self, event):

        oneEventFrame = QFrame()
        #oneEventFrame.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed))
        oneEventFrame.resize(Ui_MainWindow.widthSlot, event.duration * self.oneMinSlot)
        oneEventFrame.setContentsMargins(0, 0, 0, 0)
        color = QtGui.QColor(233, 10, 150)
        oneEventFrame.setStyleSheet("background-color: blue;")

        oneEventLayout = QHBoxLayout()
        oneEventLayout.setContentsMargins(0, 0, 0, 0)
        oneEventLayout.setObjectName("oneEventLayout")
        oneEventFrame.setLayout(oneEventLayout)


        labelNameEvent = QLabel()
        #labelNameEvent.setToolTipDuration(10)
        labelNameEvent.setObjectName("labelNameEvent")
        labelNameEvent.setText(event.time + " " + event.name)
        labelNameEvent.setAutoFillBackground(True)
        labelNameEvent.resize(Ui_MainWindow.widthSlot, oneEventFrame.height())
        oneEventLayout.addWidget(labelNameEvent)

        labelLinkImg = QLabel()
        labelLinkImg.setMouseTracking(False)
        labelLinkImg.setLayoutDirection(QtCore.Qt.RightToLeft)
        labelLinkImg.setText("")
        labelLinkImg.setPixmap(QtGui.QPixmap("gorizont.png"))
        #self.label_img.setOpenExternalLinks(True)
        #self.label_img.setObjectName("label_img")
        oneEventLayout.addWidget(labelLinkImg)

        return oneEventFrame

    def clearLayoutEvent(self, eventLayout):
        frame = eventLayout.widget().findChildren(type(QLabel()))
        frame[0].deleteLater()
        frame[1].deleteLater()
        eventLayout.widget().deleteLater()

    def clearPanelEvents(self):
        while self.panelEvents.count():
            child = self.panelEvents.takeAt(0)
            if isinstance(child, QtWidgets.QWidgetItem):
                self.clearLayoutEvent(child)
            self.panelEvents.removeItem(child)

    def add_events(self, events):
        self.clearPanelEvents()
        if len(events) == 0:
            return
        #9:00 - это начало таблицы времен
        begin_event = schedule_class.Event("", "", time="09:00", duration=0)
        for i in range(len(events)):

            self.add_space_widget(begin_event, events[i])
            event_widget = self.new_event(events[i])
            self.panelEvents.addWidget(event_widget)

            begin_event = events[i]
        self.panelEvents.setSpacing(0)
        end_event = schedule_class.Event("", "", time="22:00", duration=0)
        self.add_space_widget(begin_event, end_event)


    def add_space_widget(self, begin_event, end_event):
        dt = schedule_class.Event.time_interval(begin_event, end_event)
        heightSlotSpace = int(dt * self.oneMinSlot)
        spacerItem = QSpacerItem(20, heightSlotSpace)
        self.panelEvents.addSpacerItem(spacerItem)
        #print(dt, "пустота = ",heightSlotSpace)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "время"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "9:00"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "10:00"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "11:00"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "12:00"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "13:00"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "14:00"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "15:00"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "16:00"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "17:00"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "18:00"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "19:00"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "20:00"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "21:00"))


        self.menu.setTitle(_translate("MainWindow", "Добавить событие"))
        self.action.setText(_translate("MainWindow", "Руками"))
        self.action_2.setText(_translate("MainWindow", "Из текста"))
        self.action_3.setText(_translate("MainWindow", "Из календаря"))

