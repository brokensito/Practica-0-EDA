'''
PRÁCTICA 0 Estructura de Datos y Algoritmos IM. Curso 24/25  
- AUTOR: David Sanz Fuertes   
- EJERCICIO: 2  
- EXPLICACIONES: 

- La función frase_vocales() solicita al usuario que escriba una frase y cuenta el número de vocales presentes en ella. Utiliza un bucle para recorrer cada carácter y verifica si es una vocal, considerando tanto mayúsculas como minúsculas.

- La función min_max(lista) recibe una lista y devuelve el valor máximo y mínimo de la misma utilizando las funciones integradas `max()` y `min()`.

- La función duplicados(lista) elimina los elementos duplicados de la lista convirtiéndola en un conjunto (`set`), ya que los conjuntos no permiten elementos repetidos.

- La función inverso(lista) devuelve la lista invertida utilizando slicing con un paso de `-1`.

- La función tupla(lista) convierte la lista proporcionada en una tupla utilizando la función `tuple()`.

- En el bloque principal del programa se define una lista de ejemplo y se llama a las funciones anteriores para mostrar sus resultados por pantalla.

- Finalmente, se llama a la función frase_vocales() para que el usuario introduzca una frase, y se muestra el número total de vocales que contiene.

'''

def frase_vocales():
    # Solicita al usuario que escriba una frase
    usuario = input("Escribe una frase: ")
    vocales = ["a", "e", "i", "o", "u"]  # Lista de vocales en minúscula
    contador = 0

    # Recorre cada letra de la frase introducida
    for letra in usuario:
        # Convierte la letra a minúscula y verifica si es una vocal
        if letra.lower() in vocales:
            contador += 1  # Incrementa el contador si es una vocal

    return contador  # Devuelve el número total de vocales

def min_max(lista):
    # Devuelve el valor máximo y mínimo de la lista
    return max(lista), min(lista)

def duplicados(lista):
    # Elimina los elementos duplicados convirtiendo la lista en un conjunto
    return set(lista)

def inverso(lista):
    # Devuelve la lista invertida utilizando slicing
    return lista[::-1]

def tupla(lista):
    # Convierte la lista en una tupla
    return tuple(lista)

if __name__ == "__main__":
    # Lista de ejemplo para probar las funciones
    ejemplo = [1, 2, 3, 4, 5, 7, 5, 7, 5, 1, 1, 100, 99]

    # Obtiene el máximo y mínimo de la lista
    maximo, minimo = min_max(ejemplo)
    print(f"\nEl MAXIMO es: {maximo}\n")
    print(f"El MINIMO es: {minimo}\n")

    # Muestra la lista sin elementos duplicados
    print(f"La lista eliminando los elementos duplicados queda: {duplicados(ejemplo)}\n")

    # Muestra la lista invertida
    print(f"El inverso de la lista proporcionada es: {inverso(ejemplo)}\n")

    # Convierte la lista en una tupla y la muestra
    print(f"La lista convertida en tupla es: {tupla(ejemplo)}\n")
    
    # Llama a la función para contar las vocales en la frase introducida por el usuario
    vocales = frase_vocales()
    print(f"El número de vocales en la frase introducida es: {vocales}\n")



