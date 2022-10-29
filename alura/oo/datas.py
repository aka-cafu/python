# from datas import Data
# d = Data(21,11,2007)
# d.formatada()

class Data:
    def __init__(self, dia, mes, ano) -> str:
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatdata(self):
        print("{}/{}/{}".format(self.dia, self.mes,self.ano))

d = Data("10","05","1995")
d.formatdata()