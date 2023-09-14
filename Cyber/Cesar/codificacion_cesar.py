def cifrado_cesar(mensaje, desplazamiento):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!. '
    
    cifrado = 'SzN32rs5N12Ns6N81N0srw2;Ns6N81Ntw1Ns1N6wN0w602LM'
    
    for caracter in mensaje:
        if caracter in alfabeto: 
            posicion_actual = alfabeto.index(caracter)
            nueva_posicion = (posicion_actual + desplazamiento) % len(alfabeto)
            cifrado += alfabeto[nueva_posicion]
        else:
            cifrado += caracter  # Si el caracter no está en el alfabeto, lo añadimos sin modificar

    return cifrado

# Uso del código
mensaje = "El poder no es un medio; es un fin en si mismo!." 
desplazamiento = 14  # Puedes cambiar el número 3 por el desplazamiento que desees

resultado = cifrado_cesar(mensaje, desplazamiento)
print("Mensaje cifrado:", resultado)

