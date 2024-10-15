''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 1  
- EXPLICACIONES: 

- En la funcion nacimiento() se implementa el modulo datetime para sacar el año actual



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
        print("\n\t ¡ACCESO CONCEDIDO! ")
        return True
    else:
        print("\n\t ¡ACCESO DENEGADO!")
        return False
    
def edad():
    try: 
        numero = int(input("\nIntroduce tu edad: "))
        if numero <=0 or type(numero)!=int:
            raise TypeError
    
    except ValueError:
        print("El numero introducido tiene que ser ENTERO y POSITIVO, intentalo de nuevo...")
        return edad()
        
    except TypeError:
        print("El numero introducido no puede ser NEGATIVO o CERO, intentalo de nuevo")
        return edad()
    
    return numero


def altura():
    try:
        numero = float(input("\nIntroduce tu estatura en centimetros: "))
        if numero <=0:
            raise TypeError
        
    except ValueError:
        print("Tienes que pasar un numero entero positivo, intentalo de nuevo... ")
        return altura()

    except TypeError:
        print("La estatura no puede ser negativa, intentelo de nuevo... ")
        altura()

    return numero

def nacimiento():
    try:
        numero = int(input("\nIntroduce tu año de nacimiento: "))
        if numero>date.today().year:
            raise ValueError
    
    except ValueError:
        print("Introduce un año valido, intentalo de nuevo...")
        return nacimiento()

    actual = date.today().year 
    resultado = actual - numero

    return resultado
    

    return resultado

if __name__=="__main__":
    var = False

    while var == False:
        contrasena = input("Escribe la contraseña: ")
        contra = acceso(contrasena)
        if contra:
            var = True
        else:
            print("\nEscribe la contraseña de nuevo por favor...")
            print("\n******************************************************\n")

    print("\n---------------- EDAD ----------------")
    edad_usuario = edad()   
    
    if edad_usuario>18:
        print("Eres mayor de edad.\n")
    else:
        print("Eres menor de edad.\n")


    print("-----------------ALTURA----------------")
    altura_usuario = altura()

    if altura_usuario>170:
        print("Eres alto.\n")
    else:
        print("Eres de estatura promedio. \n")


    print("-----------------NACIMIENTO----------------")
    nacimiento_usuario = nacimiento()

    if nacimiento_usuario>=30:
        print("Tienes 30 años o mas.\n")
    else:
        print("Eres menor de 30 años.\n")


    print("********* FIN DEL PROGRAMA *********")




        


    
    
