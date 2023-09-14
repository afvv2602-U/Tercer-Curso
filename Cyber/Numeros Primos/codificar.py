# Definir alfabeto español
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrar(mensaje, p, q):
    cifrado = ""
    
    for letra in mensaje.upper():
        if letra in ALFABETO:
            M = ALFABETO.index(letra)
            C = (p * M + q) % 27
            cifrado += ALFABETO[C]
        else:
            cifrado += letra  # Para caracteres no presentes en ALFABETO, simplemente se añaden sin cambiar
            
    return cifrado

# Ejemplo de uso
mensaje = "LASCLAVESSSHOTORGANACCESOPRIVILEGIADOAMUCHOSSISTEMASINTERNOSAMENUDOESTASCLAVESNOTIENENFECHASDEVENCIMIENTOYSONDIFICILESDEMONITOREARSILASCLAVESSHSEREVELANOSEVENCOMPROMETIDOSLOSATACANTESPUEDENUSARLASPARAMOVERSELIBREMENTEDENTRODELAREADEMASACCESOFACILALASCLAVESSHALMACENADASENCOMPUTADORASOSERVIDORESFACILITAAQUELOSATACANTESSEDESPLACENLATERALMENTEDENTRODELAORGANIZACION"
clave_decimacion = 17
clave_desplazamiento = 19
mensaje_cifrado = cifrar(mensaje, clave_decimacion, clave_desplazamiento)

# Escribir resultados en archivo txt
with open("resultados.txt", "w") as archivo:
    archivo.write("Mensaje original: " + mensaje + "\n")
    archivo.write("Mensaje cifrado: " + mensaje_cifrado + "\n")

print("Los resultados han sido escritos en 'resultados.txt'")
