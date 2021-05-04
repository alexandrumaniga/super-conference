# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'review.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from src.orm.orm import get_session_maker, Proposals, ProposalsPc, ReviewResult, Sections
from src.ui.AbstractPaperView import Ui_AbstractWindow


class Ui_ReviewPapers(object):
    allProposals = []

    def __init__(self, user, conference):
        self.user = user
        self.conference = conference

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 602)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 40, 311, 241))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 16))
        self.label.setObjectName("label")
        self.viewFullPaperButton = QtWidgets.QPushButton(Form)
        self.viewFullPaperButton.setGeometry(QtCore.QRect(400, 110, 101, 41))
        self.viewFullPaperButton.setObjectName("viewFullPaperButton")
        self.viewFullPaperButton.clicked.connect(self.viewFull)

        self.viewPaperAbstractButton = QtWidgets.QPushButton(Form)
        self.viewPaperAbstractButton.setGeometry(QtCore.QRect(400, 190, 121, 41))
        self.viewPaperAbstractButton.setObjectName("viewPaperAbstractButton")
        self.viewPaperAbstractButton.clicked.connect(self.viewAbstract)

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 330, 311, 231))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 101, 16))
        self.label_2.setObjectName("label_2")

        self.strongRejectButton = QtWidgets.QPushButton(Form)
        self.strongRejectButton.setGeometry(QtCore.QRect(400, 330, 101, 31))
        self.strongRejectButton.setObjectName("strongRejectButton")
        self.strongRejectButton.clicked.connect(self.strongReject)

        self.rejectButton = QtWidgets.QPushButton(Form)
        self.rejectButton.setGeometry(QtCore.QRect(400, 380, 101, 31))
        self.rejectButton.setObjectName("rejectButton")
        self.rejectButton.clicked.connect(self.reject)

        self.borderlineButton = QtWidgets.QPushButton(Form)
        self.borderlineButton.setGeometry(QtCore.QRect(400, 430, 101, 31))
        self.borderlineButton.setObjectName("borderlineButton")
        self.borderlineButton.clicked.connect(self.borderline)

        self.acceptButton = QtWidgets.QPushButton(Form)
        self.acceptButton.setGeometry(QtCore.QRect(400, 480, 101, 31))
        self.acceptButton.setObjectName("acceptButton")
        self.acceptButton.clicked.connect(self.accept)

        self.strongAcceptButton = QtWidgets.QPushButton(Form)
        self.strongAcceptButton.setGeometry(QtCore.QRect(400, 530, 101, 41))
        self.strongAcceptButton.setObjectName("strongAcceptButton")
        self.strongAcceptButton.clicked.connect(self.strongAccept)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.populateProposals()

    def viewAbstract(self):
        print("d")
        text=self.allProposals[self.listWidget.currentRow()].proposalAbstract
        print(text)
        self.window = QtWidgets.QWidget()
        self.ui = Ui_AbstractWindow(self.allProposals[self.listWidget.currentRow()].proposalAbstract)
        self.ui.setupUi(self.window)
        self.window.show()

    def viewFull(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_AbstractWindow(self.allProposals[self.listWidget.currentRow()].proposalFull)
        self.ui.setupUi(self.window)
        self.window.show()

    def submitReview(self, review):
        Session = get_session_maker()
        session = Session()
        proposal = self.allProposals[self.listWidget.currentRow()]
        query = session.query(ReviewResult).filter(ReviewResult.proposalId == proposal.id).filter(
            ReviewResult.pcId == self.user.id)
        if query.first() is not None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("You have already reviewd this proposal!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return
        reviewResult = ReviewResult(proposal.id, self.user.id, review, self.textEdit.toPlainText())
        if(review > 2):
            section = Sections(proposal.id)
            session.add(section)
            session.commit()
        session.add(reviewResult)
        session.commit()

    def strongReject(self):
        self.submitReview(0)

    def reject(self):
        self.submitReview(1)

    def borderline(self):
        self.submitReview(2)

    def accept(self):
        self.submitReview(3)

    def strongAccept(self):
        self.submitReview(4)

    def populateProposals(self):
        self.listWidget.clear()
        Session = get_session_maker()
        session = Session()
        self.allProposals = []
        proposalsQuery = session.query(Proposals).filter(Proposals.conferenceId == self.conference.id)

        for proposal in proposalsQuery:
            proposalsQuery2 = session.query(ProposalsPc).filter(ProposalsPc.pcMemberId == self.user.id).filter(
                ProposalsPc.proposalId == proposal.id)
            for proposal2 in proposalsQuery2:
                textQuery = session.query(Proposals).filter(Proposals.id == proposal2.proposalId)
                self.allProposals.append(textQuery.first())
                text = textQuery.first().proposalName
                self.listWidget.addItem(text)
        session.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Proposals"))
        self.viewFullPaperButton.setText(_translate("Form", "View full paper"))
        self.viewPaperAbstractButton.setText(_translate("Form", "View paper abstract"))
        self.label_2.setText(_translate("Form", "Recommendations"))
        self.strongRejectButton.setText(_translate("Form", "Strong Reject"))
        self.rejectButton.setText(_translate("Form", "Reject"))
        self.borderlineButton.setText(_translate("Form", "Borderline"))
        self.acceptButton.setText(_translate("Form", "Accept"))
        self.strongAcceptButton.setText(_translate("Form", "Strong Accept"))
