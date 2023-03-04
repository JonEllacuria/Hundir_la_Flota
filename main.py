import numpy as np
#from variables import *
#from funcionesBIS import *
from funcionesTRIS import *
from clases import *
import time

dict_barcos,name,tablero,tamaño_tablero=iniciar_juego()
ocup_eslora4,ocup_eslora3,ocup_eslora2,ocup_eslora1=dict_barcos["barco4"]*4,dict_barcos["barco3"]*3,dict_barcos["barco2"]*2,dict_barcos["barco1"]*1
tablero_copia=tablero.copy()
tablero_maquina=tablero.copy()

print("\n")
tablero_copia=colocar_barcos(name,tamaño_tablero,tablero_copia,dict_barcos,ocup_eslora4,ocup_eslora3,ocup_eslora2,ocup_eslora1)
time.sleep(3)
print("\n")
tablero_maquina=crear_tablero_maquina(tamaño_tablero,tablero_maquina,dict_barcos,ocup_eslora4,ocup_eslora3,ocup_eslora2,ocup_eslora1)

while "O" in tablero_copia and "O" in tablero_maquina:
    tablero_copia,tablero_maquina=disparo_usuario(tamaño_tablero,tablero_copia,tablero_maquina,name)
    time.sleep(3)
    if (np.count_nonzero(tablero_maquina=="O"))!=0:
        tablero_copia,tablero_maquina=disparo_maquina(tamaño_tablero,tablero_copia,tablero_maquina,name)
if "O" in tablero_copia:
    print("Has ganado!")
if "O" in tablero_maquina:
    print("Has perdido!")
