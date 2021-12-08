import hashlib
import os
import sqlite3


# home = os.getcwd()#获取当前目录
# print(home)
# if 'db' not in os.listdir(home):
#     os.mkdir(os.path.join(home, 'db')) #在跟目录下生成db文件夹，如果没有db文件夹必须加上此三行，有db文件夹则不需要

dbpath = './db/LibraryManagement.db'
print(dbpath)

#定义表格
createUserTableString = """
CREATE TABLE IF NOT EXISTS User (
  StudentId     CHAR(10) UNIQUE NOT NULL,
  Name          VARCHAR(20),
  Password      CHAR(32)        NOT NULL,
  IsAdmin       BIT DEFAULT 0,
  TimesBorrowed INT DEFAULT 0,
  NumBorrowed   INT DEFAULT 0
)"""

createBookTableString = """
CREATE TABLE IF NOT EXISTS Book (
  BookName     VARCHAR(30) NOT NULL,
  BookId       CHAR(6)     NOT NULL,
  Auth         VARCHAR(20) NOT NULL,
  Category     VARCHAR(10) DEFAULT NULL,
  Publisher    VARCHAR(30) DEFAULT NULL,
  PublishTime  DATE,
  NumStorage   INT         DEFAULT 0,
  NumCanBorrow INT         DEFAULT 0,
  NumBorrowed  INT         DEFAULT 0
)"""

createUser_BookTableString = """
CREATE TABLE IF NOT EXISTS User_Book (
  StudentId   CHAR(10) NOT NULL,
  BookId      CHAR(6)  NOT NULL,
  BorrowTime  DATE,
  ReturnTime  DATE,
  BorrowState BIT DEFAULT 0
)"""
#BookId      CHAR(6)  UNIQUE NOT NULL,唯一之后他们无法借该本书
createBuyOrDropBookTableString = """
CREATE TABLE IF NOT EXISTS BuyOrDrop (
  BookId    CHAR(6) NOT NULL,
  Time      DATE,
  BuyOrDrop BIT DEFAULT 0,
  Number    INT DEFAULT 0
)"""

class DbManager(object):
    def __init__(self,dbpath): # *args
        self.db = sqlite3.connect(dbpath)
        self.cursor = self.db.cursor()
        print('类中',self.db,self.cursor)

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb): #(self, types, value, traceback):
        self.db.commit()
        return False

    def __del__(self):
        self.db.commit()
        self.db.close()
        # print(self.db)
        # print(self.cursor)

    def switchDb(self,*args):
        self.db.close()
        self.db =sqlite3.connect(*args)
        self.cursor = self.db.cursor()

    def createTable(self,tableString):
        self.cursor.execute(tableString)
        self.db.commit()

    def commitAndClose(self):
        self.db.commit()
        self.db.close()



