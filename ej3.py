''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 3  
- EXPLICACIONES: 


'''

import os

def calculadora(num1, num2, operacion):
    if operacion == "1":
        return num1+num2
    
    elif operacion == "2":
        return num1-num2
    
    elif operacion == "3":
        return num1*num2
    
    elif operacion == "4":
        return num1/num2
    
    else:
        print("La operacion no existe, intentalo de nuevo")
        operacion = input("Escribe la operacion de nuevo: ")
        return calculadora(num1, num2, operacion)

if __name__=="__main__":

    print("\n********************** CALCULADORA **************************")

    var = True

    while var:
        numero1 = float(input("\nEscribe el primer numero: "))
        numero2 = float(input("\nEscribe el segundo numero:"))
        operacion_usuario = input("\nQue operacion quieres hacer:\n\t1) Suma \n\t2) Resta  \n\t3) Multiplicacion \n\t4) Division \n\nRespuesta: ")
        resultado = calculadora(numero1, numero2, operacion_usuario)
        print(f"\nEl resultado es: {resultado} ")

        continuar = input("\nQuieres salir del programa (1) o continuar con otra operacion (2)?")
        if continuar:
            var = False
        else: 
            continue

    print("********************** FIN DEL PROGRAMA ************************")
    os.system("cls")



