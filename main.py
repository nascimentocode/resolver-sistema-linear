# With → Maior aplicação: abertura e fechamento de arquivos
import csv
import numpy as np
from numpy.linalg import solve

def readCSV(pathFile):
    valuesCSV = []
    with open(pathFile, 'r') as file:
        for line in csv.reader(file, delimiter=","):
            temp = []
            for n in line:
                temp.append(int(n))

            valuesCSV.append(temp)

    return valuesCSV

def solveLinearSystem():
    system = readCSV("arquivo.csv")
    lineSystem = len(system)
    columnSystem = len(system[0])
    equalities = []

    for i in system:
        equality = i.pop(-1)
        equalities.append(equality)

    showInfoLinearSystem(system, lineSystem, columnSystem, equalities)

    result = solve(np.array(system), np.array(equalities))
    showResult(result)

def showInfoLinearSystem(system, lineSystem, columnSystem, equalities):
    print("----- Informações do Sistema Linear -----")
    print(f"Sistema:\n {np.array(system)}")
    print(f"Igualdades: {np.array(equalities)}")
    print(f"Número de linhas: {lineSystem}")
    print(f"Número de colunas: {columnSystem}")
    print("-----------------------------------------\n")

def showResult(result):
    print("Resultado:")
    for id, x in enumerate(result):
        print(f"    x{id+1} = {x}")


if __name__ == '__main__':
    solveLinearSystem()