class userDbManager(DbManager):
    def __init__(self,database=dbpath):
        super(userDbManager, self).__init__(database)
        print('userDbManager中',self.db,self.cursor)
        self.initDb()

    def initDb(self):
        self.createTable(createUserTableString)

    #初始化默认管理员、用户
    def initDatabase(self):
        password = 'admin'
        m2 = hashlib.md5()
        m2.update(password.encode(encoding='utf-8'))   # 将密码进行md5加密  password.encode(encoding='utf-8')
        md5password =m2.hexdigest()
        print(md5password)
        self.addAdminUser('admin01','admin',md5password)

        password = 'mg'
        m2 = hashlib.md5()
        m2.update(password.encode(encoding='utf-8'))  # 将密码进行md5加密  password.encode(encoding='utf-8')
        md5password = m2.hexdigest()
        print(md5password)
        self.addUser('mg01','mg',md5password)

    # 添加普管理员
    def addAdminUser(self,id,adminname,password):
        self.addUser(id,adminname,password,isAdmin=1)

    # 添加普通用户
    def addUser(self,id,name,password,isAdmin=0):
        self.cursor.execute("""INSERT INTO User VALUES ('{0}', '{1}', '{2}','{3}','{4}','{5}')""".format(id, name, password, isAdmin, 0, 0))
        self.db.commit()
        # insertData = self.cursor.execute("""INSERT INTO User (StudentId, Name, Password,IsAdmin,TimesBorrowed,NumBorrowed) VALUES
        # ('{0}', '{1}', '{2}','{3}','{4}','{5}')""".format(id, name, password, isAdmin, 0, 0))

    def querybyUserid(self,userid):
        fetchedData = self.cursor.execute("SELECT * FROM user WHERE StudentId='{}'".format(userid))   #fetchedData = self.cursor.execute("SELECT * FROM user WHERE StudentId='%s'" % (userid))
        return fetchedData.fetchall() #cursor.fetchall() 相当于从数据库取数据，但是取完就没有了，再下一行继续 cursor.fetchall()，取到的就只是空列表。他和变量不一样，不能重复查询，推荐第一种写法，将数据取出来之后，放到一个变量里，再进行处理。
        # print('ID查找：',fetchedData.fetchall())  #print(self.cursor.fetchone())    #打印查询记录，查询不到返回none
        # p = fetchedData.fetchall()
        # print('00000',p)
        #return fetchedData

    #查找管理员id与账号
    def getAdmineUserinfo(self):
        fetchedData = self.cursor.execute("SELECT StudentId,Name FROM user WHERE IsAdmin=1")
        print('管理员查找：',fetchedData.fetchall(),fetchedData)
        return fetchedData

    #查找用户id与账号
    def getUserinfo(self):
        fetchedData = self.cursor.execute("SELECT StudentId,Name FROM user WHERE IsAdmin=0")
        print('普通用户查找：', fetchedData.fetchall(),fetchedData)
        return fetchedData

    #修改密码
    def updatePassword(self,password,studentid):
        fetchedData = self.cursor.execute("UPDATE User SET Password='%s' WHERE StudentId='%s'" %(password, studentid))
        self.db.commit()

    #更新借书、还书数量
    def borrowOrReturnBook(self,studentid,borrow=1):
        if borrow == 1:
            self.cursor.execute("UPDATE User SET TimesBorrowed=TimesBorrowed+1,NumBorrowed=NumBorrowed+1 WHERE "
                                "StudentId='{}'".format(studentid))
        else:
            self.cursor.execute("UPDATE User SET TimesBorrowed=TimesBorrowed-1,NumBorrowed=NumBorrowed-1 WHERE "
                                "StudentId='{}'".format(studentid))
        self.db.commit()


