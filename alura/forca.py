def jogar():
    print("********************************")
    print("Bem vindo ao jogo da advinhação!")
    print("********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    acertou  = False
    enforcou = False

    while (not acertou and not enforcou):
        chute = input("Insira uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                #print("A letra {} esta na posicao {}".format(letra, index))
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)


    print("Fim do jogo!")

if __name__ == "__main__":
    jogar()