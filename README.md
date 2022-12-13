# compu2_IA
# ¿Qué hace el programa? 
  Red neuronal que toma 5 imágenes de dos personas con distintos gestos y “aprende” a distinguir a persona A de B a través de algoritmos de aprendizaje automático. 
# Estructura de la red neuronal 
  En primer lugar, vale aclarar que cada fotografía de las personas A y B cuentan con 7680 pixeles en blanco y negro: 80 (ancho) x 96 (alto). Para la capa de entrada de la red neuronal que aprenderá a reconocer y clasificar a las personas, tomamos cada pixel como entrada de la misma, y una capa intermedia de n neuronas, finalizando con una neurona en la capa correspondiente a la salida. Por lo que cada neurona de la capa intermedia tendrá 7681 contando el bias, mientras que la neurona de la capa final tendrá n+1 entradas (una por cada neurona de la capa anterior + bias). 
# arquitectura cliente-servidor a travez de sockets TCP
    De esta forma es posible mantener mi codigo en un server y que cada cliente pueda enviar sus parametros a travez de dicho mecanismo ICP con el fin de obtener el resultado deseado.
    Este tipo de arquitectura nos permite tener varios clientes

# Simultaneidad de clientes a partir de hilos
    Clientes ejecutandose en el server concurrentemente a travez de hilos

# Locks para sincronizar el uso de un recurso comun a varios hilos
    Utilize un Lock para que varios hilos puedan escribir sus logs en un mismo archivo
    sin interferir uno con el otro

# Paralelismo de procesos a partir de la libreria multiprocessing 
    Analizando en que parte del codigo es aplicable y beneficioso el paralelismo de procesos, se llego a la conclusion de que la actualizacion de pesos de cada neurona puede ejecutarse paralalela e independientemente sin modificar los valores finales 

# Facilitar el manejo de objetos a la hora de pasar mensajes TCP usando PICKLE
    El modulo pickle implementa protocolos binarios para serializar y deserializar una estructura de objetos Python. «Pickling» es el proceso mediante el cual una jerarquía de objetos de Python se convierte en una secuencia de bytes
    Esto facilito y me independizo de hacer un encoding de cada mensaje y me libere de las incompatibilidades

