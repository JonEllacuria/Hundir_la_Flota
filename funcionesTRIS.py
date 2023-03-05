import numpy as np
from variables import *
import time


#1
'''Función Iniciar Juego:
	- Saluda al jugador y explica el funcionamiento del juego
	- Pregunta el nombre
	- Pregunta el tamaño de tablero
	- Output (nombre_usuario, tamaño_tablero, diccionario de barcos)'''
 
def iniciar_juego():
    print("¡Bienvenido al juego de Hundir la Flota!")
    time.sleep(2)
    name=str(input("¿Cuál es tu nombre?  "))
    print(f"\nHola {name}!")
    time.sleep(1)
    print("Te explico las Reglas Básicas:")
    time.sleep(2)
    print("\n*Tanto tú, como la máquina tenéis un tablero con barcos, y se trata de ir 'disparando'\n y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.")
    time.sleep(5)
    print("\n*Funciona por turnos y empiezas tú.") 
    time.sleep(2)
    print("\n*En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas,\n te vuelve a tocar**. En caso contrario, le toca a la máquina.")
    time.sleep(5)
    print("\n*En los turnos de la máquina, si acerta también le vuelve a tocar. ¿Dónde dispara la\n maquina? A un punto aleatorio en tu tablero.")
    time.sleep(4)
    print("\n*Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.")
    time.sleep(3)
    print("\n")
    while True:
        tamaño_tablero=int(input("Vamos a empezar a tomar decisiones... \n¿Qué tamaño de tablero quieres jugar? \n1-Pequeño\n2-Mediano\n3-Grande\n"))
        if tamaño_tablero==1 or tamaño_tablero==2 or tamaño_tablero==3:
            break
        elif tamaño_tablero=="":
            print("Respuesta incorrecta. \n¿Qué tamaño de tablero quieres jugar? \n1-Pequeño\n2-Mediano\n3-Grande\n")
    #while True:
    #    eslora1=int(input("¿Con cuántos barcos de eslora=1 quieres jugar?  "))
    #    eslora2=int(input("¿Con cuántos barcos de eslora=2 quieres jugar?  "))
    #    eslora3=int(input("¿Con cuántos barcos de eslora=3 quieres jugar?  "))
    #    eslora4=int(input("¿Con cuántos barcos de eslora=4 quieres jugar?  "))
    if tamaño_tablero==1:
        tablero=np.full((5,5)," ")
        dict_barcos={"barco4":0,"barco3":0,"barco2":0,"barco1":4}
            #if eslora1*1+eslora2*2+eslora3*3+eslora4*4<=8:
            #    break
            #if eslora1*1+eslora2*2+eslora3*3+eslora4*4>8:
            #    print("Demasiados barcos. Prueba otra vez, reduciendo el número de alguno de ellos")
    if tamaño_tablero==2:
        tablero=np.full((10,10)," ")
        dict_barcos={"barco4":1,"barco3":2,"barco2":3,"barco1":4}
            #if eslora1*1+eslora2*2+eslora3*3+eslora4*4<=22:
            #    break
            #if eslora1*1+eslora2*2+eslora3*3+eslora4*4>22:
            #    print("Demasiados barcos. Prueba otra vez, reduciendo el número de alguno de ellos")
    if tamaño_tablero==3:
        tablero=np.full((16,16)," ")
        dict_barcos={"barco4":2,"barco3":4,"barco2":6,"barco1":8}
            #if eslora1*1+eslora2*2+eslora3*3+eslora4*4<=40:
            #    break
            #if eslora1*1+eslora2*2+eslora3*3+eslora4*4>40:
            #    print("Demasiados barcos. Prueba otra vez, reduciendo el número de alguno de ellos")
    print("\n¡Perfecto! Deja que te los coloque en el tablero")
    #dict_barcos={"barco4":eslora4,"barco3":eslora3,"barco2":eslora2,"barco1":eslora1}
    return dict_barcos,name,tablero,tamaño_tablero

#if tamaño_tablero==1:
 #   tablero=np.full((5,5)," ")
#if tamaño_tablero==2:
 #   tablero=np.full((10,10)," ")
#if tamaño_tablero==3:
 #   tablero=np.full((15,15)," ")
    
#eslora1,eslora2,eslora3,eslora4,tamaño_tablero=iniciar_juego(eslora1,eslora2,eslora3,eslora4,tamaño_tablero)
#ocup_eslora1,ocup_eslora2,ocup_eslora3,ocup_eslora4=eslora1*1,eslora2*2,eslora3*3,eslora4*4

#2
'''Función Colocar Barcos y Tablero Máquina:
	- Recibe los inputs de la función previa y crea 2 tableros aleatorios (uno para el jugador y otro 
	para la máquina)
	- Depende del tamaño del tablero, coloca unos barcos u otros, pero la lógica es la misma.
	- Los barcos los coloca de manera aleatoria generando 3 valores random (coord_x,coord_y y orientación)
	- Muchas condiciones para que los barcos no se salgan del tablero ni se solapen ni estén "cerca" unos de
	de otros (un espacio de distancia, incluso de manera horizontal)
	- Output (tablero_usuario y tablero_maquina). Obviamente el tablero_maquina no lo visualiza el usuario.'''
 
