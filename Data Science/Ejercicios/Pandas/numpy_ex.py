import numpy as np
import random as rd

def main():
    # create_list()
    pass

def create_list():
    lista = [1,2,3,4]
    lista*2

    # Compresion de lista
    [elemento*2 for elemento in lista]

    # Sin embargo si lo pasamos a un vector numpy
    lista2 = np.array([2,3,4])
    lista2*2
    type(lista2)

    # Como crear un array

    # Como crear un vector a partir de una lista
    v = np.array([2,3,4])

    # Como crear una matriz a partir de una lista de listas
    x = np.array([[1,2,3],[4,5,6]])

    # Crear una matriz a partir de un rango usando el step 2
    np.arange(1,10,2)

    # Array multidimensional 3 x 4
    x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

    # Indexacion de matrices
    arr = np.array([1,2,3,4])
    print(arr[0]) # Sacamos el primer valor
    print(arr[2]+arr[3]) # Sacamos el valor 3 y 4 y los sumamos dando 7 

    arr = np.array([1,2,3,4,5],[6,7,8,9,10])
    print(arr[1,4]) # Imprimimos el valor 10 del segundo array

    arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    print(arr[0,1,2]) # Cogemos el valor 6

    # Slicing list
    arr = np.array([1,2,3,4,5,6,7])

    print(arr[1:5]) # Del index 1 al 4 el ultimo valor no cuenta
    print(arr[4:]) # Del index 4 al final
    print(arr[:4]) # Del index 0 al index 3
    print(arr[-3:-1]) # Desde el indexl -3 al -1 sin cogerlo
    print(arr[1:5:2]) # Coge el index 2 y 4
    arr[::2] # Te devuelve toda la lista de dos en dos mostrando 1,3,5,7

    arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
    print(arr[1,1:4]) # Muestra 7,8,9
    print(arr[0:2,2])
    print(arr[0:2,1:4])

    # Unir matrices horizontal
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])
    np.concatenate((arr1,arr2)) # Pasamos de dos lista a una

    # Unir 2 matrices por filas (axis=1)
    arr1 = np.array([[1,2],[3,4]])
    arr2 = np.array([[5,6],[7,8]])
    np.concatenate((arr1,arr2),axis=1) # mantenemos las dos matrices creando un bidimensional de 4 x 2

    # Dividir matrices
    arr = np.array([1,2,3,4,5,6])
    np.array_split(arr,3) # Se divide en 3 matrices [1,2][3,4][5,6]
    np.array_split(arr,4) # Se divide en 4 matrices pero se quedan los elementos 5 y 6 sueltos [1,2][3,4][5][6]

    # Buscar matrices ('WHERE')
    arr = np.array([1,2,3,4,5,4,4])
    np.where(arr==4) # Devuelve una lista con los indices donde el valor es igual a 4

    # Encuentra los indices donde los valores son pares
    arr = np.array([1,2,3,4,5,6,7,8])
    np.where(arr%2==0) # Devuelve los indices 1,3,5,7 

    # Impares
    arr = np.array([1,2,3,4,5,6,7,8])
    np.where(arr%2==1) # Devuelve los indices 0,2,4,6

    # Ordenar matrices
    arr = np.array([3,0,2,1])
    np.sort(arr) # Ordena la matriz de menor a mayor

    # Filtrar matrices
    arr = np.array([41,42,43,44])
    x = [True,False,True,False]
    nuevo = arr[x]
    print(nuevo) # Nos da los valores 41 y 43

    arr = np.array([41,42,43,44])
    print(arr[np.where(arr>42)]) # Muestra los valores mayores de 42
    
    # Crear un array aleatorio
    rd.randint(1,10) # Generamos un numero aleatorio entre 1 y 10

    [rd.randint(1,10) for cada in range(10)] # Creamos un array de 10 posiciones co numeros aleatorios del 1 al 10

    np.random.randint(1,11,20)

    # Transformar un array
    v = np.array([2,3,4])
    v.shape # Te da la dimesiones

    v = np.arange(20) # Una lista de 20 numeros
    v2 = v.reshape(2,10) # Dos listas de 10 numeros cada una

    # Operaciones con vectores
    v = np.array([2,3,4])
    v2 = np.array([5,6,7])

    print(v + v2) # Suma los arrays
    print(v - v2) # Resta los arrays
    print(v / v2) # Dividir los arrays
    print(v * v2) # Multiplicar los arrays

if __name__ == '__main__':
    main()