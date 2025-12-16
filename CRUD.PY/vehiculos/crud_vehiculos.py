from vehiculo import Vehiculo
import db_vehiculos

def crear_vehiculo(marca, color, motor):
    db_vehiculos.vehiculos.append(Vehiculo(marca, color, motor))

def listar_vehiculos():
    for v in db_vehiculos.vehiculos: v.mostrar_info()

def eliminar_vehiculo(marca):
    db_vehiculos.vehiculos=[v for v in db_vehiculos.vehiculos if v.marca!=marca]
