from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

import tuple_environment as ts

   
# data = [user,nick,status,latitude,longitude,distancia]

def updateUser(nick):
    user = ts.readUser(nick)
    data = list(user[2])
    status    = data[1]
    latitude  = data[2]
    longitude = data[3]
    distancia = data[4]
    if(status == True):
        # tela_1.label_7.setText("ONLINE")
        tela_3.label_2.setText("ONLINE")
    else:
        tela_3.label_2.setText("OFFLINE")


    print(user)

def loadConfig(data):
    tela_3.show()
    tela_3.label_10.setText(data[0])
    tela_3.label_11.setText(data[1])

    if(data[2] == True):
        tela_3.label_2.setText("ONLINE")
    else:
        tela_3.label_2.setText("OFFLINE")
    
def loadInfo(data):
    novaTelaChat = uic.loadUi("tela_2.ui")

    telasChat.append(novaTelaChat)
    for tela in telasChat:
        tela.show()
        tela.listWidget.clear()
        tela.listWidget_2.clear()

        tela.label_2.setText(data[0])
        tela.label_3.setText("@"+data[1])
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
                tela.listWidget.addItem("@"+on)
        if(offline != None and len(offline)>0):
            for off in offline:
                tela.listWidget_2.addItem("@"+off)

        tela.label_7.setText(status)
        tela.pushButton.clicked.connect(loadConfig(data))     

def createUser():
    user = tela_1.lineEdit.text()
    nick = tela_1.lineEdit_2.text()
    status = tela_1.radioButton.isChecked()
    latitude = tela_1.lineEdit_3.text()
    longitude = tela_1.lineEdit_4.text()
    distancia = tela_1.lineEdit_5.text()
    
    data = [user,nick,status,latitude,longitude,distancia]
    
    checkUser = ts.checkNick(nick)
    if(checkUser == False):
        ts.createUser(data)
        loadInfo(data)
    else:
        QMessageBox.about(tela_1,"ALERTA", "ESTE NICK JÁ EXISTE")  

def updateDataStatus():
    status =  tela_3.radioButton.isChecked()
    nick   =  tela_3.label_11.text()
    response = ts.updateStatus(nick,status)    
    QMessageBox.about(tela_1,"SUCESSO",response) 
    updateUser(nick)

    

telasChat = []
app=QtWidgets.QApplication([])
tela_1 = uic.loadUi("tela_1.ui")
tela_1.show()
tela_1.pushButton.clicked.connect(createUser) 
tela_3 = uic.loadUi("tela_3.ui")    
tela_3.pushButton.clicked.connect(updateDataStatus)
app.exec()