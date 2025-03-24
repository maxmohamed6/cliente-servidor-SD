import socket as s

HOST = '127.0.0.1'
PORT = 50000

with s.socket(s.AF_INET, s.SOCK_STREAM) as server:

    #disponiblidade & abertura de rede

    server.bind((HOST, PORT))

    server.listen() #garantir a disponibilidade de entrada de cliente

    connection, address = server.accept()

    print(f"Conectado por : {address}")

    data = connection.recv(1024)

    connection.send(data)

    


