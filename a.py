def frase_vocales():
    usuario = input("Escribe una frase: ")
    vocales = ["a","e","i","o","u"]
    contador = 0

    for i in usuario:
        if i in vocales:
            contador+=1

    return contador


if __name__=="__main__":
    print(frase_vocales())