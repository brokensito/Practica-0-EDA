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

# Se puede hacer de maneras diferentes pero preguntar si podemos usar la funcion enumerate para esto o suena muy cantoso
def buscar(palabra):

    try:
        with open("archivo.txt", "r" ) as archivo:
            lineas = archivo.readlines()

        encontrado = []
        indices = []

        for linea in lineas:
            if palabra.lower() in linea.lower():
                encontrado.append(linea)

        for palabras in encontrado:
            indices.append(lineas.index(palabras)+1)
        
        if indices:
            print(f" Se encontro la palabra {palabra} en las lineas: {indices}")

        else:
            print(f"No se encontro la palabra {palabra}")

    except FileNotFoundError:
        print("ERROR: el archivo no existe")

    except Exception as excepcion:
        print(f"Ha ocurrido un ERROR: {excepcion}")

if __name__=="__main__":

    buscar("llamo")
    




