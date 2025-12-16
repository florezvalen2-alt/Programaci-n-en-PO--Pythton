from animal import Animal
import db_animales

def crear_animal(nombre, especie, habitad, dieta, tamaño):
    db_animales.animales.append(Animal(nombre, especie, habitad, dieta, tamaño))

def listar_animales():
    for a in db_animales.animales: a.mostrar_info()

def eliminar_animal(nombre):
    db_animales.animales=[a for a in db_animales.animales if a.nombre!=nombre]
