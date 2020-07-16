import random

def ordenamiento_ins(lista):
    print("lista sin ordenar")
    print(lista)
    n = len(lista)

    for i in range(1, n):
        valor_actual = lista[i]

        print(f'Valor actual: {valor_actual}')
        print(f'Iteración {i}: {lista}')

        for j in range(i, 0, -1):
            if valor_actual < lista[j - 1]:
                lista[j] = lista[j - 1]
                lista[j - 1] = valor_actual
            else:
                break

            print(f'Iteraciones internas: {lista}')

def ordenamiento_por_insercion(lista):
    print("lista sin ordenar")
    print(lista)

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        print(f'Valor actual: {valor_actual}')
        print(f'Iteración {indice}: {lista}')

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            print(f'Iteraciones internas: {lista}')

        lista[posicion_actual] = valor_actual


if __name__ == "__main__":
    tamano_lista = int(input("De que tamaño es la lista: "))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    ordenamiento_ins(lista)

    print(f'Lista ordenada: {lista}')
