def limpa():
    from time import sleep
    from os import system
    sleep(0.5)
    system("cls")

def identmao(mes):
    n = []
    for c in range(0, 2):
        n.append(mes[c]["carta"])
    if n[0] == n[1]:
        mao = "par"
    else:
        mao = "carta alta"
    return mao

def ispar(cart):
    cards = []
    for c in range(0, len(cart)):
        cards.append(cart[c]['carta'])
    repetidos = []
    for c in range(0, len(cards)):
        if cards.count(cards[c]) == 2:
            if len(repetidos) == 0:
                repetidos.append(cards[c])
            else:
                if cards[c] != repetidos[0]:
                    repetidos.append(cards[c])
    if len(repetidos) == 1:
        return True
    else:
        return False

def is2par(cart):
    cards = []
    for c in range(0, len(cart)):
        cards.append(cart[c]['carta'])
    repetidos = []
    for c in range(0, len(cards)):
        if cards.count(cards[c]) == 2:
            if len(repetidos) == 0:
                repetidos.append(cards[c])
            else:
                if cards[c] != repetidos[0]:
                    if len(repetidos) == 2:
                        if cards[c] != repetidos[1]:
                            repetidos.append(cards[c])
                    else:
                        repetidos.append(cards[c])
    if len(repetidos) >= 2:
        return True
    else:
        return False

def istrinca(cart):
    cards = []
    for c in range(0, len(cart)):
        cards.append(cart[c]["carta"])
    repetidos = []
    for c in range(0, len(cards)):
        if cards.count(cards[c]) == 3:
            if len(repetidos) == 0:
                repetidos.append(cards[c])
            else:
                if cards[c] != repetidos[0]:
                    repetidos.append(cards[c])
    if len(repetidos) >= 1:
        return True
    else:
        return False

def istrai(cart):    
    #separação das cartas repetidas
    cards = []
    for c in range(0, len(cart)):
        for c in range(0, len(cart)):
            if len(cards) == 0:
                cards.append(cart[c])
            else:
                for a in range(0, len(cards)):
                    if cart[c]["carta"] == cards[a]["carta"]:
                        break
                else:
                    cards.append(cart[c])
    #ordena as cartas que ficaram por peso
    orden = sorted(cards, key=lambda x: x['peso'])

    #coleta o peso das cartas e tira a repetição
    pes = []
    for c in range(0, len(orden)):
        pes.append(orden[c]["peso"])
    if 13 in pes:
        pes.append(1)
    pes = sorted(set(pes))

    #identificação de sequencia
    maior_seq = []
    for i in range(len(pes)):
        seq = [pes[i]]
        for j in range(i + 1, len(pes)):
            if pes[j] == seq[-1] + 1:
                seq.append(pes[j])
            else:
                break
        if len(seq) > len(maior_seq):
            maior_seq = seq
        elif len(seq) == len(maior_seq) and seq[-1] > maior_seq[-1]:
            maior_seq = seq  # em caso de empate, pega a que termina com valor mais alto

    if len(maior_seq) >= 5:
        return True
    else:
        return False
  
def isflush(cart):
    cards = []
    for c in range(0, len(cart)):
        cards.append(cart[c]["naip"])

    for c in range(0, len(cards)):
        if cards.count(cards[c]) >= 5:
            return True
    else:
        return False

def isfull(cart):
    if istrinca(cart) == True and ispar(cart) == True:
        return True
    if istrinca(cart) == True and is2par(cart) == True:
        return True
    else:
        return False

def isquadra(cart):
    cards = []
    for c in range(0, len(cart)):
        cards.append(cart[c]['carta'])
    for c in range(0, len(cards)):
        if cards.count(cards[c]) == 4:
            return True
    else:
        return False
    
def istraiflush(cart):
    #separação das cartas repetidas
    cards = []
    for c in range(0, len(cart)):
        for c in range(0, len(cart)):
            if len(cards) == 0:
                cards.append(cart[c])
            else:
                for a in range(0, len(cards)):
                    if cart[c]["carta"] == cards[a]["carta"]:
                        break
                else:
                    cards.append(cart[c])
    #ordena as cartas que ficaram por peso
    orden = sorted(cards, key=lambda x: x['peso'])
    pes = []
    for c in range(0, len(orden)):
        pes.append([orden[c]["peso"], orden[c]["naip"]])


    tamanho_minimo = 5  # você pode ajustar esse valor
    maior_seq = []
    for i in range(len(pes)):
        seq = [pes[i]]
        for j in range(i + 1, len(pes)):
            if pes[j][0] == seq[-1][0] + 1 and pes[j][1] == seq[-1][1]:
                seq.append(pes[j])
            else:
                break
        if len(seq) > len(maior_seq):
            maior_seq = seq
        elif len(seq) == len(maior_seq) and seq[-1][0] > maior_seq[-1][0]:
            maior_seq = seq
    if len(maior_seq) >= tamanho_minimo:
        return True
    else:
        return False

def isroyal(cart):
    #separação das cartas repetidas
    cards = []
    for c in range(0, len(cart)):
        for c in range(0, len(cart)):
            if len(cards) == 0:
                cards.append(cart[c])
            else:
                for a in range(0, len(cards)):
                    if cart[c]["carta"] == cards[a]["carta"]:
                        break
                else:
                    cards.append(cart[c])
    #ordena as cartas que ficaram por peso
    orden = sorted(cards, key=lambda x: x['peso'])
    pes = []
    for c in range(0, len(orden)):
        pes.append([orden[c]["peso"], orden[c]["naip"]])

    royal_seq = [9, 10, 11, 12, 13]
    for i in range(len(pes)):
        seq = [pes[i]]
        # Se a primeira carta não for o início da sequência, ignora
        if pes[i][0] != 9:
            continue
        for j in range(i + 1, len(pes)):
            # Verifica se é o próximo número da sequência e do mesmo naipe
            if pes[j][0] == seq[-1][0] + 1 and pes[j][1] == seq[-1][1]:
                seq.append(pes[j])
            else:
                break
        # Verifica se a sequência montada é exatamente a royal
        pesos_seq = [carta[0] for carta in seq]
        if sorted(pesos_seq) == royal_seq:
            return True
    return False

def defin_force1(cards, mesa):
    if len(mesa) == 0:
        return identmao1(cards)
    else:
        p = "0"
        #merge
        merge = []
        for c in range(0,2):
            merge.append(cards[c])
        if len(mesa) != 0:
            for c in range(0, len(mesa)):
                merge.append(mesa[c])

        #maos
        if ispar(merge) == True:
            p = "1"
        if is2par(merge) == True:
            p = "2"
        if istrinca(merge) == True:
            p = "3"
        if istrai(merge) == True:
            p = "4"
        if isflush(merge) == True:
            p = "5"
        if isfull(merge) == True:
            p = "6"
        if isquadra(merge) == True:
            p = "7"
        if istraiflush(merge) == True:
            p = "8"
        if isroyal(merge) == True:
            p = "9"
        return p

def identmao1(cards, mesa):
    pes = defin_force1(cards, mesa)
    if pes == "0":
        return "Carta Alta"
    if pes == "1":
        return "Par"
    if pes == "2":
        return "Dois Pares"
    if pes == "3":
        return "Trinca"
    if pes == "4":
        return "Sequência"
    if pes == "5":
        return "Flush"
    if pes == "6":
        return "Full House"
    if pes == "7":
        return "Quadra"
    if pes == "8":
        return "Straight Flush"
    if pes == "9":
        return "Royal Straight Flush"

def ganhador(j1, j2, j3, j4):
    ...