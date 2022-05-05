def tabela(listaHorarios, listaCodigos, dias):

    for elemento in listaHorarios:
        horarios_2 = elemento
        Seg = "        "
        Ter = "        "
        Qua = "        "
        Qui = "        "
        Sex = "        "
        Sab = "        "

        for digito in dias:
            if digito == '2':
                for elemento_1 in listaCodigos:
                    lista_1 = elemento_1.split()
                    if digito in lista_1[0]:
                        Seg = lista_1[1]
                        break
            elif digito == '3':
                for elemento_1 in listaCodigos:
                    lista_1 = elemento_1.split()
                    if digito in lista_1[0]:
                        Ter = lista_1[1]
                        break
            elif digito == '4':
                for elemento_1 in listaCodigos:
                    lista_1 = elemento_1.split()
                    if digito in lista_1[0]:
                        Qua = lista_1[1]
                        break
            elif digito == '5':
               for elemento_1 in listaCodigos:
                   lista_1 = elemento_1.split()
                   if digito in lista_1[0]:
                       Qui = lista_1[1]
                       break
            elif digito == '6':
                for elemento_1 in listaCodigos:
                    lista_1 = elemento_1.split()
                    if digito in lista_1[0]:
                        Sex = lista_1[1]
                        break
            elif digito == '7':
                for elemento_1 in listaCodigos:
                    lista_1 = elemento_1.split()
                    if digito in lista_1[0]:
                        Sab = lista_1[1]
                        break

        linha = "| "+PossiveisHorarios[horarios_2]+" | "+Seg + \
            " | "+Ter+" | "+Qua+" | "+Qui+" | "+Sex+" | "+Sab+" |"
        linhasDaTabela.append(linha)
        linhasDaTabela.sort()


def formatarDTH(turno, horarios):
    horarioFormatado = ""
    mesmoHorario = []
    for elemento_1 in horarios:
        if turno in elemento_1:
            mesmoHorario.append(elemento_1)
            horarios[horarios.index(elemento_1)] = ''
    for elemento_2 in mesmoHorario:
        for caractere in elemento_2:
            if caractere.isnumeric():
                horarioFormatado += caractere
            else:
                break
    horarioFormatado += turno
    entradaForamatada = codigoDaMateria+" "+horarioFormatado
    horariosUsados.append(entradaForamatada)
    while "" in horarios:
        horarios.remove("")


def analiseHorariosComuns(horariosComuns):
    listaHorarios = []
    listaCodigos = []
    dias = ""
    for elemento_1 in horariosComuns:
        lista_1 = elemento_1.split()
        diasTurnoHorario = lista_1[1]
        codigoDaMateria = lista_1[0]
        for caractere in diasTurnoHorario:
            if caractere.isnumeric() == False:
                horario_1 = diasTurnoHorario[diasTurnoHorario.find(
                    caractere)+1:]
                x = diasTurnoHorario[:diasTurnoHorario.find(caractere)]
                codigoComIdentificador = x+" "+codigoDaMateria
                listaCodigos.append(codigoComIdentificador)
                if len(listaHorarios) == 0:
                    for digito in horario_1:
                        horario_2 = caractere+digito
                        listaHorarios.append(horario_2)
                break
            else:
                dias += caractere
    tabela(listaHorarios, listaCodigos, dias)


def imprimirtabela():
    linha1 = "+---------------+----------+----------+----------+----------+----------+----------+"
    linha2 = "|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |"
    print(linha1)
    print(linha2)

    for elemento in linhasDaTabela:
        print(linha1)
        print(elemento)
    print(linha1)


def juntarHorariosComuns(horariosUsados, listaTurnos):
    for elemento_1 in listaTurnos:
        horariosComuns = []
        for elemento_2 in horariosUsados:
            if elemento_1 in elemento_2:
                horariosComuns.append(elemento_2)
        analiseHorariosComuns(horariosComuns)


def horariosOcupados(horarios, diasEHorariosOcupados):
    for elemento_1 in horarios:
        for caractere_1 in elemento_1:
            if caractere_1.isnumeric() == False:
                p = elemento_1.find(caractere_1)
                dias = elemento_1[:p]
                horario = elemento_1[p+1:]
                for caractere_2 in dias:
                    for caractere_3 in horario:
                        diaEHorarioUsado = caractere_2+caractere_1+caractere_3
                        if diaEHorarioUsado in diasEHorariosOcupados:
                            pass
                        else:
                            diasEHorariosOcupados.append(diaEHorarioUsado)
               

