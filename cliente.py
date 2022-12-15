import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost',8888))

sair = False

print("Digite 'sair' para terminar o chat")

while not sair:
    cliente.send(input('Mensagem: ').encode('utf-8'))
    msg = cliente.recv(1024).decode("utf-8")
    if(msg == 'sair'):
        sair = True
    else:
        print(msg)
cliente.close()
