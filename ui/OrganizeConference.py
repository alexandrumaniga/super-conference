# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrganizeConference.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from src.orm.orm import get_session_maker, PC, Conferences, ConferencesPC


class Ui_OrganizeConference(object):
    ProgramMembers = []

    def __init__(self,user):
        self.user = user;

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 411, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 91, 16))
        self.label_2.setObjectName("label_2")
        self.conferenceName = QtWidgets.QLineEdit(self.centralwidget)
        self.conferenceName.setGeometry(QtCore.QRect(140, 80, 211, 20))
        self.conferenceName.setObjectName("conferenceName")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 240, 91, 16))
        self.label_4.setObjectName("label_4")
        self.startDate = QtWidgets.QDateEdit(self.centralwidget)
        self.startDate.setGeometry(QtCore.QRect(140, 190, 110, 22))
        self.startDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 6, 1), QtCore.QTime(0, 0, 0)))
        self.startDate.setObjectName("startDate")
        self.endingDate = QtWidgets.QDateEdit(self.centralwidget)
        self.endingDate.setGeometry(QtCore.QRect(140, 240, 110, 22))
        self.endingDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 6, 1), QtCore.QTime(0, 0, 0)))
        self.endingDate.setObjectName("endingDate")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 280, 91, 16))
        self.label_5.setObjectName("label_5")
        self.abstractDate = QtWidgets.QDateEdit(self.centralwidget)
        self.abstractDate.setGeometry(QtCore.QRect(140, 280, 110, 22))
        self.abstractDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 6, 1), QtCore.QTime(0, 0, 0)))
        self.abstractDate.setObjectName("abstractDate")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 320, 91, 16))
        self.label_6.setObjectName("label_6")
        self.proposalDate = QtWidgets.QDateEdit(self.centralwidget)
        self.proposalDate.setGeometry(QtCore.QRect(140, 320, 110, 22))
        self.proposalDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 6, 1), QtCore.QTime(0, 0, 0)))
        self.proposalDate.setObjectName("proposalDate")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 360, 91, 16))
        self.label_7.setObjectName("label_7")
        self.biddingDate = QtWidgets.QDateEdit(self.centralwidget)
        self.biddingDate.setGeometry(QtCore.QRect(140, 360, 110, 22))
        self.biddingDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 6, 1), QtCore.QTime(0, 0, 0)))
        self.biddingDate.setObjectName("biddingDate")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 200, 111, 16))
        self.label_8.setObjectName("label_8")
        self.pcMembers = QtWidgets.QListWidget(self.centralwidget)
        self.pcMembers.setGeometry(QtCore.QRect(370, 220, 256, 192))
        self.pcMembers.setObjectName("pcMembers")
        self.pcMemberToBeAdded = QtWidgets.QLineEdit(self.centralwidget)
        self.pcMemberToBeAdded.setGeometry(QtCore.QRect(630, 250, 113, 20))
        self.pcMemberToBeAdded.setObjectName("pcMemberToBeAdded")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(640, 230, 81, 16))
        self.label_9.setObjectName("label_9")

        self.addMember = QtWidgets.QPushButton(self.centralwidget)
        self.addMember.setGeometry(QtCore.QRect(630, 270, 41, 23))
        self.addMember.setObjectName("addMember")
        self.addMember.clicked.connect(self.addMemberButton)

        self.deleteMember = QtWidgets.QPushButton(self.centralwidget)
        self.deleteMember.setGeometry(QtCore.QRect(630, 320, 131, 23))
        self.deleteMember.setObjectName("deleteMember")
        self.deleteMember.clicked.connect(self.deleteMemberButton)

        self.organizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.organizeButton.setGeometry(QtCore.QRect(220, 450, 361, 101))
        self.organizeButton.setText("")
        self.organizeButton.setObjectName("organizeButton")
        self.organizeButton.clicked.connect(self.organizeButtonPress)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 470, 151, 51))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 130, 91, 16))
        self.label_11.setObjectName("label_11")
        self.description = QtWidgets.QTextEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(140, 110, 211, 71))
        self.description.setObjectName("description")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def organizeButtonPress(self):
        Session = get_session_maker()
        session = Session()
        conference = session.query(Conferences).filter(Conferences.conferenceName == self.conferenceName.text())
        if conference.first() is not None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("A conferance with this name already exists!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return

        conference = Conferences(self.conferenceName.text(), self.startDate.text(), self.endingDate.text(),
                                 self.abstractDate.text(), self.proposalDate.text(),
                                 self.biddingDate.text(), self.description.toPlainText(),
                                 self.user.id)  ###have to change chair later        session.add(conference)
        session.add(conference)

        session.commit()
        session = Session()

        conferencePCMember = ConferencesPC(self.user.id, conference.id, 1)
        session.add(conferencePCMember)

        for username in self.ProgramMembers:
            userQuery = session.query(PC).filter(PC.loginName == username)
            user = userQuery.first()
            conferencePCMember = ConferencesPC(user.id,conference.id,0)
            session.add(conferencePCMember)

        session.commit()
        session.close()

    def addMemberButton(self):
        Session = get_session_maker()
        session = Session()

        #cannot add yourself
        if self.pcMemberToBeAdded.text() == self.user.loginName:
            return
        users = session.query(PC).filter(PC.loginName == self.pcMemberToBeAdded.text())

        if users.first() is None:
            return

        user = users.first()
        if user.loginName not in self.ProgramMembers:
            self.ProgramMembers.append(user.loginName)
            text = "{} {}  -  {}".format(user.firstName, user.lastName, user.affiliation)
            self.pcMembers.addItem(text)

    def deleteMemberButton(self):
        if len(self.ProgramMembers) is not 0 and self.pcMembers.currentRow() is not -1:
            self.ProgramMembers.pop(self.pcMembers.currentRow())
        self.pcMembers.takeItem(self.pcMembers.currentRow())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ConferenceOrganization"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Conference Organization</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Conference Name"))
        self.label_3.setText(_translate("MainWindow", "Starting Date"))
        self.label_4.setText(_translate("MainWindow", "Ending Date"))
        self.label_5.setText(_translate("MainWindow", "Abstract Deadline"))
        self.label_6.setText(_translate("MainWindow", "Proposal Deadline"))
        self.label_7.setText(_translate("MainWindow", "Bidding Deadline"))
        self.label_8.setText(_translate("MainWindow", "Program Committee:"))
        self.label_9.setText(_translate("MainWindow", "Member name:"))
        self.addMember.setText(_translate("MainWindow", "Add"))
        self.deleteMember.setText(_translate("MainWindow", "Delete selected member"))
        self.label_10.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">ORGANIZE</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Description"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_OrganizeConference()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
