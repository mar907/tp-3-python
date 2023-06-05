class Persona:
    especie = "Humano"  # Atributo de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad  # Atributo de instancia

    def saludar(self):
        print("Hola, mi nombre es", self.nombre)

    def cumplir_anios(self):
        self.edad += 1