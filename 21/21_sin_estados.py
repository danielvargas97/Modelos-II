# generador de mazo sin estados #
# -*- coding:utf-8 -*- #

from random import *


#Establece las pintas disponibles#
def pintas():
    return ["Diamante","Pica","Corazón","Trebol"]


#Establece el nombre de las cartas#
def nombre_carta():
    return["A","2","3","4","5","6","7","8","9","10","J","Q","K"]


#Crea un mazo con las cartas en orden#
def crear_mazo(pinta,nombre):
    return [(x,y) for x in pinta for y in nombre]


#Revuelve las cartas en el mazo#
def revolver_mazo(mazo):
    return sample(mazo,len(mazo))


#Genera un mazo con cartas revueltas#
def mazo():
    return revolver_mazo(crear_mazo(pintas(),nombre_carta()))


#Le da las cartas al jugador#
def inicia_jugador(mazo):
    return mazo[0:2]

#Le da las cartas a la maquina#
def inicia_com(mazo):
    return mazo[2:4]


#Inicia el juego#
def iniciar_partida(mazo):
    return [mazo[4:],inicia_jugador(mazo),inicia_com(mazo)]



if __name__ == "__main__":
    
    print(iniciar_partida(mazo())[1:])
