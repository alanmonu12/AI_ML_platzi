class Campo:

    def __init__(self):
        self.coordenada = {}

    def anadir_borracho(self, borracho, coordenada):
        self.coordenada[borracho] = coordenada

    def mover_borracho(self, borracho):
        d_x, d_y = borracho.camina()
        coordenada_actual = self.coordenada[borracho]
        nueva_coordenada = coordenada_actual.mover(d_x, d_y)

        self.coordenada[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenada[borracho]