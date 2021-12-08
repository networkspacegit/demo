# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrowstatusviewer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlQueryModel, QSqlDatabase
from PyQt5.QtWidgets import QWidget, QApplication, QHeaderView

dbpath = './db/LibraryManagement.db'

class Ui_Form(QWidget):
    def __init__(self,userid):
        super(Ui_Form, self).__init__()
        self.userid = userid
        self.setupUi(self)

    def setupUi(self, Form):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        #self.db.setDatabaseName('./db/LibraryManagement.db')
        self.db.setDatabaseName(dbpath)
        self.db.open()

        Form.setObjectName("Form")
        Form.resize(700, 500)
        Form.setStyleSheet("background-color: rgb(242, 247, 255);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.borrowedLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.borrowedLabel.sizePolicy().hasHeightForWidth())
        self.borrowedLabel.setSizePolicy(sizePolicy)
        self.borrowedLabel.setMinimumSize(QtCore.QSize(65, 32))
        self.borrowedLabel.setMaximumSize(QtCore.QSize(65, 32))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.borrowedLabel.setFont(font)
        self.borrowedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.borrowedLabel.setObjectName("borrowedLabel")
        self.verticalLayout.addWidget(self.borrowedLabel)
        self.borrowedTableView = QtWidgets.QTableView(Form)
        self.borrowedTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.borrowedTableView.setObjectName("borrowedTableView")
        self.borrowedTableView.horizontalHeader().setCascadingSectionResizes(True)
        self.borrowedTableView.horizontalHeader().setStretchLastSection(True)
        self.borrowedTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalLayout.addWidget(self.borrowedTableView)
        self.returnedLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnedLabel.sizePolicy().hasHeightForWidth())
        self.returnedLabel.setSizePolicy(sizePolicy)
        self.returnedLabel.setMinimumSize(QtCore.QSize(65, 32))
        self.returnedLabel.setMaximumSize(QtCore.QSize(65, 32))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.returnedLabel.setFont(font)
        self.returnedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.returnedLabel.setObjectName("returnedLabel")
        self.verticalLayout.addWidget(self.returnedLabel)
        self.returnedTableView = QtWidgets.QTableView(Form)
        self.returnedTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.returnedTableView.setObjectName("returnedTableView")
        self.returnedTableView.horizontalHeader().setCascadingSectionResizes(True)
        self.returnedTableView.horizontalHeader().setStretchLastSection(True)
        self.returnedTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #随窗口放大缩小


        self.borrowedQueryModel = QSqlQueryModel()
        self.returnedQueryModel = QSqlQueryModel()
        self.borrowedTableView.setModel(self.borrowedQueryModel)
        self.returnedTableView.setModel(self.returnedQueryModel)
        self.borrowedQuery()
        self.borrowedQueryModel.setHeaderData(0, Qt.Horizontal, "书名")
        self.borrowedQueryModel.setHeaderData(1, Qt.Horizontal, "书号")
        self.borrowedQueryModel.setHeaderData(2, Qt.Horizontal, "作者")
        self.borrowedQueryModel.setHeaderData(3, Qt.Horizontal, "分类")
        self.borrowedQueryModel.setHeaderData(4, Qt.Horizontal, "出版社")
        self.borrowedQueryModel.setHeaderData(5, Qt.Horizontal, "出版时间")
        self.borrowedQueryModel.setHeaderData(6, Qt.Horizontal, "借出时间")

        self.returnedQuery()
        self.returnedQueryModel.setHeaderData(0, Qt.Horizontal, "书名")
        self.returnedQueryModel.setHeaderData(1, Qt.Horizontal, "书号")
        self.returnedQueryModel.setHeaderData(2, Qt.Horizontal, "作者")
        self.returnedQueryModel.setHeaderData(3, Qt.Horizontal, "分类")
        self.returnedQueryModel.setHeaderData(4, Qt.Horizontal, "出版社")
        self.returnedQueryModel.setHeaderData(5, Qt.Horizontal, "出版时间")
        self.returnedQueryModel.setHeaderData(6, Qt.Horizontal, "借阅时间")
        self.returnedQueryModel.setHeaderData(7, Qt.Horizontal, "归还时间")

        self.verticalLayout.addWidget(self.returnedTableView)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "欢迎使用图书馆管理系统"))
        self.borrowedLabel.setText(_translate("Form", "未归还"))
        self.returnedLabel.setText(_translate("Form", "已归还"))

    def borrowedQuery(self):
        sql = "SELECT Book.BookName,Book.BookID,Auth,Category,Publisher,PublishTime,BorrowTime  FROM Book,User_Book WHERE Book.BookID=User_Book.BookID AND User_Book.BorrowState=1 AND StudentId='%s'" % self.userid
        self.borrowedQueryModel.setQuery(sql)
        return

    def returnedQuery(self):
        sql = "SELECT Book.BookName,Book.BookID,Auth,Category,Publisher,PublishTime,BorrowTime,ReturnTime  FROM Book,User_Book WHERE Book.BookID=User_Book.BookID AND User_Book.BorrowState=0 AND StudentId='%s'" % self.userid
        self.returnedQueryModel.setQuery(sql)
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainMindow = Ui_Form('13')
    mainMindow.show()
    sys.exit(app.exec_())