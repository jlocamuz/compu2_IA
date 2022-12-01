import argparse

parser = argparse.ArgumentParser()
parser.add_argument('folder', help='folder donde estan las imagenes')
parser.add_argument('-f',help='funcion folder', action='store_true')

parser.add_argument('neuronas', help='cantidad de neuronas capa intermedia')
parser.add_argument('-n',help='funcion neuronas', action='store_true')
args = parser.parse_args()
if args.f: 
    folder = args.folder
if args.n: 
    neuronas = args.neuronas
