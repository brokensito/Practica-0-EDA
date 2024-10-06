''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 1  
- EXPLICACIONES: 


** mencionar el modulo datetime


20. Pide al usuario que ingrese una contraseña. Si la contraseña es 'python123',
imprime 'Acceso concedido'. Si no, imprime 'Acceso denegado'.

16.Pide al usuario que ingrese su edad. Si es mayor de 18, imprime 'Eres mayor
de edad'. Si no, imprime 'Eres menor de edad'

19. Pide al usuario que ingrese su altura en metros. Si la altura es mayor a 1.70,
imprime 'Eres alto'. Si es menor o igual a 1.70, imprime 'Eres de estatura
promedio'.

25. Pide al usuario que ingrese su año de nacimiento. Calcula su edad en base al
año actual y muestra si la persona es mayor o menor de 30 años --> usar datetime

'''

from datetime import date

def acceso(contra):
    if contra == "python123":
        print("Acceso concedido.")
        return True
    else:
        print("Acceso denegado.")
        return False
    
def edad(numero):
    if numero >=18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

def altura(numero):
    if numero > 1.7:
        print("Eres alto.")
    else:
        print("Eres de estatura promedio.")

def nacimiento(numero):
    actual = date.today().year # Esto tengo que comentarlo despues
    resultado = numero - actual
    return resultado

if __name__=="__main__":


# Hay que hacer control de excepciones con la edad --> ver cuando es negativo o es 0

# "" con la altura --> ver cuando es 0 o negativo

# "" con el nacimiento --> hacer un if al final para ver cuando es mayor o menor que 30

    var = False

    while var == False:
        contrasena = input("Escribe la contraseña: ")
        contra = acceso(contrasena)
        if contra:
            var = True
        else:
            print("\nEscribe la contraseña de nuevo por favor...")

        


    
    
