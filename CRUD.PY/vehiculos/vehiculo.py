class Vehiculo:
    def __init__(self, marca, color, motor):
        self.marca=marca
        self.color=color
        self.motor=motor

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Motor: {self.motor}")
        print("")
