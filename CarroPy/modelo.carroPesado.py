from modelo_carro import Vehiculo

class carroPesado(Vehiculo):
    def __init__(self, color, marca, motor, capacidad_carga):
        super().__init__(color, marca, motor)
        self.capacidad_carga = capacidad_carga

    def descargar(self):
        print(f"El camión {self.marca} está realizando la descarga del material.")

    def imprimir_info(self):
        print("Información del Camión de Cargo Pesado")
        super().imprimir_info()
        print(f"Capacidad de carga: {self.capacidad_carga}")
        print("")
