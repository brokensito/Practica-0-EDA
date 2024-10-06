''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 4  
- EXPLICACIONES: 

Ejercicios 2,6 


2. Escribe un programa que lea todo el contenido del archivo y lo muestre en
pantalla.

6. Escribe un programa que busque una palabra específica en un archivo de
texto. Si la encuentra, muestra en qué líneas aparece.


'''

def leer(archivo):
    try:
        with open(archivo, "r" ) as archivo:
            return archivo
        
    except FileNotFoundError:
        print("ERROR: el archivo no existe")

    except Exception as excepcion:
        print(f"Ha ocurrido un ERROR: {excepcion}")

def buscar(nombre_archivo):

    try:
        with open(nombre_archivo, "r" ) as archivo:
            
            lineas = archivo.readlines()
            print(lineas)

            

        
    except FileNotFoundError:
        print("ERROR: el archivo no existe")

    except Exception as excepcion:
        print(f"Ha ocurrido un ERROR: {excepcion}")

if __name__=="__main__":

    nombre = input("Introduce el nombre del archivo con la extension que le corresponde ")

    buscar(nombre)




