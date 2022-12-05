import numpy as np
import math
import matplotlib.pyplot as plt
from probando2 import *
import random
import time 
from multiprocessing import Pool

def sigmoid(x):
	sig = 1 / (1 + math.exp(-x))
	return sig

class Perceptron:
	def __init__(self, capa, neurona, nro_entradas, resultado=None, error=None):
		self.capa = capa
		self.neurona = neurona
		self.pesos = [random.uniform(-0.01, 0.01) for _ in range(nro_entradas+1)]

	def sumatoria(self, entrada):
		#print('sumatoria')
		# el cero siempre para el bias!
		z = 0  # inicializo en 0
		for i in range(len(entrada)):
			z += (entrada[i]) * self.pesos[i]
		self.resultado = sigmoid(z)

	def actualizar_pesos(self, lr, entrada):
		#print('actualizando pesos')
		for i in range(len(entrada)):
			delta = self.error * lr * entrada[i]
			self.pesos[i] += delta

	def alimentar_neurona(self,red, dato, lr, bias):
		if self.capa == 0:
			entrada = [bias] + list(dato[:-1])

		else:
			resultados_anteriores = [i.resultado for i in red[self.capa - 1]]
			entrada = [bias] + resultados_anteriores
		self.sumatoria(entrada)
		self.error = dato[-1] - self.resultado
		self.actualizar_pesos(lr, entrada)

class RedNeuronal:
	def __init__(self, x):
		#print('creando Estructura Red Neuronal')
		self.red = []
		self.estructura = x  # n capas ocultas
				#[7680, 100, 1]
		for capa, numero_neuronas in enumerate(self.estructura[1:]):
			lista_neuronas = []
			# i [100, 1] neurona [0-99]
			for neurona in range(numero_neuronas):
				# entradas? 
				lista_neuronas.append(Perceptron(capa, neurona, self.estructura[capa]))
			(self.red).append(lista_neuronas)


	def alimentarRed(self, data, sock=None):
		lr = 0.1
		epochs = 0
		bias = 1


		while epochs < 5:
			print(f'\n***epoch {epochs}*** desde socket {sock}\n')
			for indice, dato in enumerate(data):
				#print(f'--------------------indice data {indice} epoch {epochs}--------------------')
				for capa in self.red: 
					with Pool(processes=8) as pool:
						multiple_results = [pool.apply_async(neurona.alimentar_neurona(self.red, dato,lr, bias), ()) for neurona in capa]
		

			epochs += 1




if __name__ == '__main__':
	inicio_de_tiempo = time.time()
	personas = manipular_imagenes('./imagenes', './modificadas/')
	nro_entradas = len(personas[0]) - 1  # pq el ultimo elemento es 0-A y 1-B
	lista = [nro_entradas, 100, 1]
	red_neuronal = RedNeuronal(lista) # tomar primer parametro de lista como entradas.
	red_neuronal.alimentarRed(personas)
	final_de_tiempo = time.time()
	tiempo_transcurrido = final_de_tiempo - inicio_de_tiempo
	print("\nTomo %d segundos." % (tiempo_transcurrido))