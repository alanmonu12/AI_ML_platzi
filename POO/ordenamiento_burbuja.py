import random

def ordenamiento_burbuja(lista):
    n = len(lista)
    
    for i in range(n): # se recorre la lista completa entonces esto es n
        for j in range(0, n - i - 1): # recorer la lista completa y luego rediciendo n - i pero el termino más significativo es n
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista
    
    # La complejidad es O(n**2)

if __name__ == "__main__":
    tamano_lista = int(input("De que tamaño quieres la lista? "))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)

    print(lista_ordenada)