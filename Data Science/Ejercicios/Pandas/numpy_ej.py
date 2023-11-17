import numpy as np
import random as rd

def main():
    # eje_1()
    # eje_2()
    # eje_3()
    # eje_4()
    # eje_5()
    # eje_6()
    # eje_7()
    # eje_8()
    # eje_9()
    eje_10()

def eje_1():
    lista = list(range(1,11))
    lista = [elemento+5 for elemento in lista]
    print(lista)

def eje_2(): 
    v = np.array(list(range(1,11)))
    v = [elemento+5 for elemento in v]
    print(v)

def eje_3():
    v = np.array(list(range(100,201,10)))
    print(v)

def eje_4():
    v = np.random.randint(0, 2, (6, 3))
    print(v)

def eje_5():
    v = np.random.randn(100)
    print(v)

def eje_6():
    v = np.random.randint(0,101,100)
    print(v)

def eje_7():
    v = np.random.randint(0,101,100)
    v.sort()
    print(v)

def eje_8():
    v1 = np.random.randint(1,11,5)
    v2 = np.random.randint(1,11,5)
    print(v1 + v2)

def eje_9():
    v = np.random.randint(0,101,100)
    v.sort()
    vector = v.reshape(10,10)
    print(vector)

def eje_10():
    v = np.random.randint(0,101,100)
    v.sort()
    vector = v.reshape(10,10)
    print(vector*8)


if __name__ == '__main__':
    main()