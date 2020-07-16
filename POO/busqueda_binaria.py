import random

import sys
sys.setrecursionlimit(1000000)

def busqueda_binaria(lista, comienzo, final, objetivo, counter):
    
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    counter += 1

    if lista[medio] == objetivo:
        return True, counter
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, counter)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, counter)

def busqueda_lineal(lista, objeto):
    counter = 0

    match = False # 1

    for elemento in lista:  # x
        counter += 1
        if elemento == objeto:
            match = True
            break

    return match, counter  # 1

if __name__ == "__main__":
    tamano_lista = int(input('¿Cual es el tamaño de la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))
    lista = sorted([random.randint(0, 10000) for i in range(tamano_lista)])
    counter = 0

    encontrado_binaria, counter = busqueda_binaria(lista, 0, len(lista), objetivo, counter)
    print(f'El elemento {objetivo} {"esta" if encontrado_binaria else "no esta"} en la lista')
    print(f'Se encontro en {counter} iteraciones')

    encontrado_lineal, counter = busqueda_lineal(lista, objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado_lineal else "no esta"} en la lista')
    print(f'Se encontro en {counter} iteraciones')
