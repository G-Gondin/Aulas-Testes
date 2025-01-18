from random import randint
prima_digitos = []

#digitos 1
for c in range(0,9):
    prima_digitos.append(randint(0, 9))
count = soma = 0
for c in range(10, 1, -1):
    soma += prima_digitos[count] * c
    count += 1
soma_total = (soma*10) % 11
if soma_total > 9:
    dig1 = 0
else:
    dig1 = soma_total
prima_digitos.append(dig1)

#digitos 2
count = soma = 0
for c in range(11, 1, -1):
    soma += prima_digitos[count] * c
    count += 1

soma_total = (soma*10) % 11
if soma_total > 9:
    dig2 = 0
else:
    dig2 = soma_total
prima_digitos.append(dig2)

for c in range(0,11):
    print(prima_digitos[c], end="")
