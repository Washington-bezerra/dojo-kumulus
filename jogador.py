class jogador:

    def __init__(self, name, vida, forca, defesa, saude):
        self.name = name
        self.vida = vida
        self.forca = forca
        self.defesa = defesa
        self.saude = saude

    #Get
    def getName(self):
        return int(self.name)

    def getVida(self):
        return int(self.vida)

    def getForca(self):
        return int(self.forca)

    def getDefesa(self):
        return int(self.defesa)
    def getSaude(self):
        return int(self.saude)


    #Set
    def setName(self, nome):
        self.name = nome

    def setVida(self, vida):

        if self.vida >= 3:
            print("Limite maximo de vida atingido")
        else:
            self.vida = self.vida + vida
            if self.vida > 3:
                self.vida = 3

    def setForca(self, forca):
        if self.forca >= 1000:
            return "Limite maximo atingido"
        else:
            self.forca = self.forca + forca

    def setDefesa(self, defesa):
        if self.defesa >= 1000:
            return "Limite maximo atingigo"
        else:
            pass

    def setSaude(self, saude):
        if self.defesa >= 1000:
            return "Limite maximo de saude atingigo"
        else:
            self.saude = self.saude - saude
            if self.getSaude() <= 0:
                print("Sua saúde acabou, você morreu!")
                return False
