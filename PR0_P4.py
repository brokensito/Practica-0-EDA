''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 4  
- EXPLICACIONES: 

Este programa integra varias funciones que manejan excepciones y registran errores en un archivo de texto. Se utiliza el módulo `datetime` para obtener la hora exacta en que ocurre un error y registrarlo en el archivo excepciones.txt. 

- La función imprimir_linea se emplea para mejorar la presentación en consola, permitiendo imprimir líneas decorativas con mensajes centrados. 
- div_cero(): Realiza la división entre dos números introducidos por el usuario, manejando excepciones por división entre cero y entradas no numéricas.
- cadena_texto(): Convierte una cadena de texto ingresada por el usuario a un número entero, manejando la excepción si la conversión no es posible.
- raiz(): Calcula la raíz cuadrada de un número proporcionado por el usuario, manejando la excepción si el número es negativo.

'''

from datetime import datetime  # Importamos datetime para manejar fechas y horas
import math  # Importamos math para utilizar funciones matemáticas como sqrt

def div_cero():
    """
    Función para realizar la división entre dos números, manejando excepciones
    para evitar divisiones entre cero y entradas no numéricas.
    """
    try: 
        # Solicitamos al usuario que introduzca los números para la división
        a = float(input("Introduzca el PRIMER número: "))
        b = float(input("Introduzca el SEGUNDO número: "))
        resultado = a / b  # Realizamos la división
        return resultado  # Devolvemos el resultado

    except ZeroDivisionError:
        # Maneja la excepción si se intenta dividir por cero
        print("\nNo se puede dividir por cero, inténtalo de nuevo.")
        errores("Error al dividir por cero")  # Registramos el error en el archivo

    except ValueError:
        # Maneja la excepción si la entrada no es un número válido
        print("\nLos argumentos de la función tienen que ser números, inténtalo de nuevo.")
        errores("Error al introducir un valor no numerico en la division")  # Registramos el error

def cadena_texto():
    """
    Función que convierte una cadena de texto a un número entero,
    manejando la excepción si la conversión no es posible.
    """
    cadena = input("Escriba la cadena a convertir a ENTERO: ")  # Solicitamos la cadena al usuario
    try:
        numero = int(cadena)  # Intentamos convertir la cadena a entero
        return numero  # Devolvemos el número convertido
        
    except ValueError:
        # Maneja la excepción si la cadena no puede convertirse a entero
        print("\nERROR: La cadena introducida no se puede convertir a entero. Intentalo de nuevo.\n")
        errores("No es posible convertir la cadena a entero.")  # Registramos el error

def raiz(): 
    """
    Función que calcula la raíz cuadrada de un número,
    manejando la excepción si el número es negativo.
    """
    try:
        # Solicitamos al usuario que introduzca el número
        numero = float(input("Introduce el número cuya raíz quieres calcular: "))
        
        if numero < 0:
            # Si el número es negativo, lanzamos una excepción
            raise ValueError("El numero no puede ser negativo.")
        
        resultado = math.sqrt(numero)  # Calculamos la raíz cuadrada

        return numero, resultado  # Devolvemos el número y su raíz cuadrada

    except ValueError as ve:
        # Maneja excepciones relacionadas con valores inválidos
        print(f"\nError: {ve}")
        errores(f"Error al calcular la raiz cuadrada: {ve}")  # Registramos el error

def errores(mensaje):
    """
    Función que registra mensajes de error en un archivo de texto,
    incluyendo la hora en que ocurrió el error.
    """
    # Obtenemos la hora actual en formato HH:MM:SS
    hora_actual = datetime.now().strftime('%H:%M:%S')
    try:
        # Abrimos el archivo en modo adjunto y escribimos el mensaje de error
        with open("excepciones.txt", "a") as archivo:
            archivo.write(f"{hora_actual} - Error: {mensaje}\n")

    except Exception as excepcion:
        # Maneja cualquier excepción que ocurra al intentar escribir en el archivo
        print(f"\nNo se pudo escribir en el archivo de registro: {excepcion}")

def imprimir_linea(estilo='-', longitud=50, mensaje=''):
    """
    Función que imprime una línea decorativa en la consola.
    Puede incluir un mensaje centrado entre el estilo especificado.
    """
    if mensaje:
        # Calculamos la longitud de los lados para centrar el mensaje
        linea = estilo * ((longitud - len(mensaje) - 2) // 2)
        print(f"\n{linea} {mensaje} {linea} \n") 

    else:
        # Imprimimos una línea continua si no hay mensaje
        print(f"\n{estilo * longitud} \n")

if __name__ == "__main__":

    continuar = True  # Variable para controlar el bucle principal

    while continuar:

        # Mostramos el menú de operaciones
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
            if divcero_usuario is not None:  # Verificamos si se obtuvo un resultado válido
                print(f"\nEl resultado de la división es: {divcero_usuario}")

        elif opcion == '2':
            imprimir_linea('-', mensaje=" Conversión de cadena a entero ")
            cadena_usuario = cadena_texto()
            if cadena_usuario is not None:
                print(f"\nLa cadena convertida a entero es: {cadena_usuario}")

        elif opcion == '3':
            imprimir_linea('-', mensaje=" Calcular raíz cuadrada ")
            resultado = raiz()
            if resultado:  # Verificamos si se obtuvo un resultado válido
                numero, raiz_cuadrada = resultado
                print(f"\nLa raíz cuadrada de {numero} es {raiz_cuadrada}")
                
        elif opcion == '4':
            print("\nGracias por usar el programa. ¡Hasta luego!")
            continuar = False  # Cambiamos la variable para salir del bucle

        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 4.")

    imprimir_linea('*', mensaje=" FIN DEL PROGRAMA ")
