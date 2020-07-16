from borracho import Borracho_tradicional
from campo import Campo
from coordenadas import Coordenadas

from bokeh.plotting import figure, show



def graficar(x, y):
    figura = figure()
    figura.line(x, y)
    show(figura)

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))

def simulalar_caminata(pasos, numero_intentos, tipo_borracho):
    borracho = tipo_borracho(nombre='David')
    origen = Coordenadas(0, 0)
    distancias = []

    for _ in range(numero_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulalar_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulalar_caminata, 1))

    return distancias


def main(distancias, intento, tipo_borracho):

    distancias_por_camianta = []

    for pasos in distancias:
        distancias = simulalar_caminata(pasos, intentos, tipo_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_max = max(distancias)
        distancia_min = min(distancias)

        distancias_por_camianta.append(distancia_media)

        print(f'{tipo_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'La distancia media es {distancia_media}')
        print(f'La distancia maxima es {distancia_max}')
        print(f'La distancia minima es {distancia_min}')
    
    graficar(distancias, distancias_por_camianta)



if __name__ == "__main__":
    
    distancias = [10, 100, 1000, 10000]
    intentos = 100

    main(distancias, intentos, Borracho_tradicional)