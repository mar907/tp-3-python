class Persona:
    especie = "Humano"  # Atributo de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad  # Atributo de instancia

    def saludar(self):
        print("Hola, mi nombre es", self.nombre)

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        cls.especie = nueva_especie

    @staticmethod
    def obtener_especie():
        return Persona.especie