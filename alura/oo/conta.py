

# class Conta:
#     pass

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor
        print("O deposito de {}. Foi realizado!".format(valor))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("O saque no valor {}. Foi realizado!".format(valor))
        else:
            print("O valor {} ultrapassa o seu limite disponivel!".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return {"BB" : "001", "ITAU" : "341", "CAIXA" : "104"}

    # def get_saldo(self):
    #     return self.__saldo

    # def get_titular(self):
    #     return self.__titular

    # def get_limite(self):
    #     return self.__limite

    # def set_limite(self, limite):
    #     self.__limite = limite

# numero = 123
# titular = "Felipe"
# saldo = 55.5
# limite = 1550.5

# conta = Conta(numero, titular, saldo, limite)

# print("Nova conta criada!\n\nNumero: {}\nTitular: {}\nSaldo: {}\nLimite: {}".format(numero, titular, saldo, limite))
