class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es", self.nombre)

    def cumplir_anios(self):
        self.edad += 1
        
"""  juan = Persona("Juan", 25)
juan.saludar()  # Salida: Hola, mi nombre es Juan
juan.cumplir_anios()
print(juan.edad)  # Salida: 26 """