class BookDbManager(DbManager):
    def __init__(self, database=dbpath):
        super().__init__(database)
        self.initDb()

    def initDb(self):
        self.createTable(createBookTableString)

    def initDatabase(self):
        self.addBOOK('力学', 'IS1000', '刘斌', '教育', '中国科学技术大学 ', '1999-01-01', 100, 100, 0)
        self.addBOOK('微积分', 'IS1001', '牛顿莱布尼兹', '教育', '中国科学技术大学', '1998-01-01', 14, 14, 0)
        self.addBOOK('电磁场论', 'IS1002', '叶邦角', '教育', '中国科学技术大学', '1997-01-01', 24, 24, 0)
        self.addBOOK('热学', 'IS1003', '张鹏飞', '教育', '中国科学技术大学', '2002-01-01', 45, 45, 0)
        self.addBOOK('电动力学', 'IS1004', '叶邦角', '教育', '中国科学技术大学', '2003-01-01', 100, 100, 0)
        self.addBOOK('数据库', 'IS1006', '袁平波', '教育', '中国科学技术大学', '2010-01-01', 10, 10, 0)
        self.addBOOK('电磁学', 'IS1005', '叶邦角', '教育', '中国科学技术大学 ', '2012-01-01', 43, 43, 0)
        self.addBOOK('数学分析', 'IS1007', '陈卿', '教育', '中国科学技术大学', '2013-01-01', 23, 23, 0)
        self.addBOOK('吉米多维奇题解1', 'IS1008', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('吉米多维奇题解2', 'IS1009', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('吉米多维奇题解3', 'IS1010', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('吉米多维奇题解4', 'IS1011', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('吉米多维奇题解5', 'IS1012', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('吉米多维奇题解6', 'IS1013', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('朗道力学', 'IS1014', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道电动力学', 'IS1015', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道量子力学', 'IS1016', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道量子电动力学', 'IS1017', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道统计物理学', 'IS1018', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道流体力学', 'IS1019', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道弹性理论力学', 'IS1020', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道物理动力学', 'IS1021', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('植物学', 'IS1022', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('动物学', 'IS1023', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('细胞生物学', 'IS1024', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('动物生理学', 'IS1025', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('古生物学', 'IS1026', '佚名', '生物学', '高等教育出版社', '2011-05-01', 100, 100, 0)
        self.addBOOK('高等数学', 'IS1027', '佚名', '教育', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('离散数学', 'IS1028', '李安', '教育', '清华大学出版社', '2021-011-11', 50, 50, 0)
        self.addBOOK('线性代数', 'IS1029', '佚名', '教育', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('C++程序设计', 'IS1030', '孙广中', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addBOOK('C程序设计', 'IS1031', '郑重', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addBOOK('数据结构', 'IS1032', '顾为兵', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addBOOK('信号与系统', 'IS1033', '李卫平', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addBOOK('线性电子线路', 'IS1034', '陆伟', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addBOOK('阿Q正传', 'IS1035', '鲁迅', '语言文学', '文学艺术出版社', '2021-12-07', 100, 100, 0)
        self.addBOOK('父与子的编程之旅：与小卡特一起学Python', 'IS1036', '沃伦•桑德', '文化', '图灵程序设计丛书', '2021-12-07', 100, 100, 0)
        print('初始化插入图书成功！')

    def addBOOK(self,BookName,BookId,Auth,Category,Publisher,PublishTime,NumStorage,NumCanBorrow,NumBorrowed):
        self.cursor.execute(
            """INSERT INTO Book VALUES ('{0}', '{1}', '{2}','{3}','{4}','{5}','{6}','{7}','{8}')""".format(BookName,BookId,Auth,Category,Publisher,PublishTime,NumStorage,NumCanBorrow,NumBorrowed))
        self.db.commit()

    def dropBook(self,BookId):
        self.cursor.execute("DELETE from Book where BookId = '{0}'".format(BookId))
        self.db.commit()

    def updateBookinfo(self,addBookNum,BookId,addFlag=1):
        if addFlag == 1:
            self.cursor.execute("UPDATE Book SET NumStorage=NumStorage+'{0}',NumCanBorrow=NumCanBorrow+'{1}' WHERE "
                                "BookId='{2}'".format(addBookNum,addBookNum,BookId))

        else:
            self.cursor.execute("UPDATE Book SET NumStorage=NumStorage -'{0}',NumCanBorrow=NumCanBorrow -'{1}' WHERE "
                                "BookId='{2}'".format(addBookNum, addBookNum, BookId))
        print('存书状态已更新！')
        self.db.commit()

    def getBookinfo(self):
        books = self.cursor.execute("SELECT * FROM Book" )
        print('全部图书查找：',books.fetchall())
        return books.fetchall()

    def querybyBookID(self,BookId):
        book = self.cursor.execute("SELECT * FROM Book WHERE BookId='{}'".format(BookId))
        #print('图书ID查找：',book.fetchall())  #大坑：用后 book列表被清0
        return book.fetchall()

    def queryBookByKeywords(self,keywords):
        books = self.cursor.execute("SELECT * FROM Book ORDER BY {} limit {},{}".format(keywords,0,50))
        #books = self.cursor.execute("SELECT * from Book ORDER BY %s limit %s,%s" % (keywords, 0, 50))
        print('关键字查找：', books.fetchall())
        return books.fetchall()

    def borrowOrReturnBook(self,BookId,borrowflag = 1):
        if borrowflag == 1:
            self.cursor.execute("UPDATE Book SET NumStorage=NumStorage-1,NumCanBorrow=NumCanBorrow-1,NumBorrowed=NumBorrowed+1 WHERE "
                                "BookId='{}'".format(BookId))

        else:
            self.cursor.execute("UPDATE Book SET NumStorage=NumStorage+1,NumCanBorrow=NumCanBorrow+1,NumBorrowed=NumBorrowed-1 WHERE "
                                "BookId='{}'".format(BookId))
        #print('借书状态已更新！')
        self.db.commit()


class AddOrDropManager(DbManager):
    def __init__(self, database=dbpath):
        super().__init__(database)
        self.initDb()

    def initDb(self):
        self.createTable(createBuyOrDropBookTableString)

    def initDatabase(self):
        self.insertValue('IS1000', '2018-04-22', 1, 100)
        self.insertValue('IS1001', '2018-04-22', 1, 14)
        self.insertValue('IS1002', '2018-04-22', 1, 24)
        self.insertValue('IS1003', '2018-04-22', 1, 45)
        self.insertValue('IS1004', '2018-04-22', 1, 100)
        self.insertValue('IS1005', '2018-04-27', 1, 45)
        self.insertValue('IS1006', '2018-04-28', 1, 10)
        self.insertValue('IS1007', '2018-04-28', 1, 23)
        self.insertValue('IS1008', '2018-04-28', 1, 50)
        self.insertValue('IS1009', '2018-04-28', 1, 50)
        self.insertValue('IS1010', '2018-04-28', 1, 50)
        self.insertValue('IS1011', '2018-04-28', 1, 50)
        self.insertValue('IS1012', '2018-04-28', 1, 50)
        self.insertValue('IS1013', '2018-04-28', 1, 50)
        self.insertValue('IS1014', '2018-04-28', 1, 50)
        self.insertValue('IS1015', '2018-04-28', 1, 50)
        self.insertValue('IS1016', '2018-04-28', 1, 50)
        self.insertValue('IS1017', '2018-04-28', 1, 50)
        self.insertValue('IS1018', '2018-04-28', 1, 50)
        self.insertValue('IS1019', '2018-04-28', 1, 50)
        self.insertValue('IS1020', '2018-04-28', 1, 50)
        self.insertValue('IS1021', '2018-04-28', 1, 50)
        self.insertValue('IS1022', '2018-04-28', 1, 50)
        self.insertValue('IS1023', '2018-04-28', 1, 50)
        self.insertValue('IS1024', '2018-04-28', 1, 50)
        self.insertValue('IS1025', '2018-04-28', 1, 50)
        self.insertValue('IS1026', '2018-04-28', 1, 100)
        self.insertValue('IS1027', '2018-04-28', 1, 50)
        self.insertValue('IS1028', '2011-11-11', 1, 50)
        self.insertValue('IS1029', '2018-04-28', 1, 50)
        self.insertValue('IS1030', '2018-04-28', 1, 50)
        self.insertValue('IS1031', '2018-04-28', 1, 50)
        self.insertValue('IS1032', '2018-04-28', 1, 50)
        self.insertValue('IS1033', '2018-04-28', 1, 50)
        self.insertValue('IS1034', '2018-04-28', 1, 50)
        self.insertValue('IS1035', '2021-12-07', 1, 100)
        self.insertValue('IS1036', '2021-12-07', 1, 100)

    def insertValue(self,BookId,Time,BuyOrDrop,Number):
        self.cursor.execute(
            """INSERT INTO BuyOrDrop VALUES ('{0}', '{1}', '{2}','{3}')""".format(BookId,Time, BuyOrDrop,Number))
        self.db.commit()

    def addinfo(self, BookID, time, addBookNum):
        self.insertValue(BookID, time, 1, addBookNum)
        print('购买书籍:',BookID)

    def dropinfo(self, BookID, time, addBookNum):
        self.insertValue(BookID, time, 0, addBookNum)
        print('删除书籍:', BookID)

    def getAllinfo(self):
        '''获得所有书籍'''
        fetchedData = self.cursor.execute("SELECT * from BuyOrDrop ")
        print('查询全部图书：',fetchedData.fetchall())
        return fetchedData.fetchall()


class UserBookManager(DbManager):
    def __init__(self, database=dbpath):
        super().__init__(database)
        self.initDb()

    def initDb(self):
        self.createTable(createUser_BookTableString)

    def queryBorrowBook(self, StudentId, BookID):
        fetchedData = self.cursor.execute("SELECT * FROM User_Book WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (StudentId, BookID))
        print('查询某用户某本书借阅状态：', fetchedData.fetchall())
        return fetchedData.fetchall()

    def countBorrowNum(self, StudentId):
        result = self.cursor.execute(
            " SELECT COUNT(StudentId) FROM User_Book WHERE StudentId='%s' AND BorrowState=1" % (StudentId))  #" SELECT * FROM User_Book WHERE StudentId='%s' AND BorrowState=1" % (StudentId))
        #print('查询某用户借书总数：', result.fetchall())
        return result.fetchall()

    def borrowStatus(self, StudentId, BookID):
        result = self.cursor.execute("SELECT COUNT(StudentId) FROM User_Book WHERE  StudentId='%s' AND BookID='%s' AND BorrowState=1" % (StudentId, BookID))
        #print('查询某本书：', result.fetchall())
        return result.fetchall()

    def borrowOrReturnBook(self, StudentId, BookID, timenow, borrowflag=1):
        if borrowflag == 1:
            result = self.cursor.execute(
                "INSERT INTO User_Book VALUES ('%s','%s','%s',NULL,1)" % (StudentId, BookID, timenow))
        else:
            result = self.cursor.execute(
                "UPDATE User_Book SET ReturnTime='%s',BorrowState=0 WHERE StudentId='%s' AND BookID='%s' AND BorrowState=1" % (
                timenow, StudentId, BookID))
        self.db.commit()
        #print('修改借书状态！')


if __name__ == "__main__":

    #测试用户table
    #DbManager(dbpath)
    user = userDbManager()
    user.initDatabase()
    user.querybyUserid('user01')
    user.querybyUserid('admin01')
    user.getAdmineUserinfo()
    user.getUserinfo()
    # user.updatePassword('1','admin01')
    # user.updatePassword('1','user01')
    user.borrowOrReturnBook('user01')
    user.borrowOrReturnBook('admin01',0)

    #测试book table
    book = BookDbManager()
    book.initDatabase()
    #book.dropBook('IS1034')
    #book.dropBook(7)
    book.updateBookinfo('50','IS1030')
    book.updateBookinfo('50','IS1029',0)
    book.getBookinfo()
    book.querybyBookID('IS1028')
    book.queryBookByKeywords('Category')
    book.borrowOrReturnBook('IS1033')
    book.borrowOrReturnBook('IS1032',0)

    #测试 BuyOrDrop table
    table = AddOrDropManager()
    table.initDatabase()
    # table.addinfo('IS1035', '2021-11-12', 50)
    # table.addinfo('IS1035', '2021-11-12', 50)
    #table.dropinfo('IS1035', '2021-11-12', 50)
    table.getAllinfo()

    #测试 UserBookManager table
    user_book = UserBookManager()
    user_book.queryBorrowBook('user01','IS1033')
    user_book.countBorrowNum('user01')
    user_book.queryBorrowBook('user01','IS1033')
    # user_book.borrowOrReturnBook('user01','IS1001','2021-11-12')
    # user_book.borrowOrReturnBook('user01','IS1002','2021-11-12',1)
    #user_book.borrowOrReturnBook('user01','IS1003','2021-11-12',1)
    user_book.borrowOrReturnBook('user01','IS1002','2021-11-12',0)
