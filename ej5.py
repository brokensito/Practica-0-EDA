
'''
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 5 
- EXPLICACIONES: 

Incluir en un mismo programa la funcionalidad combinada de los Ejercicios 2 y 6 de la 
hoja de ejercicios 02_5_Ejercicios.pdf de la sección Python de los materiales de la 
asignatura.

2. Escribe un programa que lea todo el contenido del archivo y lo muestre en pantalla.

6. Escribe un programa que busque una palabra específica en un archivo de texto. Si la encuentra, muestra en qué líneas aparece.
'''

def leer(archivo):
    """
    Función que lee todo el contenido de un archivo y lo muestra en pantalla.
    """
    try:
        with open(archivo, "r") as arc:
            contenido = arc.read()  # Lee todo el contenido del archivo
            print("\nContenido del archivo:\n")
            print(contenido)  # Imprime el contenido en pantalla

    except FileNotFoundError:
        # Maneja la excepción si el archivo no existe
        print("ERROR: El archivo no existe.")

    except Exception as excepcion:
        # Maneja cualquier otra excepción que pueda ocurrir
        print(f"Ha ocurrido un ERROR: {excepcion}")

def buscar(archivo_usuario, palabra):
    """
    Función que busca una palabra específica en un archivo de texto y muestra en qué líneas aparece.
    """
    try:
        with open(archivo_usuario, "r") as archivo:
            lineas = archivo.readlines()  # Lee todas las líneas del archivo

        indices = []
        numero_linea = 1  # Inicia el contador de líneas en 1

        # Recorre cada línea del archivo
        for linea in lineas:
            # Verifica si la palabra está en la línea, sin importar mayúsculas o minúsculas
            if palabra.lower() in linea.lower():
                indices.append(numero_linea)  # Agrega el número de línea a la lista

            numero_linea += 1  # Incrementa el contador de líneas

        if indices:
            # Si se encontraron ocurrencias, las muestra al usuario
            print(f"\nSe encontró la palabra '{palabra}' en las líneas: {indices}")
        else:
            # Si no se encontraron ocurrencias, informa al usuario
            print(f"\nNo se encontró la palabra '{palabra}' en el archivo.")

    except FileNotFoundError:
        # Maneja la excepción si el archivo no existe
        print("ERROR: El archivo no existe.")

    except Exception as excepcion:
        # Maneja cualquier otra excepción que pueda ocurrir
        print(f"Ha ocurrido un ERROR: {excepcion}")

if __name__ == "__main__":
    # Solicita al usuario el nombre del archivo
    archivo = input("\nEscriba el nombre del archivo con su extensión: ")

    while True:
        # Muestra el menú de opciones al usuario
        print("\n¿Qué desea hacer?")
        print("1. Leer todo el contenido del archivo y mostrarlo en pantalla")
        print("2. Buscar una palabra en el archivo y mostrar en qué líneas aparece")
        print("3. Salir")
        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            # Llama a la función leer() para mostrar el contenido del archivo
            leer(archivo)

        elif opcion == "2":
            # Solicita la palabra a buscar y llama a la función buscar()
            palabra = input("Ingrese la palabra que desea buscar: ")
            buscar(archivo, palabra)

        elif opcion == "3":
            # Sale del programa
            print("Saliendo del programa.")
            break

        else:
            # Maneja entradas no válidas en el menú
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")


    




