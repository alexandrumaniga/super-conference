# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPCMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

from src.ui.AssignProposals import Ui_AssignProposals
from src.ui.BidProposals import Ui_BidProposals
from src.ui.EditConferencePC import Ui_EditConferencePC
from src.ui.OrganizeConference import Ui_OrganizeConference
from src.orm.orm import get_session_maker, Conferences, ConferencesPC
import datetime,time

from src.ui.ReviewPapers import Ui_ReviewPapers


class Ui_MainPCMenu(object):

    allConferences = []

    def __init__(self, user):
        self.user = user

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.conferencesList = QtWidgets.QListWidget(self.centralwidget)
        self.conferencesList.setGeometry(QtCore.QRect(10, 190, 521, 381))
        self.conferencesList.setObjectName("conferencesList")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 31))
        self.label.setObjectName("label")


        self.organizeConferenceButton = QtWidgets.QPushButton(self.centralwidget)
        self.organizeConferenceButton.setGeometry(QtCore.QRect(10, 120, 221, 61))
        self.organizeConferenceButton.setObjectName("organizeConferenceButton")
        self.organizeConferenceButton.clicked.connect(self.organizeConference)

        #this is actually edit conference
        self.bidConferenceButton = QtWidgets.QPushButton(self.centralwidget)
        self.bidConferenceButton.setGeometry(QtCore.QRect(540, 190, 221, 61))
        self.bidConferenceButton.setObjectName("bidConferenceButton")
        self.bidConferenceButton.clicked.connect(self.editConference)

        self.bidConferenceButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bidConferenceButton_2.setGeometry(QtCore.QRect(540, 260, 221, 61))
        self.bidConferenceButton_2.setObjectName("bidConferenceButton_2")
        self.bidConferenceButton_2.clicked.connect(self.bidProposals)

        self.reviewButton = QtWidgets.QPushButton(self.centralwidget)
        self.reviewButton.setGeometry(QtCore.QRect(540, 330, 221, 61))
        self.reviewButton.setObjectName("reviewButton")
        self.reviewButton.clicked.connect(self.reviewProposals)

        self.viewProposalsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewProposalsButton.setGeometry(QtCore.QRect(540, 400, 221, 61))
        self.viewProposalsButton.setObjectName("viewProposalsButton")
        self.viewProposalsButton.clicked.connect(self.assignProposalsButtonHandler)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #init conferences list
        self.populateConferences()

        #setup a timer that updates the conferences list every 3 seconds
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.populateConferences)
        self.timer.start()

    def reviewProposals(self):
        Session = get_session_maker()
        session = Session()
        query = session.query(ConferencesPC).filter(ConferencesPC.pcId == self.user.id).filter(
            ConferencesPC.conferenceId == self.allConferences[self.conferencesList.currentRow()].id)
        user = query.first()
        if user is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("You are not part of the Program Committee of this conference!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return
        conference = self.allConferences[self.conferencesList.currentRow()]
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ReviewPapers(self.user,conference)
        self.ui.setupUi(self.window)
        self.window.show()

    def assignProposalsButtonHandler(self):
        conference = self.allConferences[self.conferencesList.currentRow()]
        if conference.chair != self.user.id:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("You are not a chair of this conference!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AssignProposals(conference)
        self.ui.setupUi(self.window)
        self.window.show()

    def editConference(self):
        conference = self.allConferences[self.conferencesList.currentRow()]
        if conference.chair != self.user.id:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("You are not a chair of this conference!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EditConferencePC(self.user,conference)
        self.ui.setupUi(self.window)
        self.window.show()

    def bidProposals(self):
        #check if user is part of the pc of that conference
        Session = get_session_maker()
        session = Session()
        query = session.query(ConferencesPC).filter(ConferencesPC.pcId == self.user.id).filter(
            ConferencesPC.conferenceId == self.allConferences[self.conferencesList.currentRow()].id)
        user = query.first()
        if user is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("You are not part of the Program Committee of this conference!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return

        #check time
        today = datetime.date.today()
        date = today.strftime("%m/%d/%Y")
        day,month,year = date.split('/')
        currentTime = datetime.datetime(int(year), int(month), int(day)).timestamp()

        dbTime = self.allConferences[self.conferencesList.currentRow()].biddingDeadline
        day,month,year = dbTime.split('/')
        biddingTime = datetime.datetime(int(year),int(month),int(day)).timestamp()

        '''''
        if(currentTime > biddingTime):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Bidding period is over!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return
        '''

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BidProposals(self.user, self.allConferences[self.conferencesList.currentRow()])
        self.ui.setupUi(self.window)
        self.window.show()

    def populateConferences(self):
        self.conferencesList.clear()
        Session = get_session_maker()
        session = Session()
        self.allConferences = []
        conferencesQuery = session.query(Conferences).all()
        for conference in conferencesQuery:
            self.allConferences.append(conference)
            text = "{} [{}-{}] Bidding deadline: {}".format(conference.conferenceName,
                                                                                   conference.startingDate,
                                                                                   conference.endingDate,
                                                                                   conference.biddingDeadline)
            self.conferencesList.addItem(text)
        session.close()

    def organizeConference(self):
        #self.window.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OrganizeConference(self.user)
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.conferencesList.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Hello "+self.user.firstName+"</span><br/></p></body></html>"))
        self.organizeConferenceButton.setText(_translate("MainWindow", "Organize a new conference"))
        self.bidConferenceButton.setText(_translate("MainWindow", "Edit selected conference"))
        self.bidConferenceButton_2.setText(_translate("MainWindow", "Bid Proposals of Selected Confernece"))
        self.reviewButton.setText(_translate("MainWindow", "Review Proposals of Selected Conference"))
        self.viewProposalsButton.setText(_translate("MainWindow", "Assign Proposals to Reviewers(Chair)"))

