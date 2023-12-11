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
    "N4": "21:40 - 22:30",
}

ORDEM_HORARIOS = ["M1", "M2", "M3", "M4", "M5", "T1", "T2", "T3",
                   "T4", "T5", "T6", "N1", "N2", "N3", "N4"]
DIAS = ['2', '3', '4', '5', '6', '7']

# grade[(dia, slot)] = codigo_da_materia, ex.: grade[('3', 'M1')] = 'CIC0004B'
grade = {}


def slots_do_dth(dth):
    """'35M12' -> [('3','M1'), ('3','M2'), ('5','M1'), ('5','M2')]"""
    i = 0
    dias = ""
    while dth[i].isnumeric():
        dias += dth[i]
        i += 1
    turno = dth[i]
    horarios = dth[i + 1:]
    return [(dia, turno + h) for dia in dias for h in horarios]


def slots_da_instrucao(dths):
    slots = []
    for dth in dths:
        slots.extend(slots_do_dth(dth))
    return slots


def processar_instrucao(entrada):
    partes = entrada.split()
    sinal = partes[0]
    codigo = partes[1]
    slots = slots_da_instrucao(partes[2:])

    if sinal == "+":
        for slot in slots:
            if slot in grade:
                print("!(" + entrada + ")")
                return
        for slot in slots:
            grade[slot] = codigo

    elif sinal == "-":
        for slot in slots:
            if grade.get(slot) != codigo:
                print("!(" + entrada + ")")
                return
        for slot in slots:
            del grade[slot]


def imprimir_tabela():
    linha1 = "+---------------+----------+----------+----------+----------+----------+----------+"
    linha2 = "|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |"
    print(linha1)
    print(linha2)
    for slot in ORDEM_HORARIOS:
        celulas = [grade.get((dia, slot), "").ljust(8) for dia in DIAS]
        if any(c.strip() for c in celulas):
            print(linha1)
            print("| " + PossiveisHorarios[slot] + " | " + " | ".join(celulas) + " |")
    print(linha1)


entrada = ""
while entrada != "Hasta la vista, beibe!":
    entrada = input()
    if entrada == "Hasta la vista, beibe!":
        break
    if entrada == "?":
        imprimir_tabela()
    else:
        processar_instrucao(entrada)
