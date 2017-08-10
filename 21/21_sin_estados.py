# generador de mazo sin estados #
# -*- coding:utf-8 -*- #


def pintas():
    return ["Diamante","Pica","Corazón","Trebol"]

def nombre_carta():
    return["A","2","3","4","5","6","7","8","9","10","J","Q","K"]


def crear_mazo(pinta,nombre):
    return [(x,y) for x in pinta for y in nombre]





