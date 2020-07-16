import random


def busqueda_lineal(lista, objeto):
    match = False # 1

    for elemento in lista: # x
        if elemento == objeto:
            match = True
            break

    return match  # 1
    
# la complejidad es O(x) osea lineal, por eso es busqueda lineal 



if __name__ == "__main__":
    tamano_lista = int(input('¿Cual es el tamaño de la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    encontrado = busqueda_lineal(lista,objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')    