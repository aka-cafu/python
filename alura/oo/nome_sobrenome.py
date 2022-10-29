class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibe_nome_e_sobrenome(self):
        print("{} {}".format(self.nome, self.sobrenome))

pessoa = Pessoa("Felipe", "Gomes")
pessoa.exibe_nome_e_sobrenome()