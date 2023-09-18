def main():
    n, z = calculo_p_q(7, 17)
    k = coprimo(z)
    j = find_j(k, z)

    mensaje = 'HOLASOYPEDROMEENCANTANADARYHACERSKATE'

    mensaje_encrip = encriptar(mensaje, k, n)

    print(f'Mensaje encriptado: {mensaje_encrip}')

    mensaje_desencr = desencriptar(mensaje_encrip, j, n)

    print(f'Mensaje desencriptado: {"".join([ALFABETO[M] for M in mensaje_desencr])}')

# Calcula y devuelve el n y z    
def calculo_p_q(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    return n, z

# Encuentra y devuelve un numero coprimo con 'z' desde el rango 2 hasta z-1
def coprimo(z):
    for k in range(2, z):
        if mcd(z, k) == 1:
            return k
    return None

# Maximo comun divisor
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Encontrar la clave privada escapando cuando encontremos el primer numero entero usando k y z
def find_j(k, z):
    cont = 1
    while True:
        j = (1 + cont * z) / k
        cont = cont + 1
        if j.is_integer():
            return int(j)


def encriptar(mensaje, k, n):
    cifrado = []
    for letra in mensaje:
        M = ALFABETO.index(letra)
        C = pow(M, k, n) # Eleva M a k y hace el modulo de n
        cifrado.append(C)
    return cifrado


def desencriptar(mensaje, j, n):
    descifrado = []
    for C in mensaje:
        M = pow(C, j, n) # Eleva C a j y luego hace el modulo de n
        descifrado.append(M)
    return descifrado


if __name__ == '__main__':
    ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    main()
