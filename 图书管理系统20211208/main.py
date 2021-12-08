# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, sip
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import SignInWidget
import SignUpWidget
import changepassworddialog,studenthome,adminhome
from dbmanager import userDbManager,BookDbManager,AddOrDropManager,UserBookManager
dbpath = './db/LibraryManagement.db'


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
        self.setupUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        #MainWindow.setStyleSheet("background-color: rgb(242, 247, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.widget = SignInWidget.Ui_Form()
        self.setCentralWidget(self.widget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 19))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setAutoFillBackground(False)
        self.menu.setStyleSheet("")
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondkajdsfa = QtWidgets.QAction(MainWindow)
        self.actiondkajdsfa.setObjectName("actiondkajdsfa")
        self.signUpAction = QtWidgets.QAction(MainWindow)
        self.signUpAction.setObjectName("signUpAction")
        self.changePasswordAction = QtWidgets.QAction(MainWindow)
        self.changePasswordAction.setObjectName("changePasswordAction")
        self.signInAction = QtWidgets.QAction(MainWindow)
        self.signInAction.setObjectName("signInAction")
        self.quitSignInAction = QtWidgets.QAction(MainWindow)
        self.quitSignInAction.setObjectName("quitSignInAction")
        self.quitAction = QtWidgets.QAction(MainWindow)
        self.quitAction.setObjectName("quitAction")
        self.menu.addAction(self.signUpAction)
        self.menu.addAction(self.changePasswordAction)
        self.menu.addAction(self.signInAction)
        self.menu.addAction(self.quitSignInAction)
        self.menu.addAction(self.quitAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.signUpAction.setEnabled(True)
        self.changePasswordAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(False)

        self.widget.is_admin_signal.connect(self.adminSignIn)
        self.widget.is_student_signal[str].connect(self.studentSignIn)
        self.menubar.triggered[QAction].connect(self.menuTriggered)  #一定要改为 menubar

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "欢迎使用图书馆管理系统"))
        self.menu.setTitle(_translate("MainWindow", "菜单栏"))
        self.actiondkajdsfa.setText(_translate("MainWindow", "dkajdsfa "))
        self.signUpAction.setText(_translate("MainWindow", "注册"))
        self.changePasswordAction.setText(_translate("MainWindow", "修改密码"))
        self.signInAction.setText(_translate("MainWindow", "登录"))
        self.quitSignInAction.setText(_translate("MainWindow", "退出登录"))
        self.quitAction.setText(_translate("MainWindow", "退出"))

    def init(self):
        if not os.path.exists(dbpath):
            self.userdb = userDbManager()
            self.bookdb = BookDbManager()
            self.userbookdb = UserBookManager()
            self.addordropdb = AddOrDropManager()

            self.userdb.initDatabase()
            self.bookdb.initDatabase()
            self.addordropdb.initDatabase()

    def adminSignIn(self):
        sip.delete(self.widget)
        self.widget = adminhome.Ui_Form()
        self.setCentralWidget(self.widget)
        self.changePasswordAction.setEnabled(False)
        self.signUpAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)

    def studentSignIn(self, studentId):
        sip.delete(self.widget)
        self.widget = studenthome.Ui_Form(studentId)
        self.setCentralWidget(self.widget)
        self.changePasswordAction.setEnabled(False)
        self.signUpAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)

    def menuTriggered(self, q):
        if (q.text() == "修改密码"):
            changePsdDialog = changepassworddialog.Ui_Dialog(self)
            changePsdDialog.show()
            changePsdDialog.exec_()
        if (q.text() == "注册"):
            sip.delete(self.widget)
            self.widget = SignUpWidget.Ui_Form()
            self.setCentralWidget(self.widget)
            self.widget.student_signup_signal[str].connect(self.studentSignIn)
            self.signUpAction.setEnabled(False)
            self.changePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(True)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "退出登录"):
            sip.delete(self.widget)
            self.widget = SignInWidget.Ui_Form()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            self.widget.is_student_signal[str].connect(self.studentSignIn)
            self.signUpAction.setEnabled(True)
            self.changePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "登录"):
            sip.delete(self.widget)
            self.widget = SignInWidget.Ui_Form()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            self.widget.is_student_signal[str].connect(self.studentSignIn)
            self.signUpAction.setEnabled(True)
            self.changePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "退出"):
            qApp = QApplication.instance()
            qApp.quit()
        return



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainMindow = Ui_MainWindow()
    mainMindow.show()
    sys.exit(app.exec_())