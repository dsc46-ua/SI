from casilla import *

class Estado():
    def __init__(self,posicion, f, g, h, padre, calorias):
        self.posicion = posicion
        self.f = f
        self.g = g
        self.h = h
        self.padre = padre
        self.calorias = calorias
        
    def getPos (self):
        return self.posicion
    
    def getF (self):
        #Base
        #return (self.g + self.h)
        
        #Ajuste Euclidea
        w = 0.35
        return ((1-w)*self.g + w*self.h)
    
        #Ajuste Chebyshev
        #w = 0.25
        #return ((1-w)*self.g + w*self.h)
    
    def getSuma (self):
        return (self.g + self.h)
    
    def getCosteActual (self):
        return self.g
    
    def getCosteEstimado (self):
        return self.h
    
    def getPadre (self):
        return self.padre
    
    def getCalorias (self):
        return self.calorias
    
    def __eq__(self, other):
        return self.posicion.getFila() == other.posicion.getFila() and self.posicion.getCol() == other.posicion.getCol()  
