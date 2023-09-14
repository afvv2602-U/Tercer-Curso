# Importamos el módulo 'string' para tener acceso a cadenas predefinidas útiles.
import string

# Esta función decodifica un mensaje encriptado usando una variante de la Tabla de Trithemius.
def tritemius_decrypt(ciphertext):
    # Establecemos el alfabeto en mayúsculas para nuestro cifrado.
    alphabet = string.ascii_uppercase
    # Creamos una lista vacía para almacenar el mensaje descifrado.
    plaintext = []

    # Enumeramos sobre el texto cifrado. 'index' será el índice del carácter y 'char' el carácter en sí.
    for index, char in enumerate(ciphertext):
        # Comprobamos si el carácter está en nuestro alfabeto (ignoramos números, símbolos, etc.).
        if char in alphabet:
            # Obtenemos la posición actual del carácter en el alfabeto.
            original_position = alphabet.index(char)
            # Calculamos la posición descifrada usando la fórmula del desplazamiento variable de Trithemius.
            decrypted_position = (original_position - index) % len(alphabet)
            # Agregamos el carácter descifrado a nuestra lista.
            plaintext.append(alphabet[decrypted_position])
        else:
            # Si el carácter no está en el alfabeto (ejemplo: un espacio o símbolo), simplemente lo agregamos sin modificar.
            plaintext.append(char)

    # Convertimos nuestra lista en una cadena y la retornamos.
    return ''.join(plaintext)

# Punto de entrada para nuestro script.
if __name__ == '__main__':
    # Definimos los mensajes cifrados que queremos descifrar.
    message1 = "QVGRGZXYMBSYAZCCYKGKCOWJMREMWVSIKJTJFPEGQTHKAYCXWAMR"
    message2 = "QVGRGZXYMBSWMFQAQMWLMNDPMMRFXHPFJHAXMZYCFDCVLBXVO"

    # Desciframos los mensajes usando la función definida anteriormente.
    decrypted1 = tritemius_decrypt(message1)
    decrypted2 = tritemius_decrypt(message2)

    # Escribimos los resultados descifrados en un archivo llamado 'decrypted_results.txt'.
    with open("decrypted_results.txt", "w") as file:
        file.write("Desencriptación del mensaje 1:\n")
        file.write(decrypted1 + "\n")

        file.write("\nDesencriptación del mensaje 2:\n")
        file.write(decrypted2 + "\n")
