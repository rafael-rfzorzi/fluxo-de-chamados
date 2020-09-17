
import os
import csv

with open("chamados.txt", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=',')
    leitor.__next__()
    for coluna in leitor:
        if coluna[1] == '1':
            abreregiao1 = open("regiao1.txt", "a")
            regiao1 = list()
            regiao1.append(coluna)
            abreregiao1.writelines(str(regiao1) + "\n")
        if coluna[1] == '2':
            abreregiao2 = open("regiao2.txt", "a")
            regiao2 = list()
            regiao2.append(coluna)
            abreregiao2.writelines(str(regiao2) + "\n")
        if coluna[1] == '3':
            abreregiao3 = open("regiao3.txt", "a")
            regiao3 = list()
            regiao3.append(coluna)
            abreregiao3.writelines(str(regiao3) + "\n")
        if coluna[1] == '4':
            abreregiao4 = open("regiao4.txt", "a")
            regiao4 = list()
            regiao4.append(coluna)
            abreregiao4.writelines(str(regiao4) + "\n")
    arquivo_csv.close()
    os.remove("chamados.txt")





