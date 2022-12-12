from random import randint
from MLP import MLP
#from GeneralizationGraph import Grapher
import numpy as np
import cv2
import argparse as ap
from tqdm import tqdm
import multiprocessing as mp

parser = ap.ArgumentParser()
parser.add_argument("-l", "--learningrate", default=0.5, type=float)
parser.add_argument("-p", "--hiddenlayerperc", default=100, type=int)
parser.add_argument("--layers", default=1, type=int)
parser.add_argument("-i", "--iter", default=10, type=int)
parser.add_argument("--folder", type=str, default="tacetta")
parser.add_argument("--extention", type=str, default="jpg")
parser.add_argument("--identif", type=str, default="57190")

args = parser.parse_args()

# IMAGE SETTINGS
SET = args.folder
BASE_PATH = f"./img/{SET}/"
EXTENTION = args.extention
ID = args.identif
IMG_SIZE = 80*96
IMG_LIMIT = 5
IMG_RANGE = sorted([i for i in range(1, IMG_LIMIT + 1)]*2) #1 1 2 2 3 3 4 4 5 5 
PERSON_RANGE = ["A", "B"]*5
TEST_IMAGES = [f"6A{ID}", f"7A{ID}", f"8A{ID}", f"6B{ID}", f"7B{ID}", f"8B{ID}"]


# MLP SETTINGS
LR = args.learningrate
HIDDEN_LAYER_PERCEPTRONS = args.hiddenlayerperc
HIDDEN_LAYERS = args.layers
ITERACIONES = args.iter

# PLOT SETTINGS
SAVE_PATH = "./resultados/"


if __name__ == "__main__":
    
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

    # Instanciar y entrenar MLP
    print("CREANDO RED NEURONAL")
    # [100] * 1 
    print([HIDDEN_LAYER_PERCEPTRONS]*HIDDEN_LAYERS)
    mlp = MLP(IMG_SIZE, [HIDDEN_LAYER_PERCEPTRONS]*HIDDEN_LAYERS + [1], learning_rate=LR)

    print("ENTRENANDO RED NEURONAL")
    global_err_hist = {}
    runtime_test_hist = {}
    for i in tqdm(range(ITERACIONES)):
        mlp.train(img_list)
