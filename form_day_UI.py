# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_day_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem
import schedule_class
import form_add_event_UI

class Event_Frame(QFrame):
    def __init__(self, parent, table):
        super().__init__(parent)
        self.setGeometry(33, 66, Ui_MainWindow.widthSlot, 325)
        self.setFrameStyle(QFrame.Box)
        # frame.setStyleSheet("background-color: cyan;")
        self.table = table
        self.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored))

    def mousePressEvent(self, event):
        index = self.table.indexAt(event.pos())
        self.table.setCurrentCell(index.row(), 0)



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
        #self.tableWidget.setAutoScroll(False)
        #self.tableWidget.setAutoScrollMargin(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(14)
        for i in range(self.tableWidget.rowCount()):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("событие")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(280)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.itemChanged.connect(self.show_form_add_event)
        self.tableWidget.itemSelectionChanged.connect(self.show_form_add_event)
        #self.tableWidget.cellClicked.connect(show_form_add_event)
        #self.tableWidget.mousePressEvent = show_form_add_event

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

        self.actionAddHand = QtWidgets.QAction(MainWindow)
        self.actionAddHand.setObjectName("actionAddHand")

        self.actionAddText = QtWidgets.QAction(MainWindow)
        self.actionAddText.setObjectName("actionAddText")
        self.actionAddHand.triggered.connect(self.show_form_add_event)

        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.actionAddHand)
        self.menu.addAction(self.actionAddText)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        # фрейм для отображения событий
        self.panelEvents = QVBoxLayout(self)
        self.panelEvents.setContentsMargins(0, 0, 0, 0)
        self.panelEvents

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Frame для событий втечении дня
        frame = Event_Frame(self, self.tableWidget)
        frame.setLayout(self.panelEvents)
        # frame = QFrame(self)
        # #frame.setGeometry(self.tableWidget.x() + self.tableWidget.verticalHeaderItem(0), self.tableWidget.y(), self.tableWidget.rect().width()                  self.tableWidget.rect().height())
        # # frame.setMinimumSize(self.tableWidget.rect().width(), self.tableWidget.rect().height() - self.tableWidget.verticalHeader().width())
        # frame.setGeometry(33, 66, Ui_MainWindow.widthSlot, 325)
        # frame.setFrameStyle(QFrame.Box)
        # frame.setLayout(self.panelEvents)
        # #frame.setStyleSheet("background-color: cyan;")
        # frame.setContentsMargins(0, 0, 0, 0)
        # frame.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored))
        # #frame.mousePressEvent = show_form_add_event
        # # # ширина слота в одину минуту
        self.oneMinSlot = (325 - 66) / (10 * 60)

    def show_form_add_event(self):
        #print(item)
        self.form = form_add_event_UI.Ui_Dialog()
        self.form.show()

    def new_event(self, event):

        oneEventFrame = QFrame()
        heightSlot = event.duration * self.oneMinSlot
        #oneEventFrame.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed))
        #oneEventFrame.resize(Ui_MainWindow.widthSlot, heightSlot)
        oneEventFrame.setFixedHeight(heightSlot)
        oneEventFrame.setContentsMargins(0, 0, 0, 0)
        oneEventFrame.setStyleSheet("background-color: rgb(2, 116, 205); border-bottom: 1px solid rgb(128, 128, 255);")
        #color = QtGui.QColor(233, 10, 150)


        oneEventLayout = QHBoxLayout()
        oneEventLayout.setContentsMargins(0, 0, 0, 0)
        oneEventLayout.setObjectName("oneEventLayout")
        oneEventFrame.setLayout(oneEventLayout)
        oneEventLayout.setSpacing(0)

        labelNameEvent = QLabel()
        labelNameEvent.setToolTipDuration(10)
        labelNameEvent.setObjectName("labelNameEvent")
        #labelNameEvent.setText(event.time + " " + event.name)

        labelNameEvent.setAutoFillBackground(True)
        labelNameEvent.setFixedHeight(heightSlot)
        if event.link is not None:
            link = f'<a href="{event.link}">event.time + " " + event.name</a>'
        else:
            link = event.time + " " + event.name
        print(link)
        labelNameEvent.setText(link)
        labelNameEvent.setOpenExternalLinks(True)
        labelNameEvent.setStyleSheet("color: white;")
        sheet = "a { text-decoration: underline; color: white }"
        #labelNameEvent.setDefaultStyleSheet(sheet)
        #labelNameEvent.resize(Ui_MainWindow.widthSlot, oneEventFrame.height())
        oneEventLayout.addWidget(labelNameEvent)
        print(event.link)
        if event.link is not None:

            labelLinkImg = QLabel(link)
            labelLinkImg.setOpenExternalLinks(True)
            labelLinkImg.setMouseTracking(False)
            labelLinkImg.setLayoutDirection(QtCore.Qt.RightToLeft)
            labelLinkImg.setText("")
            labelLinkImg.setPixmap(QtGui.QPixmap("linkk.png"))
            labelLinkImg.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            #self.label_img.setOpenExternalLinks(True)
            #self.label_img.setObjectName("label_img")
            oneEventLayout.addWidget(labelLinkImg)

        return oneEventFrame

    def clearLayoutEvent(self, eventLayout):
        frame_temp = eventLayout.widget().findChildren(type(QLabel()))
        print(f"Удалить событие {frame_temp[0].text()}")
        frame_temp[0].deleteLater()
        if len(frame_temp) > 1:
            frame_temp[1].deleteLater()
        eventLayout.widget().deleteLater()

    def clearPanelEvents(self):
        print(f"Удалить {self.panelEvents.count()} слотов")
        while self.panelEvents.count():
            child = self.panelEvents.takeAt(0)
            if isinstance(child, QtWidgets.QWidgetItem):
                self.clearLayoutEvent(child)
            self.panelEvents.removeItem(child)
            print(type(child))


    def add_events(self, events):

        self.clearPanelEvents()
        print(f"Добавить {len(events)} событий")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Личный секретарь"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "время"))

        for i in range(1, self.tableWidget.rowCount()):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", str(8+i)+":00"))

        self.menu.setTitle(_translate("MainWindow", "Добавить событие"))
        self.actionAddHand.setText(_translate("MainWindow", "Руками"))
        self.actionAddText.setText(_translate("MainWindow", "Из текста"))
        self.action_3.setText(_translate("MainWindow", "Из календаря"))

