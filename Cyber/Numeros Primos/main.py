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

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje usando fuerza bruta")
        print("3. Salir")
        eleccion = input("Ingrese su elección: ")

        if eleccion == "1":
            mensaje = input("Ingrese el mensaje a cifrar: ")
            clave_decimacion = int(input("Ingrese la clave de decimación: "))
            clave_desplazamiento = int(input("Ingrese la clave de desplazamiento: "))
            
            mensaje_cifrado = cifrado.cifrar(mensaje, clave_decimacion, clave_desplazamiento)
            guardar_resultados(mensaje, mensaje_cifrado)
        
        elif eleccion == "2":
            mensaje_cifrado = input("Ingrese el mensaje cifrado a descifrar: ")
            resultados = cifrado.fuerza_bruta(mensaje_cifrado)
            guardar_fuerza_bruta(resultados)
        
        elif eleccion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Elección inválida. Intente nuevamente.")

if __name__ == '__main__':
    menu()