def colocar_barcos(name,tamaño_tablero,tablero_copia,dict_barcos,ocup_eslora4,ocup_eslora3,ocup_eslora2,ocup_eslora1):
    if tamaño_tablero==2:
        for i in dict_barcos:
            
            if i=="barco4": #Colocamos los barcos de eslora=4
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,10)
                    y_user=np.random.randint(0,10)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=2 and orientacion=="N"):
                        continue
                    if (x_user>=7 and orientacion=="S"):
                        continue
                    if (y_user<=2 and orientacion=="O"):
                        continue
                    if (y_user>=7 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user!=9 and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_copia[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_copia[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=9) and tablero_copia[x_user-2,y_user+1]=="O") or \
                            (y_user>2 and tablero_copia[x_user-3,y_user]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_copia[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=9) and tablero_copia[x_user-3,y_user+1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user>3 and y_user!=0) and tablero_copia[x_user-4,y_user-1]=="O") or \
                            ((x_user>3 and y_user!=9) and tablero_copia[x_user-4,y_user+1]=="O") or \
                            (y_user>3 and tablero_copia[x_user-4,y_user]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user-1,y_user)]="O"
                            tablero_copia[(x_user-2,y_user)]="O"
                            tablero_copia[(x_user-3,y_user)]="O"
                    elif orientacion=="S":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            (y_user<8 and tablero_copia[x_user+2,y_user]=="O") or \
                            ((x_user<8 and y_user!=0) and tablero_copia[x_user+2,y_user-1]=="O") \
                            or ((x_user<8 and y_user!=9) and tablero_copia[x_user+2,y_user+1]=="O") or \
                            (x_user<7 and tablero_copia[x_user+3,y_user]=="O") or \
                            ((x_user<7 and y_user!=0) and tablero_copia[x_user+3,y_user-1]=="O") \
                            or ((x_user<7 and y_user!=9) and tablero_copia[x_user+3,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user<6 and y_user!=0) and tablero_copia[x_user+4,y_user-1]=="O") \
                            or ((x_user<6 and y_user!=9) and tablero_copia[x_user+4,y_user+1]=="O") or \
                            (x_user<6 and tablero_copia[x_user+4,y_user]=="O"):
                                continue
                        else:        
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user+1,y_user)]="O"
                            tablero_copia[(x_user+2,y_user)]="O"
                            tablero_copia[(x_user+3,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user<9 and y_user<9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user<8) and tablero_copia[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<8) and tablero_copia[x_user-1,y_user+2]=="O") or \
                            (y_user<8 and tablero_copia[x_user,y_user+2]=="O") or \
                            (y_user<7 and tablero_copia[x_user,y_user+3]=="O") or \
                            ((x_user!=9 and y_user<7) and tablero_copia[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<7) and tablero_copia[x_user-1,y_user+3]=="O") or \
                            ((x_user<9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user<6) and tablero_copia[x_user+1,y_user+4]=="O") or \
                            ((x_user!=0 and y_user<6) and tablero_copia[x_user-1,y_user+4]=="O") or \
                            (y_user<6 and tablero_copia[x_user,y_user+4]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user+1)]="O"
                            tablero_copia[(x_user,y_user+2)]="O"
                            tablero_copia[(x_user,y_user+3)]="O"
                        
                    elif orientacion=="O":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user>1) and tablero_copia[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_copia[x_user-1,y_user-2]=="O") or \
                            (y_user>1 and tablero_copia[x_user,y_user-2]=="O") or \
                            (x_user>2 and tablero_copia[x_user,y_user-3]=="O") or \
                            ((x_user!=9 and y_user>2) and tablero_copia[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_copia[x_user-1,y_user-3]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user>3) and tablero_copia[x_user+1,y_user-4]=="+O") or \
                            ((x_user!=0 and y_user>3) and tablero_copia[x_user-1,y_user-4]=="O") or \
                            (x_user>3 and tablero_copia[x_user,y_user-4]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user-1)]="O"
                            tablero_copia[(x_user,y_user-2)]="O"
                            tablero_copia[(x_user,y_user-3)]="O"
            
            if i=="barco3": #Colocamos los barcos de eslora=3
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,10)
                    y_user=np.random.randint(0,10)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=1 and orientacion=="N"):
                        continue
                    if (x_user>=8 and orientacion=="S"):
                        continue
                    if (y_user<=1 and orientacion=="O"):
                        continue
                    if (y_user>=8 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user!=9 and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_copia[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_copia[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=9) and tablero_copia[x_user-2,y_user+1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_copia[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=9) and tablero_copia[x_user-3,y_user+1]=="O") or \
                            (y_user>2 and tablero_copia[x_user-3,y_user]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user-1,y_user)]="O"
                            tablero_copia[(x_user-2,y_user)]="O"
                            
                    elif orientacion=="S":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            (y_user<8 and tablero_copia[x_user+2,y_user]=="O") or \
                            ((x_user<8 and y_user!=0) and tablero_copia[x_user+2,y_user-1]=="O") \
                            or ((x_user<8 and y_user!=9) and tablero_copia[x_user+2,y_user+1]=="O") or \
                            ((x_user<7 and y_user!=0) and tablero_copia[x_user+3,y_user-1]=="O") \
                            or ((x_user<7 and y_user!=9) and tablero_copia[x_user+3,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") \
                            or ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (x_user<7 and tablero_copia[x_user+3,y_user]=="O"):
                                continue
                        else:        
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user+1,y_user)]="O"
                            tablero_copia[(x_user+2,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user<9 and y_user<9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user<8) and tablero_copia[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<8) and tablero_copia[x_user-1,y_user+2]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user<7) and tablero_copia[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<7) and tablero_copia[x_user-1,y_user+3]=="O") or \
                            (y_user<8 and tablero_copia[x_user,y_user+2]=="O") or \
                            (y_user<7 and tablero_copia[x_user,y_user+3]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user+1)]="O"
                            tablero_copia[(x_user,y_user+2)]="O"
                        
                    elif orientacion=="O":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user>1) and tablero_copia[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_copia[x_user-1,y_user-2]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user>2) and tablero_copia[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_copia[x_user-1,y_user-3]=="O") or \
                            (y_user>1 and tablero_copia[x_user,y_user-2]=="O") or \
                            (x_user>2 and tablero_copia[x_user,y_user-3]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user-1)]="O"
                            tablero_copia[(x_user,y_user-2)]="O"
            
            if i=="barco2": #Colocamos los barcos de eslora=2
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora2+ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,10)
                    y_user=np.random.randint(0,10)
                    #print(x_user,y_user,orientacion)
                    if (x_user==0 and orientacion=="N"):
                        continue
                    if (x_user==9 and orientacion=="S"):
                        continue
                    if (y_user==0 and orientacion=="O"):
                        continue
                    if (y_user==9 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_copia[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=9) and tablero_copia[x_user-2,y_user+1]=="O") or \
                            (x_user>1 and tablero_copia[x_user-2,y_user]=="O"):
                                continue        
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user-1,y_user)]="O"
                        
                    elif orientacion=="S":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            (x_user<8 and tablero_copia[x_user+2,y_user]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or\
                            ((x_user<8 and y_user!=0) and tablero_copia[x_user+2,y_user-1]=="O") or \
                            ((x_user<8 and y_user!=9) and tablero_copia[x_user+2,y_user+1]=="O"):
                                continue
                        else:        
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user+1,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            (y_user<8 and tablero_copia[x_user,y_user+2]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user<8) and tablero_copia[x_user+1,y_user+2]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user+1)]="O"
                        
                    elif orientacion=="O":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            (y_user<8 and tablero_copia[x_user,y_user-2]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user<8) and tablero_copia[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user<8) and tablero_copia[x_user-1,y_user-2]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user-1)]="O"
            
            if i=="barco1": #Colocamos los barcos de eslora=1
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora1+ocup_eslora2+ocup_eslora3+ocup_eslora4: #Que el bucle no se detenga hasta que estén los 4 barcos dibujados
                    x_user=np.random.randint(0,10)
                    y_user=np.random.randint(0,10)
                    #print(x_user,y_user)
                    if tablero_copia[x_user,y_user]=="O" or (x_user!=9 and tablero_copia[x_user+1,y_user]=="O") \
                    or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                    (y_user!=9 and tablero_copia[x_user,y_user+1]=="O") or \
                    (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                    ((x_user!=9 and y_user!=9) and tablero_copia[x_user+1,y_user+1]=="O") or \
                    ((x_user!=9 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                    ((x_user!=0 and y_user!=9) and tablero_copia[x_user-1,y_user+1]=="O") or \
                    ((y_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O"):
                        continue
                    else:
                        tablero_copia[x_user,y_user]="O"
            
                            
            
        
            
    
    
    if tamaño_tablero==1:
        for i in dict_barcos:
            
            if i=="barco4": #Colocamos los barcos de eslora=4
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,5)
                    y_user=np.random.randint(0,5)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=2 and orientacion=="N"):
                        continue
                    if (x_user>=2 and orientacion=="S"):
                        continue
                    if (y_user<=2 and orientacion=="O"):
                        continue
                    if (y_user>=2 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user!=4 and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_copia[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_copia[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=4) and tablero_copia[x_user-2,y_user+1]=="O") or \
                            (y_user>2 and tablero_copia[x_user-3,y_user]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_copia[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=4) and tablero_copia[x_user-3,y_user+1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user>3 and y_user!=0) and tablero_copia[x_user-4,y_user-1]=="O") or \
                            ((x_user>3 and y_user!=4) and tablero_copia[x_user-4,y_user+1]=="O") or \
                            (y_user>3 and tablero_copia[x_user-4,y_user]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user-1,y_user)]="O"
                            tablero_copia[(x_user-2,y_user)]="O"
                            tablero_copia[(x_user-3,y_user)]="O"
                    elif orientacion=="S":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            (y_user<3 and tablero_copia[x_user+2,y_user]=="O") or \
                            ((x_user<3 and y_user!=0) and tablero_copia[x_user+2,y_user-1]=="O") \
                            or ((x_user<3 and y_user!=4) and tablero_copia[x_user+2,y_user+1]=="O") or \
                            (x_user<2 and tablero_copia[x_user+3,y_user]=="O") or \
                            ((x_user<2 and y_user!=0) and tablero_copia[x_user+3,y_user-1]=="O") \
                            or ((x_user<2 and y_user!=4) and tablero_copia[x_user+3,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user<1 and y_user!=0) and tablero_copia[x_user+4,y_user-1]=="O") or \
                            ((x_user<1 and y_user!=4) and tablero_copia[x_user+4,y_user+1]=="O") or \
                            (x_user<1 and tablero_copia[x_user+4,y_user]=="O"):
                                continue
                        else:        
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user+1,y_user)]="O"
                            tablero_copia[(x_user+2,y_user)]="O"
                            tablero_copia[(x_user+3,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user<4 and y_user<4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user<3) and tablero_copia[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<3) and tablero_copia[x_user-1,y_user+2]=="O") or \
                            (y_user<3 and tablero_copia[x_user,y_user+2]=="O") or \
                            (y_user<2 and tablero_copia[x_user,y_user+3]=="O") or \
                            ((x_user!=4 and y_user<2) and tablero_copia[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<2) and tablero_copia[x_user-1,y_user+3]=="O") or \
                            ((x_user<4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user<1) and tablero_copia[x_user+1,y_user+4]=="O") or \
                            ((x_user!=0 and y_user<1) and tablero_copia[x_user-1,y_user+4]=="O") or \
                            (y_user<1 and tablero_copia[x_user,y_user+4]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user+1)]="O"
                            tablero_copia[(x_user,y_user+2)]="O"
                            tablero_copia[(x_user,y_user+3)]="O"
                        
                    elif orientacion=="O":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user>1) and tablero_copia[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_copia[x_user-1,y_user-2]=="O") or \
                            (y_user>1 and tablero_copia[x_user,y_user-2]=="O") or \
                            (x_user>2 and tablero_copia[x_user,y_user-3]=="O") or \
                            ((x_user!=4 and y_user>2) and tablero_copia[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_copia[x_user-1,y_user-3]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user>3) and tablero_copia[x_user+1,y_user-4]=="O") or \
                            ((x_user!=0 and y_user>3) and tablero_copia[x_user-1,y_user-4]=="O") or \
                            (x_user>3 and tablero_copia[x_user,y_user-4]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user-1)]="O"
                            tablero_copia[(x_user,y_user-2)]="O"
                            tablero_copia[(x_user,y_user-3)]="O"  
            
            if i=="barco3": #Colocamos los barcos de eslora=3
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,5)
                    y_user=np.random.randint(0,5)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=1 and orientacion=="N"):
                        continue
                    if (x_user>=3 and orientacion=="S"):
                        continue
                    if (y_user<=1 and orientacion=="O"):
                        continue
                    if (y_user>=3 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user!=4 and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_copia[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_copia[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=4) and tablero_copia[x_user-2,y_user+1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_copia[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=4) and tablero_copia[x_user-3,y_user+1]=="O") or \
                            (y_user>2 and tablero_copia[x_user-3,y_user]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user-1,y_user)]="O"
                            tablero_copia[(x_user-2,y_user)]="O"
                            
                    elif orientacion=="S":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            (y_user<3 and tablero_copia[x_user+2,y_user]=="O") or \
                            ((x_user<3 and y_user!=0) and tablero_copia[x_user+2,y_user-1]=="O") or \
                            ((x_user<3 and y_user!=4) and tablero_copia[x_user+2,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user<2 and y_user!=0) and tablero_copia[x_user+3,y_user-1]=="O") or \
                            ((x_user<2 and y_user!=4) and tablero_copia[x_user+3,y_user+1]=="O") or \
                            (x_user<2 and tablero_copia[x_user+3,y_user]=="O"):
                                continue
                        else:        
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user+1,y_user)]="O"
                            tablero_copia[(x_user+2,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user<4 and y_user<4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user<3) and tablero_copia[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<3) and tablero_copia[x_user-1,y_user+2]=="O") or \
                            (y_user<3 and tablero_copia[x_user,y_user+2]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user<2) and tablero_copia[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<2) and tablero_copia[x_user-1,y_user+3]=="O") or \
                            (y_user<2 and tablero_copia[x_user,y_user+3]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user+1)]="O"
                            tablero_copia[(x_user,y_user+2)]="O"
                        
                    elif orientacion=="O":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user>1) and tablero_copia[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_copia[x_user-1,y_user-2]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user>2) and tablero_copia[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_copia[x_user-1,y_user-3]=="O") or \
                            (y_user>1 and tablero_copia[x_user,y_user-2]=="O") or \
                            (x_user>2 and tablero_copia[x_user,y_user-3]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user-1)]="O"
                            tablero_copia[(x_user,y_user-2)]="O"
            
            if i=="barco2": #Colocamos los barcos de eslora=2
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora2+ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,5)
                    y_user=np.random.randint(0,5)
                    #print(x_user,y_user,orientacion)
                    if (x_user==0 and orientacion=="N"):
                        continue
                    if (x_user==4 and orientacion=="S"):
                        continue
                    if (y_user==0 and orientacion=="O"):
                        continue
                    if (y_user==4 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_copia[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=4) and tablero_copia[x_user-2,y_user+1]=="O") or \
                            (x_user>1 and tablero_copia[x_user-2,y_user]=="O"):
                                continue        
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user-1,y_user)]="O"
                        
                    elif orientacion=="S":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            (x_user<3 and tablero_copia[x_user+2,y_user]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user<3 and y_user!=0) and tablero_copia[x_user+2,y_user-1]=="O") or \
                            ((x_user<3 and y_user!=4) and tablero_copia[x_user+2,y_user+1]=="O"):
                                continue
                        else:        
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user+1,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            (y_user<3 and tablero_copia[x_user,y_user+2]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user<3) and tablero_copia[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<3) and tablero_copia[x_user-1,y_user+2]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user+1)]="O"
                        
                    elif orientacion=="O":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            (y_user<3 and tablero_copia[x_user,y_user-2]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user<3) and tablero_copia[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user<3) and tablero_copia[x_user-1,y_user-2]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user-1)]="O"
            
            if i=="barco1": #Colocamos los barcos de eslora=1
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora1+ocup_eslora2+ocup_eslora3+ocup_eslora4: #Que el bucle no se detenga hasta que estén los 4 barcos dibujados
                    x_user=np.random.randint(0,5)
                    y_user=np.random.randint(0,5)
                    #print(x_user,y_user)
                    if tablero_copia[x_user,y_user]=="O" or (x_user!=4 and tablero_copia[x_user+1,y_user]=="O") \
                    or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                    (y_user!=4 and tablero_copia[x_user,y_user+1]=="O") or \
                    ((x_user!=4 and y_user!=4) and tablero_copia[x_user+1,y_user+1]=="O") or \
                    ((x_user!=4 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                    ((x_user!=0 and y_user!=4) and tablero_copia[x_user-1,y_user+1]=="O") or \
                    ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                    (y_user!=0 and tablero_copia[x_user,y_user-1]=="O"):
                        continue
                    else:
                        tablero_copia[x_user,y_user]="O"
            
                            
            
        
                                
    
    
    if tamaño_tablero==3:
        for i in dict_barcos:
            
            if i=="barco4": #Colocamos los barcos de eslora=4
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,15)
                    y_user=np.random.randint(0,15)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=2 and orientacion=="N"):
                        continue
                    if (x_user>=12 and orientacion=="S"):
                        continue
                    if (y_user<=2 and orientacion=="O"):
                        continue
                    if (y_user>=12 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user!=14 and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_copia[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_copia[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=14) and tablero_copia[x_user-2,y_user+1]=="O") or \
                            (y_user>2 and tablero_copia[x_user-3,y_user]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_copia[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=14) and tablero_copia[x_user-3,y_user+1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user>3 and y_user!=0) and tablero_copia[x_user-4,y_user-1]=="O") or \
                            ((x_user>3 and y_user!=14) and tablero_copia[x_user-4,y_user+1]=="O") or \
                            (y_user>3 and tablero_copia[x_user-4,y_user]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user-1,y_user)]="O"
                            tablero_copia[(x_user-2,y_user)]="O"
                            tablero_copia[(x_user-3,y_user)]="O"
                    elif orientacion=="S":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            (y_user<13 and tablero_copia[x_user+2,y_user]=="O") or \
                            ((x_user<13 and y_user!=0) and tablero_copia[x_user+2,y_user-1]=="O") \
                            or ((x_user<13 and y_user!=14) and tablero_copia[x_user+2,y_user+1]=="O") or \
                            (x_user<12 and tablero_copia[x_user+3,y_user]=="O") or \
                            ((x_user<12 and y_user!=0) and tablero_copia[x_user+3,y_user-1]=="O") \
                            or ((x_user<12 and y_user!=14) and tablero_copia[x_user+3,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") \
                            or ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user<11 and y_user!=0) and tablero_copia[x_user+4,y_user-1]=="O") \
                            or ((x_user<11 and y_user!=14) and tablero_copia[x_user+4,y_user+1]=="O") or \
                            (x_user<11 and tablero_copia[x_user+4,y_user]=="O"):
                                continue
                        else:        
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user+1,y_user)]="O"
                            tablero_copia[(x_user+2,y_user)]="O"
                            tablero_copia[(x_user+3,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user<14 and y_user<14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user<13) and tablero_copia[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<13) and tablero_copia[x_user-1,y_user+2]=="O") or \
                            (y_user<13 and tablero_copia[x_user,y_user+2]=="O") or \
                            (y_user<12 and tablero_copia[x_user,y_user+3]=="O") or \
                            ((x_user!=14 and y_user<12) and tablero_copia[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<12) and tablero_copia[x_user-1,y_user+3]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user<11) and tablero_copia[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<11) and tablero_copia[x_user-1,y_user+4]=="O") or \
                            (y_user<11 and tablero_copia[x_user,y_user+4]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user+1)]="O"
                            tablero_copia[(x_user,y_user+2)]="O"
                            tablero_copia[(x_user,y_user+3)]="O"
                        
                    elif orientacion=="O":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user>1) and tablero_copia[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_copia[x_user-1,y_user-2]=="O") or \
                            (y_user>1 and tablero_copia[x_user,y_user-2]=="O") or \
                            (x_user>2 and tablero_copia[x_user,y_user-3]=="O") or \
                            ((x_user!=14 and y_user>2) and tablero_copia[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_copia[x_user-1,y_user-3]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user>3) and tablero_copia[x_user+1,y_user-4]=="O") or \
                            ((x_user!=0 and y_user>3) and tablero_copia[x_user-1,y_user-4]=="O") or \
                            (x_user>3 and tablero_copia[x_user,y_user-4]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user-1)]="O"
                            tablero_copia[(x_user,y_user-2)]="O"
                            tablero_copia[(x_user,y_user-3)]="O"
            
            if i=="barco3": #Colocamos los barcos de eslora=3
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,15)
                    y_user=np.random.randint(0,15)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=1 and orientacion=="N"):
                        continue
                    if (x_user>=13 and orientacion=="S"):
                        continue
                    if (y_user<=1 and orientacion=="O"):
                        continue
                    if (y_user>=13 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user!=14 and tablero_copia[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_copia[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_copia[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=14) and tablero_copia[x_user-2,y_user+1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_copia[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=14) and tablero_copia[x_user-3,y_user+1]=="O") or \
                            (y_user>2 and tablero_copia[x_user-3,y_user]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user-1,y_user)]="O"
                            tablero_copia[(x_user-2,y_user)]="O"
                            
                    elif orientacion=="S":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            (y_user<13 and tablero_copia[x_user+2,y_user]=="O") or \
                            ((x_user<13 and y_user!=0) and tablero_copia[x_user+2,y_user-1]=="O") \
                            or ((x_user<13 and y_user!=14) and tablero_copia[x_user+2,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user<12 and y_user!=0) and tablero_copia[x_user+3,y_user-1]=="O") or \
                            ((x_user<12 and y_user!=14) and tablero_copia[x_user+3,y_user+1]=="O") or \
                            (x_user<12 and tablero_copia[x_user+3,y_user]=="O"):
                                continue
                        else:        
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user+1,y_user)]="O"
                            tablero_copia[(x_user+2,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user<14 and y_user<14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user<13) and tablero_copia[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<13) and tablero_copia[x_user-1,y_user+2]=="O") or \
                            (y_user<13 and tablero_copia[x_user,y_user+2]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user<12) and tablero_copia[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<12) and tablero_copia[x_user-1,y_user+3]=="O") or \
                            (y_user<12 and tablero_copia[x_user,y_user+3]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user+1)]="O"
                            tablero_copia[(x_user,y_user+2)]="O"
                        
                    elif orientacion=="O":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user>1) and tablero_copia[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_copia[x_user-1,y_user-2]=="O") or \
                            (y_user>1 and tablero_copia[x_user,y_user-2]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user>2) and tablero_copia[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_copia[x_user-1,y_user-3]=="O") or \
                            (x_user>2 and tablero_copia[x_user,y_user-3]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user-1)]="O"
                            tablero_copia[(x_user,y_user-2)]="O"
            
            if i=="barco2": #Colocamos los barcos de eslora=2
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora2+ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,15)
                    y_user=np.random.randint(0,15)
                    #print(x_user,y_user,orientacion)
                    if (x_user==0 and orientacion=="N"):
                        continue
                    if (x_user==14 and orientacion=="S"):
                        continue
                    if (y_user==0 and orientacion=="O"):
                        continue
                    if (y_user==14 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_copia[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=14) and tablero_copia[x_user-2,y_user+1]=="O") or \
                            (x_user>1 and tablero_copia[x_user-2,y_user]=="O"):
                                continue        
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user-1,y_user)]="O"
                        
                    elif orientacion=="S":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            (x_user<13 and tablero_copia[x_user+2,y_user]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user<13 and y_user!=0) and tablero_copia[x_user+2,y_user-1]=="O") or \
                            ((x_user<13 and y_user!=14) and tablero_copia[x_user+2,y_user+1]=="O"):
                                continue
                        else:        
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user+1,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            (y_user<13 and tablero_copia[x_user,y_user+2]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user<13) and tablero_copia[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<13) and tablero_copia[x_user-1,y_user+2]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user+1)]="O"
                        
                    elif orientacion=="O":
                        if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_copia[x_user,y_user-1]=="O") or \
                            (y_user>1 and tablero_copia[x_user,y_user-2]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user>1) and tablero_copia[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_copia[x_user-1,y_user-2]=="O"):
                                continue
                        else:
                            tablero_copia[(x_user,y_user)]="O"
                            tablero_copia[(x_user,y_user-1)]="O"
            
            if i=="barco1": #Colocamos los barcos de eslora=1
                while np.count_nonzero(tablero_copia=="O")<ocup_eslora1+ocup_eslora2+ocup_eslora3+ocup_eslora4: #Que el bucle no se detenga hasta que estén los 4 barcos dibujados
                    x_user=np.random.randint(0,15)
                    y_user=np.random.randint(0,15)
                    #print(x_user,y_user)
                    if tablero_copia[x_user,y_user]=="O" or (x_user!=14 and tablero_copia[x_user+1,y_user]=="O") \
                    or (x_user!=0 and tablero_copia[x_user-1,y_user]=="O") or \
                    (y_user!=14 and tablero_copia[x_user,y_user+1]=="O") or \
                    ((x_user!=14 and y_user!=14) and tablero_copia[x_user+1,y_user+1]=="O") or \
                    ((x_user!=14 and y_user!=0) and tablero_copia[x_user+1,y_user-1]=="O") or \
                    ((x_user!=0 and y_user!=14) and tablero_copia[x_user-1,y_user+1]=="O") or \
                    ((x_user!=14 and y_user!=0) and tablero_copia[x_user-1,y_user-1]=="O") or \
                    (y_user!=0 and tablero_copia[x_user,y_user-1]=="O"):
                        continue
                    else:
                        tablero_copia[x_user,y_user]="O"
            
                            
            
        
            
    print(f"--Tablero de {name}--")
    print(tablero_copia)
    return tablero_copia

