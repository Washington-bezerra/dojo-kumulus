from jogador import jogador
from random import choice

def choice_campo ():
    return choice(["equipamento", "vida"])

nome = input("Informe o nome do guerreiro: ")


Jogador = jogador(nome, 3, 500, choice([100,200,300,400,500,600,700,800,900,1000]), 1000)

def batalha (Jogador):
    forca_inimigo = choice([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    defesa_inimigo = choice([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])


    if Jogador.forca > forca_inimigo:

        desc_saude = Jogador.getForca()-defesa_inimigo
        if desc_saude < 0:
            desc_saude = desc_saude*(-1)
        Jogador.setSaude(desc_saude)

        print(f"Voce matou o inimigo, a forca do inimigo era {forca_inimigo} e a sua forca era {Jogador.forca}")
        print(f"Vida: {Jogador.getVida()}\nForça: {Jogador.getForca()}\nDefesa: {Jogador.getDefesa()}\nSaúde: {Jogador.getSaude()}")

    elif Jogador.forca < forca_inimigo:

        Jogador.vida = Jogador.vida - 1
        desc_saude = Jogador.getForca() - defesa_inimigo
        if desc_saude < 0:
            desc_saude = desc_saude * (-1)
        Jogador.setSaude(desc_saude)

        print(f'>>>>>>{desc_saude}')
        print(f"Voce perdeu a batalha e uma vida, a forca do inimigo era {forca_inimigo} e a sua forca era {Jogador.forca}\nTotal de vidas {Jogador.vida}")
        print(f"Vida: {Jogador.getVida()}\nForça: {Jogador.getForca()}\nDefesa: {Jogador.getDefesa()}\nSaúde: {Jogador.getSaude()}")

    elif Jogador.forca == forca_inimigo:
        print("Voces empataram!!!")
        print(f"Vida: {Jogador.getVida()}\nForça: {Jogador.getForca()}\nDefesa: {Jogador.getDefesa()}\nSaúde: {Jogador.getSaude()}")

while Jogador.getVida() > 0 and Jogador.getSaude() > 0:
    campo = choice_campo()

    if Jogador.vida == 0:
        print("Vc morreu pq sua vida é 0")
        break

    elif campo == "equipamento":

        escolha_equipamento = choice(["forca", "defesa"])

        if escolha_equipamento == "forca":
            qtde_forca = choice([100,200,300])
            Jogador.setVida(qtde_forca)
            #Jogador.forca = Jogador.forca + qtde_forca
            print(f'Voce ganhou {qtde_forca} de forca, total: {Jogador.forca}')

        if escolha_equipamento == "defesa":

            qtde_defesa = choice([100,200,300])
            #Jogador.defesa = Jogador.defesa + qtde_defesa
            Jogador.setDefesa(qtde_defesa)
            print(f'Voce ganhou {qtde_defesa} de defesa, total: {Jogador.defesa}')

        batalha(Jogador)

    elif campo == "vida":
            qtde_vida = choice([1,2,3])
            #Jogador.vida = Jogador.vida + qtde_vida
            Jogador.setVida(qtde_vida)
            print(f'Voce ganhou {qtde_vida} vida(s), total: {Jogador.vida}')

    print('='*15)
    input("Digite algo para continuar")
