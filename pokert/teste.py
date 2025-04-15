from random import shuffle
from lutv import cor
from luti import *
from time import sleep

fases = """[1] Pagar
[2] Aumentar
[3] Vender
[4] Mesa"""




cartas = [    {"carta": "2", "peso": 1, "naip": "♦️"},
    {"carta": "3", "peso": 2, "naip": "♦️"},
    {"carta": "4", "peso": 3, "naip": "♦️"},
    {"carta": "5", "peso": 4, "naip": "♦️"},
    {"carta": "6", "peso": 5, "naip": "♦️"},
    {"carta": "7", "peso": 6, "naip": "♦️"},
    {"carta": "8", "peso": 7, "naip": "♦️"},
    {"carta": "9", "peso": 8, "naip": "♦️"},
    {"carta": "10", "peso": 9, "naip": "♦️"},
    {"carta": "J", "peso": 10, "naip": "♦️"},
    {"carta": "Q", "peso": 11, "naip": "♦️"},
    {"carta": "K", "peso": 12, "naip": "♦️"},
    {"carta": "A", "peso": 13, "naip": "♦️"},

    {"carta": "2", "peso": 1, "naip": "♣"},
    {"carta": "3", "peso": 2, "naip": "♣"},
    {"carta": "4", "peso": 3, "naip": "♣"},
    {"carta": "5", "peso": 4, "naip": "♣"},
    {"carta": "6", "peso": 5, "naip": "♣"},
    {"carta": "7", "peso": 6, "naip": "♣"},
    {"carta": "8", "peso": 7, "naip": "♣"},
    {"carta": "9", "peso": 8, "naip": "♣"},
    {"carta": "10", "peso": 9, "naip": "♣"},
    {"carta": "J", "peso": 10, "naip": "♣"},
    {"carta": "Q", "peso": 11, "naip": "♣"},
    {"carta": "K", "peso": 12, "naip": "♣"},
    {"carta": "A", "peso": 13, "naip": "♣"},
    
    {"carta": "2", "peso": 1, "naip": "❤"},
    {"carta": "3", "peso": 2, "naip": "❤"},
    {"carta": "4", "peso": 3, "naip": "❤"},
    {"carta": "5", "peso": 4, "naip": "❤"},
    {"carta": "6", "peso": 5, "naip": "❤"},
    {"carta": "7", "peso": 6, "naip": "❤"},
    {"carta": "8", "peso": 7, "naip": "❤"},
    {"carta": "9", "peso": 8, "naip": "❤"},
    {"carta": "10", "peso": 9, "naip": "❤"},
    {"carta": "J", "peso": 10, "naip": "❤"},
    {"carta": "Q", "peso": 11, "naip": "❤"},
    {"carta": "K", "peso": 12, "naip": "❤"},
    {"carta": "A", "peso": 13, "naip": "❤"},
    
    {"carta": "2", "peso": 1, "naip": "♠️"},
    {"carta": "3", "peso": 2, "naip": "♠️"},
    {"carta": "4", "peso": 3, "naip": "♠️"},
    {"carta": "5", "peso": 4, "naip": "♠️"},
    {"carta": "6", "peso": 5, "naip": "♠️"},
    {"carta": "7", "peso": 6, "naip": "♠️"},
    {"carta": "8", "peso": 7, "naip": "♠️"},
    {"carta": "9", "peso": 8, "naip": "♠️"},
    {"carta": "10", "peso": 9, "naip": "♠️"},
    {"carta": "J", "peso": 10, "naip": "♠️"},
    {"carta": "Q", "peso": 11, "naip": "♠️"},
    {"carta": "K", "peso": 12, "naip": "♠️"},
    {"carta": "A", "peso": 13, "naip": "♠️"}]

shuffle(cartas)
shuffle(cartas)
jogador1 = []
jogador2 = []
jogador3 = []
jogador4 = []
comunitaria = []


#distribuição das cartas
for c in range(0,2):
    jogador1.append(cartas[0])
    cartas.remove(cartas[0])    
    jogador2.append(cartas[0])
    cartas.remove(cartas[0])
    jogador3.append(cartas[0])
    cartas.remove(cartas[0])
    jogador4.append(cartas[0])
    cartas.remove(cartas[0])

#flop
cartas.remove(cartas[0])
comunitaria.append(cartas[0])
cartas.remove(cartas[0])
comunitaria.append(cartas[0])
cartas.remove(cartas[0])
comunitaria.append(cartas[0])

#turn
cartas.remove(cartas[0])
comunitaria.append(cartas[0])

#river
cartas.remove(cartas[0])
comunitaria.append(cartas[0])


for c in range(0, len(comunitaria)):
    print(cor(f"{comunitaria[c]}", "ciano"))

print(f"""jogador 1: {cor(jogador1, "verde")}{identmao1(jogador1, comunitaria)}

jogador 2: {cor(jogador2, "vermelho")}{identmao1(jogador2, comunitaria)}

jogador 3: {cor(jogador3, "magenta")}{identmao1(jogador3, comunitaria)}

jogador 4: {cor(jogador4, "azul")}{identmao1(jogador4, comunitaria)}
""")
