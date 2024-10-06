''' 
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 2  
- EXPLICACIONES: 

Ejercicios 5, 13, 14, 15 y 20

El ejercicio 5 es independiente del resto, para los que debe crear una 
lista de números proporcionados por el usuario y del tamaño deseado por dicho usuario

5. Conteo de vocales: Solicita una cadena al usuario y cuenta cuántas vocales
contiene usando un bucle for.

13. Encontrar el máximo y mínimo en una lista: Escribe un programa que
encuentre el número más grande y el más pequeño en una lista.

14.  Eliminar duplicados: Dada una lista de números, elimina los elementos
duplicados y devuelve una lista única.

15. Invertir una lista: Escribe un programa que invierta el orden de una lista sin
utilizar funciones predefinidas como reverse()

20. Convertir lista en tupla: Escribe un programa que convierta una lista en una
tupla.

'''

# Preguntar a que se refiere con lo de arriba del todo --> debe pedir al usuario numeros hasta que pare?
def frase_vocales(): # Mirar si esta bien
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
    """lista_inversa = []                  # Tambien se podria hacer de esta forma pero la tipica es la de abajo.
    for i in range(len(lista)):
        lista_inversa.append(lista[-i-1])"""

    return lista[::-1]

if __name__=="__main__":

    ejemplo = [1,2,3,4,5,7,5,1,]

    print(frase_vocales())









    















































