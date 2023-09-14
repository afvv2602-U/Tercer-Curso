# main.py

import cifrado

def guardar_resultados(mensaje, mensaje_cifrado):
    with open("resultados.txt", "w") as archivo:
        archivo.write("Mensaje original: " + mensaje + "\n")
        archivo.write("Mensaje cifrado: " + mensaje_cifrado + "\n")
    print("Los resultados han sido escritos en 'resultados.txt'")

def guardar_fuerza_bruta(resultados):
    with open("resultados_fuerza_bruta.txt", "w") as archivo:
        for p, q, descifrado in resultados:
            archivo.write(f"Clave decimación: {p}, Clave desplazamiento: {q}\n")
            archivo.write("Mensaje descifrado: " + descifrado + "\n")
            archivo.write("="*50 + "\n")
    print("Los resultados han sido escritos en 'resultados_fuerza_bruta.txt'")

if __name__ == '__main__':
    mensaje = "LASCLAVESSSHOTORGANACCESOPRIVILEGIADOAMUCHOSSISTEMASINTERNOSAMENUDOESTASCLAVESNOTIENENFECHASDEVENCIMIENTOYSONDIFICILESDEMONITOREARSILASCLAVESSHSEREVELANOSEVENCOMPROMETIDOSLOSATACANTESPUEDENUSARLASPARAMOVERSELIBREMENTEDENTRODELAREADEMASACCESOFACILALASCLAVESSHALMACENADASENCOMPUTADORASOSERVIDORESFACILITAAQUELOSATACANTESSEDESPLACENLATERALMENTEDENTRODELAORGANIZACION"
    clave_decimacion = 17
    clave_desplazamiento = 19

    mensaje_cifrado = cifrado.cifrar(mensaje, clave_decimacion, clave_desplazamiento)
    guardar_resultados(mensaje, mensaje_cifrado)

    resultados = cifrado.fuerza_bruta(mensaje_cifrado)
    guardar_fuerza_bruta(resultados)
