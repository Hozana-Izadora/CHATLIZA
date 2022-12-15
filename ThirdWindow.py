from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
import SecondWindow
import tuple_environment as ts

# data = [user,nick,status,latitude,longitude,distancia]
class ThirdWindow():
    def __init__(self):
        super(ThirdWindow,self).__init__()
        
        self = uic.loadUi("tela_3.ui")    
        self.pushButton.clicked.connect(self.updateDataStatus)  

        self.init_screen()
 

    def updateUser(self,nick):
        user = ts.readUser(nick)
        data = list(user[2])
        status    = data[1]
        latitude  = data[2]
        longitude = data[3]
        distancia = data[4]
        if(status == True):
            # tela_1.label_7.setText("ONLINE")
            self.label_2.setText("ONLINE")
        else:
            self.label_2.setText("OFFLINE")


        print(user)
    def loadConfig(self,data):
        self.show()
        self.label_10.setText(data[0])
        self.label_11.setText(data[1])

        if(data[2] == True):
            self.label_2.setText("ONLINE")
        else:
            self.label_2.setText("OFFLINE")
    
    def updateDataStatus(self):
        status =  self.radioButton.isChecked()
        nick   =  self.label_11.text()
        response = ts.updateStatus(nick,status)    
        QMessageBox.about(self,"SUCESSO",response) 
        self.updateUser(nick)