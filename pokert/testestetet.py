from luti import *

#play1 = [{'carta': '8', 'peso': 7, 'naip': '♠️'}, {'carta': '9', 'peso': 8, 'naip': '♠️'}]
play2 = [{'carta': 'J', 'peso': 10, 'naip': '♠️'}, {'carta': 'Q', 'peso': 11, 'naip': '♠️'}]

mesa = [{'carta': 'Q', 'peso': 11, 'naip': '♦️'},
        {'carta': 'K', 'peso': 12, 'naip': '❤'},
        {'carta': '10', 'peso': 9, 'naip': '♠️'},
        {'carta': 'K', 'peso': 12, 'naip': '♠️'},
        {'carta': 'A', 'peso': 13, 'naip': '♠️'}]

# straight flush
# Royal flush


print(isroyal(play2, mesa))
    
#f"""O Jogador 1 tem: {testemao(play1, mesa)}
#O Jogador 2 tem: {testemao(play2, mesa)}
#O Jogador 3 tem: {testemao(play3, mesa)}
#O Jogador 4 tem: {testemao(play4, mesa)}
#""")




    