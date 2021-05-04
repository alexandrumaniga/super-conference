from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from src.orm.orm import get_session_maker, PC, User, Listeners


class Ui_RegisterListener(object):

    def __init__(self,parent):
        self.parent = parent

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -20, 401, 121))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 251, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 47, 13))
        self.label_3.setObjectName("label_3")
        self.loginId = QtWidgets.QLineEdit(self.centralwidget)
        self.loginId.setGeometry(QtCore.QRect(90, 170, 171, 20))
        self.loginId.setObjectName("loginId")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(36, 220, 51, 20))
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(90, 220, 171, 20))
        self.password.setObjectName("password")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(90, 270, 171, 20))
        self.email.setObjectName("email")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 270, 51, 20))
        self.label_5.setObjectName("label_5")

        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(260, 450, 231, 51))
        self.registerButton.setObjectName("registerButton")
        self.registerButton.clicked.connect(self.registerButtonPress)

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(260, 500, 231, 51))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.backButtonPress)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 110, 251, 41))
        self.label_6.setObjectName("label_6")
        self.loginId_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.loginId_2.setGeometry(QtCore.QRect(530, 170, 171, 20))
        self.loginId_2.setObjectName("loginId_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 170, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(460, 220, 71, 16))
        self.label_8.setObjectName("label_8")
        self.loginId_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.loginId_3.setGeometry(QtCore.QRect(530, 220, 171, 20))
        self.loginId_3.setObjectName("loginId_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(460, 270, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(460, 320, 71, 16))
        self.label_10.setObjectName("label_10")
        self.loginId_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.loginId_4.setGeometry(QtCore.QRect(530, 270, 171, 20))
        self.loginId_4.setObjectName("loginId_4")
        self.loginId_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.loginId_5.setGeometry(QtCore.QRect(530, 320, 171, 20))
        self.loginId_5.setObjectName("loginId_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(460, 370, 71, 16))
        self.label_11.setObjectName("label_11")
        self.loginId_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.loginId_6.setGeometry(QtCore.QRect(530, 370, 171, 20))
        self.loginId_6.setObjectName("loginId_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def validateRegister(self):
        Session = get_session_maker()
        session = Session()
        if self.password.text() is "":
            return "pass"
        if self.loginId.text() is "":
            return "user"
        if self.email.text() is "":
            return "email"
        users = session.query(PC).filter(PC.loginName == self.loginId.text())
        if users.first() is None:
            users = session.query(User).filter(User.loginName == self.loginId.text())
            if users.first() is None:
                users = session.query(Listeners).filter(Listeners.loginName == self.loginId.text())
                if users.first() is None:
                    return "ok"
        return "exists"

    def registerButtonPress(self):
        res = self.validateRegister()
        if res is "ok":
            Session = get_session_maker()
            session = Session()
            listener = Listeners(self.loginId.text(),self.password.text(),self.email.text(),self.loginId_2.text(),self.loginId_3.text(),self.loginId_4.text(),self.loginId_5.text(),self.loginId_6.text())
            session.add(listener)
            session.commit()
            session.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = self.parent
            self.ui.setupUi(self.window)
            self.window.show()
        elif res is "user":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Invalid username!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
        elif res is "pass":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Invalid password!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
        elif res is "email":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Invalid email!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()
        elif res is "exists":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("An user with that name already exists!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            retval = msg.exec_()

    def backButtonPress(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = self.parent
        self.ui.setupUi(self.window)
        self.window.show()

        #MainWindow.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Listener Registration</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">CMS Account Information:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Login id:"))
        self.label_4.setText(_translate("MainWindow", "Password:"))
        self.label_5.setText(_translate("MainWindow", "E-mail:"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Personal Information:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Affiliation:"))
        self.label_8.setText(_translate("MainWindow", "Webpage:"))
        self.label_9.setText(_translate("MainWindow", "First name:"))
        self.label_10.setText(_translate("MainWindow", "Last name:"))
        self.label_11.setText(_translate("MainWindow", "Phone:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterListener()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())