from random import shuffle
from lutv import cor

cartas = [
["a","♦️"], ["2","♦️"], ["3","♦️"], ["4","♦️"], ["5","♦️"], ["6","♦️"], ["7","♦️"], ["8","♦️"], ["9","♦️"], ["10","♦️"], ["J","♦️"], ["Q","♦️"], ["K","♦️"],
["a","♠️"], ["2","♠️"], ["3","♠️"], ["4","♠️"], ["5","♠️"], ["6","♠️"], ["7","♠️"], ["8","♠️"], ["9","♠️"], ["10","♠️"], ["J","♠️"], ["Q","♠️"], ["K","♠️"],
["a","❤"], ["2","❤"], ["3","❤"], ["4","❤"], ["5","❤"], ["6","❤"], ["7","❤"], ["8","❤"], ["9","❤"], ["10","❤"], ["J","❤"], ["Q","❤"], ["K","❤"],
["a","♣"], ["2","♣"], ["3","♣"], ["4","♣"], ["5","♣"], ["6","♣"], ["7","♣"], ["8","♣"], ["9","♣"], ["10","♣"], ["J","♣"], ["Q","♣"], ["K","♣"]]

shuffle(cartas)
shuffle(cartas)

jogador1 = [["8","❤"], ["2","♦️"]]
jogador2 = [["6","♣"], ["6","❤"]]
jogador3 = [["a","♦️"], ["4","♠️"]]
jogador4 = [["10","♣"], ["10","♦️"]]
jogador5 = [["7","♣"], ["K","♠️"]]
jogador6 = [["K","❤"], ["7","❤"]]

print(jogador1)
print(jogador2)
print(jogador3)
print(jogador4)
print(jogador5)
print(jogador6)

def identmao1(jogad):
    n = []
    n = jogad.copy()
    print(cor(n,"verde"))
    if n[0][0] == n[1][0]:
        mao = "par"
    else:
        mao = "carta alta"
    return cor(mao, "ciano")

print(identmao1(jogador1))
print(identmao1(jogador2))
print(identmao1(jogador3))
print(identmao1(jogador4))
print(identmao1(jogador5))
print(identmao1(jogador6))

def ispar():
    ...
def is2par():
    ...
def istrinca():
    ...
def istrai():
    ...
def isflush():
    ...
def isfull():
    ...
def isquadra():
    ...
def istraiflush():
    ...
def isroyal():
    ...

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

comunitaria = [["9","♦️"], ["10","❤"], ["4", "❤"]]
print(comunitaria)
print("jogador1 ",identmao(jogador1, comunitaria))
print("jogador2 ",identmao(jogador2, comunitaria))
print("jogador3 ",identmao(jogador3, comunitaria))
print("jogador4 ",identmao(jogador4, comunitaria))

comunitaria = [["9","♦️"], ["10","❤"], ["4", "❤"], ["a", "♠️"]]
print(comunitaria)
print("jogador1 ",identmao(jogador1, comunitaria))
print("jogador2 ",identmao(jogador2, comunitaria))
print("jogador3 ",identmao(jogador3, comunitaria))
print("jogador4 ",identmao(jogador4, comunitaria))


comunitaria = [["9","♦️"], ["10","❤"], ["4", "❤"], ["a", "♠️"], ["a", "❤"]]
print(comunitaria)
print("jogador1 ",identmao(jogador1, comunitaria))
print("jogador2 ",identmao(jogador2, comunitaria))
print("jogador3 ",identmao(jogador3, comunitaria))
print("jogador4 ",identmao(jogador4, comunitaria))

