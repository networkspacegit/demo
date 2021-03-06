# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'returnbookdialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from dbmanager import BookDbManager,UserBookManager,userDbManager

class Ui_Dialog(QDialog):
    return_book_success_signal = pyqtSignal()
    def __init__(self, userID, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.userID = userID
        self.userbookdb = UserBookManager()  # 借书记录
        self.bookdb = BookDbManager()  # 书籍管理
        self.userdb = userDbManager()  # 用户管理
        self.setupUi(self)

    def setupUi(self, Dialog):
        # 书名，书号，作者，分类，添加数量.出版社,出版日期
        # 书籍分类：哲学类、社会科学类、政治类、法律类、军事类、经济类、文化类、教育类、体育类、语言文字类、艺术类、历史类、地理类、天文学类、生物学类、医学卫生类、农业类
        BookCategory = ["哲学", "社会科学", "政治", "法律", "军事", "经济", "文化", "教育", "体育", "语言文字", "艺术", "历史"
            , "地理", "天文学", "生物学", "医学卫生", "农业"]

        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(320, 450)
        Dialog.setStyleSheet("background-color: rgb(237, 252, 255);")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(18, 20, 291, 378))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(12)
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
        self.returnStudentLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnStudentLabel.sizePolicy().hasHeightForWidth())
        self.returnStudentLabel.setSizePolicy(sizePolicy)
        self.returnStudentLabel.setMinimumSize(QtCore.QSize(80, 30))
        self.returnStudentLabel.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.returnStudentLabel.setFont(font)
        self.returnStudentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.returnStudentLabel.setObjectName("returnStudentLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.returnStudentLabel)
        self.returnuseridLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnuseridLabel.sizePolicy().hasHeightForWidth())
        self.returnuseridLabel.setSizePolicy(sizePolicy)
        self.returnuseridLabel.setMinimumSize(QtCore.QSize(201, 31))
        self.returnuseridLabel.setMaximumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.returnuseridLabel.setFont(font)
        self.returnuseridLabel.setObjectName("returnuseridLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.returnuseridLabel)
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
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bookNameLabel)
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
        self.bookNameEdit.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.bookNameEdit.setText("")
        self.bookNameEdit.setMaxLength(10)
        self.bookNameEdit.setReadOnly(True)
        self.bookNameEdit.setObjectName("bookNameEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bookNameEdit)
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
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.bookIdLabel)
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
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bookIdEdit)
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
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.authNameLabel)
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
        self.authNameEdit.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.authNameEdit.setMaxLength(10)
        self.authNameEdit.setReadOnly(True)
        self.authNameEdit.setObjectName("authNameEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.authNameEdit)
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
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.categoryComboBox = QtWidgets.QComboBox(self.layoutWidget)
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
        self.categoryComboBox.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.categoryComboBox.setEditable(False)
        self.categoryComboBox.setCurrentText("")
        self.categoryComboBox.setMaxVisibleItems(20)
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.categoryComboBox.addItems(BookCategory)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.categoryComboBox)
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
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.publisherLabel)
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
        self.publisherEdit.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.publisherEdit.setMaxLength(10)
        self.publisherEdit.setReadOnly(True)
        self.publisherEdit.setObjectName("publisherEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.publisherEdit)
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
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.publishDateLabel)
        self.publishTime = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.publishTime.sizePolicy().hasHeightForWidth())
        self.publishTime.setSizePolicy(sizePolicy)
        self.publishTime.setMinimumSize(QtCore.QSize(201, 31))
        self.publishTime.setMaximumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.publishTime.setFont(font)
        self.publishTime.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.publishTime.setMaxLength(10)
        self.publishTime.setReadOnly(True)
        self.publishTime.setObjectName("publishTime")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.publishTime)
        self.returnBookButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnBookButton.sizePolicy().hasHeightForWidth())
        self.returnBookButton.setSizePolicy(sizePolicy)
        self.returnBookButton.setMinimumSize(QtCore.QSize(140, 32))
        self.returnBookButton.setMaximumSize(QtCore.QSize(140, 32))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.returnBookButton.setFont(font)
        self.returnBookButton.setObjectName("returnBookButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.returnBookButton)

        self.retranslateUi(Dialog)
        self.bookIdEdit.textChanged['QString'].connect(Dialog.BookIDEditChanged)
        self.bookIdEdit.returnPressed.connect(Dialog.returnButtonClicked)
        self.returnBookButton.clicked.connect(Dialog.returnButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "归还书籍"))
        self.titlelabel.setText(_translate("Dialog", "归还书籍"))
        self.returnStudentLabel.setText(_translate("Dialog", "还 书 人："))
        self.returnuseridLabel.setText(_translate("Dialog", self.userID))
        self.bookNameLabel.setText(_translate("Dialog", "书    名："))
        self.bookIdLabel.setText(_translate("Dialog", "书    号："))
        self.authNameLabel.setText(_translate("Dialog", "作    者："))
        self.categoryLabel.setText(_translate("Dialog", "分    类："))
        self.publisherLabel.setText(_translate("Dialog", "出 版 社："))
        self.publishDateLabel.setText(_translate("Dialog", "出版日期："))
        self.returnBookButton.setText(_translate("Dialog", "确认归还"))

    def BookIDEditChanged(self):
        BookID = self.bookIdEdit.text()
        if (BookID == ""):
            self.bookNameEdit.clear()
            self.authNameEdit.clear()
            self.publisherEdit.clear()
            self.publishTime.clear()

        bookinfo = self.bookdb.querybyBookID(BookID)
        #print(bookinfo)
        # 查询对应书号，如果存在就更新form
        if (bookinfo):
            self.bookNameEdit.setText(bookinfo[0][0])
            self.authNameEdit.setText(bookinfo[0][2])
            self.categoryComboBox.setCurrentText(bookinfo[0][3])
            self.publisherEdit.setText(bookinfo[0][4])
            self.publishTime.setText(bookinfo[0][5])
            #print(self.publishTime.text())
        return

    def returnButtonClicked(self):
        # 获取书号，书号为空或并未借阅，则弹出错误
        # 更新Book_User表User表以及Book表
        BookID = self.bookIdEdit.text()
        # BookID为空的处理
        if (BookID == ""):
            print(QMessageBox.warning(self, "警告", "你所要还的书不存在，请查看输入", QMessageBox.Yes, QMessageBox.Yes))
            return

        # 如果未借阅
        borrowbook = self.userbookdb.borrowStatus(self.userID, BookID)
        if (not borrowbook[0][0]):
            print(QMessageBox.information(self, "提示", "您并未借阅此书，故无需归还", QMessageBox.Yes, QMessageBox.Yes))
            return

        # 更新User表
        self.userdb.borrowOrReturnBook(self.userID, borrow=0)

        # 更新Book表
        self.bookdb.borrowOrReturnBook(BookID, borrowflag=0)

        # 更新User_Book表
        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.userbookdb.borrowOrReturnBook(self.userID, BookID, timenow, borrowflag=0)

        print(QMessageBox.information(self, "提示", "归还成功!", QMessageBox.Yes, QMessageBox.Yes))
        self.return_book_success_signal.emit()
        self.close()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainMindow = Ui_Dialog('user01')
    mainMindow.show()
    sys.exit(app.exec_())