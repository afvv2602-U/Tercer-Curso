# Se importa la biblioteca hashlib, que proporciona algoritmos de hash para cadenas de texto.
import hashlib

def main():
    # Se crea un nuevo objeto hash usando el algoritmo SHA-256.
    m = hashlib.sha256()

    # Se actualiza el objeto hash con el fragmento de texto "Nobody inspects".
    m.update(b"Nobody inspects")

    # Se actualiza el objeto hash con el fragmento de texto " the spammish repetition". 
    # Nota: Es importante mencionar que al usar la función update consecutivamente, 
    # es equivalente a hacer un update con la cadena completa "Nobody inspects the spammish repetition".
    m.update(b" the spammish repetition")

    # Se obtiene el valor hash en formato de bytes. 
    # Aunque esta línea está en el código, su resultado no se utiliza ni se muestra.
    m.digest()

    # Se imprime la representación hexadecimal del valor hash.
    print(m.hexdigest())

if __name__ == "__main__":
    main()