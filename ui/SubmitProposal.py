# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubmitProposal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from src.orm.orm import get_session_maker, Proposals, ProposalsKeywords, ProposalsAuthors


class QStringList(object):
    pass


class Ui_SubmitProposal(object):

    keywords=[]
    authorNames=[]
    abstractPaper = None
    fullPaper = None

    def __init__(self,user,conference):
        self.user = user
        self.conference = conference

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 751, 51))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 81, 16))
        self.label_2.setObjectName("label_2")

        self.proposalName = QtWidgets.QLineEdit(self.centralwidget)
        self.proposalName.setGeometry(QtCore.QRect(100, 120, 201, 20))
        self.proposalName.setObjectName("proposalName")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 47, 13))
        self.label_3.setObjectName("label_3")

        self.listOfKeywords = QtWidgets.QListWidget(self.centralwidget)
        self.listOfKeywords.setGeometry(QtCore.QRect(100, 200, 256, 192))
        self.listOfKeywords.setObjectName("listOfKeywords")

        self.keywordAddText = QtWidgets.QLineEdit(self.centralwidget)
        self.keywordAddText.setGeometry(QtCore.QRect(10, 200, 81, 20))
        self.keywordAddText.setText("")
        self.keywordAddText.setObjectName("keywordAddText")

        self.keywordAddButton = QtWidgets.QPushButton(self.centralwidget)
        self.keywordAddButton.setGeometry(QtCore.QRect(60, 220, 31, 23))
        self.keywordAddButton.setObjectName("keywordAddButton")
        self.keywordAddButton.clicked.connect(self.addKeyword)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 430, 47, 13))
        self.label_4.setObjectName("label_4")

        self.topicText = QtWidgets.QLineEdit(self.centralwidget)
        self.topicText.setGeometry(QtCore.QRect(100, 430, 201, 20))
        self.topicText.setObjectName("topicText")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 120, 81, 16))
        self.label_5.setObjectName("label_5")

        self.listOfAuthors = QtWidgets.QListWidget(self.centralwidget)
        self.listOfAuthors.setGeometry(QtCore.QRect(390, 120, 256, 192))
        self.listOfAuthors.setObjectName("listOfAuthors")

        self.deleteKeywordButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteKeywordButton.setGeometry(QtCore.QRect(0, 270, 91, 23))
        self.deleteKeywordButton.setObjectName("deleteKeywordButton")
        self.deleteKeywordButton.clicked.connect(self.deleteKeyword)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(650, 120, 81, 16))
        self.label_6.setObjectName("label_6")

        self.authorNameText = QtWidgets.QLineEdit(self.centralwidget)
        self.authorNameText.setGeometry(QtCore.QRect(650, 140, 141, 20))
        self.authorNameText.setObjectName("authorNameText")

        self.authorAddButton = QtWidgets.QPushButton(self.centralwidget)
        self.authorAddButton.setGeometry(QtCore.QRect(650, 160, 31, 23))
        self.authorAddButton.setObjectName("authorAddButton")
        self.authorAddButton.clicked.connect(self.addAuthor)

        self.deleteAuthorButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteAuthorButton.setGeometry(QtCore.QRect(650, 190, 91, 23))
        self.deleteAuthorButton.setObjectName("deleteAuthorButton")
        self.deleteAuthorButton.clicked.connect(self.deleteAuthor)

        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(180, 490, 411, 81))
        self.submitButton.setText("")
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.submit)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 510, 141, 41))
        self.label_7.setObjectName("label_7")

        self.uploadAbstractButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadAbstractButton.setGeometry(QtCore.QRect(390, 340, 111, 31))
        self.uploadAbstractButton.setObjectName("uploadAbstractButton")
        self.uploadAbstractButton.clicked.connect(self.uploadAbstract)

        self.labelAbstract = QtWidgets.QLabel(self.centralwidget)
        self.labelAbstract.setGeometry(QtCore.QRect(510, 350, 271, 16))
        self.labelAbstract.setObjectName("labelAbstract")

        self.uploadFullPaperButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadFullPaperButton.setGeometry(QtCore.QRect(390, 400, 111, 31))
        self.uploadFullPaperButton.setObjectName("uploadFullPaperButton")
        self.uploadFullPaperButton.clicked.connect(self.uploadFull)

        self.labelFullPaper = QtWidgets.QLabel(self.centralwidget)
        self.labelFullPaper.setGeometry(QtCore.QRect(510, 410, 271, 16))
        self.labelFullPaper.setObjectName("labelFullPaper")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submit(self):
        Session = get_session_maker()
        session = Session()
        proposal = session.query(Proposals).filter(Proposals.proposalName == self.proposalName.text())

        # if a proposal with the same name already exists
        if proposal.first() is not None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("A proposal with this name already exists!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return

        # if the user did not upload abstract -> error
        if self.abstractPaper is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("The abstract needs to be uploaded!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
            return

        proposal = Proposals(self.proposalName.text(), self.topicText.text(),self.abstractPaper,self.fullPaper,self.user.id,self.conference.id)
        session.add(proposal)
        session.commit()
        session = Session()
        for keyword in self.keywords:
            proposalKeyword = ProposalsKeywords(keyword,proposal.id)
            session.add(proposalKeyword)

        session.commit()
        session = Session()

        for authorName in self.authorNames:
            proposalAuthorName = ProposalsAuthors(authorName,proposal.id)
            session.add(proposalAuthorName)

        session.commit()
        session.close()

    def addKeyword(self):
        if self.keywordAddText.text() == "":
            return

        if self.keywordAddText.text() not in self.keywords:
            self.keywords.append(self.keywordAddText.text())
            self.listOfKeywords.addItem(self.keywordAddText.text())

    def deleteKeyword(self):
        if(len(self.keywords)) is not 0 and self.listOfKeywords.currentRow() is not -1:
            self.keywords.pop(self.listOfKeywords.currentRow())
        self.listOfKeywords.takeItem(self.listOfKeywords.currentRow())

    def addAuthor(self):
        if self.authorNameText.text() == "":
            return

        if self.authorNameText.text() not in self.authorNames:
            self.authorNames.append(self.authorNameText.text())
            self.listOfAuthors.addItem(self.authorNameText.text())

    def deleteAuthor(self):
        if (len(self.authorNames)) is not 0 and self.listOfAuthors.currentRow() is not -1:
            self.authorNames.pop(self.listOfAuthors.currentRow())
        self.listOfAuthors.takeItem(self.listOfAuthors.currentRow())

    def uploadAbstract(self):
        qd = QFileDialog()
        qd.setFileMode(QFileDialog.AnyFile)
        if qd.exec_():
            fnames = qd.selectedFiles()
            f=open(fnames[0], 'r')
            with f:
                data=f.read()
                self.abstractPaper=data
                _translate = QtCore.QCoreApplication.translate
                self.labelAbstract.setText(_translate("MainWindow", "Uploaded"))

    def uploadFull(self):
        qd = QFileDialog()
        qd.setFileMode(QFileDialog.AnyFile)
        if qd.exec_():
            fnames = qd.selectedFiles()
            f = open(fnames[0], 'r')
            with f:
                data = f.read()
                self.fullPaper = data
                _translate = QtCore.QCoreApplication.translate
                self.labelFullPaper.setText(_translate("MainWindow", "Uploaded"))
                
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Submit Proposal at "+self.conference.conferenceName+" </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Proposal Name"))
        self.label_3.setText(_translate("MainWindow", "Keywords:"))
        self.keywordAddButton.setText(_translate("MainWindow", "+"))
        self.label_4.setText(_translate("MainWindow", "Topic"))
        self.label_5.setText(_translate("MainWindow", "Authors"))
        self.deleteKeywordButton.setText(_translate("MainWindow", "Delete Keyword"))
        self.label_6.setText(_translate("MainWindow", "Name"))
        self.authorAddButton.setText(_translate("MainWindow", "+"))
        self.deleteAuthorButton.setText(_translate("MainWindow", "Delete Author"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">SUBMIT</span></p></body></html>"))
        self.uploadAbstractButton.setText(_translate("MainWindow", "Upload Abstract"))
        self.labelAbstract.setText(_translate("MainWindow", "Required (Not uploaded)"))
        self.uploadFullPaperButton.setText(_translate("MainWindow", "Upload Full Paper"))
        self.labelFullPaper.setText(_translate("MainWindow", "Optional (Not uploaded)"))
