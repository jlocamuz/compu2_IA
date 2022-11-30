import cv2
import os 

# solo apto para imagenes 80x96
def manipular_imagenes(carpeta, carpeta_nueva):
    
    # 0 = A = CLAUDIA
    # 1 = B = ROSARIO
    persona = 0
    # carpeta = path carpeta donde estan las imagenes que quiero modificar
    contenido = os.listdir(carpeta)
    contenido.sort()
    tabla_de_verdad = []
    for i in contenido:
        datos_foto = [] # renglon tabla d verdad
        img = cv2.imread('./imagenes/'+i)

        if i[1] == 'A':
            persona = 0
        else: 
            persona = 1

        #borramos parte izquierda
        img[0:96, 0:15] = (255, 255, 255)
        #borramos parte derecha
        img[0:96, -15:] = (255, 255, 255)
        #eliminamos arriba
        img[0:25, 0:80] = (255, 255, 255)
        #eliminamos abajo
        img[75:, 0:80] = (255, 255, 255)
        contador = 0
        for j in img:
            for k in j: 
                contador += 1
                datos_foto.append((k[0])/255)
        
        datos_foto.append(persona)
        #print(contador) corroboracion 7680 
        tabla_de_verdad.append(datos_foto)
        #cv2.imwrite(carpeta_nueva+i,img)

    #print(len(tabla_de_verdad)) #10
    #print(len(tabla_de_verdad[0])) # 7681 = pixeles + persona

    return tabla_de_verdad