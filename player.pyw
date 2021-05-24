import sys,os, codecs
from myplayer import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
from pygame import mixer
mixer.init()

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        p=os.getcwd()+'\\dir.txt'
        if(os.path.exists(p)):
            file=open(u''+p)
            self.ui.lineEdit.setText(file.read().strip())
            file.close()
            self.mode='mp3'

                             
        self.ui.pushButton.clicked.connect(self.scandisk)
        self.ui.listWidget.currentTextChanged.connect(self.getfiles)
        self.ui.listWidget_2.currentTextChanged.connect(self.playmusic)
        self.ui.pushButton_2.clicked.connect(self.playmusic)
        self.ui.pushButton_3.clicked.connect(self.stopmusic)
        self.songs=[]
        self.flag=0
        self.scandisk()
   
        
    def scandisk(self):
        self.mode='mp3'
        mas=[]
        mas2=[]
        p=str(self.ui.lineEdit.text()).strip()
        file = codecs.open(u''+os.getcwd()+'\\dir.txt', "w", "utf-8")
        file.write(p)
        file.close()
            
        for rootdir, dirs, files in os.walk(str(p)):
            for file in files:       
                if((file.split('.')[-1])=='mp3'):
                    mas.append(os.path.join(rootdir, file))
                    mas2.append(os.path.join(rootdir, file).split('\\')[-2])
        mas2 = dict(zip(mas2, mas2)).values()
        self.mp3=mas
        self.ui.listWidget.clear()
        for x in mas2:
            self.ui.listWidget.addItem(x.strip())
        
    
    def getfiles(self):
        self.flag=1
        self.mode='song'
        self.songs=[]
        self.ui.listWidget_2.clear()
        catname=self.ui.listWidget.currentItem().text()
        for x in self.mp3:
            mp3=x.split('\\')[-2]
            if(catname==mp3.strip()):
                self.songs.append(x)
                self.ui.listWidget_2.addItem(x.split('\\')[-1])
        self.ui.listWidget_2.setFocus()
        self.flag=0
        
    def playmusic(self):
        if(self.flag==0):
            selitem=self.ui.listWidget_2.currentRow()
            put=self.songs[selitem]
            mixer.music.stop()
            mixer.music.load(u''+put)
            mixer.music.play()
    
    def stopmusic(self):
        mixer.music.stop()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
