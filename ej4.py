''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 4  
- EXPLICACIONES: 

Ejercicios 19, 1, 2, 14 

El ejercicio 19 integra a los otros tres

20. Registro de errores en archivo: Crea un programa que intente realizar varias
operaciones, maneje las excepciones, y guarde los mensajes de error en un
archivo de texto.

1. División entre cero: Crea una función que divida dos números e implementa un
manejo de excepciones para evitar divisiones entre cero

2. Conversión de cadena a entero: Escribe una función que convierta una cadena
a un número entero. Maneja la excepción si la conversión no es posible.

14. Excepción al calcular raíz cuadrada: Escribe una función que calcule la raíz
cuadrada de un número, pero maneja la excepción si el número es negativo.

'''
import math

def div_cero():

    a = float(input("Introduzca el PRIMER numero: \n"))
    b = float(input("Introduzca el SEGUNDO numero: \n "))

    try: 
        resultado = a/b
        return resultado
    
    except ZeroDivisionError:
        print("No se puede dividir por cero, intentalo de nuevo.")
        errores("Error al dividir por 0")
        return div_cero()



def cadena_texto():

    cadena = input("Escriba la cadena a convertir a ENTERO: ")

    try:
        cadena = int(cadena)
        return cadena

    except ValueError:
        print("La cadena introducida no se puede convertir a entero. Intentelo de nuevo.")
        errores("No es posible convertir la cadena a entero")
        return cadena_texto()
    

def raiz(): # Preguntar si tambien tengo que manejar la excepcion si el numero es un string o algo del estilo 
    numero = float(input("\nIntroduce el numero cuya raiz quieres calcular: "))

    try:
        if numero <0:
            print("\n El numero introducido no puede ser MENOR o IGUAL a  CERO")
            errores("Introducir un valor negativo en una raiz")
            raise ValueError
        else:
            return math.sqrt(numero)
    except ValueError:
        print("\nIntentelo de nuevo...")
        return raiz()

def errores(mensaje):
    with open("excepciones.txt","a") as archivo:
        # preguntar si tambien tenemos que poner la fecha en la que se cometio el error o que hacer
        archivo.write(f"Error: {mensaje}\n")

# Preguntar si hay que hacer mas control de excepciones o no
if __name__=="__main__":
    div_cero()
    cadena_texto/()
    raiz()

    




        





