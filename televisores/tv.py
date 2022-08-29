class TV:
    _numTV = 0
    def __init__(self,marca,estado):
        self._marca = marca
        self._canal = 1
        self._estado = estado
        self._volumen = 1
        self._precio = 500
        self._numTV += 1
    
    def getMarca(self):
        return self._marca
    def setMarca(self,marca):
        self._marca = marca
    
    def getCanal(self):
        return self._canal
    def setCanal(self,canal):
        if canal<120 and canal>1 and self._estado==True:
            self._canal = canal
    def canalUp(self):
        if self._canal<120 and self._estado==True:
            self._canal+=1
    def canalDown(self):
        if self._canal>1 and self._estado==True:
            self._canal-=1

    def getEstado(self):
        return self._estado
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False

    def getVolumen(self):
        return self._volumen
    def volumenUp(self):
        if self._volumen<7 and self._estado==True:
            self._volumen += 1
    def volumenDown(self):
        if self._volumen>0 and self._estado==True:
            self._volumen -= 1
    def setVolumen(self, val):
        if val >= 0 and val <= 7 and self._estado==True:
            self._volumen = val

    def getPrecio(self):
        return self._precio
    def setPrecio(self,precio):
        self._precio = precio

    def getControl(self):
        return self._control
    def setControl(self,control):
        self._control = control

    @classmethod
    def getNumTV(cls):
        return cls._numTV
    @classmethod
    def setNumTV(cls,num):
        cls._numTV = num