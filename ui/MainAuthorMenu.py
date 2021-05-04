# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainAuthorMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

from src.orm.orm import get_session_maker, Conferences
from src.ui.SubmitProposal import Ui_SubmitProposal
from src.ui.UpdateProposals import Ui_UpdateProposals


class Ui_MainAuthorMenu(object):

    ConferencesList = []

    def __init__(self, user):
        self.user = user

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 191, 61))
        self.label.setObjectName("label")
        self.listConferences = QtWidgets.QListWidget(self.centralwidget)
        self.listConferences.setGeometry(QtCore.QRect(10, 160, 511, 371))
        self.listConferences.setObjectName("listConferences")
        self.submitProposalButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitProposalButton.setGeometry(QtCore.QRect(530, 210, 231, 71))
        self.submitProposalButton.setObjectName("submitProposalButton")
        self.submitProposalButton.clicked.connect(self.submitProposal)

        #status

        #update button
        self.submitProposalButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.submitProposalButton_2.setGeometry(QtCore.QRect(530, 300, 231, 71))
        self.submitProposalButton_2.setObjectName("submitProposalButton_2")
        self.submitProposalButton_2.clicked.connect(self.updateProposals)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #initialize conference menu
        self.populateConferences()

        #setup a timer that updates the conferences list every 10 seconds
        self.timer = QTimer()
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.populateConferences)
        self.timer.start()


    def submitProposal(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SubmitProposal(self.user,self.ConferencesList[self.listConferences.currentRow()])
        self.ui.setupUi(self.window)
        self.window.show()

    def updateProposals(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_UpdateProposals(self.user, self.ConferencesList[self.listConferences.currentRow()])
        self.ui.setupUi(self.window)
        self.window.show()

    def populateConferences(self):
        self.listConferences.clear()
        Session = get_session_maker()
        session = Session()
        conferencesQuery = session.query(Conferences).all()
        self.ConferencesList = []
        for conference in conferencesQuery:
            self.ConferencesList.append(conference)
            text = "{} [{}-{}] Abstract deadline: {} Proposal deadline: {}".format(conference.conferenceName,conference.startingDate,conference.endingDate,
                                                                                            conference.abstractDeadline,conference.proposalDeadline)
            self.listConferences.addItem(text)
        session.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Hello " + self.user.firstName + "</span></p></body></html>"))
        self.submitProposalButton.setText(_translate("MainWindow", "Submit proposal at the selected conference"))
        self.submitProposalButton_2.setText(_translate("MainWindow", "Update proposal at the selected conference"))

