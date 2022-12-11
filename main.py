from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

import tuple_environment as ts

def openTela2():
    tela_2.show()

def loadInfo(data):
    openTela2()
    tela_2.label_2.setText(data[0])
    tela_2.label_3.setText(data[1])
    if(data[2] == True):
        status = "ONLINE"
    else:
        status = "OFFLINE"
    tela_2.label_7.setText(status)

def createUser():

    user = tela_1.lineEdit.text()
    nick = tela_1.lineEdit_2.text()
    status = tela_1.radioButton.isChecked()
    latitude = tela_1.lineEdit_3.text()
    longitude = tela_1.lineEdit_4.text()
    distancia = tela_1.lineEdit_5.text()
    
    data = [user,nick,status,latitude,longitude,distancia]
    data2 = [nick,status]
    checkUser = ts.checkNick(nick)
    if(checkUser == False):
        ts.createUser(data)
        ts.updateStatus(data2)
        loadInfo(data)
    else:
        QMessageBox.about(tela_1,"ALERTA", "ESTE NICK JÁ EXISTE")  


app=QtWidgets.QApplication([])
tela_1 = uic.loadUi("tela_1.ui")
tela_2 = uic.loadUi("tela_2.ui")
tela_1.show()
tela_1.pushButton.clicked.connect(createUser) 

app.exec()