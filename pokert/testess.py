from luti import identmao1

cartas = [{'carta': '6', 'peso': 5, 'naip': '♦️'},
{'carta': '8', 'peso': 7, 'naip': '♣'},
{'carta': '5', 'peso': 4, 'naip': '♠️'},
{'carta': '3', 'peso': 2, 'naip': '♠️'},
{'carta': '9', 'peso': 8, 'naip': '♣'}]

jogador1= [{'carta': '6', 'peso': 5, 'naip': '♣'}, {'carta': '6', 'peso': 5, 'naip': '❤'}]#Trinca       

jogador2= [{'carta': '7', 'peso': 6, 'naip': '♣'}, {'carta': 'Q', 'peso': 11, 'naip': '♣'}]#Sequência   

jogador3= [{'carta': 'J', 'peso': 10, 'naip': '❤'}, {'carta': 'K', 'peso': 12, 'naip': '♦️'}]#Carta Alta

jogador4 = [{'carta': '5', 'peso': 4, 'naip': '♦️'}, {'carta': 'J', 'peso': 10, 'naip': '♦️'}]#Par

for c in range(1, 5):
    f"jogador{c}['forca']" = identmao1(f"jogador{c}", cartas)

print(jogador1)
