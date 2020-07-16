class Coordenadas:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, d_x, d_y):
        return Coordenadas(self.x + d_x, self.y + d_y)

    def distancia(self, otra_coordenada):
        d_x = self.x + otra_coordenada.x
        d_y = self.y + otra_coordenada.y

        return (d_x ** 2 + d_y ** 2)** 0.5
        