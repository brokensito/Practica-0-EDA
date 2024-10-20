''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 2  
- EXPLICACIONES: 

ejs 5,13,14,15,20

1. En la primera funcion se pide al usuario una cadena y se recorre toda la cadena utilizando la funcion lower para contar tambien las vocales 
mayusculas. 
2. En la funcion min_max() se hace return de dos argumentos (o lo que sea eso) que nos da el maximo y el minimo
3. En la funcion duplicados() se pasa una lista y se hace return con la funcion set() que elimina los duplicados



'''


def frase_vocales(): 
    usuario = input("Escribe una frase: ")
    vocales = ["a","e","i","o","u"]
    contador = 0

    for letra in usuario:
        if letra.lower() in vocales:
            contador+=1

    return contador

def min_max(lista): 
    return max(lista), min(lista)

def duplicados(lista):
    return set(lista)

def inverso(lista):
    return lista[::-1]

def tupla(lista):
    return tuple(lista)

if __name__=="__main__":

    ejemplo = [1,2,3,4,5,7,5,7,5,1,1,100,99]
    maximo, minimo = min_max(ejemplo)
    print(f"\nEl MAXIMO es: {maximo}\n")
    print(f"El MINIMO es: {minimo}\n")

    print(f"La lista eliminando los elementos duplicados queda tal que {duplicados(ejemplo)}\n")
    print(f"El inverso de la lista proporcionada es: {inverso(ejemplo)}\n")
    print(f"La lista convertida en tupla es {tupla(ejemplo)}\n")
    
    vocales = frase_vocales()
    print(f"El numero de vocales en la frase introducida es: {vocales}\n")


