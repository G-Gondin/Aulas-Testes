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

def cor(msg, cor="branco"):
    import colorama
    colorama.init()
    color = {
        "vermelho": colorama.Fore.RED,
        "verde": colorama.Fore.GREEN,
        "amarelo": colorama.Fore.YELLOW,
        "azul": colorama.Fore.BLUE,
        "preto": colorama.Fore.BLACK,
        "ciano": colorama.Fore.CYAN,
        "magenta": colorama.Fore.MAGENTA,
        "branco": colorama.Fore.WHITE,
        "reset": colorama.Fore.RESET}
    n1 = f"{color[f'{cor}']}{msg}{color['reset']}"
    return n1

def linha():
    print("---" * 13)

def cadastro_prod(arq, cod, nome, preco=0):
    from datetime import date
    try:
        data = date.today()
        a = open(arq, "at")
        a.write(f"{cod} {nome} {preco} {data}")
        a.write("\n")
        a.close()
    except:
        return "Houve um erro inesperado"
    else:
        return "Produto cadastrada com sucesso!"

def lercadat_prod(arq):
    def linha1():
        print("-" * 57)

    a = open(arq, "rt")
    linha1()
    for c in a:
        dado = c.split()
        print(f"{f"{dado[0]} {dado[1]}":<25}\t {f"R$ {dado[2]} Data: {dado[3]}":>2}")
    linha1()
    a.close()

def alt_arq_cadat(arq, cod):
    a = open(arq, "rt")
    produtos = []
    for c in a:
        dado = c.split()
        produtos.append(dado)
    a.close()
    n1 = cod
    for c in range(0, len(produtos)):
        n = produtos[c][0]
        if n1 == n:
            lis = produtos[c]
            produtos.remove(lis)
            break
    ops = str(input("""Deseja alterar algum dado ou removelo? [A/R] """)).strip().upper()
    if ops not in "AR" or ops == "" or len(ops) > 1:
        while ops not in "AR" or ops == "" or len(ops) > 1:
            ops = str(input(cor("Erro! Digite novamente: ", "vermelho"))).strip().upper()
    if ops == "A":
        n1 = str(input("""[1] código
[2] Nome
[3] Preço
Qual dado você quer alterar? """)).strip()
        if n1 not in "123" or n1 == "" or len(n1) > 1:
            while n1 not in "123" or n1 == "" or len(n1) > 1:
                n1 = str(input(cor("Erro! Digite novamente: ", "vermelho"))).strip()
        if n1 == "1":
            new = str(input("Digite o novo código: "))
            lis[0] = new
        if n1 == "2":
            new = str(input("Digite o novo nome: "))
            lis[1] = new
        if n1 == "3":
            while True:
                try:
                    new = int(input("Digite o novo preço: "))
                    lis[2] = new
                except:
                    continue
                else:
                    break
        produtos.append(lis)
        a = open(arq, "wt")
        for c in range(0, len(produtos)):
            cadastro_prod(arq, produtos[c][0], produtos[c][1], produtos[c][2])
        return "Alteração realizada com sucesso."
    if ops == "R":
        a = open(arq, "wt")
        for c in range(0, len(produtos)):
            cadastro_prod(arq, produtos[c][0], produtos[c][1], produtos[c][2])
        return "Produto removido com sucesso!"

def verify_in(arq, ver):
    n1 = open(arq, "rt")
    for c in n1:
        lis = c.split()
        if lis[0] == ver:
            n1.close()
            return True
    else:
        n1.close()
        return False

def pull_dados(arq, ver):
    n1 = open(arq, "rt")
    for c in n1:
        lis = c.split()
        if lis[0] == ver:
            n1.close()
            return lis
