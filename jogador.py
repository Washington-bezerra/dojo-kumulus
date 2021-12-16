class jogador:

    def __init__(self, name, vida, forca, defesa):
        self.name = name
        self.vida = vida
        self.forca = forca
        self.defesa = defesa

    #Get
    def getName(self):
        return self.name

    def getVida(self):
        return self.vida

    def getForca(self):
        return self.forca

    def getDefesa(self):
        return self.defesa

    #Set
    def setName(self, nome):
        self.name = nome

    def setVida(self, vida):

        if self.vida >= 10:
            return "Limite maximo atingido"
        else:
            self.vida = self.vida + vida

    def setForca(self, forca):
        if self.forca >= 1000:
            return "Limite maximo atingido"
        else:
            self.forca = self.forca + forca

    def setDefesa(self, defesa):
        if self.defesa >= 1000:
            return "Limite maximo atingigo"
        else:
            self.defesa = self.defesa + defesa
