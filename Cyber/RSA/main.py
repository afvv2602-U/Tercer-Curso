def main():
    n, z = calculo_p_q(5, 11) # La multiplicacion de los dos numeros tiene que ser mayor que 27
        
    # Clave publica
    k = coprimo(z)

    # Clave privada
    j = find_j(k, z)

    print(f'valor n {n} valor de z {z} valor k {k} valor de j {j}')

    # ver_letras_limpias(mensaje)
    mensaje = ''
    cifrado_num,cifrado_letras = encriptar(mensaje, k, n)

    print(f'Mensaje encriptado: {cifrado_num}{cifrado_letras}')
    
    mensaje_desencr = desencriptar(cifrado_num, j, n)

    print(f'Mensaje desencriptado: {"".join([ALFABETO2[M] for M in mensaje_desencr])}')

# Calcula y devuelve el n y z    
def calculo_p_q(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    return n, z

# Ver las letras del mensaje original pasados a la posicion del alfabeto original
def ver_letras_limpias(mensaje):
    posiciones = [ALFABETO.index(letra) for letra in mensaje]
    print(posiciones)

# Encuentra y devuelve un numero coprimo con 'z' desde el rango 2 hasta z-1
# Dos numeros son coprimos si su MCD es 1
# Si el resultado es 1 entonces k es coprimo con z
# Y usamos esa K como clave publica
def coprimo(z):
    for k in range(2, z):
        if mcd(z, k) == 1:
            return k
    return None

# Maximo comun divisor usando el metodo de euclides
# Dado dos numeros naturales a y b , a >= b y b != 0
# Este metodo se basa en tras hacer divisones sucesivas encontrar el numero
# Rn siendo Rn el ultimo resto no nulo de las divisiones sucesivas
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
    
# convierte un mensaje de texto en una serie de numeros cifrados 
# usando la clave publica k y el modulo n
def encriptar(mensaje, k, n):
    cifrado = []
    cifrado_letras = []
    for letra in mensaje:
        M = ALFABETO.index(letra)
        C = pow(M, k, n) # Eleva M a k y hace el modulo de n
        cifrado.append(C)
        cifrado_letras.append(ALFABETO[C % len(ALFABETO)]) # Le aplicamos a cada numero el mod 
    return cifrado,cifrado_letras

# Toma un mensaje cifrado y lo convierte de nuevo en texto 
# Usando la clave privada j y el modulo n
def desencriptar(mensaje, j, n):
    descifrado = []
    for C in mensaje:
        M = pow(C, j, n) # Eleva C a j y luego hace el modulo de n
        descifrado.append(M)
    return descifrado

if __name__ == '__main__':
    ALFABETO = "1234567890"
    ALFABETO2 = 'ABCDEFGHIJKLMN.OPQRSTUVWXYZ '
    main()
