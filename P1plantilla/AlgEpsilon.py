import sys
from estado import *
from casilla import *
from heuristicas import *
from AlgEstrella import *

def getMin(listaFrontera):
    m = sys.maxsize
    for n in listaFrontera:
        if n.getSuma() < m:
            m = n.getSuma()         
    return m

def crearListaFocal(listaFrontera, epsilon):
    # Paso 1: Encontrar el valor mínimo de f(n) en listaFrontera
    f_min = getMin(listaFrontera)
    # Paso 2: Filtrar nodos en listaFrontera cuya f(n) no exceda (1 + ε) * f_min
    listaFocal = []
    for n in listaFrontera:
        if n.getSuma() <= (1 + epsilon) * f_min:
            listaFocal.append(n)
    return listaFocal

def obtenerMenorCalorias(listaFocal):
    menor = listaFocal[0]  # Inicializamos con el primer elemento
    for est in listaFocal:
        if est.getCalorias() < menor.getCalorias():
            menor = est
    return menor

def AlgEpsilon(origen, destino, mapi, camino, coste):
#------------------
    epsilon=0.3
#------------------
    listaInterior = []
    listaFrontera = [Estado(origen,0,0,Euclidea(origen, destino),None,0)]
    listaFocal = []
    calorias = 0
    while listaFrontera:
        
#NUEVO CODIGO A*e-----------------------------------------------------------------------        
        #Escogemos el estado de la frontera con menor valor de f
        n = obtenerMenor(listaFrontera)    
        listaFocal = crearListaFocal(listaFrontera, epsilon)
        
        # Escogemos el nodo con menos calorías en listaFocal
        n = obtenerMenorCalorias(listaFocal)
            
#---------------------------------------------------------------------------------------
        #Si es el destino se acaba el agoritmo
        if ((n.posicion.getFila() == destino.getFila()) and (n.posicion.getCol() == destino.getCol())):
            reconstruir(n, camino)
            coste = n.getSuma()
            calorias = n.getCalorias()
            return coste, calorias
        else:
            listaFrontera.remove(n)
            listaInterior.append(n)       
        #para cada hijo m de n que no esté en lista interior
            for m in obtenerHijos(n, mapi):
                if m not in listaInterior:
                    g_m = n.g + costeSalto(n,m)
                    
                    if m not in listaFrontera:
                        m.g = g_m
                        m.h = Euclidea(m.posicion, destino)
                        m.f = m.getSuma()
                        #Ya hemos añadido el padre en la funcion obtenerHijos
                        listaFrontera.append(m)
                    
                    elif g_m < m.g:
                        #Ya hemos añadido el padre en la funcion obtenerHijos
                        #recalcular f y g del nodo m
                        m.g = g_m
                        m.f = m.getSuma()
    #Error
    return -1, calorias