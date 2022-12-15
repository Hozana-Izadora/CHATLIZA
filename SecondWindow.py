from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox

import tuple_environment as ts

# data = [user,nick,status,latitude,longitude,distancia]
class SecondWindow():
    def __init__(self):
        super(SecondWindow,self).__init__()
        self = uic.loadUi("tela_2.ui")    

    def loadInfo(self,data):
        # self.telasChat.append(novaTelaChat)
        # for tela in self.telasChat:
        self.show()
        self.listWidget.clear()
        self.listWidget_2.clear()

        self.label_2.setText(data[0])
        self.label_3.setText("@"+data[1])
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
                self.listWidget.addItem("@"+on)
        if(offline != None and len(offline)>0):
            for off in offline:
                self.listWidget_2.addItem("@"+off)

        self.label_7.setText(status)
        self.pushButton.clicked.connect(self.loadConfig(data))     
 