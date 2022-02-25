print("********************************")
print("Bem vindo ao jogo da advinhação!")
print("********************************")

# Definindo valor para o numero a ser advinhado
numero_secreto = 42

# Quantidade de tentativas
qnt_tentativas = 3 

# Rodadas
rodada = 1 

# Laco enquanto (while) a condicao for verdadeira

for rodada in range(rodada, qnt_tentativas + 1):
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
        print("Você acertou!")
        break
    else:
        if (chute_maior):
            print("Você errou! O seu chute foi maior que o numero secreto!")
        elif (chute_menor):
            print("Você errou! O seu chute foi menor que o numero secreto!")

# Final do programa
print("Fim de jogo!")