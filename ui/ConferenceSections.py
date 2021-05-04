# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conferenceSections.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from src.orm.orm import get_session_maker, Sections, Proposals,User



class Ui_ConferenceSections(object):


    def __init__(self,conference):
        self.conference = conference

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.conferenceSections = QtWidgets.QListWidget(self.centralwidget)
        self.conferenceSections.setGeometry(QtCore.QRect(10, 21, 771, 541))
        self.conferenceSections.setObjectName("conferenceSections")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.populateSections()

    def populateSections(self):
        self.conferenceSections.clear()
        Session = get_session_maker()
        session = Session()
        sectionQuery = session.query(Sections).all()
        for section in sectionQuery:
            proposalQuery = session.query(Proposals).filter(Proposals.id==section.proposalId)
            userQuery = session.query(User).filter(User.id==proposalQuery.first().authorId)
            text = "Section name: {}   Speaker: {} {}".format(proposalQuery.first().proposalName,userQuery.first().firstName,userQuery.first().lastName)
            self.conferenceSections.addItem(text)
        session.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

