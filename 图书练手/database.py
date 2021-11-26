import os
import sqlite3


home = os.getcwd()
print(home)
if 'db' not in os.listdir(home):
    os.mkdir(os.path.join(home, 'db'))

dbpath = './db/LibraryManagement.db'
print(dbpath)



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
  StudentId   CHAR(10) UNIQUE NOT NULL,
  BookId      CHAR(6)         NOT NULL,
  BorrowTime  DATE,
  ReturnTime  DATE,
  BorrowState BIT DEFAULT 0
)"""

createBuyOrDropBookTableString = """
CREATE TABLE IF NOT EXISTS BuyOrDrop (
  BookId    CHAR(6) NOT NULL,
  Time      DATE,
  BuyOrDrop BIT DEFAULT 0,
  Number    INT DEFAULT 0
)"""



if __name__ == '__main__':
    conn = sqlite3.connect(dbpath)
    print("Opened database successfully")
    c = conn.cursor()
    print(conn, c)

    c.execute(createUserTableString)
    c.execute(createUser_BookTableString)
    c.execute(createBookTableString)
    c.execute(createBuyOrDropBookTableString)
    print(c)

    c = conn.close()
    print(c)





"""
User表
StudentId：学号
Name：姓名
Password：密码
IsAdmin：是否为管理员
TimesBorrowed：借阅次数
NumBorrowed：借阅数量

Book表
BookName：书名
BookId：书号
Auth：作者
CateGory：分类
Publisher：出版社
PublishTime：出版时间
NumStorage：库存量
NumCanBorrowed：可借量
NumBorrowed：被借阅次数

User_Book表
userid :  用户名
BookID: 书号
BorrowTime : 借阅时间
ReturnTime : 归还时间,
BorrowState : 借阅状态

AddOrDrop表
BookID 书号
ModifyTime  入库或者出库时间
AddOrDrop  入库或者删除
Numbers INT  书本数量
"""