import random  


def jogar():
    msg_bem_vindo()
    palavra_secreta = carregar_palavras()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    acertou  = False
    enforcou = False
    erros = 0
    tentativas = 6

    while (not acertou and not enforcou):

        chute = chute_do_usuario()

        if (chute in palavra_secreta):
            chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            tentativas -= 1
            if tentativas == 0:
                print("A letra {} nao existe na palavra. Acabou!!\n".format(chute, tentativas))
            else:
                print("A letra {} nao existe na palavra. Tente novamente! Restam {} tentativas!!\n".format(chute, tentativas))
            erros += 1
    
        acertou  = "_" not in letras_acertadas
        print(letras_acertadas)

        if (erros == 6):
            break
        if (acertou):
            break    

    if (acertou):
        jogo_ganho()
    else:
        jogo_perdido()


def carregar_palavras():
    arquivo  = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def msg_bem_vindo():
    print("********************************")
    print("Bem vindo ao jogo da advinhação!")
    print("********************************")


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1 

def jogo_ganho():
    print('Você ganhou!')

def jogo_perdido():
    print('Você perdeu!')

def chute_do_usuario():
    chute = input("Insira uma letra: ")
    chute = chute.strip().upper()
    return chute

if __name__ == "__main__":
    jogar()
    