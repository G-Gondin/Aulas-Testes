def arqexiste(nome):
    try:
        a = open(nome, "rt")
    except FileNotFoundError:
        return False
    else:
        return True

def criararq(nome):
    a = open(nome, "wt+")
    a.close()

def cadastra_users(arq, name, region, city, age):
    try:
        a = open(arq, "at")
        a.write(f"{name},{region},{city},{age}")
        a.close()
    except:
        return "Houve um erro inesperado"
    else:
        return "Pessoa cadastrada com sucesso!"

def jogalist(arq):
    a = open(arq, "rt")
    tusuarios = []
    for c in a:
        tusuarios.append(c.split(","))
    a.close()
    return tusuarios

def limpalist(lix):
    n = lix.copy()
    n1 = lix.copy()
    temp = []
    for c in range(0, len(n1)):
        if n1.count(n1[c]) > 1:
            if temp.count(n1[c]) == 0:
                temp.append(n1[c])
            n.remove(n1[c])
    for c in range(0, len(temp)):
        n.append(temp[c])
    n.append(temp)
    return n