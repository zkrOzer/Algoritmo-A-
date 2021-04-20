#Clase nodo, permite g,h,f
class Node():
    #constructor del nodo
    def __init__(self, x = 0, y = 0, padre = None):
        self.x = x
        self.y = y

        self.padre = padre


        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

#Algoritmo
def aestrella(matriz, inicio, end):

    #Asignamos las cordenadas a los nodos inicial y final
    nodoinicial = Node(inicio[0], inicio[1], None)
    nodofinal = Node(end[0], end[1], None)

    #Inicializamos las listas abierta y cerrada
    lista_abierta = []
    lista_cerrada = []

    #Pasamos el nodo inicial o inicio a la lista abierta
    lista_abierta.append(nodoinicial)


    while len(lista_abierta) > 0:

        #Si el nodo en el que nos encontramos esta en la posicion 0 de la lista abierta
        nodo_actual = lista_abierta[0]
        posicion_actual = 0

        #Enumeramos todos los elementos de la lista abierta, y los recorremos
        for index, node in enumerate(lista_abierta):
            #Primera condicion, comparamos las f
            if node.f < nodo_actual.f:
                #Cambiamos la posicion actual a la posicion siguiente, la cual ya se encuentra en la lista abierta
                nodo_actual = node
                posicion_actual = index

        #Eliminamos la posicion en la que nos encontramos de la lista abierta, para agregarl el nodo actual
        #a la lista cerrada
        lista_abierta.pop(posicion_actual)
        lista_cerrada.append(nodo_actual)

        #Si el nodo en el que nos encontramos, es igual al nodo final, iniciamos el arreglo del camino
        #para posteriormente agregar en esa lista los nodos posteriores correspondientes al camino
        if nodo_actual == nodofinal:
            camino = []
            actual = nodo_actual
            while actual is not None:
                #se agregan las cordenadas de la posicion actual al camino.
                camino.append((actual.x,actual.y))
                actual = actual.padre
            return camino[::-1]

        #se definen las cordenadas de los nodos vecinosRs
        hijo = []
        vecinosR = [(0,1), (0,-1), (-1,0), (1,0)]
        vecinosD = [(1,1), (-1,-1), (1,-1), (-1,1)]

        #Recorremos las listas de diagonales y rectas
        for node in vecinosR and vecinosD:
            #Identificamos la posicion del nodo vecinosR al que se movera

            if node in vecinosD:
                x_aux = nodo_actual.x + node[0]
                y_aux = nodo_actual.y + node[1]

                #Verificamos que el nodo siguiente se encuentre dentro de la matriz
                if x_aux > (len(matriz) - 1) or x_aux < 0 or y_aux > (len(matriz[len(matriz)-1]) - 1) or y_aux < 0:
                    continue

             #Identificamos por donde no podemos pasar
                if matriz[x_aux][y_aux] == 'X':
                    continue

                #Agregamos a la lista hijo el nuevo nodo con cordenadas del hijo para movernos
                nuevo_nodo = Node(x_aux, y_aux, nodo_actual)

                hijo.append(nuevo_nodo)

                for child in hijo:

                    if child in lista_cerrada:
                        continue

                    #Calculammos la g sumandole el valor del avance
                    child.g = nodo_actual.g + 14
                    #Calculamos H, los saltos hasta el final
                    child.h = (end[0] - child.x) + (end[1] - child.y)
                    #Se calcula f sumando g y h
                    child.f = child.g + child.h

                    #Recorremos la lista abierta
                    for nodo_abierto in lista_abierta:
                        #Si el hijo se encuentra en la lista abierta y el hojo tiene mayor g
                        if child == nodo_abierto and child.g > nodo_abierto.g:
                            continue

                    #agregamos a la lista abierta el nodo hijo al cual se avanzo
                    lista_abierta.append(child)

            if node in vecinosR:
                x_aux = nodo_actual.x + node[0]
                y_aux = nodo_actual.y + node[1]

                # Verificamos que el nodo siguiente se encuentre dentro de la matriz
                if x_aux > (len(matriz) - 1) or x_aux < 0 or y_aux > (len(matriz[len(matriz) - 1]) - 1) or y_aux < 0:
                    continue

                # Identificamos por donde no podemos pasar
                if matriz[x_aux][y_aux] == 'X':
                    continue

                # Agregamos a la lista hijo el nuevo nodo con cordenadas del hijo para movernos
                nuevo_nodo = Node(x_aux, y_aux, nodo_actual)

                hijo.append(nuevo_nodo)

                for child in hijo:

                    if child in lista_cerrada:
                        continue

                    # Calculammos la g sumandole el valor del avance
                    child.g = nodo_actual.g + 10
                    # Calculamos H, los saltos hasta el final
                    child.h = (end[0] - child.x) + (end[1] - child.y)
                    # Se calcula f sumando g y h
                    child.f = child.g + child.h

                    # Recorremos la lista abierta
                    for nodo_abierto in lista_abierta:
                        # Si el hijo se encuentra en la lista abierta y el hojo tiene mayor g
                        if child == nodo_abierto and child.g > nodo_abierto.g:
                            continue

                    # agregamos a la lista abierta el nodo hijo al cual se avanzo
                    lista_abierta.append(child)


def imprimir_matriz(matriz):
    for i in matriz:
        for j in i:
            print("%5s" % (j), end="")
        print()


cuadrado2 = [[0, 0, 0, 'X', 0, 0, 0, 0, 0, 'X'],
            [0, 0, 0, 0, 'X', 0, 'X', 0, 0, 0],
            [0, 'X', 0, 0, 0, 'X', 0, 'X', 0, 'X'],
            ['X', 0, 'X', 0, 'X', 0, 'X', 0, 'X', 0],
            [0, 0, 0, 0, 0, 'X', 0, 0, 0, 0],
            [0, 0, 'X', 0, 0, 0, 0, 0, 'X', 0],
            [0, 0, 0, 'X', 0, 0, 0, 0, 0, 'X'],
            [0, 0, 'X', 0, 0, 0, 0, 0, 0, 0],
            [0, 'X', 'X', 0, 0, 'X', 0, 'X', 0, 0],
            [0, 0, 0, 0, 'X', 0, 'X', 0, 0, 0]]

cuadrado =  [[0, 0, 0, 0, 0],
            [0, 0, 'X', 0, 0],
            [0, 0, 'X', 0, 0],
            [0, 0, 'X', 0, 0],
            [0, 0, 0, 0, 0]]

inicio2 = (9, 3)
final2 = (0, 0)

inicio = (2, 0)
final = (2, 4)

cuadrado[inicio[0]][inicio[1]] = 'INICIO'
cuadrado[final[0]][final[1]] = 'FIN'

imprimir_matriz(cuadrado)

camino = aestrella(cuadrado, inicio, final)
print(" ")

for i in camino:
    cuadrado[i[0]][i[1]] = "█"


imprimir_matriz(cuadrado)

print("Ruta mas corta:")
print(camino)