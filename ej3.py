''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 3  
- EXPLICACIONES:

Calculadora simple: Crea una función que simule una calculadora básica. La
función debe aceptar dos números y un operador (suma, resta, multiplicación
o división) y devolver el resultado.


'''

def calculadora(num1, num2, operacion):

    if operacion == "1":
        return num1 + num2
    
    elif operacion == "2":
        return num1 - num2
    
    elif operacion == "3":
        return num1 * num2
    
    elif operacion == "4":

        if num2 != 0:
            return num1 / num2
        
        else:
            print("Error: División por cero")
            return None
        
    else:
        print("La operación no existe, inténtalo de nuevo.")
        return None

if __name__ == "__main__":

    print("\n********************** CALCULADORA **************************")

    continuar = True

    while continuar:

        try:
            numero1 = float(input("\nEscribe el primer número: "))
            numero2 = float(input("Escribe el segundo número: "))
            operacion_usuario = input("\n¿Qué operación quieres hacer?\n\t1) Suma\n\t2) Resta\n\t3) Multiplicación\n\t4) División\n\nRespuesta: ")
            resultado = calculadora(numero1, numero2, operacion_usuario)

            if resultado is not None:
                print(f"\nEl resultado es: {resultado}")

        except Exception as excepcion:
            print(f"ERROR ({excepcion}):Entrada inválida, por favor ingresa números válidos.")

        opcion = input("\n¿Quieres realizar otra operación? (si/no): ").lower()
        if opcion != 'si':
            continuar = False

    print("\n********************** FIN DEL PROGRAMA ************************\n")

