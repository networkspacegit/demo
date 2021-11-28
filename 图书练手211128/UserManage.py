# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserManage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QHeaderView


class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
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
        self.tableWidget.setRowCount(0)
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
        # self.deleteUserButton.clicked.connect(Dialog.deleteUser)
        # self.superUserButton.clicked.connect(Dialog.superUser)
        # self.ordinaryUserButton.clicked.connect(Dialog.ordinaryUser)
        #self.tableWidget.itemClicked['QTableWidgetItem*'].connect(Dialog.getStudentInfo)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainMindow = Ui_Dialog()
    mainMindow.show()
    sys.exit(app.exec_())