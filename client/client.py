import socket
from datetime import datetime
import pickle
import argparse
import time
import itertools
import threading
import sys

PORT = 2222
SERVER = '127.0.1.1' 
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--learningrate", default=0.5, type=float)
parser.add_argument("-p", "--hiddenlayerperc", default=100, type=int)
parser.add_argument("--layers", default=1, type=int)
parser.add_argument("-i", "--iter", default=10, type=int)
parser.add_argument("--folder", type=str, default="tacetta")
parser.add_argument("--extention", type=str, default="jpg")
parser.add_argument("--identif", type=str, default="57190")

args = parser.parse_args()

client = socket.socket()
client.connect(ADDR)
connected = True

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rServer entrenando red..' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')

t = threading.Thread(target=animate)
t.start()


while connected == True:

    # MLP SETTINGS
    LR = args.learningrate
    HIDDEN_LAYER_PERCEPTRONS = args.hiddenlayerperc
    HIDDEN_LAYERS = args.layers
    ITERACIONES = args.iter
    FOLDER = args.folder
    EXTENTION = args.extention
    IDENTIF = args.identif 
    msg = [LR, HIDDEN_LAYER_PERCEPTRONS, ITERACIONES, FOLDER, EXTENTION, IDENTIF]
    msg_s = pickle.dumps(msg)
    client.send(msg_s)

    # loading...


    rta = client.recv(1024)
    rta_des = pickle.loads(rta)
    print(rta_des)

    # mandamos test_imgs que queremos probar...
    TEST_IMAGES = [f"6A{IDENTIF}", f"7A{IDENTIF}", f"8A{IDENTIF}", f"6B{IDENTIF}", f"7B{IDENTIF}", f"8B{IDENTIF}"]

    msg_s = pickle.dumps(TEST_IMAGES)
    client.send(msg_s)

    # recibimos resultado 
    rta = client.recv(1024)
    rta_des = pickle.loads(rta)
    print('')
    print(rta_des)
    connected = False
    done = True