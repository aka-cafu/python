# Importando biblioteca random
import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo da advinhação!")
    print("********************************")

    # Definindo valor para o numero a ser advinhado - v1
    #numero_secreto = round(random.random() * 50)

    # Definindo valor para o numero a ser advinhado - v1
    numero_secreto = random.randrange(1,51)

    # Quantidade de tentativas
    qnt_tentativas = 0

    # Variavel que guarda a quantidade de pontos
    pontos = 1000

    # Incluindo niveis de dificuldade baseado na resposta do usuario
    print("Niveis de dificuldade")
    print("(1) Facil (2) Normal (3) Dificil\n")

    nivel_str = input("Escolha o nivel: ")
    nivel = int(nivel_str)

    if (nivel == 1):
        qnt_tentativas = 20
    elif (nivel == 2):
        qnt_tentativas = 10
    else:
        qnt_tentativas = 5

    # Laco enquanto (while) a condicao for verdadeira

    for rodada in range(1, qnt_tentativas + 1):
        # Obtendo valor de entrada do usuario - v2
        print("Tentativa {} de {}".format(rodada, qnt_tentativas))

        chute_str = input("Digite um numero: ")
        chute = int(chute_str)

        # Informar numero entre 1 e 50
        if (chute < 1 or chute > 50):
            print("Voce deve digitar um numero entre 1 e 50!")
            continue

        # Definindo valores de chute (se maior, menor ou chute correto)
        chute_certo = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto


        # Comparar o valor informado pelo usuario com o valor pre-definido
        if (chute_certo):
            print("Você acertou! Você fez {} pontos!".format(pontos))
            break
        else:
            if (chute_maior):
                print("Você errou! O seu chute foi maior que o numero secreto!")
            elif (chute_menor):
                print("Você errou! O seu chute foi menor que o numero secreto!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    # Final do programa
    print("Fim de jogo!")


if __name__ == "__main__":
    jogar()