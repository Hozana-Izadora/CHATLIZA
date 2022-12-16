from PyQt5 import QtWidgets,uic

from PyQt5.QtWidgets import QMessageBox
import SecondWindow
import tuple_environment as ts
import User

# data = [user,nick,status,latitude,longitude,distancia]
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        
        self.tela = uic.loadUi("tela_1.ui")
        self.tela.pushButton.clicked.connect(self.createUser) 

        # self.tela2 = SecondWindow.SecondWindow()
        self.listTelas = []
        self.listUsers = []

    def getLastId(self):
        quantityUsers = len(self.listUsers)
        if quantityUsers == 0:
            return 0
        lastUser = self.listUsers[quantityUsers - 1]
        return lastUser.id

    def createUserModel(self, data):
        lastID = self.getLastId()
        currentUserID = lastID + 1
        self.listUsers.append(User.User(currentUserID, data))

    def createScreen(self):
        self.listTelas.append(SecondWindow.SecondWindow())

    def createUser(self):
        user = self.tela.lineEdit.text()
        nick = self.tela.lineEdit_2.text()
        status = self.tela.radioButton.isChecked()
        latitude = self.tela.lineEdit_3.text()
        longitude = self.tela.lineEdit_4.text()
        distancia = self.tela.lineEdit_5.text()
        
        data = [user,nick,status,latitude,longitude,distancia]

        self.createUserModel(data)
        self.createScreen()
        
        checkUser = ts.checkNick(nick)
        if(checkUser == False):
            ts.createUser(data)
            SecondWindow.SecondWindow.loadInfo(self.listTelas[len(self.listTelas) - 1],data) 
        else:
            QMessageBox.about(self,"ALERTA", "ESTE NICK JÁ EXISTE")  

    

        

