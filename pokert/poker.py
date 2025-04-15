from random import shuffle
from lutv import cor
from luti import *
from time import sleep

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

for c in range(0,2):
    jogador1.append(cartas[0])
    cartas.remove(cartas[0])    
    jogador2.append(cartas[0])
    cartas.remove(cartas[0])
    jogador3.append(cartas[0])
    cartas.remove(cartas[0])
    jogador4.append(cartas[0])
    cartas.remove(cartas[0])

print()
print(jogador1)
print(identmao(jogador1))
print()

print(jogador2)
print(identmao(jogador2))
print()

print(jogador3)
print(identmao(jogador3))
print()

print(jogador4)
print(identmao(jogador4))
print()

a = str(input("da enter: "))
limpa()


#flop
cartas.remove(cartas[0])
comunitaria.append(cartas[0])
print(comunitaria[0])
sleep(0.5)

cartas.remove(cartas[0])
comunitaria.append(cartas[0])
print(comunitaria[1])
sleep(0.5)

cartas.remove(cartas[0])
comunitaria.append(cartas[0])
print(comunitaria[2])
sleep(0.5)

print(jogador1)
print(identmao1(jogador1, comunitaria))
print()

print(jogador2)
print(identmao1(jogador2, comunitaria))
print()

print(jogador3)
print(identmao1(jogador3, comunitaria))
print()

print(jogador4)
print(identmao1(jogador4, comunitaria))
print()


a = str(input("da enter: "))
limpa()


#turn
cartas.remove(cartas[0])
comunitaria.append(cartas[0])
print(comunitaria[3])
sleep(0.5)

print(jogador1)
print(identmao1(jogador1, comunitaria))
print()

print(jogador2)
print(identmao1(jogador2, comunitaria))
print()

print(jogador3)
print(identmao1(jogador3, comunitaria))
print()

print(jogador4)
print(identmao1(jogador4, comunitaria))
print()


a = str(input("da enter: "))
limpa()

#river
cartas.remove(cartas[0])
comunitaria.append(cartas[0])
print(comunitaria[4])
sleep(0.5)

print(jogador1)
print(identmao1(jogador1, comunitaria))
print()

print(jogador2)
print(identmao1(jogador2, comunitaria))
print()

print(jogador3)
print(identmao1(jogador3, comunitaria))
print()

print(jogador4)
print(identmao1(jogador4, comunitaria))
print()


a = str(input("da enter: "))
limpa()

print(f"""jogador 1: {cor(jogador1, "verde")}

jogador 2: {cor(jogador2, "vermelho")}

jogador 3: {cor(jogador3, "magenta")}

jogador 4: {cor(jogador4, "azul")}
""")


for c in range(0, len(comunitaria)):
    print(cor(f"{comunitaria[c]}", "ciano"))

print(jogador1)
print(identmao1(jogador1, comunitaria))
print()

print(jogador2)
print(identmao1(jogador2, comunitaria))
print()

print(jogador3)
print(identmao1(jogador3, comunitaria))
print()

print(jogador4)
print(identmao1(jogador4, comunitaria))
print()
