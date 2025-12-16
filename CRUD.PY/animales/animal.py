class Animal:
    def __init__(self, nombre, especie, habitad, dieta, tamaño):
        self.nombre = nombre
        self.especie = especie
        self.habitad = habitad
        self.dieta = dieta
        self.tamaño = tamaño

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Hábitat: {self.habitad}")
        print(f"Dieta: {self.dieta}")
        print(f"Tamaño: {self.tamaño}")
        print("")
