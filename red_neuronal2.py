import numpy as np
import math
import matplotlib.pyplot as plt
from probando2 import *
import random

def sigmoid(x):
	sig = 1 / (1 + math.exp(-x))
	return sig

class Perceptron:
	def __init__(self, capa, neurona, nro_entradas, resultado=None, error=None):
		self.capa = capa
		self.neurona = neurona
		self.pesos = [random.uniform(-0.01, 0.01) for _ in range(nro_entradas+1)]


	def sumatoria(self, entrada):
		print('sumatoria')
		# el cero siempre para el bias!
		z = 0  # inicializo en 0
		for i in range(len(entrada)):
			z += (entrada[i]) * self.pesos[i]
		self.resultado = sigmoid(z)

	def actualizar_pesos(self, lr, entrada):
		print('actualizando pesos')
		for i in range(len(entrada)):
			delta = self.error * lr * entrada[i]
			self.pesos[i] += delta


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



	def alimentarRed(self, data):
		errorA = 1
		errorB = 1
		plt.xlabel('x')
		plt.ylabel('errores')
		plt.grid(True)
		lr = 0.1
		epochs = 0
		bias = 1
		x1 = 0
		while errorA > 0.005 and errorB > 0.005:
			print(f'\n\n\n***epoch {epochs}***\n\n')
			for indice, dato in enumerate(data):
				print(f'--------------------indice data {indice} epoch {epochs}--------------------')
				try:
					for indiceCapa, capa in enumerate(self.red):
						print(f'se procesara {len(capa)} neuronas')
						for indice_neurona, neurona in enumerate(capa):
							print(f'neurona {indice_neurona} en capa {neurona.capa}')
							if neurona.capa == 0:
								# PRIMERA CAPA
								# entran mis data.shape[:-1]  --> 1 x peso!  me queda un peso. para el bias :)
								entrada = [bias] + list(dato[:-1])

							else:
								# CAPAS INTERMEDIAS
								resultados_anteriores = [i.resultado for i in self.red[neurona.capa - 1]]
								entrada = [bias] + resultados_anteriores
							neurona.sumatoria(entrada)
							neurona.error = dato[-1] - neurona.resultado
							if indice % 2 == 0:
								color = 'green'
								errorA = abs(neurona.error)
							else:
								color = 'orange'
								errorB = abs(neurona.error)

							# ultima capa. 
							if len(capa) == 1:
								plt.plot(x1, abs(neurona.error),"o", color=color)

							# for i in neurona.pesos:
							#   plot2.plot(x,i,".",color='black')
							x1 += 0.1
							neurona.actualizar_pesos(lr, entrada)
				except OverflowError:
					print('pass')
			epochs += 1
		plt.plot(x1, abs(errorA), label = "ERRORES Claudia",color='green')
		plt.plot(x1, abs(errorB), label = "ERRORES Rosario", color='orange')
		plt.legend()
		plt.show()



if __name__ == '__main__':
	personas = manipular_imagenes('./imagenes', './modificadas/')
	nro_entradas = len(personas[0]) - 1  # pq el ultimo elemento es 0-A y 1-B
	lista = [nro_entradas, 100, 1]
	red_neuronal = RedNeuronal(lista) # tomar primer parametro de lista como entradas.
	red_neuronal.alimentarRed(personas)
