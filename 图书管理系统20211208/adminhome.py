# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminhome.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout
import UserManage
import dropbookdialog
import addbookdialog
import BookStorageViewer

class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 600)

        self.layout = QHBoxLayout()
        self.buttonlayout = QVBoxLayout()
        self.setLayout(self.layout)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        #Form.setStyleSheet("background-color: rgb(247, 253, 255);")
        self.addBookButton = QtWidgets.QPushButton(Form)
        self.addBookButton.setGeometry(QtCore.QRect(10, 90, 100, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBookButton.sizePolicy().hasHeightForWidth())
        self.addBookButton.setSizePolicy(sizePolicy)
        self.addBookButton.setMinimumSize(QtCore.QSize(100, 42))
        self.addBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.addBookButton.setFont(font)
        self.addBookButton.setObjectName("addBookButton")
        self.dropBookButton = QtWidgets.QPushButton(Form)
        self.dropBookButton.setGeometry(QtCore.QRect(10, 270, 100, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dropBookButton.sizePolicy().hasHeightForWidth())
        self.dropBookButton.setSizePolicy(sizePolicy)
        self.dropBookButton.setMinimumSize(QtCore.QSize(100, 42))
        self.dropBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dropBookButton.setFont(font)
        self.dropBookButton.setObjectName("dropBookButton")
        self.userManageButton = QtWidgets.QPushButton(Form)
        self.userManageButton.setGeometry(QtCore.QRect(10, 450, 100, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userManageButton.sizePolicy().hasHeightForWidth())
        self.userManageButton.setSizePolicy(sizePolicy)
        self.userManageButton.setMinimumSize(QtCore.QSize(100, 42))
        self.userManageButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.userManageButton.setFont(font)
        self.userManageButton.setObjectName("userManageButton")

        self.buttonlayout.addWidget(self.addBookButton)
        self.buttonlayout.addWidget(self.dropBookButton)
        self.buttonlayout.addWidget(self.userManageButton)
        self.layout.addLayout(self.buttonlayout)
        self.storageView = BookStorageViewer.Ui_Form()
        self.layout.addWidget(self.storageView)    #需手动加入layout，否则无法显示


        self.retranslateUi(Form)
        self.addBookButton.clicked.connect(Form.addBookButtonClicked)
        self.dropBookButton.clicked.connect(Form.dropBookButtonClicked)
        self.userManageButton.clicked.connect(Form.userManage)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "\"欢迎使用图书馆管理系统\""))
        self.addBookButton.setText(_translate("Form", "添加书籍"))
        self.dropBookButton.setText(_translate("Form", "淘汰书籍"))
        self.userManageButton.setText(_translate("Form", "用户管理"))

    def addBookButtonClicked(self):
        addDialog = addbookdialog.Ui_Dialog()
        addDialog.add_book_success_signal.connect(self.storageView.searchButtonClicked)
        addDialog.show()
        addDialog.exec_()

    def dropBookButtonClicked(self):
        dropDialog = dropbookdialog.Ui_Dialog()
        dropDialog.drop_book_successful_signal.connect(self.storageView.searchButtonClicked)
        dropDialog.show()
        dropDialog.exec_()

    def userManage(self):
        UserDelete = UserManage.Ui_Dialog()
        UserDelete.show()
        UserDelete.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainMindow = Ui_Form()
    mainMindow.show()
    sys.exit(app.exec_())