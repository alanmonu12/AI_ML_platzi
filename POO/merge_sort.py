import random

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Llamada recursiva para cada mitad de la lista que estamos trabajando
        merge_sort(izquierda)
        merge_sort(derecha)

        #iteradores para recorrer sublistas
        i = 0
        j = 0
        #Iterador para la lista principal
        k = 0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista


if __name__ == "__main__":
    list_length = int(input("Cual es el tamaño de la lista? "))

    lista = [random.randint(0, 100) for i in range(0, list_length)]
    print(lista)

    print('-' * 20)

    lista_ordenada = merge_sort(lista)
    print(lista_ordenada)

