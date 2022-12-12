from random import uniform
from math import exp
import numpy as np


class Perceptron:
    """
    Clase que replica el comportamiento de un perceptron con tasa de
    aprendizaje (Learning rate) fija.
    """

    def __init__(self, no_of_inputs: int = 0, weights: list[float] = [], LR: float = 0.1) -> None:
        self.weights: list[float] = weights# or [uniform(-1, 1) for i in range(no_of_inputs + 1)]
        self.learning_rate = LR
        self.last_input = []
        self.last_output = None

    def run(self, input: list[int]) -> float:
        # Agregar el bias en las entradas
        input = np.append(input, [1])
        self.last_input = input

        # Producto escalar entre vector de entradas y pesos
        # x = sum([i*w for w, i in zip(self.weights, input)]) # Python way
        x = np.dot(input, self.weights) # Numpy way

        # Pasarlo por la fc. de activacion y devolver resultado
        self.last_output = 1/(1+exp(-x))
        return self.last_output
    
    def learn(self, dw_list: list[float]) -> list[float]:
        self.weights = [dw + w for dw, w in zip(dw_list, self.weights)]
        return self.weights


    def __str__(self) -> str:
        return f"Perceptron( weights = {[round(w, 5) for w in self.weights]} )\n\tI: {self.last_input}\n\tO: {self.last_output}\n"
