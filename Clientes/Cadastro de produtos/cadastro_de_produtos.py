import os, time, lutv

os.system("cls")
if lutv.arqexiste("cadastro_de_produtos.txt") == False:
    lutv.criararq("cadastro_de_produtos.txt")
inter_menu = """[1] ver itens
[2] Cadastrar itens
[3] Consultar produto
[4] Sair"""
while True:
    time.sleep(1.5)
    os.system("cls")
    print(lutv.cor(inter_menu, "verde"))
    options = str(input(lutv.cor("Selecione sua opção: ", "branco")))
    if options not in "1234" or options == "" or len(options) > 1:
        while options not in "1234" or options == "" or len(options) > 1:
            options = str(input(lutv.cor("Erro! Digite novamente: ", "vermelho")))
    if options == "4":
        break
    elif options == "1":
        lutv.lercadat_prod("cadastro_de_produtos.txt")
        edit = str(input("Deseja editar algum produto? [S/N]")).strip().upper()
        if edit not in "SN" or edit == "" or len(edit) > 1:
            while edit not in "SN" or edit == "" or len(edit) > 1:
                edit = str(input(lutv.cor("Erro! Digite novamente: ", "vermelho"))).strip().upper()
        if edit == "S":
            op = str(input("Digite o código do produto que você quer editar: "))
            print(lutv.alt_arq_cadat("cadastro_de_produtos.txt", op))
    elif options == "2":
        new_produt = str(input("Leia o código do produto: "))
        verif = lutv.verify_in("cadastro_de_produtos.txt", new_produt)
        if verif == True:
            present = lutv.pull_dados("cadastro_de_produtos.txt", new_produt)
            print(lutv.cor("O produto escaniado já está presente no banco", "ciano"))
            for c in range(0, len(present)):
                print(present[c], end=" ")
            print("""
""")
        else:
            n1 = str(input("Qual o nome do produto? ")).title().strip()
            if n1 == "":
                while n1 == "":
                    n1 = str(input(lutv.cor("Erro, digite novamente: ", "vermelho")))
            if n1.find(" ") != -1:
                n = n1.split()
                nome = "_".join(n)
            else:
                nome = n1
            while True:
                try:
                    price = int(input("Qual o valor do item: "))
                except:
                    continue
                else:
                    break
            lutv.cadastro_prod("cadastro_de_produtos.txt", new_produt, nome, price)
    elif options == "3":
        verif_prod = str(input("Leia o código do produto: "))
        verif = lutv.verify_in("cadastro_de_produtos.txt", verif_prod)
        if verif == True:
            present = lutv.pull_dados("cadastro_de_produtos.txt", verif_prod)
            print(lutv.cor("O produto escaniado já está presente no banco", "ciano"))
            print(f"{f"{present[0]} {present[1]}":<20}\t {f"R$ {present[2]} Data de adição: {present[3]}":<{len(present[1])+5}}")
            print()
            exit = input("Digite qualquer coisa para sair: ")
        else:
            print(lutv.cor(f"o código {verif_prod} não está presente no banco", "vermelho"))
            add = str(input("Deseja adicionar o produto no banco? [S/N] ")).strip().upper()
            if add not in "SN" or add == "" or len(add) > 1:
                while add not in "SN" or add == "" or len(add) > 1:
                    add = str(input(lutv.cor("Erro! Digite novamente: ", "vermelho"))).strip().upper()
            if add == "S":
                nome = str(input("Qual o nome do produto? ")).title().strip()
                if nome == "":
                    while nome == "":
                        nome = str(input(lutv.cor("Erro, digite novamente: ", "vermelho")))
                while True:
                    try:
                        price = int(input("Qual o valor do item: "))
                    except:
                        continue
                    else:
                        break
                lutv.cadastro_prod("cadastro_de_produtos.txt", verif_prod, nome, price)