#3

#tablero_maquina=tablero.copy()
def crear_tablero_maquina(tamaño_tablero,tablero_maquina,dict_barcos,ocup_eslora4,ocup_eslora3,ocup_eslora2,ocup_eslora1):
    if tamaño_tablero==2:
        for i in dict_barcos:
            
            if i=="barco4": #Colocamos los barcos de eslora=4
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,10)
                    y_user=np.random.randint(0,10)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=2 and orientacion=="N"):
                        continue
                    if (x_user>=7 and orientacion=="S"):
                        continue
                    if (y_user<=2 and orientacion=="O"):
                        continue
                    if (y_user>=7 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_maquina[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_maquina[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=9) and tablero_maquina[x_user-2,y_user+1]=="O") or \
                            (y_user>2 and tablero_maquina[x_user-3,y_user]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_maquina[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=9) and tablero_maquina[x_user-3,y_user+1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user>3 and y_user!=0) and tablero_maquina[x_user-4,y_user-1]=="O") or \
                            ((x_user>3 and y_user!=9) and tablero_maquina[x_user-4,y_user+1]=="O") or \
                            (y_user>3 and tablero_maquina[x_user-4,y_user]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user-1,y_user)]="O"
                            tablero_maquina[(x_user-2,y_user)]="O"
                            tablero_maquina[(x_user-3,y_user)]="O"
                    elif orientacion=="S":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            (y_user<8 and tablero_maquina[x_user+2,y_user]=="O") or \
                            ((x_user<8 and y_user!=0) and tablero_maquina[x_user+2,y_user-1]=="O") \
                            or ((x_user<8 and y_user!=9) and tablero_maquina[x_user+2,y_user+1]=="O") or \
                            (x_user<7 and tablero_maquina[x_user+3,y_user]=="O") or \
                            ((x_user<7 and y_user!=0) and tablero_maquina[x_user+3,y_user-1]=="O") \
                            or ((x_user<7 and y_user!=9) and tablero_maquina[x_user+3,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user<6 and y_user!=0) and tablero_maquina[x_user+4,y_user-1]=="O") \
                            or ((x_user<6 and y_user!=9) and tablero_maquina[x_user+4,y_user+1]=="O") or \
                            (x_user<6 and tablero_maquina[x_user+4,y_user]=="O"):
                                continue
                        else:        
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user+1,y_user)]="O"
                            tablero_maquina[(x_user+2,y_user)]="O"
                            tablero_maquina[(x_user+3,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user<9 and y_user<9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user<8) and tablero_maquina[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<8) and tablero_maquina[x_user-1,y_user+2]=="O") or \
                            (y_user<8 and tablero_maquina[x_user,y_user+2]=="O") or \
                            (y_user<7 and tablero_maquina[x_user,y_user+3]=="O") or \
                            ((x_user!=9 and y_user<7) and tablero_maquina[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<7) and tablero_maquina[x_user-1,y_user+3]=="O") or \
                            ((x_user<9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user<6) and tablero_maquina[x_user+1,y_user+4]=="O") or \
                            ((x_user!=0 and y_user<6) and tablero_maquina[x_user-1,y_user+4]=="O") or \
                            (y_user<6 and tablero_maquina[x_user,y_user+4]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user+1)]="O"
                            tablero_maquina[(x_user,y_user+2)]="O"
                            tablero_maquina[(x_user,y_user+3)]="O"
                        
                    elif orientacion=="O":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user>1) and tablero_maquina[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_maquina[x_user-1,y_user-2]=="O") or \
                            (y_user>1 and tablero_maquina[x_user,y_user-2]=="O") or \
                            (x_user>2 and tablero_maquina[x_user,y_user-3]=="O") or \
                            ((x_user!=9 and y_user>2) and tablero_maquina[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_maquina[x_user-1,y_user-3]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user>3) and tablero_maquina[x_user+1,y_user-4]=="+O") or \
                            ((x_user!=0 and y_user>3) and tablero_maquina[x_user-1,y_user-4]=="O") or \
                            (x_user>3 and tablero_maquina[x_user,y_user-4]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user-1)]="O"
                            tablero_maquina[(x_user,y_user-2)]="O"
                            tablero_maquina[(x_user,y_user-3)]="O"
            
            if i=="barco3": #Colocamos los barcos de eslora=3
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,10)
                    y_user=np.random.randint(0,10)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=1 and orientacion=="N"):
                        continue
                    if (x_user>=8 and orientacion=="S"):
                        continue
                    if (y_user<=1 and orientacion=="O"):
                        continue
                    if (y_user>=8 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_maquina[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_maquina[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=9) and tablero_maquina[x_user-2,y_user+1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_maquina[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=9) and tablero_maquina[x_user-3,y_user+1]=="O") or \
                            (y_user>2 and tablero_maquina[x_user-3,y_user]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user-1,y_user)]="O"
                            tablero_maquina[(x_user-2,y_user)]="O"
                            
                    elif orientacion=="S":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            (y_user<8 and tablero_maquina[x_user+2,y_user]=="O") or \
                            ((x_user<8 and y_user!=0) and tablero_maquina[x_user+2,y_user-1]=="O") \
                            or ((x_user<8 and y_user!=9) and tablero_maquina[x_user+2,y_user+1]=="O") or \
                            ((x_user<7 and y_user!=0) and tablero_maquina[x_user+3,y_user-1]=="O") \
                            or ((x_user<7 and y_user!=9) and tablero_maquina[x_user+3,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") \
                            or ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (x_user<7 and tablero_maquina[x_user+3,y_user]=="O"):
                                continue
                        else:        
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user+1,y_user)]="O"
                            tablero_maquina[(x_user+2,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user<9 and y_user<9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user<8) and tablero_maquina[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<8) and tablero_maquina[x_user-1,y_user+2]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user<7) and tablero_maquina[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<7) and tablero_maquina[x_user-1,y_user+3]=="O") or \
                            (y_user<8 and tablero_maquina[x_user,y_user+2]=="O") or \
                            (y_user<7 and tablero_maquina[x_user,y_user+3]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user+1)]="O"
                            tablero_maquina[(x_user,y_user+2)]="O"
                        
                    elif orientacion=="O":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user>1) and tablero_maquina[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_maquina[x_user-1,y_user-2]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user>2) and tablero_maquina[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_maquina[x_user-1,y_user-3]=="O") or \
                            (y_user>1 and tablero_maquina[x_user,y_user-2]=="O") or \
                            (x_user>2 and tablero_maquina[x_user,y_user-3]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user-1)]="O"
                            tablero_maquina[(x_user,y_user-2)]="O"
            
            if i=="barco2": #Colocamos los barcos de eslora=2
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora2+ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,10)
                    y_user=np.random.randint(0,10)
                    #print(x_user,y_user,orientacion)
                    if (x_user==0 and orientacion=="N"):
                        continue
                    if (x_user==9 and orientacion=="S"):
                        continue
                    if (y_user==0 and orientacion=="O"):
                        continue
                    if (y_user==9 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_maquina[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=9) and tablero_maquina[x_user-2,y_user+1]=="O") or \
                            (x_user>1 and tablero_maquina[x_user-2,y_user]=="O"):
                                continue        
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user-1,y_user)]="O"
                        
                    elif orientacion=="S":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            (x_user<8 and tablero_maquina[x_user+2,y_user]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or\
                            ((x_user<8 and y_user!=0) and tablero_maquina[x_user+2,y_user-1]=="O") or \
                            ((x_user<8 and y_user!=9) and tablero_maquina[x_user+2,y_user+1]=="O"):
                                continue
                        else:        
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user+1,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            (y_user<8 and tablero_maquina[x_user,y_user+2]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user<8) and tablero_maquina[x_user+1,y_user+2]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user+1)]="O"
                        
                    elif orientacion=="O":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            (y_user<8 and tablero_maquina[x_user,y_user-2]=="O") or \
                            ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=9 and y_user!=9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=9 and y_user<8) and tablero_maquina[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user<8) and tablero_maquina[x_user-1,y_user-2]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user-1)]="O"
            
            if i=="barco1": #Colocamos los barcos de eslora=1
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora1+ocup_eslora2+ocup_eslora3+ocup_eslora4: #Que el bucle no se detenga hasta que estén los 4 barcos dibujados
                    x_user=np.random.randint(0,10)
                    y_user=np.random.randint(0,10)
                    #print(x_user,y_user)
                    if tablero_maquina[x_user,y_user]=="O" or (x_user!=9 and tablero_maquina[x_user+1,y_user]=="O") \
                    or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                    (y_user!=9 and tablero_maquina[x_user,y_user+1]=="O") or \
                    (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                    ((x_user!=9 and y_user!=9) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                    ((x_user!=9 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                    ((x_user!=0 and y_user!=9) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                    ((y_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O"):
                        continue
                    else:
                        tablero_maquina[x_user,y_user]="O"
            
                            
            
        
            
    
    
    if tamaño_tablero==1:
        for i in dict_barcos:
            
            if i=="barco4": #Colocamos los barcos de eslora=4
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,5)
                    y_user=np.random.randint(0,5)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=2 and orientacion=="N"):
                        continue
                    if (x_user>=2 and orientacion=="S"):
                        continue
                    if (y_user<=2 and orientacion=="O"):
                        continue
                    if (y_user>=2 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_maquina[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_maquina[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=4) and tablero_maquina[x_user-2,y_user+1]=="O") or \
                            (y_user>2 and tablero_maquina[x_user-3,y_user]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_maquina[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=4) and tablero_maquina[x_user-3,y_user+1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user>3 and y_user!=0) and tablero_maquina[x_user-4,y_user-1]=="O") or \
                            ((x_user>3 and y_user!=4) and tablero_maquina[x_user-4,y_user+1]=="O") or \
                            (y_user>3 and tablero_maquina[x_user-4,y_user]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user-1,y_user)]="O"
                            tablero_maquina[(x_user-2,y_user)]="O"
                            tablero_maquina[(x_user-3,y_user)]="O"
                    elif orientacion=="S":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            (y_user<3 and tablero_maquina[x_user+2,y_user]=="O") or \
                            ((x_user<3 and y_user!=0) and tablero_maquina[x_user+2,y_user-1]=="O") \
                            or ((x_user<3 and y_user!=4) and tablero_maquina[x_user+2,y_user+1]=="O") or \
                            (x_user<2 and tablero_maquina[x_user+3,y_user]=="O") or \
                            ((x_user<2 and y_user!=0) and tablero_maquina[x_user+3,y_user-1]=="O") \
                            or ((x_user<2 and y_user!=4) and tablero_maquina[x_user+3,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user<1 and y_user!=0) and tablero_maquina[x_user+4,y_user-1]=="O") or \
                            ((x_user<1 and y_user!=4) and tablero_maquina[x_user+4,y_user+1]=="O") or \
                            (x_user<1 and tablero_maquina[x_user+4,y_user]=="O"):
                                continue
                        else:        
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user+1,y_user)]="O"
                            tablero_maquina[(x_user+2,y_user)]="O"
                            tablero_maquina[(x_user+3,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user<4 and y_user<4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user<3) and tablero_maquina[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<3) and tablero_maquina[x_user-1,y_user+2]=="O") or \
                            (y_user<3 and tablero_maquina[x_user,y_user+2]=="O") or \
                            (y_user<2 and tablero_maquina[x_user,y_user+3]=="O") or \
                            ((x_user!=4 and y_user<2) and tablero_maquina[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<2) and tablero_maquina[x_user-1,y_user+3]=="O") or \
                            ((x_user<4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user<1) and tablero_maquina[x_user+1,y_user+4]=="O") or \
                            ((x_user!=0 and y_user<1) and tablero_maquina[x_user-1,y_user+4]=="O") or \
                            (y_user<1 and tablero_maquina[x_user,y_user+4]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user+1)]="O"
                            tablero_maquina[(x_user,y_user+2)]="O"
                            tablero_maquina[(x_user,y_user+3)]="O"
                        
                    elif orientacion=="O":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user>1) and tablero_maquina[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_maquina[x_user-1,y_user-2]=="O") or \
                            (y_user>1 and tablero_maquina[x_user,y_user-2]=="O") or \
                            (x_user>2 and tablero_maquina[x_user,y_user-3]=="O") or \
                            ((x_user!=4 and y_user>2) and tablero_maquina[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_maquina[x_user-1,y_user-3]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user>3) and tablero_maquina[x_user+1,y_user-4]=="O") or \
                            ((x_user!=0 and y_user>3) and tablero_maquina[x_user-1,y_user-4]=="O") or \
                            (x_user>3 and tablero_maquina[x_user,y_user-4]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user-1)]="O"
                            tablero_maquina[(x_user,y_user-2)]="O"
                            tablero_maquina[(x_user,y_user-3)]="O"  
            
            if i=="barco3": #Colocamos los barcos de eslora=3
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,5)
                    y_user=np.random.randint(0,5)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=1 and orientacion=="N"):
                        continue
                    if (x_user>=3 and orientacion=="S"):
                        continue
                    if (y_user<=1 and orientacion=="O"):
                        continue
                    if (y_user>=3 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_maquina[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_maquina[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=4) and tablero_maquina[x_user-2,y_user+1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_maquina[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=4) and tablero_maquina[x_user-3,y_user+1]=="O") or \
                            (y_user>2 and tablero_maquina[x_user-3,y_user]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user-1,y_user)]="O"
                            tablero_maquina[(x_user-2,y_user)]="O"
                            
                    elif orientacion=="S":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            (y_user<3 and tablero_maquina[x_user+2,y_user]=="O") or \
                            ((x_user<3 and y_user!=0) and tablero_maquina[x_user+2,y_user-1]=="O") or \
                            ((x_user<3 and y_user!=4) and tablero_maquina[x_user+2,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user<2 and y_user!=0) and tablero_maquina[x_user+3,y_user-1]=="O") or \
                            ((x_user<2 and y_user!=4) and tablero_maquina[x_user+3,y_user+1]=="O") or \
                            (x_user<2 and tablero_maquina[x_user+3,y_user]=="O"):
                                continue
                        else:        
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user+1,y_user)]="O"
                            tablero_maquina[(x_user+2,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user<4 and y_user<4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user<3) and tablero_maquina[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<3) and tablero_maquina[x_user-1,y_user+2]=="O") or \
                            (y_user<3 and tablero_maquina[x_user,y_user+2]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user<2) and tablero_maquina[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<2) and tablero_maquina[x_user-1,y_user+3]=="O") or \
                            (y_user<2 and tablero_maquina[x_user,y_user+3]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user+1)]="O"
                            tablero_maquina[(x_user,y_user+2)]="O"
                        
                    elif orientacion=="O":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user>1) and tablero_maquina[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_maquina[x_user-1,y_user-2]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user>2) and tablero_maquina[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_maquina[x_user-1,y_user-3]=="O") or \
                            (y_user>1 and tablero_maquina[x_user,y_user-2]=="O") or \
                            (x_user>2 and tablero_maquina[x_user,y_user-3]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user-1)]="O"
                            tablero_maquina[(x_user,y_user-2)]="O"
            
            if i=="barco2": #Colocamos los barcos de eslora=2
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora2+ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,5)
                    y_user=np.random.randint(0,5)
                    #print(x_user,y_user,orientacion)
                    if (x_user==0 and orientacion=="N"):
                        continue
                    if (x_user==4 and orientacion=="S"):
                        continue
                    if (y_user==0 and orientacion=="O"):
                        continue
                    if (y_user==4 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_maquina[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=4) and tablero_maquina[x_user-2,y_user+1]=="O") or \
                            (x_user>1 and tablero_maquina[x_user-2,y_user]=="O"):
                                continue        
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user-1,y_user)]="O"
                        
                    elif orientacion=="S":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            (x_user<3 and tablero_maquina[x_user+2,y_user]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user<3 and y_user!=0) and tablero_maquina[x_user+2,y_user-1]=="O") or \
                            ((x_user<3 and y_user!=4) and tablero_maquina[x_user+2,y_user+1]=="O"):
                                continue
                        else:        
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user+1,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            (y_user<3 and tablero_maquina[x_user,y_user+2]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user<3) and tablero_maquina[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<3) and tablero_maquina[x_user-1,y_user+2]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user+1)]="O"
                        
                    elif orientacion=="O":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            (y_user<3 and tablero_maquina[x_user,y_user-2]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user!=4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=4 and y_user<3) and tablero_maquina[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user<3) and tablero_maquina[x_user-1,y_user-2]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user-1)]="O"
            
            if i=="barco1": #Colocamos los barcos de eslora=1
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora1+ocup_eslora2+ocup_eslora3+ocup_eslora4: #Que el bucle no se detenga hasta que estén los 4 barcos dibujados
                    x_user=np.random.randint(0,5)
                    y_user=np.random.randint(0,5)
                    #print(x_user,y_user)
                    if tablero_maquina[x_user,y_user]=="O" or (x_user!=4 and tablero_maquina[x_user+1,y_user]=="O") \
                    or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                    (y_user!=4 and tablero_maquina[x_user,y_user+1]=="O") or \
                    ((x_user!=4 and y_user!=4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                    ((x_user!=4 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                    ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                    ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                    (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O"):
                        continue
                    else:
                        tablero_maquina[x_user,y_user]="O"
            
                            
            
        
                                
    
    
    if tamaño_tablero==3:
        for i in dict_barcos:
            
            if i=="barco4": #Colocamos los barcos de eslora=4
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,15)
                    y_user=np.random.randint(0,15)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=2 and orientacion=="N"):
                        continue
                    if (x_user>=12 and orientacion=="S"):
                        continue
                    if (y_user<=2 and orientacion=="O"):
                        continue
                    if (y_user>=12 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_maquina[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_maquina[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=14) and tablero_maquina[x_user-2,y_user+1]=="O") or \
                            (y_user>2 and tablero_maquina[x_user-3,y_user]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_maquina[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=14) and tablero_maquina[x_user-3,y_user+1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user>3 and y_user!=0) and tablero_maquina[x_user-4,y_user-1]=="O") or \
                            ((x_user>3 and y_user!=14) and tablero_maquina[x_user-4,y_user+1]=="O") or \
                            (y_user>3 and tablero_maquina[x_user-4,y_user]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user-1,y_user)]="O"
                            tablero_maquina[(x_user-2,y_user)]="O"
                            tablero_maquina[(x_user-3,y_user)]="O"
                    elif orientacion=="S":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            (y_user<13 and tablero_maquina[x_user+2,y_user]=="O") or \
                            ((x_user<13 and y_user!=0) and tablero_maquina[x_user+2,y_user-1]=="O") \
                            or ((x_user<13 and y_user!=14) and tablero_maquina[x_user+2,y_user+1]=="O") or \
                            (x_user<12 and tablero_maquina[x_user+3,y_user]=="O") or \
                            ((x_user<12 and y_user!=0) and tablero_maquina[x_user+3,y_user-1]=="O") \
                            or ((x_user<12 and y_user!=14) and tablero_maquina[x_user+3,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") \
                            or ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user<11 and y_user!=0) and tablero_maquina[x_user+4,y_user-1]=="O") \
                            or ((x_user<11 and y_user!=14) and tablero_maquina[x_user+4,y_user+1]=="O") or \
                            (x_user<11 and tablero_maquina[x_user+4,y_user]=="O"):
                                continue
                        else:        
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user+1,y_user)]="O"
                            tablero_maquina[(x_user+2,y_user)]="O"
                            tablero_maquina[(x_user+3,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user<14 and y_user<4) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=4) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user<13) and tablero_maquina[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<13) and tablero_maquina[x_user-1,y_user+2]=="O") or \
                            (y_user<13 and tablero_maquina[x_user,y_user+2]=="O") or \
                            (y_user<12 and tablero_maquina[x_user,y_user+3]=="O") or \
                            ((x_user!=14 and y_user<12) and tablero_maquina[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<12) and tablero_maquina[x_user-1,y_user+3]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user<11) and tablero_maquina[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<11) and tablero_maquina[x_user-1,y_user+4]=="O") or \
                            (y_user<11 and tablero_maquina[x_user,y_user+4]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user+1)]="O"
                            tablero_maquina[(x_user,y_user+2)]="O"
                            tablero_maquina[(x_user,y_user+3)]="O"
                        
                    elif orientacion=="O":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user>1) and tablero_maquina[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_maquina[x_user-1,y_user-2]=="O") or \
                            (y_user>1 and tablero_maquina[x_user,y_user-2]=="O") or \
                            (x_user>2 and tablero_maquina[x_user,y_user-3]=="O") or \
                            ((x_user!=14 and y_user>2) and tablero_maquina[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_maquina[x_user-1,y_user-3]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user>3) and tablero_maquina[x_user+1,y_user-4]=="O") or \
                            ((x_user!=0 and y_user>3) and tablero_maquina[x_user-1,y_user-4]=="O") or \
                            (x_user>3 and tablero_maquina[x_user,y_user-4]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user-1)]="O"
                            tablero_maquina[(x_user,y_user-2)]="O"
                            tablero_maquina[(x_user,y_user-3)]="O"
            
            if i=="barco3": #Colocamos los barcos de eslora=3
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,15)
                    y_user=np.random.randint(0,15)
                    #print(x_user,y_user,orientacion)
                    
                    if (x_user<=1 and orientacion=="N"):
                        continue
                    if (x_user>=13 and orientacion=="S"):
                        continue
                    if (y_user<=1 and orientacion=="O"):
                        continue
                    if (y_user>=13 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            (y_user>1 and tablero_maquina[x_user-2,y_user]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_maquina[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=14) and tablero_maquina[x_user-2,y_user+1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user>2 and y_user!=0) and tablero_maquina[x_user-3,y_user-1]=="O") or \
                            ((x_user>2 and y_user!=14) and tablero_maquina[x_user-3,y_user+1]=="O") or \
                            (y_user>2 and tablero_maquina[x_user-3,y_user]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user-1,y_user)]="O"
                            tablero_maquina[(x_user-2,y_user)]="O"
                            
                    elif orientacion=="S":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            (y_user<13 and tablero_maquina[x_user+2,y_user]=="O") or \
                            ((x_user<13 and y_user!=0) and tablero_maquina[x_user+2,y_user-1]=="O") \
                            or ((x_user<13 and y_user!=14) and tablero_maquina[x_user+2,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user<12 and y_user!=0) and tablero_maquina[x_user+3,y_user-1]=="O") or \
                            ((x_user<12 and y_user!=14) and tablero_maquina[x_user+3,y_user+1]=="O") or \
                            (x_user<12 and tablero_maquina[x_user+3,y_user]=="O"):
                                continue
                        else:        
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user+1,y_user)]="O"
                            tablero_maquina[(x_user+2,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user<14 and y_user<14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user<13) and tablero_maquina[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<13) and tablero_maquina[x_user-1,y_user+2]=="O") or \
                            (y_user<13 and tablero_maquina[x_user,y_user+2]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user<12) and tablero_maquina[x_user+1,y_user+3]=="O") or \
                            ((x_user!=0 and y_user<12) and tablero_maquina[x_user-1,y_user+3]=="O") or \
                            (y_user<12 and tablero_maquina[x_user,y_user+3]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user+1)]="O"
                            tablero_maquina[(x_user,y_user+2)]="O"
                        
                    elif orientacion=="O":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user>1) and tablero_maquina[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_maquina[x_user-1,y_user-2]=="O") or \
                            (y_user>1 and tablero_maquina[x_user,y_user-2]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user>2) and tablero_maquina[x_user+1,y_user-3]=="O") or \
                            ((x_user!=0 and y_user>2) and tablero_maquina[x_user-1,y_user-3]=="O") or \
                            (x_user>2 and tablero_maquina[x_user,y_user-3]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user-1)]="O"
                            tablero_maquina[(x_user,y_user-2)]="O"
            
            if i=="barco2": #Colocamos los barcos de eslora=2
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora2+ocup_eslora3+ocup_eslora4:
                    opciones_orientacion=["N","S","E","O"]
                    orientacion=np.random.choice(opciones_orientacion)
                    x_user=np.random.randint(0,15)
                    y_user=np.random.randint(0,15)
                    #print(x_user,y_user,orientacion)
                    if (x_user==0 and orientacion=="N"):
                        continue
                    if (x_user==14 and orientacion=="S"):
                        continue
                    if (y_user==0 and orientacion=="O"):
                        continue
                    if (y_user==14 and orientacion=="E"):
                        continue
                    if orientacion=="N":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user>1 and y_user!=0) and tablero_maquina[x_user-2,y_user-1]=="O") or \
                            ((x_user>1 and y_user!=14) and tablero_maquina[x_user-2,y_user+1]=="O") or \
                            (x_user>1 and tablero_maquina[x_user-2,y_user]=="O"):
                                continue        
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user-1,y_user)]="O"
                        
                    elif orientacion=="S":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            (x_user<13 and tablero_maquina[x_user+2,y_user]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user<13 and y_user!=0) and tablero_maquina[x_user+2,y_user-1]=="O") or \
                            ((x_user<13 and y_user!=14) and tablero_maquina[x_user+2,y_user+1]=="O"):
                                continue
                        else:        
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user+1,y_user)]="O"
                    
                    elif orientacion=="E":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            (y_user<13 and tablero_maquina[x_user,y_user+2]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user<13) and tablero_maquina[x_user+1,y_user+2]=="O") or \
                            ((x_user!=0 and y_user<13) and tablero_maquina[x_user-1,y_user+2]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user+1)]="O"
                        
                    elif orientacion=="O":
                        if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                            or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                            (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                            (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O") or \
                            (y_user>1 and tablero_maquina[x_user,y_user-2]=="O") or \
                            ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                            ((x_user!=0 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                            ((x_user!=14 and y_user!=14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                            ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                            ((x_user!=14 and y_user>1) and tablero_maquina[x_user+1,y_user-2]=="O") or \
                            ((x_user!=0 and y_user>1) and tablero_maquina[x_user-1,y_user-2]=="O"):
                                continue
                        else:
                            tablero_maquina[(x_user,y_user)]="O"
                            tablero_maquina[(x_user,y_user-1)]="O"
            
            if i=="barco1": #Colocamos los barcos de eslora=1
                while np.count_nonzero(tablero_maquina=="O")<ocup_eslora1+ocup_eslora2+ocup_eslora3+ocup_eslora4: #Que el bucle no se detenga hasta que estén los 4 barcos dibujados
                    x_user=np.random.randint(0,15)
                    y_user=np.random.randint(0,15)
                    #print(x_user,y_user)
                    if tablero_maquina[x_user,y_user]=="O" or (x_user!=14 and tablero_maquina[x_user+1,y_user]=="O") \
                    or (x_user!=0 and tablero_maquina[x_user-1,y_user]=="O") or \
                    (y_user!=14 and tablero_maquina[x_user,y_user+1]=="O") or \
                    ((x_user!=14 and y_user!=14) and tablero_maquina[x_user+1,y_user+1]=="O") or \
                    ((x_user!=14 and y_user!=0) and tablero_maquina[x_user+1,y_user-1]=="O") or \
                    ((x_user!=0 and y_user!=14) and tablero_maquina[x_user-1,y_user+1]=="O") or \
                    ((x_user!=14 and y_user!=0) and tablero_maquina[x_user-1,y_user-1]=="O") or \
                    (y_user!=0 and tablero_maquina[x_user,y_user-1]=="O"):
                        continue
                    else:
                        tablero_maquina[x_user,y_user]="O"
     
    #print("--Tablero de la máquina--")
    #print(tablero_maquina)
    return tablero_maquina
#4
'''Función Disparo Usuario:
	- Recibe el input del usuario (coord_x y coord_y) para orientar el disparo.
	- Si metes una coordenada fuera del rango, te obliga a repetir
	- Si el disparo:
		*impacta en un barco: Se sustituye la "O" por "X" y te mantiene en el bucle para que dispares otra vez.
		*impacta en el agua: Se sustituye el " " por "_" y te saca del bucle pasando el turno a la máquina.
		*impacta en una celda impactada previamente: Detecta que hay "X" o "_" y te manda repetir tirada.
	- Después de cada tirada, imprime tanto el tablero_usuario como el tablero_espejo.'''
 
def disparo_usuario(tamaño_tablero,tablero_copia,tablero_maquina,name):
    while True:
        if tamaño_tablero==2:
            disp_x=int(input("\nCoordenada de disparo x (entre 0 y 9): "))
            while (disp_x!=0 and disp_x!=1 and disp_x!=2 and disp_x!=3 and disp_x!=4 and disp_x!=5 and disp_x!=6 and disp_x!=7 and disp_x!=8 and disp_x!=9):
                disp_x=int(input("La coordinada 'x' debe ser un número entero entre 0 y 9: "))
                continue
            disp_y=int(input("Coordenada de disparo y (entre 0 y 9): "))
            while (disp_y!=0 and disp_y!=1 and disp_y!=2 and disp_y!=3 and disp_y!=4 and disp_y!=5 and disp_y!=6 and disp_y!=7 and disp_y!=8 and disp_y!=9):
                disp_y=int(input("La coordinada 'y' debe ser un número entero entre 0 y 9: "))
                continue
            
        elif tamaño_tablero==1:
            disp_x=int(input("\nCoordenada de disparo x (entre 0 y 4): "))
            while (disp_x!=0 and disp_x!=1 and disp_x!=2 and disp_x!=3 and disp_x!=4):
                disp_x=int(input("La coordinada 'x' debe ser un número entero entre 0 y 4: "))
                continue
            disp_y=int(input("Coordenada de disparo y (entre 0 y 4): "))
            while (disp_y!=0 and disp_y!=1 and disp_y!=2 and disp_y!=3 and disp_y!=4):
                disp_y=int(input("La coordinada 'y' debe ser un número entero entre 0 y 4: "))
                continue
        
        elif tamaño_tablero==3:
            disp_x=int(input("\nCoordenada de disparo x (entre 0 y 14): "))
            while (disp_x!=0 and disp_x!=1 and disp_x!=2 and disp_x!=3 and disp_x!=4 and disp_x!=5 and disp_x!=6 and disp_x!=7 and disp_x!=8 and disp_x!=9 and disp_x!=10 and disp_x!=11 and disp_x!=12 and disp_x!=13 and disp_x!=14):
                disp_x=int(input("La coordinada 'x' debe ser un número entero entre 0 y 14: "))
                continue
            disp_y=int(input("Coordenada de disparo y (entre 0 y 14): "))
            while (disp_y!=0 and disp_y!=1 and disp_y!=2 and disp_y!=3 and disp_y!=4 and disp_y!=5 and disp_y!=6 and disp_y!=7 and disp_y!=8 and disp_y!=9 and disp_y!=10 and disp_y!=11 and disp_y!=12 and disp_y!=13 and disp_y!=14):
                disp_y=int(input("La coordinada 'y' debe ser un número entero entre 0 y 14: "))
                continue

        
        if tablero_maquina[disp_x,disp_y]=="O":#"X" si da al barco y "-" si da al agua
            tablero_maquina[disp_x,disp_y]="X"
            tablero_espejo=tablero_maquina.copy()
            tablero_espejo_2=np.char.replace(tablero_espejo,"O"," ")
            print(f"--Tablero de {name}--")
            print(tablero_copia)
            print("\n")
            print("--Tablero de la máquina--")
            print(tablero_espejo_2)
            print("Has acertado!")
            if (np.count_nonzero(tablero_maquina=="O"))==0:
                break
            else: 
                print("Dispara otra vez")
        elif tablero_maquina[disp_x,disp_y]=="X" or tablero_maquina[disp_x,disp_y]=="-":
            tablero_espejo=tablero_maquina.copy()
            tablero_espejo_2=np.char.replace(tablero_espejo,"O"," ")
            print(f"--Tablero de {name}--")
            print(tablero_copia)
            print("\n")
            print("--Tablero de la máquina--")
            print(tablero_espejo_2)
            print("Ya has disparado a esa coordenada previamente, intenta otra vez")
        elif tablero_maquina[disp_x,disp_y]==" ":
            tablero_maquina[disp_x,disp_y]="-"
            tablero_espejo=tablero_maquina.copy()
            tablero_espejo_2=np.char.replace(tablero_espejo,"O"," ")
            print(f"--Tablero de {name}--")
            print(tablero_copia)
            print("\n")
            print("--Tablero de la máquina--")
            print(tablero_espejo_2)
            print("Has fallado. Turno de la máquina")
            print("\n")
            break
    return tablero_copia,tablero_maquina
    
#5     
'''Función Disparo Máquina:
	- Genera aleatoriamente una tirada (coord_x, coord_y) y dispara (dependiendo del tamaño del tablero, ajusta
	el límite)
	- Prácticamente lo mismo que Disparo Usuario
	- Tablero_espejo es un reflejo del Tablero_máquina donde se ven las tiradas anteriores pero no la posición
	de los barcos.'''   
 
def disparo_maquina(tamaño_tablero,tablero_copia,tablero_maquina,name):
    while True:
        while True:
            if tamaño_tablero==2:
                dispa_x=np.random.randint(0,10)
                dispa_y=np.random.randint(0,10)
                break
            elif tamaño_tablero==1:
                dispa_x=np.random.randint(0,5)
                dispa_y=np.random.randint(0,5)
                print(dispa_x,dispa_y)
                break
            elif tamaño_tablero==3:
                dispa_x=np.random.randint(0,15)
                dispa_y=np.random.randint(0,15)
                break

        if tablero_copia[dispa_x,dispa_y]=="O":#"X" si da al barco y "-" si da al agua
            tablero_copia[dispa_x,dispa_y]="X"
            tablero_espejo=tablero_maquina.copy()
            tablero_espejo_2=np.char.replace(tablero_espejo,"O"," ")
            print(f"--Tablero de {name}--")
            print(tablero_copia)
            print("\n")
            print("--Tablero de la máquina--")
            print(tablero_espejo_2)
            print("La máquina te ha dado!")
            print("\n")
            time.sleep(3)
            if (np.count_nonzero(tablero_copia=="O"))==0:
                break
        elif tablero_copia[dispa_x,dispa_y]=="X" or tablero_copia[dispa_x,dispa_y]=="-":
            continue
        elif tablero_copia[dispa_x,dispa_y]==" ":
            tablero_copia[dispa_x,dispa_y]="-"
            tablero_espejo=tablero_maquina.copy()
            tablero_espejo_2=np.char.replace(tablero_espejo,"O"," ")
            print(f"--Tablero de {name}--")
            print(tablero_copia)
            print("\n")
            print("--Tablero de la máquina--")
            print(tablero_espejo_2)
            print("La máquina ha fallado. Te toca de nuevo")
            print("\n")
            tablero_copia[dispa_x,dispa_y]="-"
            break
    return tablero_copia,tablero_maquina
        