def verificarComando(horarios, diasEHorariosOcupados, codigoDaMateria, historicoDeCodigos):
    if entrada[0] == "+":
        for elemento_1 in horarios:
            for caractere_1 in elemento_1:
                if caractere_1.isnumeric() == False:
                    p = elemento_1.find(caractere_1)
                    dias = elemento_1[:p]
                    horario = elemento_1[p+1:]
                    for caractere_2 in dias:
                        for caractere_3 in horario:
                            diaEHorarioUsado = caractere_2+caractere_1+caractere_3
                            if diaEHorarioUsado in diasEHorariosOcupados:
                                print("!("+entrada+")")
                                return False
        historicoDeCodigos.append(codigoDaMateria)
        return True

    if entrada[0] == "-":
        temp_1= []
        temp_2= []
        if codigoDaMateria in historicoDeCodigos:
            for elemento_1 in horarios:
                for caractere_1 in elemento_1:
                    if caractere_1.isnumeric() == False:
                        p = elemento_1.find(caractere_1)
                        dias = elemento_1[:p]
                        horario = elemento_1[p+1:]
                        for caractere_2 in dias:
                            for caractere_3 in horario:
                                diaEHorarioUsado = caractere_2+caractere_1+caractere_3
                                turno = caractere_1+caractere_3
                                if diaEHorarioUsado in diasEHorariosOcupados:
                                    temp_1.append(diaEHorarioUsado)
                                    if turno in temp_2:
                                        pass
                                    else:
                                        temp_2.append(caractere_1+caractere_3)
                                else:
                                    print("!("+entrada+")")
                                    return False
            for elemento_2 in temp_1:
                if elemento_2 in diasEHorariosOcupados:
                    diasEHorariosOcupados.remove(elemento_2)
            historicoDeCodigos.remove(codigoDaMateria)
            for elemento_3 in temp_2:
                for elemento_4 in horariosUsados:
                    if elemento_3 in elemento_4:
                        horariosUsados.remove(elemento_4)
            for elemento_5 in temp_2:
                for elemento_6 in listaTurnos:
                    if elemento_5 == elemento_6:
                        listaTurnos.remove(elemento_6)           
            return False
        else:
            print("!("+entrada+")")
            return False

PossiveisHorarios = {
    "M1": "08:00 - 08:55",
    "M2": "08:55 - 09:50",
    "M3": "10:00 - 10:55",
    "M4": "10:55 - 11:50",
    "M5": "12:00 - 12:55",
    "T1": "12:55 - 13:50",
    "T2": "14:00 - 14:55",
    "T3": "14:55 - 15:50",
    "T4": "16:00 - 16:55",
    "T5": "16:55 - 17:50",
    "T6": "18:00 - 18:55",
    "N1": "19:00 - 19:50",
    "N2": "19:50 - 20:40",
    "N3": "20:50 - 21:40",
    "N4": "21:40 - 22:30", }

entrada = "iniciar"
listaTurnos = []
linhasDaTabela = []
horariosUsados = []
entradasFormatadas = []
historicoDeCodigos = []
diasEHorariosOcupados = []

while entrada != "Hasta la vista, beibe!":
    x = True
    while x == True:
        x = False
        entrada = input()
        if entrada == "?":
            juntarHorariosComuns(horariosUsados, listaTurnos)
            imprimirtabela()
            linhasDaTabela.clear()
            break
        else:
            lista_1 = entrada.split()
            codigoDaMateria = lista_1[1]
            horarios = lista_1[2:]
            if verificarComando(horarios, diasEHorariosOcupados, codigoDaMateria, historicoDeCodigos) == False:
                break
            horariosOcupados(horarios, diasEHorariosOcupados)
            entradaSemSinal = entrada[2:]
            while len(horarios) != 0:
                for elemento_1 in horarios:
                    for caractere in elemento_1:
                        if caractere.isnumeric() == False:
                            x = elemento_1.find(caractere)
                            dias = elemento_1[:x]
                            turno = elemento_1[x:]
                            if entradaSemSinal in horariosUsados:
                                pass
                            else:
                                formatarDTH(turno, horarios)
                                if turno in listaTurnos:
                                    break
                                else:
                                    listaTurnos.append(turno)
                                break
        break