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

while (rodada <= qnt_tentativas):
    # Obtendo valor de entrada do usuario - v2
    print("Tentativa {} de {}".format(rodada, qnt_tentativas))
    chute = int(input("Digite um numero: "))

    # Definindo valores de chute (se maior, menor ou chute correto)
    chute_certo = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto


    # Comparar o valor informado pelo usuario com o valor pre-definido
    if (chute_certo):
        print("Você acertou!")
    else:
        if (chute_maior):
            print("Você errou! O seu chute foi maior que o numero secreto!")
        elif (chute_menor):
            print("Você errou! O seu chute foi menor que o numero secreto!")

    # Aumentando a quantidade de tentativas
    rodada = rodada + 1

# Final do programa
print("Fim de jogo!")