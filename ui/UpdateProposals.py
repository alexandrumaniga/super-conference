# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateProposals.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from src.orm.orm import get_session_maker, Proposals, User


class Ui_UpdateProposals(object):
    allProposals = []

    def __init__(self,user,conference):
        self.user = user
        self.conference = conference

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.proposalsList = QtWidgets.QListWidget(self.centralwidget)
        self.proposalsList.setGeometry(QtCore.QRect(10, 50, 761, 361))
        self.proposalsList.setObjectName("proposalsList")
        self.labelConference = QtWidgets.QLabel(self.centralwidget)
        self.labelConference.setGeometry(QtCore.QRect(10, 0, 521, 41))
        self.labelConference.setObjectName("labelConference")
        self.updateAbstractButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateAbstractButton.setGeometry(QtCore.QRect(50, 440, 171, 41))
        self.updateAbstractButton.setObjectName("updateAbstractButton")
        self.updateAbstractButton.clicked.connect(self.updateAbstract)

        self.updateFullButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateFullButton.setGeometry(QtCore.QRect(240, 440, 171, 41))
        self.updateFullButton.setObjectName("updateFullButton")
        self.updateFullButton.clicked.connect(self.updateFull)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.populateProposals()

    def populateProposals(self):
        self.proposalsList.clear()
        Session = get_session_maker()
        session = Session()
        proposalsQuery = session.query(Proposals).filter(Proposals.conferenceId == self.conference.id).filter(Proposals.authorId==self.user.id)
        self.allProposals = []
        for proposal in proposalsQuery:
            self.allProposals.append(proposal)
            text = "{} Topic: {} ".format(proposal.proposalName,
                                                        proposal.proposalTopic)
            self.proposalsList.addItem(text)
        session.close()

    def updateAbstract(self):
        qd = QFileDialog()
        qd.setFileMode(QFileDialog.AnyFile)
        if qd.exec_():
            fnames = qd.selectedFiles()
            f = open(fnames[0], 'r')
            with f:
                data = f.read()
                Session = get_session_maker()
                session = Session()
                query = session.query(Proposals).filter(Proposals.id==self.allProposals[self.proposalsList.currentRow()].id).update({"proposalAbstract":data})
                session.commit()


    def updateFull(self):
        qd = QFileDialog()
        qd.setFileMode(QFileDialog.AnyFile)
        if qd.exec_():
            fnames = qd.selectedFiles()
            f = open(fnames[0], 'r')
            with f:
                data = f.read()
                Session = get_session_maker()
                session = Session()
                query = session.query(Proposals).filter(Proposals.id==self.allProposals[self.proposalsList.currentRow()].id).update({"proposalFull":data})
                session.commit()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelConference.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Your proposals at " + self.conference.conferenceName + "</span></p></body></html>"))
        self.updateAbstractButton.setText(_translate("MainWindow", "Update Abstract"))
        self.updateFullButton.setText(_translate("MainWindow", "Update Full Paper"))

