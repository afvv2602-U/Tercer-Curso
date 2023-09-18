def main():
    n,z = formulas(11,3)
    k = coprimo(z)
    j = find_j(k,z)
    mensaje = 'HOLASOYPEDRO'
    mensaje_encrip = encriptar(mensaje,k,n)
    print(f'Mensaje encriptado {mensaje_encrip}')
    mensaje__desencr = reverse(mensaje_encrip,j,n)
    print(f'Mensaje desencriptado {mensaje__desencr}')
    
def formulas(p,q):
    n = p*q
    z = (p - 1) * (q -1)
    return n,z

# Función para encontrar un número coprimo con 'z' en el rango de 2 a 'z-1'
def coprimo(z):
    # Itera desde 2 hasta 'z-1'
    for k in range(2, z):
        # Si el MCD de 'z' y 'k' es 1, significa que son coprimos
        if gcd(z, k) == 1:
            # Retorna el valor 'k' que es coprimo con 'z'
            return k
    # Si la función no encontró ningún valor 'k' que sea coprimo con 'z', retorna None
    return None

# Función para calcular el Greates Common Divisor (gcd) de dos números usando el algoritmo de Euclides
def gcd(a, b):
    # Mientras b sea diferente de cero, realiza la operación
    while b:
        # Reemplaza 'a' con 'b' y 'b' con 'a' modulo 'b'
        a, b = b, a % b
    # Cuando 'b' se convierte en cero, 'a' contiene el MCD de los dos números iniciales
    return a

def find_j(k,z):
    cont = 1
    while True:
        j = (1 + cont * z) / k
        cont = cont +1
        if j.is_integer():
            return j

# def find_j(k, z):
#     for j in range(1, z):
#         if (j * k) % z == 1:
#             return j
#     return None

def encriptar(mensaje, k, n):
    M = ALFABETO.index(mensaje)
    C = pow(M, k, n)
    return ALFABETO[C % len(ALFABETO)]
        
def reverse(mensaje,j, n):  
    desencriptado = ''
    for letra in mensaje:
        C = ALFABETO.index(letra)
        # Realizar la operación de desencriptación
        M = pow(C, int(j), n)  # Utilizar la función pow con tres argumentos para eficiencia
        M = M % len(ALFABETO)
        desencriptado += ALFABETO[M]
        
    return desencriptado

if __name__ == '__main__':
    ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    main()