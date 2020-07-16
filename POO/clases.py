# Definicion de clases

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otras_personas):
        return (f'Hola {otras_personas.nombre}, me llamo {self.nombre}')
        
#uso

david = Persona('David', 25)
Alan = Persona('Alan', 26)

print(Alan.saluda(david))