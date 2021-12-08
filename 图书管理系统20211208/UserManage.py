# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserManage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets, sip
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QDialog, QHeaderView, QTableWidgetItem, QMessageBox


class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()

        # 用户数
        self.userCount = 0
        self.oldDeleteId = ""
        self.oldDeleteName = ""
        self.deleteId = ""
        self.deleteName = ""

        self.setupUi(self)

    def setupUi(self, Dialog):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('./db/LibraryManagement.db')
        self.db.open()
        self.query = QSqlQuery()
        self.getResult()

        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(580, 400))
        Dialog.setMaximumSize(QtCore.QSize(580, 400))
        Dialog.setStyleSheet("background-color: rgb(237, 255, 254);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(561, 331))
        self.tableWidget.setMaximumSize(QtCore.QSize(561, 331))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        #self.tableWidget.setRowCount(20)
        self.tableWidget.setRowCount(self.userCount)  # 行数
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        # 标题可拉伸
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tableWidget)
        self.setRows()

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.superUserButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.superUserButton.sizePolicy().hasHeightForWidth())
        self.superUserButton.setSizePolicy(sizePolicy)
        self.superUserButton.setMinimumSize(QtCore.QSize(181, 36))
        self.superUserButton.setMaximumSize(QtCore.QSize(181, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.superUserButton.setFont(font)
        self.superUserButton.setObjectName("superUserButton")
        self.horizontalLayout.addWidget(self.superUserButton)
        self.ordinaryUserButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ordinaryUserButton.sizePolicy().hasHeightForWidth())
        self.ordinaryUserButton.setSizePolicy(sizePolicy)
        self.ordinaryUserButton.setMinimumSize(QtCore.QSize(181, 36))
        self.ordinaryUserButton.setMaximumSize(QtCore.QSize(181, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.ordinaryUserButton.setFont(font)
        self.ordinaryUserButton.setObjectName("ordinaryUserButton")
        self.horizontalLayout.addWidget(self.ordinaryUserButton)
        self.deleteUserButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteUserButton.sizePolicy().hasHeightForWidth())
        self.deleteUserButton.setSizePolicy(sizePolicy)
        self.deleteUserButton.setMinimumSize(QtCore.QSize(181, 36))
        self.deleteUserButton.setMaximumSize(QtCore.QSize(181, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.deleteUserButton.setFont(font)
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.horizontalLayout.addWidget(self.deleteUserButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.deleteUserButton.clicked.connect(Dialog.deleteUser)
        self.superUserButton.clicked.connect(Dialog.superUser)
        self.ordinaryUserButton.clicked.connect(Dialog.ordinaryUser)
        self.tableWidget.itemClicked['QTableWidgetItem*'].connect(Dialog.getStudentInfo)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "管理用户"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "账号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "用户类型"))
        self.superUserButton.setText(_translate("Dialog", "转为超级管理用户"))
        self.ordinaryUserButton.setText(_translate("Dialog", "转为普通用户"))
        self.deleteUserButton.setText(_translate("Dialog", "删 除 用 户"))

    def getResult(self):
        # sql = "SELECT userid,Name FROM User WHERE IsAdmin=0"
        sql = "SELECT StudentId,Name,IsAdmin FROM User"
        self.query.exec_(sql)
        self.userCount = 0;
        while (self.query.next()):
            self.userCount += 1;
        # sql = "SELECT userid,Name FROM User WHERE IsAdmin=0"
        sql = "SELECT StudentId,Name,IsAdmin FROM User"
        self.query.exec_(sql)

    def setRows(self):
        font = QFont()
        font.setPixelSize(14)
        for i in range(self.userCount):
            if (self.query.next()):
                useridItem = QTableWidgetItem(self.query.value(0))
                StudentNameItem = QTableWidgetItem(self.query.value(1))
                if self.query.value(2) == 1:
                    usertypeItem = QTableWidgetItem('管理员')
                elif self.query.value(2) == 0:
                    usertypeItem = QTableWidgetItem('普通用户')
                else:
                    print(self.query.value(0))
                    print(self.query.value(1))
                    print(self.query.value(2))
                    usertypeItem = QTableWidgetItem('用户')

                useridItem.setFont(font)
                StudentNameItem.setFont(font)
                usertypeItem.setFont(font)
                useridItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                StudentNameItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                usertypeItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.tableWidget.setItem(i, 0, useridItem)
                self.tableWidget.setItem(i, 1, StudentNameItem)
                self.tableWidget.setItem(i, 2, usertypeItem)
        return

    def getStudentInfo(self):
        row = self.tableWidget.currentIndex().row()
        self.tableWidget.verticalScrollBar().setSliderPosition(row)
        self.getResult()
        i = 0
        while(self.query.next() and i != row):
            # print('row:', row)
            # print('i：', i)
            i = i+1
        print('self.oldDeleteId1:', self.oldDeleteId)
        print('self.deleteId1:', self.deleteId)
        self.oldDeleteId = self.deleteId
        self.oldDeleteName = self.deleteName
        print('self.oldDeleteId2:', self.oldDeleteId)
        self.deleteId = self.query.value(0)
        self.deleteName = self.query.value(1)
        print('self.deleteId2', self.deleteId)

    def deleteUser(self):
        if (self.deleteId == "" and self.deleteName == ""):
            print(QMessageBox.warning(self, "警告", "请选中要删除的用户", QMessageBox.Yes, QMessageBox.Yes))
            return
        elif (self.deleteId == self.oldDeleteId and self.deleteName == self.oldDeleteName):
            print(QMessageBox.warning(self, "警告", "请选中要删除的用户", QMessageBox.Yes, QMessageBox.Yes))
            return
        if (QMessageBox.information(self, "提醒", "删除用户:%s,%s\n用户一经删除将无法恢复，是否继续?" % (self.deleteId, self.deleteName),
                                    QMessageBox.Yes | QMessageBox.No,QMessageBox.No) == QMessageBox.No):
            return
        # 从User表删除用户
        sql = "DELETE FROM User WHERE StudentId='%s'" % (self.deleteId)
        self.query.exec_(sql)
        self.db.commit()
        # 归还所有书籍
        sql = "SELECT * FROM User_Book  WHERE StudentId='%s' AND BorrowState=1" % self.deleteId
        a = self.query.exec_(sql)
        print(a)
        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        print(timenow)
        updateQuery = QSqlQuery()
        while (self.query.next()):
            BookID = self.query.value(1)
            sql = "UPDATE Book SET NumStorage=NumStorage+1,NumCanBorrow=NumCanBorrow+1,NumBorrowed=NumBorrowed-1 WHERE BookID='%s'" % BookID
            updateQuery.exec_(sql)
            self.db.commit()
        sql = "UPDATE User_Book SET ReturnTime='%s',BorrowState=0 WHERE StudentId='%s' AND BorrowState=1" % (
            timenow, self.deleteId)
        self.query.exec_(sql)
        self.db.commit()
        print(QMessageBox.information(self, "提醒", "删除用户成功!", QMessageBox.Yes, QMessageBox.Yes))
        self.updateUI()
        return

    def ordinaryUser(self):
        if (self.deleteId == "" and self.deleteName == ""):
            print(QMessageBox.warning(self, "警告", "请选中用户", QMessageBox.Yes, QMessageBox.Yes))
            return
        # elif (self.deleteId == self.oldDeleteId and self.deleteName == self.oldDeleteName):
        #     print(QMessageBox.warning(self, "警告", "请选中用户", QMessageBox.Yes, QMessageBox.Yes))
        #     return
        updateQuery = QSqlQuery()
        if self.query.value(2) == 1:
            sql = "UPDATE User SET IsAdmin=%d WHERE StudentId='%s'" % (0, self.deleteId)
            updateQuery.exec_(sql)
            self.db.commit()
            print(QMessageBox.information(self, "提醒", "用户权限修改成功!", QMessageBox.Yes, QMessageBox.Yes))
            self.updateUI()
            return
        else:
            QMessageBox.information(self, "提醒", "用户权限已经是普通用户，无需修改!", QMessageBox.Yes, QMessageBox.Yes)
            return

    def superUser(self):
        if (self.deleteId == "" and self.deleteName == ""):
            print(QMessageBox.warning(self, "警告", "请选中用户", QMessageBox.Yes, QMessageBox.Yes))
            return
        # elif (self.deleteId == self.oldDeleteId and self.deleteName == self.oldDeleteName):
        #     print(QMessageBox.warning(self, "警告", "请选中用户", QMessageBox.Yes, QMessageBox.Yes))
        #     return
        updateQuery = QSqlQuery()
        if self.query.value(2) == 0:
            sql = "UPDATE User SET IsAdmin=%d WHERE StudentId='%s'" % (1, self.deleteId)
            updateQuery.exec_(sql)
            self.db.commit()
            print(QMessageBox.information(self, "提醒", "用户权限修改成功!", QMessageBox.Yes, QMessageBox.Yes))
            self.updateUI()
            return
        else:
            QMessageBox.information(self, "提醒", "用户权限已经是超级管理员，无需修改!", QMessageBox.Yes, QMessageBox.Yes)
            return

    def updateUI(self):
        self.getResult()
        # self.verticalLayout.removeWidget(self.tableWidget)
        # self.horizontalLayout.removeWidget(self.superUserButton)
        # self.horizontalLayout.removeWidget(self.ordinaryUserButton)
        # self.horizontalLayout.removeWidget(self.deleteUserButton)
        sip.delete(self.horizontalLayout)
        sip.delete(self.tableWidget)

        self.tableWidget = QtWidgets.QTableWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(561, 331))
        self.tableWidget.setMaximumSize(QtCore.QSize(561, 331))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setRowCount(20)
        self.tableWidget.setRowCount(self.userCount)  # 行数
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        # 标题可拉伸
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tableWidget)
        self.setRows()

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.superUserButton = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.superUserButton.sizePolicy().hasHeightForWidth())
        self.superUserButton.setSizePolicy(sizePolicy)
        self.superUserButton.setMinimumSize(QtCore.QSize(181, 36))
        self.superUserButton.setMaximumSize(QtCore.QSize(181, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.superUserButton.setFont(font)
        self.superUserButton.setObjectName("superUserButton")
        self.horizontalLayout.addWidget(self.superUserButton)
        self.ordinaryUserButton = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ordinaryUserButton.sizePolicy().hasHeightForWidth())
        self.ordinaryUserButton.setSizePolicy(sizePolicy)
        self.ordinaryUserButton.setMinimumSize(QtCore.QSize(181, 36))
        self.ordinaryUserButton.setMaximumSize(QtCore.QSize(181, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.ordinaryUserButton.setFont(font)
        self.ordinaryUserButton.setObjectName("ordinaryUserButton")
        self.horizontalLayout.addWidget(self.ordinaryUserButton)
        self.deleteUserButton = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteUserButton.sizePolicy().hasHeightForWidth())
        self.deleteUserButton.setSizePolicy(sizePolicy)
        self.deleteUserButton.setMinimumSize(QtCore.QSize(181, 36))
        self.deleteUserButton.setMaximumSize(QtCore.QSize(181, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.deleteUserButton.setFont(font)
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.horizontalLayout.addWidget(self.deleteUserButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(self)
        self.deleteUserButton.clicked.connect(self.deleteUser)
        self.superUserButton.clicked.connect(self.superUser)
        self.ordinaryUserButton.clicked.connect(self.ordinaryUser)
        self.tableWidget.itemClicked['QTableWidgetItem*'].connect(self.getStudentInfo)
        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainMindow = Ui_Dialog()
    mainMindow.show()
    sys.exit(app.exec_())