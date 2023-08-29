import csv
import os
from operator import itemgetter

def juncaoDeArquivos():
    txt = ""
    for arquivo in arquivos_lidos:
        with open(arquivo, 'r') as file:
            next(file)
            txt += file.read()
    with open("juncaoArquivos.csv", "w") as saida:
        saida.write(txt)

def codigoExiste(codigo):
    if len(arquivos_lidos) > 1:
        juncaoDeArquivos()
        for line in leia("juncaoArquivos.csv"):
            if codigo == line[0]:
                return True
        return False
    else:
        if len(arquivos_lidos) == 0:
            return False
        else:
            for line in leia(arquivos_lidos[-1]):
                if codigo == line[0]:
                    return True
            return False

def nomeExiste(nome):
    if len(arquivos_lidos) > 1:
        juncaoDeArquivos()
        for line in leia("juncaoArquivos.csv"):
            if nome in line[4]:
                return True
        return False
    else:
        if len(arquivos_lidos) == 0:
            return False
        else:
            for line in leia(arquivos_lidos[-1]):
                if nome in line[4]:
                    return True
            return False    

def juntarTurmasComunsDaMesmaMateria(infDoDocente):
    fimDoWhile = len(infDoDocente)
    while fimDoWhile > 0:
        temp = []
        verificador = infDoDocente[0][0]
        for materia_1 in infDoDocente:
            if verificador in materia_1:
                temp.append(materia_1)
                infDoDocente[infDoDocente.index(materia_1)] = ""
        if len(temp) > 1:
            listaAJustada = [verificador]
            for materia_2 in temp:
                listaAJustada.append(materia_2[1])
            infDoDocente.append(listaAJustada)
            fimDoWhile -= len(listaAJustada)-1
        else:
            infDoDocente.append(temp[0])
            fimDoWhile -= 1
        while "" in infDoDocente:
            infDoDocente.remove("")

def separarNomeCargaHoraria(linha):
    nomeDocente = linha[4].split("(")[0].strip()
    cargaHorariaDocente = linha[4].split("(")[1].split(")")[0].strip()
    return [nomeDocente, cargaHorariaDocente]

def leia(arquivo):
    if os.path.isfile(arquivo):
        with open(arquivo, encoding="utf-8") as csv_file:
            next(csv_file)
            matriz_csv_file = csv.reader(csv_file)
            if arquivo in arquivos_lidos or arquivo == "juncaoArquivos.csv":
                pass
            else:
                arquivos_lidos.append(arquivo)
            return list(matriz_csv_file)
    else:
        print("O arquivo não existe")

def carga(nome):
    if nomeExiste(nome) == True:
        if len(arquivos_lidos) != 0:
            print(nome+":")
            infDoDocente = []
            totalDeAlunos = 0
            totalDeHoras = 0
            if len(arquivos_lidos) > 1:
                juncaoDeArquivos()
                ordenadaPelaTurma = sorted(
                    leia("juncaoArquivos.csv"), key=itemgetter(2))
                for linha in ordenadaPelaTurma:
                    if "Código" in linha:
                        ordenadaPelaTurma.remove(linha)
                for linha in ordenadaPelaTurma:
                    if separarNomeCargaHoraria(linha)[0] == nome:
                        materiaCodigo = " * "+linha[1]+" ("+linha[0]+"):"
                        turmaCargaHorariaQuantAlunos = "     Turma " + \
                            linha[2]+": " + \
                            separarNomeCargaHoraria(
                                linha)[1]+" ("+linha[7]+" alunos)"
                        infDoDocente.append(
                            [materiaCodigo, turmaCargaHorariaQuantAlunos])
                        if int(linha[7]) >= 6:
                            totalDeAlunos += int(linha[7])
                            totalDeHoras += int(separarNomeCargaHoraria(linha)[1].replace("h", ""))
                juntarTurmasComunsDaMesmaMateria(infDoDocente)
                ordenada = sorted(infDoDocente)
                for a in ordenada:
                    for b in a:
                        print(b)
                if totalDeAlunos != 0 and totalDeHoras != 0:
                    print(f"[Carga total considerada: {totalDeHoras}h ({totalDeHoras/totalDeAlunos:.2f}h/aluno)]")
                else:
                    print(f"[Carga total considerada: 0h (0.00h/aluno)]")
            else:
                ordenadaPelaTurma = sorted(leia(arquivos_lidos[-1]), key=itemgetter(2))
                for linha in ordenadaPelaTurma:
                    if separarNomeCargaHoraria(linha)[0] == nome:
                        materiaCodigo = " * "+linha[1]+" ("+linha[0]+"):"
                        turmaCargaHorariaQuantAlunos = "     Turma " + \
                            linha[2]+": " + \
                            separarNomeCargaHoraria(
                                linha)[1]+" ("+linha[7]+" alunos)"
                        infDoDocente.append(
                            [materiaCodigo, turmaCargaHorariaQuantAlunos])
                        if int(linha[7]) >= 6:
                            totalDeAlunos += int(linha[7])
                            totalDeHoras += int(separarNomeCargaHoraria(linha)
                                                [1].replace("h", ""))
                juntarTurmasComunsDaMesmaMateria(infDoDocente)
                ordenada = sorted(infDoDocente)
                for a in ordenada:
                    for b in a:
                        print(b)
                if totalDeAlunos != 0 and totalDeHoras != 0:
                    print(f"[Carga total considerada: {totalDeHoras}h ({totalDeHoras/totalDeAlunos:.2f}h/aluno)]")
                else:
                    print(f"[Carga total considerada: 0h (0.00h/aluno)]")
        else:
            print(f"No hay {nome}...")
    else:
        print(f"No hay {nome}...")

