''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 3  
- EXPLICACIONES:

- Programa que implementa una calculadora con diferentes funcionalidades, utilizando un menu para elegir las opciones y controlando las excepciones si la entrada de numeros no es valida para la calculadora.

'''

def calculadora(num1, num2, operacion):
    """
    Función que simula una calculadora básica realizando operaciones de suma, resta,
    multiplicación y división entre dos números.
    """

    if operacion == "1":
        return num1 + num2  # Realiza la suma
    
    elif operacion == "2":
        return num1 - num2  # Realiza la resta
    
    elif operacion == "3":
        return num1 * num2  # Realiza la multiplicación
    
    elif operacion == "4":

        if num2 != 0:
            return num1 / num2  # Realiza la división si el divisor no es cero
        else:
            print("Error: División por cero")
            return None  # Retorna None si hay división por cero
        
    else:
        print("La operación no existe, inténtalo de nuevo.")
        return None  # Retorna None si la operación no es válida

if __name__ == "__main__":

    print("\n********************** CALCULADORA **************************")

    continuar = True  # Variable para controlar el bucle principal

    while continuar:
        try:
            # Solicita al usuario los dos números para la operación
            numero1 = float(input("\nEscribe el primer número: "))
            numero2 = float(input("Escribe el segundo número: "))
            # Muestra el menú de operaciones disponibles
            operacion_usuario = input("\n¿Qué operación quieres hacer?\n\t1) Suma\n\t2) Resta\n\t3) Multiplicación\n\t4) División\n\nRespuesta: ")
            # Llama a la función calculadora con los números y la operación seleccionada
            resultado = calculadora(numero1, numero2, operacion_usuario)

            if resultado is not None:
                # Muestra el resultado si es válido
                print(f"\nEl resultado es: {resultado}")

        except Exception as excepcion:
            # Maneja cualquier excepción que ocurra durante la entrada de datos
            print(f"ERROR ({excepcion}): Entrada inválida, por favor ingresa números válidos.")

        # Pregunta al usuario si desea realizar otra operación
        opcion = input("\n¿Quieres realizar otra operación? (si/no): ").lower()

        if opcion != 'si':
            continuar = False  # Cambia la variable para salir del bucle

    print("\n********************** FIN DEL PROGRAMA ************************\n")

