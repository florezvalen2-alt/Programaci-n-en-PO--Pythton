class Botella:
    def __init__(self, material, capacidad):
        self.material=material
        self.capacidad=capacidad

    def mostrar_info(self):
        print(f"Material: {self.material}")
        print(f"Capacidad: {self.capacidad}")
        print("")
