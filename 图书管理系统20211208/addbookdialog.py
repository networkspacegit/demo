# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addbookdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

from dbmanager import BookDbManager, AddOrDropManager


class Ui_Dialog(QDialog):
    add_book_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.bookdb = BookDbManager()
        self.addordropdb = AddOrDropManager()

    def setupUi(self, Dialog):
        # 书名，书号，作者，分类，添加数量.出版社,出版日期
        # 书籍分类：哲学类、社会科学类、政治类、法律类、军事类、经济类、文化类、教育类、体育类、语言文字类、艺术类、历史类、地理类、天文学类、生物学类、医学卫生类、农业类
        BookCategory = ["哲学", "社会科学", "政治", "法律", "军事", "经济", "文化", "教育", "体育", "语言文字", "艺术", "历史"
            , "地理", "天文学", "生物学", "医学卫生", "农业"]

        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(320, 450)
        Dialog.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 292, 420))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(5, 10, 5, 10)
        self.formLayout.setHorizontalSpacing(1)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.titlelabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titlelabel.sizePolicy().hasHeightForWidth())
        self.titlelabel.setSizePolicy(sizePolicy)
        self.titlelabel.setMinimumSize(QtCore.QSize(121, 31))
        self.titlelabel.setMaximumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.titlelabel.setFont(font)
        self.titlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titlelabel.setObjectName("titlelabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titlelabel)
        self.bookNameLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookNameLabel.sizePolicy().hasHeightForWidth())
        self.bookNameLabel.setSizePolicy(sizePolicy)
        self.bookNameLabel.setMinimumSize(QtCore.QSize(80, 30))
        self.bookNameLabel.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.bookNameLabel.setFont(font)
        self.bookNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bookNameLabel.setObjectName("bookNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bookNameLabel)
        self.bookNameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookNameEdit.sizePolicy().hasHeightForWidth())
        self.bookNameEdit.setSizePolicy(sizePolicy)
        self.bookNameEdit.setMinimumSize(QtCore.QSize(201, 31))
        self.bookNameEdit.setMaximumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bookNameEdit.setFont(font)
        self.bookNameEdit.setMaxLength(10)
        self.bookNameEdit.setObjectName("bookNameEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bookNameEdit)
        self.bookIdLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookIdLabel.sizePolicy().hasHeightForWidth())
        self.bookIdLabel.setSizePolicy(sizePolicy)
        self.bookIdLabel.setMinimumSize(QtCore.QSize(80, 30))
        self.bookIdLabel.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.bookIdLabel.setFont(font)
        self.bookIdLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bookIdLabel.setObjectName("bookIdLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bookIdLabel)
        self.bookIdEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookIdEdit.sizePolicy().hasHeightForWidth())
        self.bookIdEdit.setSizePolicy(sizePolicy)
        self.bookIdEdit.setMinimumSize(QtCore.QSize(201, 31))
        self.bookIdEdit.setMaximumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bookIdEdit.setFont(font)
        self.bookIdEdit.setMaxLength(10)
        self.bookIdEdit.setObjectName("bookIdEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bookIdEdit)
        self.authNameLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authNameLabel.sizePolicy().hasHeightForWidth())
        self.authNameLabel.setSizePolicy(sizePolicy)
        self.authNameLabel.setMinimumSize(QtCore.QSize(80, 30))
        self.authNameLabel.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.authNameLabel.setFont(font)
        self.authNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.authNameLabel.setObjectName("authNameLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.authNameLabel)
        self.authNameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authNameEdit.sizePolicy().hasHeightForWidth())
        self.authNameEdit.setSizePolicy(sizePolicy)
        self.authNameEdit.setMinimumSize(QtCore.QSize(201, 31))
        self.authNameEdit.setMaximumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.authNameEdit.setFont(font)
        self.authNameEdit.setMaxLength(10)
        self.authNameEdit.setObjectName("authNameEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.authNameEdit)
        self.categoryLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryLabel.sizePolicy().hasHeightForWidth())
        self.categoryLabel.setSizePolicy(sizePolicy)
        self.categoryLabel.setMinimumSize(QtCore.QSize(80, 30))
        self.categoryLabel.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.categoryLabel.setObjectName("categoryLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.publisherLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.publisherLabel.sizePolicy().hasHeightForWidth())
        self.publisherLabel.setSizePolicy(sizePolicy)
        self.publisherLabel.setMinimumSize(QtCore.QSize(80, 30))
        self.publisherLabel.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.publisherLabel.setFont(font)
        self.publisherLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.publisherLabel.setObjectName("publisherLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.publisherLabel)
        self.publisherEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.publisherEdit.sizePolicy().hasHeightForWidth())
        self.publisherEdit.setSizePolicy(sizePolicy)
        self.publisherEdit.setMinimumSize(QtCore.QSize(201, 31))
        self.publisherEdit.setMaximumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.publisherEdit.setFont(font)
        self.publisherEdit.setMaxLength(10)
        self.publisherEdit.setObjectName("publisherEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.publisherEdit)
        self.publishDateLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.publishDateLabel.sizePolicy().hasHeightForWidth())
        self.publishDateLabel.setSizePolicy(sizePolicy)
        self.publishDateLabel.setMinimumSize(QtCore.QSize(80, 30))
        self.publishDateLabel.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.publishDateLabel.setFont(font)
        self.publishDateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.publishDateLabel.setObjectName("publishDateLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.publishDateLabel)
        self.addNumLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addNumLabel.sizePolicy().hasHeightForWidth())
        self.addNumLabel.setSizePolicy(sizePolicy)
        self.addNumLabel.setMinimumSize(QtCore.QSize(80, 30))
        self.addNumLabel.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.addNumLabel.setFont(font)
        self.addNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addNumLabel.setObjectName("addNumLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.addNumLabel)
        self.addNumEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addNumEdit.sizePolicy().hasHeightForWidth())
        self.addNumEdit.setSizePolicy(sizePolicy)
        self.addNumEdit.setMinimumSize(QtCore.QSize(201, 31))
        self.addNumEdit.setMaximumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addNumEdit.setFont(font)
        self.addNumEdit.setMaxLength(12)
        self.addNumEdit.setObjectName("addNumEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.addNumEdit)
        self.addBookButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBookButton.sizePolicy().hasHeightForWidth())
        self.addBookButton.setSizePolicy(sizePolicy)
        self.addBookButton.setMinimumSize(QtCore.QSize(140, 32))
        self.addBookButton.setMaximumSize(QtCore.QSize(140, 32))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.addBookButton.setFont(font)
        self.addBookButton.setObjectName("addBookButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.addBookButton)
        self.categoryComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.categoryComboBox.addItems(BookCategory) #收到添加分类
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryComboBox.sizePolicy().hasHeightForWidth())
        self.categoryComboBox.setSizePolicy(sizePolicy)
        self.categoryComboBox.setMinimumSize(QtCore.QSize(201, 31))
        self.categoryComboBox.setMaximumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.categoryComboBox.setFont(font)
        self.categoryComboBox.setEditable(False)
        self.categoryComboBox.setCurrentText("")
        self.categoryComboBox.setMaxVisibleItems(10)
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.categoryComboBox)
        self.publishTime = QtWidgets.QDateTimeEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.publishTime.sizePolicy().hasHeightForWidth())
        self.publishTime.setSizePolicy(sizePolicy)
        self.publishTime.setMinimumSize(QtCore.QSize(201, 31))
        self.publishTime.setMaximumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.publishTime.setFont(font)
        self.publishTime.setObjectName("publishTime")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.publishTime)

        self.retranslateUi(Dialog)
        self.addBookButton.clicked.connect(Dialog.addBookButtonCicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加书籍"))
        self.titlelabel.setText(_translate("Dialog", "添加书籍"))
        self.bookNameLabel.setText(_translate("Dialog", "书    名："))
        self.bookIdLabel.setText(_translate("Dialog", "书    号："))
        self.authNameLabel.setText(_translate("Dialog", "作    者："))
        self.categoryLabel.setText(_translate("Dialog", "分    类："))
        self.publisherLabel.setText(_translate("Dialog", "出 版 社："))
        self.publishDateLabel.setText(_translate("Dialog", "出版日期："))
        self.addNumLabel.setText(_translate("Dialog", "数    量："))
        self.addBookButton.setText(_translate("Dialog", "添   加"))
        self.publishTime.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd H:mm"))

    def addBookButtonCicked(self):
        bookName = self.bookNameEdit.text()
        bookId = self.bookIdEdit.text()
        authName = self.authNameEdit.text()
        bookCategory = self.categoryComboBox.currentText()
        publisher = self.publisherEdit.text()
        publishTime = self.publishTime.text()
        addBookNum = self.addNumEdit.text()
        if (
                bookName == "" or bookId == "" or authName == "" or bookCategory == "" or publisher == "" or publishTime == "" or addBookNum == ""):
            print(QMessageBox.warning(self, "警告", "有字段为空，添加失败", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            addBookNum = int(addBookNum)
            bookinfo = self.bookdb.querybyBookID(bookId)
            print('bookinfo:',bookinfo)
            if (bookinfo):
                print('更新')
                self.bookdb.updateBookinfo(addBookNum, bookId, addFlag=1)
            #elif (len(bookinfo) == 0):
            else:
                print('添加')
                self.bookdb.addBOOK(bookName, bookId, authName, bookCategory, publisher, publishTime, addBookNum,
                                    addBookNum, 0)

            # 插入droporinsert表
            timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            print(timenow)
            self.addordropdb.addinfo(bookId, timenow, addBookNum)
            print(QMessageBox.information(self, "提示", "添加书籍成功!", QMessageBox.Yes, QMessageBox.Yes))
            self.add_book_success_signal.emit()
            self.close()
            self.clearEdit()
        return



    def clearEdit(self):
        self.bookNameEdit.clear()
        self.bookIdEdit.clear()
        self.authNameEdit.clear()
        self.addNumEdit.clear()
        self.publisherEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainMindow = Ui_Dialog()
    mainMindow.show()
    sys.exit(app.exec_())