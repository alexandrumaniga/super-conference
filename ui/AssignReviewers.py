# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reviewers.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from src.orm.orm import get_session_maker
from src.orm.orm import PC, BiddingResults, ProposalsPc


class Ui_AssignReviewers(object):
    allReviewers = []

    def __init__(self, proposal):
        self.proposal = proposal

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(582, 548)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 291, 231))
        self.listWidget.setObjectName("listWidget")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 40, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonHandler)

        self.populateReviewers()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Potential Reviewers"))
        self.pushButton.setText(_translate("Form", "Assign"))

    def populateReviewers(self):
        self.listWidget.clear()
        Session = get_session_maker()
        session = Session()
        self.allReviewers = []
        biddindResultsQuery = session.query(BiddingResults).filter(BiddingResults.result == 1).filter(
            BiddingResults.proposalId == self.proposal.id)
        for biddingResult in biddindResultsQuery:
            reviewers = session.query(PC).filter(PC.id == biddingResult.pcMemberId)
            for reviewer in reviewers:
                self.allReviewers.append(reviewer)
        for reviewer in self.allReviewers:
            text = "{} {}".format(reviewer.firstName, reviewer.lastName)
            self.listWidget.addItem(text)
        session.close()

    def buttonHandler(self):
        Session = get_session_maker()
        session = Session()
        selectedReviewer = self.allReviewers[self.listWidget.currentRow()]
        assigned = ProposalsPc(selectedReviewer.id, self.proposal.id)
        session.add(assigned)
        session.commit()