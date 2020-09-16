from filtros import *
from datetime import *


def gera_menu(printVar):
    num_repete = int(len(printVar))
    a = 1
    while a <= num_repete:
        a = str(a)
        print(a + " - " + printVar[a])
        a = int(a)
        a = a + 1

matricula = input("Digite sua matricula:")

gera_menu(regiao)
regiao_var = input("Selecione a região de acordo com o menu:")

gera_menu(tipo_servico)
servico_var = input("Selecione o tipo de serviço de acordo com o menu:")

gera_menu(criticidade)
criticidade_var = input("Selecione o nivel critico de acordo com o menu:")

#hj = date.today()
hj = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

abrechamado = open("chamados.txt", "a")
dadoschamado = list()
dadoschamado.append("\n" + matricula + ",")
dadoschamado.append(regiao_var + ",")
dadoschamado.append(servico_var + ",")
dadoschamado.append(criticidade_var + ",")
dadoschamado.append(hj)

abrechamado.writelines(dadoschamado)



