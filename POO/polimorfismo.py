
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print('Ando caminando')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanzar(self):
        print('Ando moviendo en bici')

def main():
    persona = Persona('Alan')
    persona.avanzar()

    ciclista = Ciclista('David')
    ciclista.avanzar()

if __name__ == "__main__":
    main()