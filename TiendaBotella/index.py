from modelo_botella import Botella
from modelo_botella_plastico import*
#codigo principal
#aqui va la logica del negocio
# instancia del padre
objBotella= Botella("coca cola","1.5L","Especial")
objBotella.imprimir_info()
#instancia hija
objBotella_plastica= Botella_plastico ("pepsi","500ml","comun","redondo","plastico","blanco")
dato_out= objBotella_plastica.imprimir_info()
print(dato_out)