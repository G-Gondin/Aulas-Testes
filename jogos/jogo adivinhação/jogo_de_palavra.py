import random, lutv, os
palavras = ["abacate", "melancia", "abacaxi", "maça", "kiwi"]
vit = tentativas = d = 0
usadas = []
presente = []
palavra = []
lpala = []
while True:
    if tentativas == 0:
        escolhida = random.choice(palavras)
        for c in range(0,len(escolhida)):
            palavra.append(escolhida[c])
            if escolhida[c] not in lpala:
                lpala.append(escolhida[c])    
        lutv.linha()
        print(f"""Dica! a palavra 
escolhida tem {len(escolhida)} letras.""")
        lutv.linha()
    print()

    lutv.linha()
    for c in range(0, len(escolhida)):
        if palavra[c] in presente:
            print(palavra[c], end="")
        else:
            print("*", end="")
    print()
    lutv.linha()
    print()

    print("""[1] ver letras usadas
[2] Ver letras presentes
[3] Tentar nova letra
[4] Temtar a palavra""")
    n1 = str(input("Qual sua escolha? ")).strip()
    print()
    if n1 not in "1234" or n1 == "":
        while n1 not in "1234" or n1 == "":
            n1 = str(input("Erro, digite novamente: ")).strip()
    if n1 == "1":
        lutv.limpa()
        print(usadas)
    elif n1 == "2":
        lutv.limpa()
        print(presente)
    elif n1 == "3":
        while True:
            lutv.limpa()
            test = str(input("Digite uma letra: ")).strip().lower()
            if test in usadas:
                print("Letra já utilizada, tente novamente")
                continue
            if len(test) > 1:
                print("Digite apenas uma letra, tente de novo")
                continue
            if test in escolhida:
                print(f"A letra {test} está presente na palavra escolhida.")
                print(f"A sua letra aparece {escolhida.count(test)} vezes na palavra.")
                presente.append(test)
                usadas.append(test)
                break
            else:
                print(f"A letra {test} não está presente na palavra escolhida.")
                usadas.append(test)
                break
        if len(lpala) == len(presente):
            lutv.linha()
            for c in range(0, len(escolhida)):
                if palavra[c] in presente:
                    print(palavra[c], end="")
                else:
                    print("*", end="")
            print()
            lutv.linha()
            print()
            d += 1
    if n1 == "4":
        sorte = str(input("Digite seu chute: ")).strip().lower()
        if sorte == escolhida:
            d += 1
        else:
            print("palavra errada, tente novamente.")
    tentativas += 1
    if d == 1:
        print(f"Parabéns. Você acertou a palavra em {tentativas} tentativas!")
        vit += 1
        n3 = str(input("Jogar novamente? [S/N] ")).strip().lower()
        if n3 not in "sn" or n3 == "":
            while n3 not in "sn" or n3 == "":
                n3  = str(input("Erro digite novamente: ")).strip().lower()
        if n3 == "s":
            usadas.clear()
            presente.clear()
            d = 0
            tentativas = 0
            palavra.clear()
            lpala.clear()
            os.system("cls")
        if n3 == "n":
            break
print()
print(f"Você teve um total de {vit} vitórias.")
