# Definir alfabeto español
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Función para encontrar el inverso multiplicativo de 'a' modulo 'm'
def encontrar_inverso(a, m):
    for i in range(1, m):  # Iteramos desde 1 hasta m-1
        # Si i es el inverso multiplicativo de a modulo m
        if (a * i) % m == 1:
            return i  # Retornamos el inverso
    return None  # Si no existe inverso, retornamos None

# Función para descifrar un mensaje cifrado usando las claves p y q
def descifrar(mensaje_cifrado, p, q):
    descifrado = ""  # Inicializamos el mensaje descifrado
    inverso_p = encontrar_inverso(p, 27)  # Buscamos el inverso multiplicativo de p modulo 27
    
    # Iteramos sobre cada letra en el mensaje cifrado
    for letra in mensaje_cifrado.upper():
        # Si la letra está en nuestro alfabeto
        if letra in ALFABETO:
            C = ALFABETO.index(letra)  # Encontramos la posición de la letra en el alfabeto
            # Usamos la fórmula para descifrar la letra y la añadimos al mensaje descifrado
            M = (inverso_p * (C - q)) % 27
            descifrado += ALFABETO[M]
        else:
            # Para caracteres no presentes en ALFABETO, simplemente se añaden sin cambiar
            descifrado += letra
            
    return descifrado  # Retornamos el mensaje descifrado

# Función para descifrar un mensaje usando fuerza bruta
def fuerza_bruta(mensaje_cifrado):
    primos_menores_20 = [2, 3, 5, 7, 11, 13, 17, 19]  # Lista de números primos menores a 20
    resultados = []  # Lista para guardar los resultados

    # Iteramos sobre cada número primo en la lista
    for p in primos_menores_20:
        # Solo consideramos el número si tiene un inverso multiplicativo modulo 27
        if encontrar_inverso(p, 27):
            # Probamos cada combinación de p con otros números primos
            for q in primos_menores_20:
                # Desciframos el mensaje usando p y q
                descifrado = descifrar(mensaje_cifrado, p, q)
                # Añadimos el resultado a la lista de resultados
                resultados.append((p, q, descifrado))

    return resultados  # Retornamos los resultados

# Ejemplo de uso
mensaje_cifrado = "DETWETNTEQSKOSQWSKSWULPXSKOUZKTVTCTXCOSKTNNTCXKPNTOSPKHSCUMSGUPCFPXPKHSKECSGGTQPWKULUOTHUSNPSOPQQUQXTVSQUCXTKCPQ"

# Llamamos a la función de fuerza bruta con el mensaje cifrado
resultados = fuerza_bruta(mensaje_cifrado)

# Escribir resultados en archivo txt
with open("resultados_fuerza_bruta.txt", "w") as archivo:
    # Iteramos sobre cada resultado
    for p, q, descifrado in resultados:
        # Escribimos las claves y el mensaje descifrado en el archivo
        archivo.write(f"Clave decimación: {p}, Clave desplazamiento: {q}\n")
        archivo.write("Mensaje descifrado: " + descifrado + "\n")
        archivo.write("="*50 + "\n")  # Añadimos un separador

# Mensaje final para informar al usuario
print("Los resultados han sido escritos en 'resultados_fuerza_bruta.txt'")
