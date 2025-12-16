from botella import Botella
import db_botellas

def crear_botella(material, capacidad):
    db_botellas.botellas.append(Botella(material, capacidad))

def listar_botellas():
    for b in db_botellas.botellas: b.mostrar_info()

def eliminar_botella(material):
    db_botellas.botellas=[b for b in db_botellas.botellas if b.material!=material]
