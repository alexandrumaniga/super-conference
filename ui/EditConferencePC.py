from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

from src.orm.orm import get_session_maker, PC, ConferencesPC, Conferences


class Ui_EditConferencePC(object):

    allMembers = []

    def __init__(self, user,conference):
        self.user = user
        self.conference = conference

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.membersLabel = QtWidgets.QLabel(self.centralwidget)
        self.membersLabel.setObjectName("membersLabel")
        self.verticalLayout.addWidget(self.membersLabel)
        self.membersList = QtWidgets.QListWidget(self.centralwidget)
        self.membersList.setObjectName("membersList")
        self.verticalLayout.addWidget(self.membersList)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 4, 1)
        self.coChairButton = QtWidgets.QPushButton(self.centralwidget)
        self.coChairButton.setObjectName("coChairButton")
        self.coChairButton.clicked.connect(self.onCoChairButtonClick)
        self.gridLayout_2.addWidget(self.coChairButton, 0, 1, 1, 2)
        self.listenerButton = QtWidgets.QPushButton(self.centralwidget)
        self.listenerButton.setObjectName("listenerButton")
        self.listenerButton.clicked.connect(self.onListenerButtonClick)

        self.gridLayout_2.addWidget(self.listenerButton, 1, 1, 1, 2)
        self.deadlineLabel = QtWidgets.QLabel(self.centralwidget)
        self.deadlineLabel.setObjectName("deadlineLabel")
        self.gridLayout_2.addWidget(self.deadlineLabel, 2, 1, 1, 1)
        self.deadLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.deadLineEdit.setObjectName("deadLineEdit")
        self.gridLayout_2.addWidget(self.deadLineEdit, 2, 2, 1, 1)
        self.updateDeadlineButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateDeadlineButton.setObjectName("updateDeadlineButton")
        self.updateDeadlineButton.clicked.connect(self.onUpdateDeadlineButtonClick)

        self.gridLayout_2.addWidget(self.updateDeadlineButton, 3, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.membersLabel.setBuddy(self.membersList)
        self.deadlineLabel.setBuddy(self.deadLineEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.populateMembers()

        #setup a timer that updates the conferences list every 3 seconds
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.populateMembers)
        self.timer.start()

    def populateMembers(self):
        self.membersList.clear()
        Session = get_session_maker()
        session = Session()
        membersQuery = session.query(ConferencesPC).filter(ConferencesPC.pcId != self.user.id).filter(ConferencesPC.conferenceId == self.conference.id)
        self.allMembers = []
        for member in membersQuery:
            pcQuery = session.query(PC).filter(PC.id == member.pcId)
            pc = pcQuery.first()
            self.allMembers.append(member)
            if member.chair == 0:
                text=" Co Chair: False"
            else:
                text=" Co Chair: True"
            self.membersList.addItem(pc.firstName + " " + pc.lastName + text)
        session.close()

    def onUpdateDeadlineButtonClick(self):
        deadline = self.deadLineEdit.text()
        Session = get_session_maker()
        session = Session()
        query = session.query(Conferences).filter(Conferences.id==self.conference.id).update({"abstractDeadline": deadline})
        session.commit()

    def onCoChairButtonClick(self):
        member = self.allMembers[self.membersList.currentRow()]
        if member.chair == 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("User is already chaired!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return

        Session = get_session_maker()
        session = Session()
        query = session.query(ConferencesPC).filter(
            ConferencesPC.pcId == member.id).update({"chair": 1})
        session.commit()

    def onListenerButtonClick(self):
        member = self.allMembers[self.membersList.currentRow()]
        if member.chair == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("User is not chair!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return
        Session = get_session_maker()
        session = Session()
        query = session.query(ConferencesPC).filter(
            ConferencesPC.pcId == member.id).update({"chair": 0})
        session.commit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.membersLabel.setText(_translate("MainWindow", "Members:"))
        self.coChairButton.setText(_translate("MainWindow", "Make member Co-chair"))
        self.listenerButton.setText(_translate("MainWindow", "Revoke Co-chair rights"))
        self.deadlineLabel.setText(_translate("MainWindow", "New Abstract Deadline: "))
        self.updateDeadlineButton.setText(_translate("MainWindow", "Update Deadline"))