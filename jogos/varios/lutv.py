def titulo(n1):
    print("-" * 30)
    print("{:^30}".format(n1))
    print("-" * 30)

def linha():
    print("---" * 13)

def limpa():
    from time import sleep
    from os import system
    sleep(1)
    system("cls")

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

def cadastro(arq, nome="anonimo", lnome="anonimo", idade=0):
    from datetime import date
    try:
        data = date.today()
        a = open(arq, "at")
        a.write(f"{nome} {lnome} {idade} {data}")
        a.write("\n")
        a.close()
    except:
        return "Houve um erro inesperado"
    else:
        return "Pessoa cadastrada com sucesso!"

def lercadat(arq):
    def linha1():
        print("-" * 57)

    a = open(arq, "rt")
    linha1()
    for c in a:
        dado = c.split()
        print(f"{f"{dado[0]} {dado[1]}":<20}{f"{dado[2]} anos":<10} {f"Data de adição: {dado[3]}":>3}")
    linha1()
    a.close()

def sorteio():
    from random import randint
    while True:
        dice_scape_player = randint(1, 6)
        dice_scape = randint(1, 6)
        if dice_scape_player == dice_scape:
            continue
        if dice_scape_player < dice_scape:
            print()
            print(cor(f"Dado do saida: {dice_scape}", "ciano"))
            print(cor(f"Seu dado: {dice_scape_player}", "vermelho"))
            linha()
            print("Você tentou fugir mas recebeu um ataque covarde pelas costas e morreu.")
            return False

        if dice_scape_player > dice_scape:
            print()
            print(cor(f"Dado do saida: {dice_scape}", "ciano"))
            print(cor(f"Seu dado: {dice_scape_player}", "verde"))
            linha()
            print("Você se vira e consegue fugir dele, porém no meio do caminho encontra com outro monstro")
            return True
        break

def identmao1(jogad):
    n = []
    n = jogad.copy()
    print(n)
    if n[0][0] == n[1][0]:
        mao = "par"
    else:
        mao = "carta alta"
    return mao

def jogalis(jogad, comu):
    ls = []
    for c in range(0, 2):
        ls.append(jogad[c])
    for c in range(0, 5):
        ls.append(comu[c])
    return ls

def identmao(jogad, comu):
    ls = jogalis(jogad, comu)

    if ispar(ls) == True:
        mao = "Par"
    if is2par(ls) == True:
        mao = "Dois Pares"
    if istrinca(ls) == True:
        mao = "Trinca"
    if istrai(ls) == True:
        mao = "Straight"
    if isflush(ls) == True:
        mao = "Flush"
    if isfull(ls) == True:
        mao = "Full House"
    if isquadra(ls) == True:
        mao = "Quadra"
    if istraiflush(ls) == True:
        mao = "Straight Flush"
    if isroyal(ls) == True:
        mao = "Royal Flush"    
    else:
        mao = "Carta Alta"
    return mao