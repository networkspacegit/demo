# -*- coding: utf-8 -*-
# @Time    : 2021 2021/10/25 22:33
# @Author  : mengsr
# @Email   : 277841892@qq.com
# @File    : musicmain.py
# @Software: demo


import os
import sys
import time

import pygame
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication
from music import Ui_Form

# PyQt5 + pygame 实现音乐播放器，默认播放 F:\KuGou\  目录下MP3文件

voice = 0.5
file_path = r'F:\KuGou'
print(file_path)
SongList = os.listdir(file_path)  # 浏览文件路径的文件
print(SongList)
print('------------------------------------------')
SongPath = [file_path +'\\' + i for i in SongList]   #将文件以列表形式组合起来
print(SongPath)


def mian():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # app.exec_()
    sys.exit(app.exec_())


class MainWindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.drawn()
        self.flag = True
        self.default_volume = self.horizontalSlider.value()
        print('默认音量格数：',self.default_volume)

        #self.listWidget.addItems(SongName)

    def playbutton(self):
        print('play')
        file = r'F:\KuGou\那英 - 默.mp3'
        play(file)
        self.label.setText('那英 - 默.mp3')
        print('播放')


        # pygame.mixer.init()
        # pygame.mixer.music.load(file)
        # #pygame.mixer.music.set_volume(voice)
        # pygame.mixer.music.play(3)
        # self.label.setText('笑看风云.mp3')
        # #self.listWidget.setWindowTitle('笑看风云.mp3')
        # time.sleep(1)
        # print('播放')

    def stopbutton(self):
        print('停止')
        pygame.mixer.music.stop()
        self.label.setText(str('歌曲详情'))

    def gequ(self):
        print('歌曲')
        self.label.setText(str('笑看风云.mp3'))


    def pausebutton(self):
        if self.flag:
            print('暂停')
            pygame.mixer.music.pause()
            self.flag = False
            self.pushButton_3.setText('恢复')
        else:
            print('恢复')
            pygame.mixer.music.unpause()
            self.flag = True
            self.pushButton_3.setText('暂停')

    def lastbutton(self):
        try:
            str = self.listWidget.currentItem().text()  # 获取当前选中歌曲，当前播放歌曲
            print('当前播放:', str)
            print('上一首')
            print(SongList.index(str))
            last = SongList.index(str) - 1
            if last < 0:
                last = len(SongList) - 1
            string = SongList[last]
            print('已经变为:', string)
            tem_path = 'F:\KuGou' + '\\' + string  # 获取被双击项文件路径
            print(tem_path)
            play(tem_path)
            self.label.setText(tem_path)
            self.listWidget.currentItem().setText(string)  # 更新listwidget 当前播放歌曲

        except:
            print('列表为空，请先加载歌曲并播放')

    def nextbutton(self):
        try:
            str = self.listWidget.currentItem().text()  # 获取当前选中歌曲
            print('当前播放:',str)
            print('下一首')
            print(SongList.index(str))
            next = SongList.index(str) + 1
            if next > len(SongList)-1:
                next = 0
            string = SongList[next]
            print('已经变为:',string)
            tem_path = 'F:\KuGou' + '\\' + string  # 获取被双击项文件路径
            print(tem_path)
            play(tem_path)
            self.label.setText(tem_path)
            self.listWidget.currentItem().setText(string)  # 更新listwidget 当前播放歌曲
        except:
            print('列表为空，请先加载歌曲并播放')


    def setValue(self):
        current_value = self.horizontalSlider.value()
        print('当前音量格数：',current_value)
        if current_value > self.default_volume:
            VOICEUP()
            print('增加音量格数：')
        elif current_value < self.default_volume:
            VOICEDOWN()
            print('减少音量格数：')
        self.default_volume = current_value
        print('系统音量格数变为：',self.default_volume)

    def loadmusicbutton(self):
        print('加载本地文件 %s 中音乐:'%file_path)
        self.listWidget.addItems(SongList) #音乐列表加载到 listWidget 控件

    #listwigget控件双击播放事件
    def listWidgetDoubleClick(self):
        item = self.listWidget.selectedItems()[0]  #获取被双击项
        print('双击',item.text())  #打印被双击文件详情
        self.label.setText(item.text())   # 显示到播放歌曲标题
        tem_path = 'F:\KuGou'+ '\\'+ item.text() #获取被双击项文件路径
        print(tem_path)
        play(tem_path)


    # def VOICEUP(self):
    #     global voice
    #     voice += 0.1
    #     if voice > 1:
    #         voice = 1
    #     pygame.mixer.music.set_volume(voice)
    #     v = pygame.mixer.music.get_volume()
    #     print('++++++',v)
    #
    # def VOICEDOWN(self):
    #     print('------')
    #     global voice
    #     voice -= 0.1
    #     if voice < 0:
    #         voice = 0
    #     pygame.mixer.music.set_volume(voice)
    #     v = pygame.mixer.music.get_volume()
    #     print('------', v)
    #     print('#######',voice)

    #设置窗口背景图片，大坑
    def drawn(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("a.jpg")))
        self.setPalette(self.palette)



def play(file_mp3):
    pygame.mixer.init()
    pygame.mixer.music.load(file_mp3)
    # pygame.mixer.music.set_volume(voice)
    pygame.mixer.music.play(3)
    time.sleep(1)

def VOICEUP():
    global voice
    voice += 0.1
    if voice > 1:
        voice = 1
    pygame.mixer.music.set_volume(voice)
    v = pygame.mixer.music.get_volume()
    print('++++++',v)

def VOICEDOWN():
    print('------')
    global voice
    voice -= 0.1
    if voice < 0:
        voice = 0
    pygame.mixer.music.set_volume(voice)
    v = pygame.mixer.music.get_volume()
    print('------', v)
    print('#######',voice)


if __name__ == '__main__':
    mian()


    # app = QtWidgets.QApplication(sys.argv)
    # filename = r'F:\KuGou\追梦人.mp3'
    # fullpath = QtCore.QDir.current().absoluteFilePath(filename)
    # url = QtCore.QUrl.fromLocalFile(fullpath)
    # content = QtMultimedia.QMediaContent(url)
    # player = QtMultimedia.QMediaPlayer()
    # player.setMedia(content)
    # player.play()
    # sys.exit(app.exec_())
