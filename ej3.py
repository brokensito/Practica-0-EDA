''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 3  
- EXPLICACIONES: 


'''


def calculadora(num1, num2, operacion):
    if operacion.lower() == "suma":
        return suma(num1,num2)
    
    elif operacion.lower() == "resta":
        return resta(num1,num2)
    
    elif operacion.lower() == "multiplicacion":
        return multiplicacion(num1,num2)
    
    elif operacion.lower() == "division":
        return division(num1,num2)
    else:
        print("La operacion no existe, intentalo de nuevo")
        operacion = input("Escribe la operacion de nuevo: ")
        return calculadora(num1, num2, operacion)

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicacion(num1, num2):
    return num1*num2

def division(num1, num2):
    return num1/num2

if __name__=="__main__":

    try:
        numero1 = float(input("Escribe el primer numero: "))
        numero2 = float(input("Escribe el segundo numero:"))
        operacion_usuario = input("Escribe el nombre de la operacion (suma, resta, multiplicacion, division): ")

    except Exception as excepcion:
        print(f"ERROR: ha habido un error en el programa. ")

    
    calculadora(numero1, numero2, operacion_usuario)

