#!/usr/bin/python3
import socket, os, threading, datetime
from probando2 import *
import pickle
from red_neuronal import *
import time

MAX_SIZE=512
KEY="12135"

TODAY=datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")


def th_server(sock_full):
    name = "_"
    key="_"
    email="_"
    sock,addr = sock_full
    print("Launching thread... addr: %s" % str(addr))
    exit = False
    ip=str(addr)
    stage = 0
    while True:
        msg = sock.recv(MAX_SIZE)
        msg_d = pickle.loads(msg)
        print("Recibido: %s" % msg_d)
        resp = 'imagenes procesadas'

        # codigo
        inicio_de_tiempo = time.time()
        personas = manipular_imagenes('./imagenes', './modificadas/')
        nro_entradas = len(personas[0]) - 1  # pq el ultimo elemento es 0-A y 1-B
        lista = [nro_entradas, 100, 1]
        red_neuronal = RedNeuronal(lista) # tomar primer parametro de lista como entradas.
        red_neuronal.alimentarRed(personas)
        final_de_tiempo = time.time()
        tiempo_transcurrido = final_de_tiempo - inicio_de_tiempo
        print("\nTomo %d segundos." % (tiempo_transcurrido))


        if msg[0:4] == "exit":
            resp = "200"
            exit = True
        rta_s = pickle.dumps(resp)
        sock.send(rta_s) # ************
        data = "%s|%s|%s|%s|%s" % (TODAY,name,email,key,ip)
        print(data)
        sock.close()
        
        break
            




# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# get local machine name
#host = socket.gethostname()
host = socket.gethostbyname(socket.gethostname()) 
port= 2222 # ****

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket = serversocket.accept()

    print("Got a connection from %s" % str(clientsocket[1]))

#    msg = 'Thank you for connecting'+ "\r\n"
#    clientsocket[0].send(msg.encode('ascii'))
    th = threading.Thread(target=th_server, args=(clientsocket,))
    th.start()


