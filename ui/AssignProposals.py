# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proposals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from src.orm.orm import get_session_maker
from src.orm.orm import Proposals
from src.ui.AssignReviewers import Ui_AssignReviewers


class Ui_AssignProposals(object):
    allProposals = []

    def __init__(self, conference):
        self.conference = conference

    def setupUi(self, Form):
        Form.setObjectName("MainWindow")
        Form.resize(586, 554)
        self.proposalList = QtWidgets.QListWidget(Form)
        self.proposalList.setGeometry(QtCore.QRect(10, 30, 311, 231))
        self.proposalList.setObjectName("proposalList")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")

        self.seeReviewersButton = QtWidgets.QPushButton(Form)
        self.seeReviewersButton.setGeometry(QtCore.QRect(390, 30, 131, 41))
        self.seeReviewersButton.setObjectName("seeReviewersButton")
        self.seeReviewersButton.clicked.connect(self.seeReviewersButtonHandler)

        self.populateProposals()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Proposals"))
        self.seeReviewersButton.setText(_translate("Form", "See Potential Reviewers"))

    def populateProposals(self):
        self.proposalList.clear()
        Session = get_session_maker()
        session = Session()
        self.allProposals = []
        proposalsQuery = session.query(Proposals).filter(Proposals.conferenceId == self.conference.id)
        for proposal in proposalsQuery:
            self.allProposals.append(proposal)
            text = proposal.proposalName
            self.proposalList.addItem(text)
        session.close()

    def seeReviewersButtonHandler(self):
        self.window = QtWidgets.QMainWindow()
        selectedProposal = self.allProposals[self.proposalList.currentRow()]
        self.ui = Ui_AssignReviewers(selectedProposal)
        self.ui.setupUi(self.window)
        self.window.show()