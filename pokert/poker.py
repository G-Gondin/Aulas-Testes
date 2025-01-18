from random import shuffle
from lutv import cor
from luti import *
cartas = [
    {"carta": "2", "peso": 1, "naip": "♦️"},
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
cartas.remove(cartas[0])

#turn
cartas.remove(cartas[0])
comunitaria.append(cartas[0])
cartas.remove(cartas[0])

#river
cartas.remove(cartas[0])
comunitaria.append(cartas[0])


print(f"""jogador 1: {cor(jogador1, "verde")}

jogador 2: {cor(jogador2, "vermelho")}

jogador 3: {cor(jogador3, "magenta")}

jogador 4: {cor(jogador4, "azul")}
""")


for c in range(0, len(comunitaria)):
    print(cor(f"{comunitaria[c]}", "ciano"))