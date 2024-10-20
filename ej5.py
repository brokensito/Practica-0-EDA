''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 5 
- EXPLICACIONES: 

Incluir en un mismo programa la funcionalidad combinada de los Ejercicios 2 y 6 de la 
hoja de ejercicios 02_5_Ejercicios.pdf de la sección Python de los materiales de la 
asignatura.


2. Escribe un programa que lea todo el contenido del archivo y lo muestre en
pantalla

6. Escribe un programa que busque una palabra específica en un archivo de
texto. Si la encuentra, muestra en qué líneas aparece.

'''

'''
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25
- AUTOR: David Sanz Fuertes
- EJERCICIO: 5
- EXPLICACIONES:

Incluir en un mismo programa la funcionalidad combinada de los Ejercicios 2 y 6 de la
hoja de ejercicios 02_5_Ejercicios.pdf de la sección Python de los materiales de la
asignatura.

2. Escribe un programa que lea todo el contenido del archivo y lo muestre en pantalla.

6. Escribe un programa que busque una palabra específica en un archivo de
texto. Si la encuentra, muestra en qué líneas aparece.
'''

def leer(archivo):
    try:
        with open(archivo, "r") as arc:
            contenido = arc.read()
            print("\nContenido del archivo:\n")
            print(contenido)

    except FileNotFoundError:
        print("ERROR: El archivo no existe.")

    except Exception as excepcion:
        print(f"Ha ocurrido un ERROR: {excepcion}")

def buscar(archivo_usuario, palabra):
    try:
        with open(archivo_usuario, "r") as archivo:
            lineas = archivo.readlines()

        indices = []
        numero_linea = 1  # Iniciamos el contador de líneas en 1

        for linea in lineas:

            if palabra.lower() in linea.lower():
                indices.append(numero_linea)
                
            numero_linea += 1  # Incrementamos el contador en cada iteración

        if indices:
            print(f"\nSe encontró la palabra '{palabra}' en las líneas: {indices}")

        else:
            print(f"\nNo se encontró la palabra '{palabra}' en el archivo.")

    except FileNotFoundError:
        print("ERROR: El archivo no existe.")

    except Exception as excepcion:
        print(f"Ha ocurrido un ERROR: {excepcion}")

if __name__ == "__main__":

    archivo = input("\nEscriba el nombre del archivo con su extensión: ")

    while True:
        print("\n¿Qué desea hacer?")
        print("1. Leer todo el contenido del archivo y mostrarlo en pantalla")
        print("2. Buscar una palabra en el archivo y mostrar en qué líneas aparece")
        print("3. Salir")
        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            leer(archivo)

        elif opcion == "2":
            palabra = input("Ingrese la palabra que desea buscar: ")
            buscar(archivo, palabra)

        elif opcion == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

    




