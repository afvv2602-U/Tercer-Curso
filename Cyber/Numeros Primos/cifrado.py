# Definir alfabeto español
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Cifrado afín: C = (a * M + b) mod m
# M representa la posición de la letra en el alfabeto (texto claro)
# C representa la posición de la letra cifrada
# a es la clave de decimación, debe ser coprimo con m (longitud del alfabeto)
# b es la clave de desplazamiento
def cifrar(mensaje, a, b):
    cifrado = ""
    m = len(ALFABETO)  # m representa la longitud del alfabeto
    for letra in mensaje.upper():
        if letra in ALFABETO:
            M = ALFABETO.index(letra) # Coge la posicion del a letra en el alfabeto
            C = (a * M + b) % m # Se transforma a una posicion cifrada dependiendo de los valores de a y b
            cifrado += ALFABETO[C] # Añadimos al cifrado la nueva letra en la posicion cifrada
        else:
            cifrado += letra
    return cifrado


# Descifrado afín: M = a_inv * (C - b) mod m
# a_inv es el inverso multiplicativo de a mod m
# Siendo C la posicion de la letra Cifrada en nuestro alfabeto
# b es la clave de desplazamiento
# a_inv sigue siendo nuestra clave de decimacion.
def descifrar(mensaje_cifrado, a, b):
    descifrado = ""
    m = len(ALFABETO)
    a_inv = encontrar_inverso(a, m)
    
    for letra in mensaje_cifrado.upper():
        if letra in ALFABETO:
            C = ALFABETO.index(letra)
            M = (a_inv * (C - b)) % m  
            descifrado += ALFABETO[M] # guardamos la letra que se encuentra en la posicion M que es ya nuestro alfabeto normal
        else:
            descifrado += letra
    return descifrado

# Función de fuerza bruta para encontrar posibles claves y mensajes descifrados
def fuerza_bruta(mensaje_cifrado):
    primos_menores_20 = [2, 3, 5, 7, 11, 13, 17, 19]  # Lista de números primos menores a 27
    resultados = []  # Lista para guardar los resultados
    m = len(ALFABETO)
    
    for a in primos_menores_20:
        if encontrar_inverso(a, m):  # Si 'a' tiene un inverso multiplicativo modulo 'm'
            for b in primos_menores_20:  # Iteramos solo sobre números primos para 'b'
                print(f'El valor a {a} el valor b {b}')
                descifrado = descifrar(mensaje_cifrado, a, b)  # Desciframos el mensaje usando 'a' y 'b'
                resultados.append((a, b, descifrado))  # Añadimos el resultado a la lista de resultados
    return resultados

# Función para encontrar el inverso multiplicativo de 'a' modulo 'm'
# Si existe un número i tal que (a * i) mod m = 1, entonces i es el inverso multiplicativo de a mod m
def encontrar_inverso(a, m):
    for i in range(1, m):  
        if (a * i) % m == 1:
            return i
    return None
