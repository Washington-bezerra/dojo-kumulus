from jogador import jogador
from random import choice

def choice_campo ():
    return choice(["equipamento", "vida"])

nome = input("Informe o nome do guerreiro: ")


Jogador = jogador(nome, 5, 500, choice([100,200,300,400,500,600,700,800,900,1000]))

def batalha (Jogador):
    forca_inimigo = choice([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    if Jogador.forca > forca_inimigo:
        return print(f"Voce matou o inimigo, a forca do inimigo era {forca_inimigo} e a sua forca era {Jogador.forca}")

    elif Jogador.forca < forca_inimigo:
        Jogador.vida = Jogador.vida - 1
        return print(f"Voce perdeu a batalha e uma vida, a forca do inimigo era {forca_inimigo} e a sua forca era {Jogador.forca}\nTotal de vidas {Jogador.vida}")

    elif Jogador.forca == forca_inimigo:
        return print("Voces empataram!!!")


while Jogador.vida >= 0:
    campo = choice_campo()

    if Jogador.vida == 0:
        print("Vc morreu pq sua vida é 0")
        break

    elif campo == "equipamento":

        escolha_equipamento = choice(["forca", "defesa"])

        if escolha_equipamento == "forca":
            qtde_forca = choice([100,200,300])
            Jogador.forca = Jogador.forca + qtde_forca
            print(f'Voce ganhou {qtde_forca} de forca, total: {Jogador.forca}')

        if escolha_equipamento == "defesa":

            qtde_defesa = choice([100,200,300])
            Jogador.defesa = Jogador.defesa + qtde_defesa
            print(f'Voce ganhou {qtde_defesa} de defesa, total: {Jogador.defesa}')

        batalha(Jogador)

    elif campo == "vida":
            qtde_vida = choice([1,2,3])
            Jogador.vida = Jogador.vida + qtde_vida
            print(f'Voce ganhou {qtde_vida} vida(s), total: {Jogador.vida}')

    print('='*15)
    input("Digite algo para continuar")
