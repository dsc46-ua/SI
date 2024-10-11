import sys
from estado import *
from casilla import *
from math import sqrt

def Manhattan(origen, destino):
    return (abs(destino.getFila() - origen.getFila()) + abs(destino.getCol() - origen.getCol()))

def Euclidea(origen, destino):
    return sqrt(pow((destino.getFila() - origen.getFila()),2) + pow((destino.getCol() - origen.getCol()),2))
     
def Chebyshev(origen, destino):
    return max((destino.getFila() - origen.getFila()),(destino.getCol() - origen.getCol()))