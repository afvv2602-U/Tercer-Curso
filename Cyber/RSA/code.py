def main():
    p = 11
    q = 3
    n = p*q
    z = (p - 1) * (q -1)
    k = coprimo(z)
    j = find_j(k,z)
    print(f'el valor n{n}, k {k}')
    mensaje = reverse(j,n)
    print(mensaje)
    

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
        print(j)
        cont = cont +1
        if j.is_integer():
            return j
        
def reverse(j, n):  
    mensaje = 'QINOQBWJJXBONG'
    ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    desencriptado = ''
    
    for letra in mensaje:
        C = ALFABETO.index(letra)
        # Realizar la operación de desencriptación
        M = pow(C, int(j), n)  # Utilizar la función pow con tres argumentos para eficiencia
        M = M % len(ALFABETO)
        desencriptado += ALFABETO[M]
        
    return desencriptado

         




if __name__ == '__main__':
    main()