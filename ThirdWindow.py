from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
import SecondWindow
import tuple_environment as ts

# data = [user,nick,status,latitude,longitude,distancia]
class ThirdWindow():
    def __init__(self):
        super(ThirdWindow,self).__init__()        
        self.tela3 = uic.loadUi("tela_3.ui")    

    def updateUser(self,nick):
        user = ts.readUser(nick)
        data = list(user[2])
        status    = data[1]
        latitude  = data[2]
        longitude = data[3]
        distancia = data[4]
        if(status == True):
            # tela_1.label_7.setText("ONLINE")
            self.tela3.label_2.setText("ONLINE")
        else:
            self.tela3.label_2.setText("OFFLINE")

    def loadConfig(self,data):
        self.tela3.show()
        self.tela3.label_10.setText(data[0])
        self.tela3.label_11.setText(data[1])

        if(data[2] == True):
            self.tela3.label_2.setText("ONLINE")
        else:
            self.tela3.label_2.setText("OFFLINE")
    
    def updateDataStatus(self):
        status =  self.tela3.radioButton.isChecked()
        nick   =  self.tela3.label_11.text()
        response = ts.updateStatus(nick,status)    
        QMessageBox.about(self.tela3,"SUCESSO",response) 
        self.updateUser(nick)