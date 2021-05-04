# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainListenerMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

from src.orm.orm import get_session_maker, Conferences, PaidFees
from src.ui.ConferenceSections import Ui_ConferenceSections


class Ui_MainListenerMenu(object):

    ConferencesList = []

    def __init__(self,user):
        self.user = user

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listOfConferences = QtWidgets.QListWidget(self.centralwidget)
        self.listOfConferences.setGeometry(QtCore.QRect(10, 130, 541, 441))
        self.listOfConferences.setObjectName("listOfConferences")
        self.labelUsername = QtWidgets.QLabel(self.centralwidget)
        self.labelUsername.setGeometry(QtCore.QRect(0, 0, 701, 51))
        self.labelUsername.setObjectName("labelUsername")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 811, 51))
        self.label_2.setObjectName("label_2")


        self.payFeeButton = QtWidgets.QPushButton(self.centralwidget)
        self.payFeeButton.setGeometry(QtCore.QRect(570, 160, 191, 51))
        self.payFeeButton.setObjectName("payFeeButton")
        self.payFeeButton.clicked.connect(self.payFee)

        self.conferenceDetailsButton = QtWidgets.QPushButton(self.centralwidget)
        self.conferenceDetailsButton.setGeometry(QtCore.QRect(570, 240, 191, 51))
        self.conferenceDetailsButton.setObjectName("conferenceDetailsButton")
        self.conferenceDetailsButton.clicked.connect(self.attend)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.populateConferences()

        # setup a timer that updates the conferences list every 10 seconds
        self.timer = QTimer()
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.populateConferences)
        self.timer.start()

    def payFee(self):
        Session = get_session_maker()
        session = Session()
        query = session.query(PaidFees).filter(PaidFees.listenerId==self.user.id).filter(PaidFees.conferenceId==self.ConferencesList[self.listOfConferences.currentRow()].id)
        if query.first() is not None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("You have already paid the fee for this conference!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return

        qm = QMessageBox()
        qm.setIcon(QMessageBox.Question)
        qm.setWindowTitle("Pay fee")
        qm.setText(
            "Are you sure you want to pay the fee for " + self.ConferencesList[self.listOfConferences.currentRow()].conferenceName + "?")
        qm.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = qm.exec_()
        if retval == qm.Yes:
            paidFee = PaidFees(self.user.id, self.ConferencesList[self.listOfConferences.currentRow()].id)
            Session = get_session_maker()
            session = Session()
            session.add(paidFee)
            session.commit()
            session.close()

    def attend(self):
        Session = get_session_maker()
        session = Session()
        query = session.query(PaidFees).filter(PaidFees.listenerId==self.user.id).filter(PaidFees.conferenceId==self.ConferencesList[self.listOfConferences.currentRow()].id)
        if query.first() is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("You have not paid the fee for this conference yet!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ConferenceSections(self.ConferencesList[self.listOfConferences.currentRow()])
        self.ui.setupUi(self.window)
        self.window.show()


    def populateConferences(self):
        self.listOfConferences.clear()
        Session = get_session_maker()
        session = Session()
        conferencesQuery = session.query(Conferences).all()
        self.ConferencesList = []
        for conference in conferencesQuery:
            self.ConferencesList.append(conference)
            text = "{} Period [{}-{}]".format(conference.conferenceName,
                                                                                   conference.startingDate,
                                                                                   conference.endingDate)

            self.listOfConferences.addItem(text)
        session.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelUsername.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Hello "+self.user.firstName+"</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Choose any conference you want to attend, you will have to pay a fee before attending.</span></p></body></html>"))
        self.payFeeButton.setText(_translate("MainWindow", "Pay fee for selected conference"))
        self.conferenceDetailsButton.setText(_translate("MainWindow", "See conferance details and structure"))

