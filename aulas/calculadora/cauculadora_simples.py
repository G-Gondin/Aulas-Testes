from lutv import cor
while True:
    try:
        n1 = float(input("Digite um número: "))
    except:
        print(cor("O que foi digitado não é valido", "vermelho"))
        continue
    try:
        n2 = float(input("Digite outro número: "))
    except:
        print(cor("O que foi digitado não é valido", "vermelho"))
        continue
    print(cor("""[1] Soma
[2] Subtração
[3] Divisão
[4] Multiplicação""", "ciano"))
    op = str(input("Qual sua escolha de operação?  ")).strip()
    if op not in "1234" or op == "":
        while op not in "1234" or op == "":
            op = str(input(cor("Erro, digite novamente: ", "vermelho"))).strip()
    if op == "1":
        print(cor(f"A soma entre {n1} e {n2} é igual à {n1 + n2}", "verde"))
    elif op == "2":
        print(cor(f"A subtração de {n2} em {n1} é igual à {n1 - n2}", "verde"))
    elif op == "3":
        print(cor(f"A divisão de {n1} por {n2} é igual à {n1 / n2}", "verde"))
    elif op == "4":
        print(cor(f"A multiplacação entre {n1} e {n2} é igual à {n1 * n2}", "verde"))
    cont = str(input("Deseja continuar?[S/N] ")).strip().upper()
    if cont not in "SN" or cont == "":
        while cont not in "SN" or cont == "":
            cont = str(input(cor("Erro, digite novamente: ", "vermelho"))).strip().upper()
    if cont == "N":
        print()
        break
    elif cont == "S":
        print()
print(cor("Volte sempre!","magenta"))
