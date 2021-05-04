# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from src.orm.orm import get_session_maker, User, PC, Listeners
from src.ui.MainAuthorMenu import Ui_MainAuthorMenu
from src.ui.MainListenerMenu import Ui_MainListenerMenu
from src.ui.MainPCMenu import Ui_MainPCMenu
from src.ui.RegisterListener import Ui_RegisterListener
from src.ui.RegisterPC import Ui_RegisterPC
from src.ui.RegisterUser import Ui_RegisterUser


class Ui_MainWindowLogin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.registerUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerUserButton.setGeometry(QtCore.QRect(270, 470, 201, 51))
        self.registerUserButton.setObjectName("registerUserButton")
        self.registerUserButton.clicked.connect(self.buttonRegisterUser)


        self.registerListenerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerListenerButton.setGeometry(QtCore.QRect(270, 540, 201, 51))
        self.registerListenerButton.setObjectName("registerUserButton")
        self.registerListenerButton.clicked.connect(self.buttonRegisterListener)



        self.registerPCButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerPCButton.setGeometry(QtCore.QRect(270, 400, 201, 51))
        self.registerPCButton.setObjectName("registerPCButton")
        self.registerPCButton.clicked.connect(self.buttonRegisterPC)

        self.usernameText = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameText.setGeometry(QtCore.QRect(180, 190, 381, 20))
        self.usernameText.setText("")
        self.usernameText.setObjectName("usernameText")

        self.passwordText = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordText.setGeometry(QtCore.QRect(180, 270, 381, 20))
        self.passwordText.setText("")
        self.passwordText.setObjectName("passwordText")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 711, 121))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 190, 47, 13))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 270, 47, 13))
        self.label_3.setObjectName("label_3")

        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(270, 320, 201, 51))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.buttonlogin)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registerUserButton.setText(_translate("MainWindow", "Register as User"))
        self.registerPCButton.setText(_translate("MainWindow", "Register as Program Committee"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Conference Management System</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.registerListenerButton.setText(_translate("MainWindow", "Register as Listener"))

    def buttonlogin(self):
        account=self.checkaccount(self.usernameText.text(),self.passwordText.text())
        if(account[1]=="invalid"):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Invalid Username or password")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok )
            msg.show()
            retval = msg.exec_()

        if(account[1]=="author"):

            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainAuthorMenu(account[0])
            self.ui.setupUi(self.window)
            self.window.show()

        if(account[1]=="pc"):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainPCMenu(account[0])
            self.ui.setupUi(self.window)
            self.window.show()

        if (account[1] == "listener"):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainListenerMenu(account[0])
            self.ui.setupUi(self.window)
            self.window.show()

    def buttonRegisterPC(self):
        MainWindow.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterPC(self)
        self.ui.setupUi(self.window)
        self.window.show()

    def buttonRegisterUser(self):
        MainWindow.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterUser(self)
        self.ui.setupUi(self.window)
        self.window.show()

    def buttonRegisterListener(self):
        MainWindow.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterListener(self)
        self.ui.setupUi(self.window)
        self.window.show()


    def checkaccount(self,username,passowrd):
        Session = get_session_maker()
        session = Session()
        users = session.query(PC).filter(PC.loginName == username).filter(PC.password == passowrd)
        if users.first() is None:
            # check if user is a normal user
            users = session.query(User).filter(User.loginName == username).filter(User.password == passowrd)
            if users.first() is None:
                users = session.query(Listeners).filter(Listeners.loginName == username).filter(Listeners.password == passowrd)
                if users.first() is None:
                    return (0,"invalid")
                else:
                    MainWindow.close()
                    user = users.first()
                    return (user, "listener")
            else:
                MainWindow.close()
                user = users.first()
                return (user,"author")

        MainWindow.close()
        user = users.first()
        return (user,"pc")
        #here return PC GUI
        #return "pc"



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowLogin()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
