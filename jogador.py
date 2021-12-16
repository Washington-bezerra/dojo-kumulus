class jogador:

    def __init__(self, name, vida, forca, defesa, saude):
        self.name = name
        self.vida = vida
        self.forca = forca
        self.defesa = defesa
        self.saude = saude

    #Get
    def getName(self):
        return self.name

    def getVida(self):
        return self.vida

    def getForca(self):
        return self.forca

    def getDefesa(self):
        return self.defesa

    def getSaude(self):
        return self.saude


    #Set
    def setName(self, nome):
        self.name = nome

    def setVida(self, vida):

        if self.vida >= 10:
            return print("Limite maximo de vida atingido")
        else:
            self.vida = self.vida + vida
            if self.vida > 10:
                self.vida = 10

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

    def setSaude(self, saude):
        if self.defesa >= 1000:
            return "Limite maximo atingigo"
        else:
            self.defesa = self.defesa + defesa