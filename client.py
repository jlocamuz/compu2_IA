import socket
from datetime import datetime
import argumentos
import pickle

PORT = 2222
SERVER = '127.0.1.1' 
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
FOLDER = argumentos.folder
NEURONAS = argumentos.neuronas

client = socket.socket()
client.connect(ADDR)
connected = True

while connected == True:
    msg = [FOLDER, NEURONAS]
    msg_s = pickle.dumps(msg)
    client.send(msg_s)
    rta = client.recv(1024)
    rta_des = pickle.loads(rta)
    print(rta_des)
    connected = False