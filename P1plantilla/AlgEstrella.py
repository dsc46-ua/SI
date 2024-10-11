import sys
from estado import *
from casilla import *
from heuristicas import *


def obtenerMenor(lista):
    menorSuma = sys.maxsize
    for estado in lista:
        suma = estado.getF()
        if suma < menorSuma:
            menorSuma = suma
            menor = estado
    return menor
            
def obtenerHijos(padre, mapi):
    x = padre.posicion.getFila()
    y = padre.posicion.getCol()
    hijos = []
    for i in [x-1,x,x+1]:
        for j in [y-1,y,y+1]:
            if i == x and j == y:
                continue
            #Comprobamos si es pared y añadimos calorias
            if mapi.getCelda(i,j)!=1:
                hijoPos = Casilla(i,j)
                if mapi.getCelda(i,j)==0:
                    hijo = Estado(hijoPos, 0, 0, 0, padre, padre.getCalorias() + 2)
                    hijos.append(hijo)
                elif mapi.getCelda(i,j)==4:
                    hijo = Estado(hijoPos, 0, 0, 0, padre, padre.getCalorias() + 4)
                    hijos.append(hijo)
                elif mapi.getCelda(i,j)==5:
                    hijo = Estado(hijoPos, 0, 0, 0, padre, padre.getCalorias() + 6)
                    hijos.append(hijo)
                                    
    return hijos

def costeSalto(n,m):
    x = n.posicion.getFila() - m.posicion.getFila()
    y = n.posicion.getCol() - m.posicion.getCol()
    #Usando el absoluto de la diferencia sabemos si es diagonal o hor/ver
    if (abs(x) + abs(y)) == 2:
        return 1.5
    else:
        return 1

def reconstruir(nodoFinal, camino):
    nodo = nodoFinal
    while nodo is not None:
        fila = nodo.posicion.getFila()
        col = nodo.posicion.getCol()
        
        camino[fila][col] = 'x'
        nodo = nodo.padre


def AlgEstrella(origen, destino, mapi, camino, coste):
    listaInterior = []
    listaFrontera = [Estado(origen,0,0,Euclidea(origen, destino),None,0)]
    calorias = 0
    while listaFrontera:
        #Escogemos el estado de la frontera con menor valor de f
        n = obtenerMenor(listaFrontera)
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
                        m.f = m.getF()
                        #Ya hemos añadido el padre en la funcion obtenerHijos
                        listaFrontera.append(m)
                    
                    elif g_m < m.g:
                        #Ya hemos añadido el padre en la funcion obtenerHijos
                        #recalcular f y g del nodo m
                        m.g = g_m
                        m.f = m.getF()
    #Error
    return -1, calorias
