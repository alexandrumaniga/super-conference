# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BidProposals.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

from src.orm.orm import get_session_maker, Proposals, User, BiddingResults
from src.ui.AbstractPaperView import Ui_AbstractWindow


class Ui_BidProposals(object):
    allProposals = []

    def __init__(self, user, conference):
        self.user = user
        self.conference = conference

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.conferenceName = QtWidgets.QLabel(self.centralwidget)
        self.conferenceName.setGeometry(QtCore.QRect(20, 20, 761, 61))
        self.conferenceName.setObjectName("conferenceName")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 121, 21))
        self.label.setObjectName("label")

        self.listOfProposals = QtWidgets.QListWidget(self.centralwidget)
        self.listOfProposals.setGeometry(QtCore.QRect(10, 120, 511, 331))
        self.listOfProposals.setObjectName("listOfProposals")

        self.viewAbstractButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewAbstractButton.setGeometry(QtCore.QRect(530, 120, 191, 51))
        self.viewAbstractButton.setObjectName("viewAbstractButton")
        self.viewAbstractButton.clicked.connect(self.viewAbstractButtonFunction)

        self.viewFullButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewFullButton.setGeometry(QtCore.QRect(530, 190, 191, 51))
        self.viewFullButton.setObjectName("viewFullButton")
        self.viewFullButton.clicked.connect(self.viewFullButtonFunction)

        self.acceptReviewButton = QtWidgets.QPushButton(self.centralwidget)
        self.acceptReviewButton.setGeometry(QtCore.QRect(10, 470, 191, 51))
        self.acceptReviewButton.setObjectName("acceptReviewButton")
        self.acceptReviewButton.clicked.connect(self.acceptProposal)

        self.refuseReviewButton = QtWidgets.QPushButton(self.centralwidget)
        self.refuseReviewButton.setGeometry(QtCore.QRect(220, 470, 191, 51))
        self.refuseReviewButton.setObjectName("refuseReviewButton")
        self.refuseReviewButton.clicked.connect(self.refuseProposal)

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

        self.populateProposals()

        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.populateProposals)
        self.timer.start()

    def acceptProposal(self):
        #check if user did not already bid
        Session = get_session_maker()
        session = Session()
        query = session.query(BiddingResults).filter(BiddingResults.pcMemberId == self.user.id).filter(
            BiddingResults.proposalId == self.allProposals[self.listOfProposals.currentRow()].id
        )
        if query.first() is not None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("You have already bid this paper!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return
        #
        qm = QMessageBox()
        qm.setIcon(QMessageBox.Question)
        qm.setWindowTitle("Bid paper")
        qm.setText("Are you sure you want to bid "+ self.allProposals[self.listOfProposals.currentRow()].proposalName+"?")
        qm.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = qm.exec_()
        if retval == qm.Yes:
            result = BiddingResults(self.user.id,self.allProposals[self.listOfProposals.currentRow()].id,1)
            Session = get_session_maker()
            session = Session()
            session.add(result)
            session.commit()
            session.close()

    def refuseProposal(self):
        # check if user did not already bid
        Session = get_session_maker()
        session = Session()
        query = session.query(BiddingResults).filter(BiddingResults.pcMemberId == self.user.id).filter(
            BiddingResults.proposalId == self.allProposals[self.listOfProposals.currentRow()].id
        )
        if query.first() is not None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("You have already bid this paper!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return
        #
        qm = QMessageBox()
        qm.setWindowTitle("Refuse paper")
        qm.setIcon(QMessageBox.Question)
        qm.setText("Are you sure you want to refuse "+ self.allProposals[self.listOfProposals.currentRow()].proposalName+"?")
        qm.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = qm.exec_()
        if retval == qm.Yes:
            result = BiddingResults(self.user.id,self.allProposals[self.listOfProposals.currentRow()].id,0)
            Session = get_session_maker()
            session = Session()
            session.add(result)
            session.commit()
            session.close()

    def populateProposals(self):
        self.listOfProposals.clear()
        Session = get_session_maker()
        session = Session()
        proposalsQuery = session.query(Proposals).filter(Proposals.conferenceId == self.conference.id)
        self.allProposals = []
        for proposal in proposalsQuery:
            self.allProposals.append(proposal)
            author = session.query(User).filter(User.id == proposal.authorId)
            authorr = author.first()

            text = "{} Topic: {}  Author: {} {}".format(proposal.proposalName,
                                                        proposal.proposalTopic,
                                                        authorr.firstName,
                                                        authorr.lastName)
            self.listOfProposals.addItem(text)
        session.close()

    def viewAbstractButtonFunction(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_AbstractWindow(self.allProposals[self.listOfProposals.currentRow()].proposalAbstract)
        self.ui.setupUi(self.window)
        self.window.show()

    def viewFullButtonFunction(self):
        text = self.allProposals[self.listOfProposals.currentRow()].proposalFull
        if text is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("The author has not uploaded the full paper yet!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return

        self.window = QtWidgets.QWidget()
        self.ui = Ui_AbstractWindow(text)
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.conferenceName.setText(_translate("MainWindow",
                                               "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Bidding proposals for " + self.conference.conferenceName + "</span></p></body></html>"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:12pt;\">List of proposals:</span></p></body></html>"))
        self.viewAbstractButton.setText(_translate("MainWindow", "View Abstract of selected proposal"))
        self.viewFullButton.setText(_translate("MainWindow", "View Full Paper of selected proposal"))
        self.acceptReviewButton.setText(_translate("MainWindow", "Accept review of selected paper"))
        self.refuseReviewButton.setText(_translate("MainWindow", "Refuse review of selected paper"))
