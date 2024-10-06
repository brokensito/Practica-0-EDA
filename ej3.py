''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 3  
- EXPLICACIONES: 

20. Calculadora simple: Crea una función que simule una calculadora básica. La
función debe aceptar dos números y un operador (suma, resta, multiplicación
o división) y devolver el resultado.
'''


# Preguntar como tengo que hacer la funcion multiplicacion
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
        print("La operacion no existe, intenalo de nuevo")
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

    print(calculadora(num1=3,num2=4, operacion="division"))

