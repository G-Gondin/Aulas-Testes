jogador1 = []
fases = """"""
while True:
    #pagamento de pote, pote de 10 fichas
    print(f"""Suas cartas são: 
{jogador1[0]["carta"]}{jogador1[0]["naip"]}
{jogador1[1]["carta"]}{jogador1[1]["naip"]}

{fases}""")
    jogada = str(input("Qual sua escolha? ")).strip()
    if jogada not in "1234" or jogada == "" or len(jogada) > 1:
        while jogada not in "1234" or jogada == "" or len(jogada) > 1:
            jogada = str(input("Erro, digite novamente: ")).strip()
    
    if jogada == 1:
        ...
    if jogada == 2:
        ...
    if jogada == 3:
        ...
    if jogada == 4:        
        ...
