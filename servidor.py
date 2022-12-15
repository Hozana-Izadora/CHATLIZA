import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost',8888))

servidor.listen()
cliente, end = servidor.accept()

sair = False

while not sair:
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'sair':
        sair = True
    else:
        print(msg)
    cliente.send(input("Mensagem: ").encode('utf-8'))

cliente.close()
servidor.close()