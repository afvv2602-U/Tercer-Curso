import datetime

def descifrar_cesar_con_desplazamiento(mensaje, desplazamiento):
    alfabeto = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decodificado = ''

    for caracter in mensaje:
        if caracter in alfabeto:
            posicion_actual = alfabeto.index(caracter)
            nueva_posicion = (posicion_actual - desplazamiento) % len(alfabeto)
            decodificado += alfabeto[nueva_posicion]
        else:
            decodificado += caracter  # Si el carácter no está en el alfabeto, lo añadimos sin modificar

    return decodificado

# Uso del código
mensaje_cifrado = """SLLYOHZ!HLSMPUHS&S"LNVLQLJ"!HYSHHZPN"PLU!LZHJJPVULZA
O!!WZA66#LUHMP5JVT6ISVN6>4KH!H4IYLHJOLZ4JH"ZLK4O"THU4LYYVY4KPK4LUJY&W!PVU4WSH&4YVSL6
JHSJ"SHYSHZ"THHSNLIYHPJHKLSHZJPMYHZKLSHSPULHHU!LYPVY
HUV!HYSHLUSHWP'HYYHPKLU!PMPJHUKVLSU"TLYVKLNY"WV
PNUVYHYSVZKVZWHZVZHU!LYPVYLZ&OHJLY"UYLZ"TLUKLSWVZ!JP!HKVLUSH"YSHU!LYPVY"""

# Generar el nombre del archivo basado en la fecha y hora actuales
nombre_archivo = 'descifrado_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.txt'

with open(nombre_archivo, 'w') as f:
    for desplazamiento in range(len(' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
        mensaje_descifrado = descifrar_cesar_con_desplazamiento(mensaje_cifrado, desplazamiento)
        f.write(f"Desplazamiento {desplazamiento}:\n{mensaje_descifrado}\n\n")
        print(f"El mensaje descifrado con desplazamiento {desplazamiento} ha sido añadido al archivo '{nombre_archivo}'")
