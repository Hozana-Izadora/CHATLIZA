from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
import SecondWindow
import tuple_environment as ts

# data = [user,nick,status,latitude,longitude,distancia]
class MainWindow():
    def __init__(self):
        super(MainWindow,self).__init__()
        
        self.tela = uic.loadUi("tela_1.ui")
        # self = uic.loadUi("tela_1.ui") 
        self.show()
        self.pushButton.clicked.connect(self.createUser) 

        self.init_screen()
     
    def createUser(self):
        user = self.tela.lineEdit.text()
        nick = self.tela.lineEdit_2.text()
        status = self.tela.radioButton.isChecked()
        latitude = self.tela.lineEdit_3.text()
        longitude = self.tela.lineEdit_4.text()
        distancia = self.tela.lineEdit_5.text()
        
        data = [user,nick,status,latitude,longitude,distancia]
        
        checkUser = ts.checkNick(nick)
        if(checkUser == False):
            ts.createUser(data)
            SecondWindow.SecondWindow.loadInfo(data)
        else:
            QMessageBox.about(self,"ALERTA", "ESTE NICK JÁ EXISTE")  

    

        

