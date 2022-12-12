#!/usr/bin/python3
import socket, os, threading, datetime
import pickle
import time
from logear import *
import cv2
import numpy as np
import tqdm
from MLP import MLP


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

		[LR, HIDDEN_LAYER_PERCEPTRONS, ITERACIONES, FOLDER, EXTENTION, IDENTIF] = msg_d
		print("Recibido: %s" % [LR, HIDDEN_LAYER_PERCEPTRONS, ITERACIONES, FOLDER, EXTENTION, IDENTIF])


		# IMAGE SETTINGS
		SET = FOLDER
		BASE_PATH = f"./img/{SET}/"
		EXTENTION = EXTENTION
		ID = IDENTIF
		IMG_SIZE = 80*96
		IMG_LIMIT = 5
		IMG_RANGE = sorted([i for i in range(1, IMG_LIMIT + 1)]*2) #1 1 2 2 3 3 4 4 5 5 
		PERSON_RANGE = ["A", "B"]*5
		TEST_IMAGES = [f"6A{ID}", f"7A{ID}", f"8A{ID}", f"6B{ID}", f"7B{ID}", f"8B{ID}"]

		# CODIGO

		# Leer imagenes
		print("CARGANDO IMAGENES")
		img_list = []
		path_list = []
		for gesture, person in zip(IMG_RANGE, PERSON_RANGE):
			path = f"{BASE_PATH}{gesture}{person}{ID}.{EXTENTION}"
			print(f"CARGANDO: {path}")
			flat_img = cv2.imread(path, 0).flatten()/255
			if person == "A":
				flat_img = np.append(flat_img, [0])
			else:
				flat_img = np.append(flat_img, [1])

			img_list.append(flat_img)
			path_list.append(path)
		
		print("CREANDO RED NEURONAL")
		# [100] * 1 
		print([HIDDEN_LAYER_PERCEPTRONS])
		mlp = MLP(IMG_SIZE, [HIDDEN_LAYER_PERCEPTRONS] + [1], learning_rate=LR)

		print("ENTRENANDO RED NEURONAL")
		global_err_hist = {}
		runtime_test_hist = {}
		for i in tqdm.tqdm(range(ITERACIONES)):
			mlp.train(img_list)

		# RESPUESTA A CLIENT --> para decirle que proporcione imagen de prueba 

		resp = 'RED ENTRENADA'
		rta_s = pickle.dumps(resp, protocol=2)
		sock.send(rta_s) # ************

		# RECIBIMOS IMAGEN QUE EL CLIENTE QUIERE PROBAR...
		msg = sock.recv(MAX_SIZE)
		TEST_IMAGES = pickle.loads(msg)

		
		
		try:
			resultados = ''
			for test_img in TEST_IMAGES:
				flat_img = cv2.imread(f"{BASE_PATH}{test_img}.{EXTENTION}", 0).flatten()/255
				r = mlp.run(flat_img)
				resultados += f"EXAMPLE: {test_img}.{EXTENTION} --> {r}\n"
			rta_s = pickle.dumps(resultados, protocol=2)
			sock.send(rta_s) # ************
		except Exception:
			pass

		# LOGGER 
		#data = "%s|%s|%s|%s|%s" % (TODAY,name,email,key,ip) + '\n'
		#print(data)
		#escribir_log(data, locki, str(addr[1]))

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
locki = threading.Lock()


while True:
	# establish a connection
	clientsocket = serversocket.accept()

	print("Got a connection from %s" % str(clientsocket[1]))

#    msg = 'Thank you for connecting'+ "\r\n"
#    clientsocket[0].send(msg.encode('ascii'))
	th = threading.Thread(target=th_server, args=(clientsocket, ))
	th.start()