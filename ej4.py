''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 4  
- EXPLICACIONES: 


'''
import os
from datetime import datetime
import math

def div_cero():

    try: 
        a = float(input("Introduzca el PRIMER numero: \n"))
        b = float(input("Introduzca el SEGUNDO numero: \n "))
        resultado = a/b
        return resultado
    
    except ZeroDivisionError:
        print("No se puede dividir por cero, intentalo de nuevo.")
        errores("Error al dividir por 0")
        return div_cero()
    
    except ValueError:
        print("Los argumentos de la funcion tienen que ser numeros, intentalo de nuevo")
        errores("Error al introducir string en vez de numero")
        return div_cero()



def cadena_texto():

    cadena = input("Escriba la cadena a convertir a ENTERO: ")

    try:
        cadena = int(cadena)
        return cadena

    except ValueError:
        print("ERROR: La cadena introducida no se puede convertir a entero. Intentelo de nuevo.\n")
        errores("No es posible convertir la cadena a entero.")
        return cadena_texto()
    

def raiz(): 
    numero = float(input("\nIntroduce el numero cuya raiz quieres calcular: "))

    try:
        if numero <0:
            raise TypeError
        else:
            return math.sqrt(numero)
        
    except ValueError:
        print("\nEl argumento introducido tiene que ser un numero, intentelo de nuevo. ")
        errores("Introducir un string en vez de un numero")
        raiz()
        
    except TypeError:
        print("\n El numero introducido no puede ser MENOR o IGUAL a  CERO")
        errores("Introducir un valor negativo en una raiz")
        return raiz()
    
def errores(mensaje):
    with open("excepciones.txt","a") as archivo:
        archivo.write(f"{datetime.now()} Error: {mensaje}\n")

def imprimir_linea(estilo='-', longitud=50, mensaje=''):
    if mensaje:
        linea = estilo * ((longitud - len(mensaje) - 2) // 2)
        print(f"{linea} {mensaje} {linea}")
    else:
        print(estilo * longitud)

if __name__=="__main__":
    print("**********************************************************")
    print("\n\tPrograma para dividir dos numeros (con excepciones)")
    div_cero()
    

    
    print("**********************************************************")
    print("\n\tPrograma para convertir una cadena a entero.")
    cadena_texto()
    raiz()



        





