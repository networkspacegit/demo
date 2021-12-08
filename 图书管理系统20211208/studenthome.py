# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studenthome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, sip
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
import BookStorageViewer,borrowbookdialog,returnbookdialog,borrowstatusviewer

class Ui_Form(QWidget):
    def __init__(self,userid):
        super().__init__()
        self.userid = userid
        self.setupUi(self)

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(900, 600)

        self.layout = QHBoxLayout()
        self.buttonlayout = QVBoxLayout()
        self.setLayout(self.layout)  #必须要有，否则无法加载

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        #Form.setStyleSheet("background-color: rgb(247, 253, 255);")
        self.myBookStatus = QtWidgets.QPushButton(Form)
        self.myBookStatus.setGeometry(QtCore.QRect(9, 469, 100, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.myBookStatus.sizePolicy().hasHeightForWidth())
        self.myBookStatus.setSizePolicy(sizePolicy)
        self.myBookStatus.setMinimumSize(QtCore.QSize(100, 42))
        self.myBookStatus.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.myBookStatus.setFont(font)
        self.myBookStatus.setObjectName("myBookStatus")
        self.allBookButton = QtWidgets.QPushButton(Form)
        self.allBookButton.setGeometry(QtCore.QRect(9, 342, 100, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allBookButton.sizePolicy().hasHeightForWidth())
        self.allBookButton.setSizePolicy(sizePolicy)
        self.allBookButton.setMinimumSize(QtCore.QSize(100, 42))
        self.allBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.allBookButton.setFont(font)
        self.allBookButton.setObjectName("allBookButton")
        self.borrowBookButton = QtWidgets.QPushButton(Form)
        self.borrowBookButton.setGeometry(QtCore.QRect(9, 215, 100, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.borrowBookButton.sizePolicy().hasHeightForWidth())
        self.borrowBookButton.setSizePolicy(sizePolicy)
        self.borrowBookButton.setMinimumSize(QtCore.QSize(100, 42))
        self.borrowBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.borrowBookButton.setFont(font)
        self.borrowBookButton.setObjectName("borrowBookButton")
        self.returnBookButton = QtWidgets.QPushButton(Form)
        self.returnBookButton.setGeometry(QtCore.QRect(9, 88, 100, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnBookButton.sizePolicy().hasHeightForWidth())
        self.returnBookButton.setSizePolicy(sizePolicy)
        self.returnBookButton.setMinimumSize(QtCore.QSize(100, 42))
        self.returnBookButton.setMaximumSize(QtCore.QSize(100, 42))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.returnBookButton.setFont(font)
        self.returnBookButton.setObjectName("returnBookButton")

        self.buttonlayout.addWidget(self.borrowBookButton)
        self.buttonlayout.addWidget(self.returnBookButton)
        self.buttonlayout.addWidget(self.myBookStatus)
        self.buttonlayout.addWidget(self.allBookButton)

        self.storageView = BookStorageViewer.Ui_Form()
        self.borrowStatusView = borrowstatusviewer.Ui_Form(self.userid)
        self.allBookButton.setEnabled(False)
        self.layout.addLayout(self.buttonlayout)
        self.layout.addWidget(self.storageView)


        self.retranslateUi(Form)
        self.borrowBookButton.clicked.connect(Form.borrowBookButtonClicked)
        self.returnBookButton.clicked.connect(Form.returnBookButtonClicked)
        self.myBookStatus.clicked.connect(Form.myBookStatusClicked)
        self.allBookButton.clicked.connect(Form.allBookButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "\"欢迎使用图书馆管理系统\""))
        self.myBookStatus.setText(_translate("Form", "借阅状态"))
        self.allBookButton.setText(_translate("Form", "所有书籍"))
        self.borrowBookButton.setText(_translate("Form", "借书"))
        self.returnBookButton.setText(_translate("Form", "还书"))

    def borrowBookButtonClicked(self):
        addDialog = borrowbookdialog.Ui_Dialog(self.userid)
        addDialog.borrow_book_success_signal.connect(self.borrowStatusView.borrowedQuery)
        addDialog.borrow_book_success_signal.connect(self.storageView.searchButtonClicked)
        addDialog.show()
        addDialog.exec_()

    def returnBookButtonClicked(self):
        addDialog = returnbookdialog.Ui_Dialog(self.userid)
        addDialog.return_book_success_signal.connect(self.borrowStatusView.returnedQuery)
        addDialog.return_book_success_signal.connect(self.borrowStatusView.borrowedQuery)
        addDialog.return_book_success_signal.connect(self.storageView.searchButtonClicked)
        addDialog.show()
        addDialog.exec_()

    def myBookStatusClicked(self):
        self.layout.removeWidget(self.storageView)
        sip.delete(self.storageView)
        self.storageView = BookStorageViewer.Ui_Form()
        self.borrowStatusView = borrowstatusviewer.Ui_Form(self.userid)
        self.layout.addWidget(self.borrowStatusView)
        self.allBookButton.setEnabled(True)
        self.myBookStatus.setEnabled(False)
        return

    def allBookButtonClicked(self):
        self.layout.removeWidget(self.borrowStatusView)
        sip.delete(self.borrowStatusView)
        self.borrowStatusView = borrowstatusviewer.Ui_Form(self.userid)
        self.storageView = BookStorageViewer.Ui_Form()
        self.layout.addWidget(self.storageView)
        self.allBookButton.setEnabled(False)
        self.myBookStatus.setEnabled(True)
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainMindow = Ui_Form('13')
    mainMindow.show()
    sys.exit(app.exec_())