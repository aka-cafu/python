import advinhacao
import forca

def escolha_jogo():
    print("********************************")
    print("****** Escolha o seu jogo! *****")
    print("********************************")

    print ("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo você escolhe?"))

    if (jogo == 1):
        print("Iniciando jogo da forca!")
        forca.jogar()
    elif (jogo == 2):
        print("Iniciando jogo da advinhação!")
        advinhacao.jogar()

if __name__ == "__main__":
    escolha_jogo()