# generador de mazo sin estados #
# -*- coding:utf-8 -*- #

from random import *


#Establece las pintas disponibles#
def pintas():
    return ["Diamante","Pica","Corazón","Trebol"]
def nombres():
    return ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

def mazo(pinta,nombre):
    return [(x,y) for x in pinta for y in nombre]

def revolver(mazo): #Revuelve el mazo de cartas que tenemos# 
    print("Revolviendo cartas...")
    return sample(mazo,len(mazo))


def pide_carta(mano,mazo): #Pide una carta al dealer#
    mano.append(mazo[0])
    mazo.remove(mazo[0])

    return mazo

def valor_carta(carta): #Da un valor a la carta segun su nombre#
    if carta[1] == 'J':
        return 10
    elif carta[1] == 'Q':
        return 10
    elif carta[1] == 'K':
        return 10
    elif carta[1] == 'A':
        return 1
    else:
        return int(carta[1])
"""
def decide_as(suma): #Determina el valor del as#

    if suma <= 10: #Si tengo 10, se asume como 11#
        return 11
    else: #El jugador solo puede asumir la carta como 1#
        return 1
"""


def ver_mano_player(mano): #Imprime las cartas del jugador#
    print("Tienes estas cartas: "+ str(mano))

def ver_mano_casa(mano): #Imprime las cartas del dealer#
    print("La casa tiene: "+str(mano[0]))

def repartir(mazo,dealer,player): #Reparte las cartas al principio de la partida#
    print("Repartiendo las cartas")

    player.append(mazo[0])
    player.append(mazo[1])
    dealer.append(mazo[2])
    dealer.append(mazo[3])
    return mazo[4:]

def sumar_cartas(mano): #Toma cada carta y suma su valor#
    if mano == []:
        return 0
    else:
        return valor_carta(mano[0]) + sumar_cartas(mano[1:])


"""def jugar_maquina(mazo,mano):
    if sumar_cartas(mano) >= 17:
        return 
    else:
        return jugar_maquina(pide_carta(mazo,mano))

def quitar_cartas(mano,mazo):
    for x in mano:
        mazo.remove(mazo[mazo.index(x)])
    return mazo
"""    

def jugar(mazo,jugador,casa,estado,turno): #Empieza el juego de verdad#

    if turno == 1: #Empieza el turno de la maquina#
        print("El turno de la máquina comienza...")


    if  turno == 0 and estado == 0: #Empezar la partida revolviendo el mazo#
        jugar(revolver(mazo),jugador,casa,estado+1,turno)
    elif turno == 0 and estado == 1: #Repartiendo las cartas#
        jugar(repartir(mazo,casa,jugador),jugador,casa,estado+1,turno)
    elif turno == 0:
        print("Tu turno comienza...")
        ver_mano_player(jugador)
        print("Tienes:"+str(sumar_cartas(jugador)))
        ver_mano_casa(casa)
        
        if(sumar_cartas(jugador) >21):
            print("La casa GANA")
            return False
        else:
            print("¿Pides otra carta?")
            print("SI/NO (S/N)")
            if input()== 'S':
                jugar(pide_carta(jugador,mazo),jugador,casa,estado+1,turno)
            else: #Aqui empieza a jugar la maquina#
                jugar(mazo,jugador,casa,0,turno+1)
    

if __name__ == "__main__":
    print()
    print("21")
    print()
    jugar(mazo(pintas(),nombres()),[],[],0,0)


