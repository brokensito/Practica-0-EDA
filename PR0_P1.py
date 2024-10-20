''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 1  
- EXPLICACIONES: 

- En la funcion nacimiento() se implementa el modulo datetime para sacar el año actual, de manera que se resta con el año introducido por el 
usuario para sacar su edad actual (y que se pueda utiliza el programa por ejemplo el año siguiente y no solo con el numero actual "2024".)
- Se han hecho excepciones para evaluar la mayoria de los casos en las diferentes funciones.
- Al principio del programa se establece un bucle para introducir la contraseña y que se conceda el acceso unicamente si es la correcta,
si es diferente se le pide al usuario de nuevo. 
- En los demas apartados en vez de utilizar bucles se utiliza recursividad.
- 


'''

from datetime import date  # Importamos el módulo date para obtener el año actual

def acceso(contra):
    """
    Función que verifica si la contraseña introducida es correcta.
    """
    if contra == "python123":
        print("\n\t ¡ACCESO CONCEDIDO! ")
        return True  # Devuelve True si la contraseña es correcta
    
    else:
        print("\n\t ¡ACCESO DENEGADO!")
        return False  # Devuelve False si la contraseña es incorrecta

def edad():
    """
    Función que solicita al usuario que introduzca su edad y la valida.
    """
    try: 
        numero = int(input("\nIntroduce tu edad: "))

        if numero <= 0:
            raise TypeError  # Lanza una excepción si el número es negativo o cero
        
    except ValueError:
        # Se ejecuta si el usuario no introduce un número entero
        print("El número introducido tiene que ser ENTERO y POSITIVO, inténtalo de nuevo...")
        return edad()  # Llamada recursiva hasta que se introduzca un valor válido
    
    except TypeError:
        # Se ejecuta si el número es negativo o cero
        print("El número introducido no puede ser NEGATIVO o CERO, inténtalo de nuevo")
        return edad()  # Llamada recursiva hasta que se introduzca un valor válido
    
    return numero  # Devuelve la edad válida

def altura():
    """
    Función que solicita al usuario su estatura en centímetros y la valida.
    """
    try:
        numero = float(input("\nIntroduce tu estatura en centímetros: "))
        if numero <= 0:
            raise TypeError  # Lanza una excepción si la estatura es negativa o cero
        
    except ValueError:
        # Se ejecuta si el usuario no introduce un número válido
        print("Tienes que pasar un número positivo, inténtalo de nuevo... ")
        return altura()  # Llamada recursiva hasta que se introduzca un valor válido
    
    except TypeError:
        # Se ejecuta si la estatura es negativa o cero
        print("La estatura no puede ser negativa o cero, inténtalo de nuevo... ")
        return altura()  # Llamada recursiva hasta que se introduzca un valor válido
    
    return numero  # Devuelve la estatura válida

def nacimiento():
    """
    Función que solicita el año de nacimiento y calcula la edad actual del usuario.
    """
    try:
        numero = int(input("\nIntroduce tu año de nacimiento: "))
        actual = date.today().year  # Obtiene el año actual

        if numero > actual or actual - numero > 130 : # Lanza una excepción si el año de nacimiento es en el futuro o si es mayor de 130 años
            raise ValueError  
        
    except ValueError: # Se ejecuta si el año introducido no es válido
        print("Introduce un año válido, inténtalo de nuevo...")
        return nacimiento()  # Llamada recursiva hasta que se introduzca un valor válido
    
    resultado = actual - numero # Calcula la edad actual del usuario
    return resultado  # Devuelve la edad calculada

if __name__ == "__main__":
    var = False

    # Bucle para solicitar la contraseña hasta que sea correcta
    while not var:
        contrasena = input("Escribe la contraseña: ")
        contra = acceso(contrasena)

        if contra:
            var = True  # Cambia el estado si el acceso es concedido
       
        else:
            print("\nEscribe la contraseña de nuevo por favor...")
            print("\n******************************************************\n")

    print("\n---------------- EDAD ----------------")
    edad_usuario = edad()  # Llama a la función edad para obtener la edad del usuario

    if edad_usuario >= 18: # Verifica si el usuario es mayor o menor de edad
        print("Eres mayor de edad.\n")
    else:
        print("Eres menor de edad.\n")

    print("-----------------ALTURA----------------")
    altura_usuario = altura()  # Llama a la función altura para obtener la estatura del usuario
    
    if altura_usuario > 170: # Verifica si el usuario es alto o de estatura promedio
        print("Eres alto.\n")
    else:
        print("Eres de estatura promedio.\n")

    print("-----------------NACIMIENTO----------------")
    nacimiento_usuario = nacimiento()  # Llama a la función nacimiento para calcular la edad del usuario

    if nacimiento_usuario >= 30: # Verifica si el usuario tiene 30 años o más
        print("Tienes 30 años o más.\n")
    else:
        print("Eres menor de 30 años.\n")

    print("********* FIN DEL PROGRAMA ***********")




        


    
    