def matriculas(listCodigos):
    dic_codigos = {}
    list_definitiva = []
    if len(arquivos_lidos) != 0:
        for codigo in listCodigos:
            if codigoExiste(codigo) == True:
                dic_codigos[codigo] = ["", []]
            else:
                listCodigos[listCodigos.index(codigo)] = ""
                print("No hay "+codigo+"...")
        while "" in listCodigos:
            listCodigos.remove("")
        for codigo in listCodigos:
            historicoDeTurmasContadas = []
            if len(arquivos_lidos) > 1:
                juncaoDeArquivos()
                for line in leia("juncaoArquivos.csv"):
                    if codigo == line[0]:
                        if dic_codigos[codigo][0] == "":
                            dic_codigos[codigo][0] = line[1]
                            dic_codigos[codigo][1].append(int(line[7]))
                            historicoDeTurmasContadas.append(line[2])
                        else:
                            if line[2] in historicoDeTurmasContadas:
                                pass
                            else:
                                dic_codigos[codigo][1].append(int(line[7]))
                                historicoDeTurmasContadas.append(line[2])
            else:
                for line in leia(arquivos_lidos[-1]):
                    if codigo == line[0]:
                        if dic_codigos[codigo][0] == "":
                            dic_codigos[codigo][0] = line[1]
                            dic_codigos[codigo][1].append(int(line[7]))
                            historicoDeTurmasContadas.append(line[2])
                        else:
                            if line[2] in historicoDeTurmasContadas:
                                pass
                            else:
                                dic_codigos[codigo][1].append(int(line[7]))
                                historicoDeTurmasContadas.append(line[2])
        for chave_1 in dic_codigos:
            conversao = [dic_codigos[chave_1][0] +" ("+chave_1+")", -1*sum(dic_codigos[chave_1][1])]
            list_definitiva.append(tuple(conversao))
        ordenada = sorted(list_definitiva, key=itemgetter(1, 0))
        for linha in ordenada:
            print(str(-1*linha[1])+" matriculados em "+linha[0])
    else:
        for codigo in listCodigos:
            print("No hay "+codigo+"...")

def disciplina(numero):
    list_org = []
    dict_materia = {}
    dict_definitivo = {}
    if len(arquivos_lidos) != 0:
        if len(arquivos_lidos) > 1:
            juncaoDeArquivos()
            for line_1 in leia("juncaoArquivos.csv"):
                codigoNomeTurma = "|".join(line_1[:3])
                dict_materia[codigoNomeTurma] = 0
                for line_2 in leia("juncaoArquivos.csv"):
                    verificadorDeLinha = "|".join(line_2[:3])
                    if verificadorDeLinha == codigoNomeTurma:
                        dict_materia[codigoNomeTurma] += 1
            for chave in dict_materia:
                if dict_materia[chave] >= int(numero):
                    lista_chave = chave.split("|")
                    lista_temp = [lista_chave[1]+" ("+lista_chave[0]+"): ", lista_chave[2], " ("+str(dict_materia[chave])+"), "]
                    list_org.append(lista_temp)
            if len(list_org) > 0:
                ordenada = sorted(list_org)
                for list_3 in ordenada:
                    dict_definitivo[list_3[0]] = []
                    for list_4 in ordenada:
                        if list_3[0] == list_4[0]:
                            temp = list_4[1:3]
                            dict_definitivo[list_3[0]].append(temp)
                print("Turmas com pelo menos "+str(numero)+" docentes:")
                for key in dict_definitivo:
                    string = " * "
                    string += key
                    for valor in dict_definitivo[key]:
                        string += valor[0]
                        string += valor[1]
                    print(string[:-2])
            else:
                print("No hay "+numero+"...")
        else:
            for line_1 in leia(arquivos_lidos[-1]):
                codigoNomeTurma = "|".join(line_1[:3])
                dict_materia[codigoNomeTurma] = 0
                for line_2 in leia(arquivos_lidos[-1]):
                    verificadorDeLinha = "|".join(line_2[:3])
                    if verificadorDeLinha == codigoNomeTurma:
                        dict_materia[codigoNomeTurma] += 1
            for chave in dict_materia:
                if dict_materia[chave] >= int(numero):
                    lista_chave = chave.split("|")
                    lista_temp = [
                        lista_chave[1]+" ("+lista_chave[0]+"): ", lista_chave[2], " ("+str(dict_materia[chave])+"), "]
                    list_org.append(lista_temp)
            if len(list_org) > 0:
                ordenada = sorted(list_org)
                for list_3 in ordenada:
                    dict_definitivo[list_3[0]] = []
                    for list_4 in ordenada:
                        if list_3[0] == list_4[0]:
                            temp = list_4[1:3]
                            dict_definitivo[list_3[0]].append(temp)
                print("Turmas com pelo menos "+str(numero)+" docentes:")
                for key in dict_definitivo:
                    string = " * "
                    string += key
                    for valor in dict_definitivo[key]:
                        string += valor[0]
                        string += valor[1]
                    print(string[:-2])
            else:
                print("No hay "+numero+"...")
    else:
        print("No hay "+numero+"...")

entrada = "começo"
arquivos_lidos = []

while entrada != "FIM":
    entrada = input()
    lista_entrada = entrada.split()
    if lista_entrada[0] == "leia":
        leia(lista_entrada[1])
    elif lista_entrada[0] == "carga":
        carga(" ".join(lista_entrada[1:]))
    elif lista_entrada[0] == "disciplina":
        disciplina(lista_entrada[1])
    elif lista_entrada[0] == "matriculas":
        matriculas(lista_entrada[1:])
