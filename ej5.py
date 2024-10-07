''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 5 
- EXPLICACIONES: 

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
# Tambien preguntar si tenemoso que poner la fecha en la que se ha cometido el error o tambien sonaria muy cantoso
def buscar(archivo_usuario, palabra):

    try:
        with open(archivo_usuario, "r" ) as archivo:
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

    archivo = input("Escriba el nombre del archivo con su extension: ")

    leer(archivo)
    buscar(archivo, "david") # Esta en el archivo.txt de esta misma carpeta (por probar)
    




