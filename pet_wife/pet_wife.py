import sys
import os
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtWidgets

import pygame


#点击音效
file = r'ouni.mp3'
def music():
    # songs = os.listdir(music_dir)
    # print(songs)
    # song = random.randint(0, len(songs))
    # print(songs[song])  ## Prints The Song Name
    # os.startfile(os.path.join(music_dir, songs[song]))
    pygame.mixer.init()

    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.4)
#退出————————————————
class yimoduo(QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        quit = QAction("退出", self, triggered=os._exit)
        quit.setIcon(QIcon("pet_ico.png"))


        self.pet = myPet()
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(quit)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("pet_ico.png"))
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()
#——————————————————————
#动作————————————————
class myPet(QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.repaint()
        self.img = QLabel(self)
        self.actionDatas = []
        self.initData()
        self.index = 0
        self.setPic("pet3.png")
        self.resize(350, 347)
        self.show()
        self.runing = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.actionRun)
        self.timer.start(0)
        self.randomPos()

    def getImgs(self, pics):
        listPic = []
        for item in pics:
            img = QImage()
            img.load('img/'+item)
            listPic.append(img)
        return listPic

    def initData(self):
        imgs = self.getImgs(["pet31.png","pet31.png","pet32.png"])
        self.actionDatas.append(imgs)




    def actionRun(self):
        if not self.runing:
            self.action = random.randint(0, len(self.actionDatas)-1)
            self.index = 0
            self.runing = True
        self.runFunc(self.actionDatas[self.action])

    def setPic(self, pic):
        img = QImage()
        img.load('img/'+pic)
        self.img.setPixmap(QPixmap.fromImage(img))

    def runFunc(self, imgs):
        if self.index >= len(imgs):
            self.index = 0
            self.runing = False
        self.img.setPixmap(QPixmap.fromImage(imgs[self.index]))
        self.index += 1

    def randomPos(self):
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move(int((screen.width()-size.width())*random.random()), int((screen.height()-size.height())*random.random()))

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            music()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
#main______________
if __name__ == "__main__":
    global pets
    pets=[]
    app = QApplication(sys.argv)
    w = yimoduo()
    sys.exit(app.exec_())
