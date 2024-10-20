''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 4  
- EXPLICACIONES: 

Incluir en un mismo programa la funcionalidad combinada de los Ejercicios 19, 1, 2 y 14 
de la hoja de ejercicios 02_4_Ejercicios.pdf de la sección Python de los materiales de 
la asignatura. El ejercicio 19 integra a los otros tres.

Ej 19. Registro de errores en archivo: Crea un programa que intente realizar varias
operaciones, maneje las excepciones, y guarde los mensajes de error en un
archivo de texto.

1. División entre cero: Crea una función que divida dos números e implementa un
manejo de excepciones para evitar divisiones entre cero.

2. Conversión de cadena a entero: Escribe una función que convierta una cadena
a un número entero. Maneja la excepción si la conversión no es posible.

14. Excepción al calcular raíz cuadrada: Escribe una función que calcule la raíz
cuadrada de un número, pero maneja la excepción si el número es negativo.



'''

from datetime import datetime
import math

def div_cero():

    try: 
        a = float(input("Introduzca el PRIMER número: "))
        b = float(input("Introduzca el SEGUNDO número: "))
        resultado = a / b
        return resultado

    except ZeroDivisionError:
        print("\nNo se puede dividir por cero, inténtalo de nuevo.")
        errores("Error al dividir por cero")

    except ValueError:
        print("\nLos argumentos de la función tienen que ser números, inténtalo de nuevo.")
        errores("Error al introducir un valor no numérico en la división")

def cadena_texto():

    cadena = input("Escriba la cadena a convertir a ENTERO: ")
    try:
        numero = int(cadena)
        return numero
        
    except ValueError:
        print("\nERROR: La cadena introducida no se puede convertir a entero. Inténtalo de nuevo.\n")
        errores("No es posible convertir la cadena a entero.")

def raiz(): 
    
    try:
        numero = float(input("Introduce el número cuya raíz quieres calcular: "))
        
        if numero < 0:
            raise ValueError("El número no puede ser negativo.")
        
        resultado = math.sqrt(numero)

        return numero, resultado

    except ValueError as ve:
        print(f"\nError: {ve}")
        errores(f"Error al calcular la raíz cuadrada: {ve}")

def errores(mensaje):
    hora_actual = datetime.now().strftime('%H:%M:%S') #Ya que la funcion datetime.now() nos da hasta los microsegundos, tenemos que coger unicamente las horas, minutos y segundos donde se cometio el error...
    try:
        with open("excepciones.txt", "a") as archivo:
            archivo.write(f"{hora_actual} - Error: {mensaje}\n")

    except Exception as excepcion:
        print(f"\nNo se pudo escribir en el archivo de registro: {excepcion}")


def imprimir_linea(estilo='-', longitud=50, mensaje=''):

    if mensaje:
        linea = estilo * ((longitud - len(mensaje) - 2) // 2)
        print(f"\n{linea} {mensaje} {linea} \n") 

    else:
        print(f"\n{estilo * longitud} \n")

if __name__ == "__main__":

    continuar = True

    while continuar:

        imprimir_linea('*', mensaje=" MENÚ DE OPERACIONES ")

        print("Seleccione una opción:")
        print("1) División entre dos números")
        print("2) Conversión de cadena a entero")
        print("3) Calcular raíz cuadrada")
        print("4) Salir")

        opcion = input("\nOpción seleccionada: ")

        if opcion == '1':
            imprimir_linea('-', mensaje=" División entre dos números ")
            divcero_usuario = div_cero()
            print(f"\nEl resultado de la división es: {divcero_usuario}")

        elif opcion == '2':
            imprimir_linea('-', mensaje=" Conversión de cadena a entero ")
            cadena_usuario = cadena_texto()
            print(f"\nLa cadena convertida a entero es: {cadena_usuario}")

        elif opcion == '3':
            imprimir_linea('-', mensaje=" Calcular raíz cuadrada ")
            numero, resultado = raiz()
            print(f"\nLa raíz cuadrada de {numero} es {resultado}")
            
        elif opcion == '4':
            print("\nGracias por usar el programa. ¡Hasta luego!")
            continuar = False

        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 4.")

    imprimir_linea('*', mensaje=" FIN DEL PROGRAMA ")



        





