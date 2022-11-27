# compu2_IA
# ¿Qué hace el programa? 
  Red neuronal que toma 5 imágenes de dos personas con distintos gestos y “aprende” a distinguir a persona A de B a través de algoritmos de aprendizaje automático. 
# Estructura de la red neuronal 
  En primer lugar, vale aclarar que cada fotografía de las personas A y B cuentan con 7680 pixeles en blanco y negro: 80 (ancho) x 96 (alto). Para la capa de entrada de la red neuronal que aprenderá a reconocer y clasificar a las personas, tomamos cada pixel como entrada de la misma, y una capa intermedia de 100 neuronas, finalizando con una neurona en la capa correspondiente a la salida. Por lo que cada neurona de la capa intermedia tendrá 7681 contando el bias, mientras que la neurona de la capa final tendrá 101 entradas (una por cada neurona de la capa anterior + bias). 
