from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

import tuple_environment as ts

def openTela2(tela):
    tela.show()

def openTela3():
    tela_3.show()
# data = [user,nick,status,latitude,longitude,distancia]
def loadInfo(data):
    novaTelaChat = uic.loadUi("tela_2.ui")
    telasChat.append(novaTelaChat)
    for tela in telasChat:
        openTela2(tela)
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
        tela.pushButton.clicked.connect(openTela3) 

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

telasChat = []
app=QtWidgets.QApplication([])
tela_1 = uic.loadUi("tela_1.ui")
tela_3 = uic.loadUi("tela_3.ui")
# telaAtual = uic.loadUi("tela_2.ui")
tela_1.show()
tela_1.pushButton.clicked.connect(createUser) 

app.exec()