from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox
import ThirdWindow
import tuple_environment as ts

# data = [user,nick,status,latitude,longitude,distancia]
class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SecondWindow,self).__init__()
        self.tela2 = uic.loadUi("tela_2.ui") 
        self.tela3 = ThirdWindow.ThirdWindow()   
        self.tela2.pushButton.clicked.connect(self.jonas) 
        self.receivedData = []

    def loadInfo(self,data):        
        self.receivedData = data
        self.tela2.show()
        self.tela2.listWidget.clear()
        self.tela2.listWidget_2.clear()

        self.tela2.label_2.setText(data[0])
        self.tela2.label_3.setText("@"+data[1])
        online = []
        offline= []
        online = ts.listOnline() #nick e status
        offline = ts.listOffline() #nick e status
        if(data[2] == True):
            status = "ONLINE"        
        else:
            status = "OFFLINE"

        if(online != None and len(online)>0):
            for on in online:
                self.tela2.listWidget.addItem("@"+on)
        if(offline != None and len(offline)>0):
            for off in offline:
                self.tela2.listWidget_2.addItem("@"+off)

        self.tela2.label_7.setText(status)

    def jonas(self):
        ThirdWindow.ThirdWindow.loadConfig(self.tela3,self.receivedData)
        # print(self.receivedData)
    # def abreAlgo(self):
    #     self.tela2.pushButton.clicked.connect(ThirdWindow.ThirdWindow.loadConfig(self.tela3,self.receivedData))     
        # self.tela2.pushButton.clicked.connect(ThirdWindow.ThirdWindow.loadConfig(self.tela3,data))     
