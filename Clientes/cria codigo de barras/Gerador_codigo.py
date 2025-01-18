import random, lutv

cod = "782147"
som = 29
ultimo_dig = 0
while True:
    print()
    for c in range(0, 5):
        num = random.randint(0, 9)
        cod += str(num)
        ultimo_dig += num
    if ultimo_dig > 10:
        while ultimo_dig >= 10:
            ultimo_dig -= 10

    cod += str(ultimo_dig)

    print(lutv.cor(f"{cod}", "ciano"))
    ultimo_dig = 0
    cod = "782147"
    
    verif = str(input("Quer continuar? ")).lower().strip()
    if verif not in "sn" or verif == "" or len(verif) > 1:
        while verif not in "sn" or verif == "" or len(verif) > 1:
            verif = str(input(lutv.cor("Erro, digite novamente: ", "vermelho"))).lower().strip()
    if verif == "n":
        break
