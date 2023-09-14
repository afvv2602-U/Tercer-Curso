# cifrado.py

# Definir alfabeto español
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Función para encontrar el inverso multiplicativo de 'a' modulo 'm'
def encontrar_inverso(a, m):
    for i in range(1, m):  # Iteramos desde 1 hasta m-1
        # Si i es el inverso multiplicativo de a modulo m
        if (a * i) % m == 1:
            return i  # Retornamos el inverso
    return None  # Si no existe inverso, retornamos None

def cifrar(mensaje, clave_decimacion, clave_desplazamiento):
    cifrado = ""
    for letra in mensaje.upper():
        if letra in ALFABETO:
            M = ALFABETO.index(letra)
            C = (clave_decimacion * M + clave_desplazamiento) % 27
            cifrado += ALFABETO[C]
        else:
            cifrado += letra  # Para caracteres no presentes en ALFABETO, simplemente se añaden sin cambiar
    return cifrado

def descifrar(mensaje_cifrado, p, q):
    descifrado = ""  # Inicializamos el mensaje descifrado
    inverso_p = encontrar_inverso(p, 27)  # Buscamos el inverso multiplicativo de p modulo 27
    
    for letra in mensaje_cifrado.upper():
        if letra in ALFABETO:
            C = ALFABETO.index(letra)
            M = (inverso_p * (C - q)) % 27
            descifrado += ALFABETO[M]
        else:
            descifrado += letra
    return descifrado

def fuerza_bruta(mensaje_cifrado):
    primos_menores_20 = [2, 3, 5, 7, 11, 13, 17, 19]  
    resultados = []

    for p in primos_menores_20:
        if encontrar_inverso(p, 27):
            for q in primos_menores_20:
                descifrado = descifrar(mensaje_cifrado, p, q)
                resultados.append((p, q, descifrado))
    return resultados
