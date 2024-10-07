''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 4  
- EXPLICACIONES: 


'''
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
        print("La cadena introducida no se puede convertir a entero. Intentelo de nuevo.")
        errores("No es posible convertir la cadena a entero")
        return cadena_texto()
    

def raiz(): # Preguntar si tambien tengo que manejar la excepcion si el numero es un string o algo del estilo 
    numero = float(input("\nIntroduce el numero cuya raiz quieres calcular: "))

    try:
        if numero <0:
            raise TypeError
        else:
            return math.sqrt(numero)
        
    except ValueError:
        print("El argumento introducido tiene que ser un numero, intentelo de nuevo. ")
        errores("Introducir un string en vez de un numero")
        raiz()
        
    except TypeError:
        print("\n El numero introducido no puede ser MENOR o IGUAL a  CERO")
        errores("Introducir un valor negativo en una raiz")
        return raiz()
    
# Tambien preguntar si tenemoso que poner la fecha en la que se ha cometido el error o tambien sonaria muy cantoso
def errores(mensaje):
    with open("excepciones.txt","a") as archivo:
        archivo.write(f"Error: {mensaje}\n")

# Preguntar si hay que hacer mas control de excepciones o no
if __name__=="__main__":
    div_cero()
    cadena_texto()
    raiz()
    




        





