import lutv, random, time, os

#definição de interfaces de navegação

#interface principal
itprinc = """[1] calculadora
[2] cadastrar nome
[3] jogos
[4] sair"""

#interface da calculadora
itcal = """[1] Soma
[2] Subtração
[3] Divisão
[4] Multiplicação
[5] sair dessa opção"""

#interace do cadastro de nomes
itcad = """[1] cadastrar novo nome
[2] ver nomes cadastrados
[3] sair dessa opção"""

#inteface dos jogos
itjog = """[1] jogo de luta
[2] jogo de adivinhação
[3] jogo jokenpo
[4] sair"""

while True:
    lutv.titulo("Opções principais")
    print(itprinc)
    option = str(input("Qual a sua escolha? ")).strip()
    
    if option == "":
        print(lutv.cor("Escolha algo.", "amarelo"))
        time.sleep(2)
        os.system("cls")
        continue

    if option in "567890":
        print(lutv.cor("Digite uma opção valida!", "amarelo"))
        time.sleep(2)
        os.system("cls")
        continue    
    
    if option not in "1234" or option == "":
        while option not in "1234" or option == "":
            option = str(input(lutv.cor("Erro, digite novamente: ", "vermelho"))).strip()

    if len(option) != 1:
        print(lutv.cor("Digite apenas uma opção!", "amarelo"))
        time.sleep(2)
        os.system("cls")
        continue
    
    time.sleep(1.5)
    os.system("cls")
    
    #calculadora
    if option == "1":
        while True:
            lutv.titulo("calculadora")
            print(itcal)
            opcal = str(input("Qual sua opção? ")).strip()
            if opcal == "":
                print(lutv.cor("Escolha algo.", "amarelo"))
                time.sleep(2)
                os.system("cls")
                continue

            if opcal in "67890":
                print(lutv.cor("Digite uma opção valida!", "amarelo"))
                time.sleep(2)
                os.system("cls")
                continue    
            
            if opcal not in "12345" or opcal == "":
                while opcal not in "12345" or opcal == "":
                    opcal = str(input(lutv.cor("Erro, digite novamente: ", "vermelho"))).strip()

            if len(opcal) != 1:
                print(lutv.cor("Digite apenas uma opção!", "amarelo"))
                time.sleep(2)
                os.system("cls")
                continue
            if opcal == "5":
                time.sleep(1.5)
                os.system("cls")
                break

            time.sleep(1.5)
            
            while True:
                try:
                    n1 = float(input("Digite um número: "))
                except:
                    print(lutv.cor("O que foi digitado não é valido", "vermelho"))
                    continue
                try:
                    n2 = float(input("Digite outro número: "))
                except:
                    print(lutv.cor("O que foi digitado não é valido", "vermelho"))
                    continue
                if opcal == "1":
                    print(lutv.cor(f"A soma entre {n1} e {n2} é igual à {n1 + n2}", "verde"))
                    time.sleep(1.5)
                    os.system("cls")
                    break
                elif opcal == "2":
                    print(lutv.cor(f"A subtração de {n2} em {n1} é igual à {n1 - n2}", "verde"))
                    time.sleep(1.5)
                    os.system("cls")                   
                    break
                elif opcal == "3":
                    print(lutv.cor(f"A divisão de {n1} por {n2} é igual à {n1 / n2}", "verde"))
                    time.sleep(1.5)
                    os.system("cls")
                    break
                elif opcal == "4":
                    print(lutv.cor(f"A multiplacação entre {n1} e {n2} é igual à {n1 * n2}", "verde"))
                    time.sleep(1.5)
                    os.system("cls")
                    break
    
    #cadastrar nomes
    if option == "2":
        if lutv.arqexiste("cadastro_de_pessoas.txt") == False:
            lutv.criararq("cadastro_de_pessoas.txt")
        while True:
            lutv.titulo("Cadastro de pessoas")
            print(itcad)
            opcad = str(input("Qual sua escolha? ")).strip()
            if opcad == "":
                    print(lutv.cor("Escolha algo.", "amarelo"))
                    time.sleep(2)
                    os.system("cls")
                    continue

            if opcad in "4567890":
                print(lutv.cor("Digite uma opção valida!", "amarelo"))
                time.sleep(2)
                os.system("cls")
                continue    
            
            if opcad not in "123" or opcad == "":
                while opcad not in "123" or opcad == "":
                    opcad = str(input(lutv.cor("Erro, digite novamente: ", "vermelho"))).strip()

            if len(opcad) != 1:
                print(lutv.cor("Digite apenas uma opção!", "amarelo"))
                time.sleep(2)
                os.system("cls")
                continue

            if opcad == "3":
                time.sleep(1.5)
                os.system("cls")
                break

            time.sleep(1.5)

            if opcad == "1":
                while True:
                    nomeu = str(input("Digite o nome desejado: ")).strip().title()
                    verify = len(nomeu.split())
                    if verify != 1:
                        print("Digite apenas o primeiro nome da pessoa.")
                        continue
                    lnomeu = str(input("Digite o último sobrenome: ")).strip().title()
                    verify = len(lnomeu.split())
                    if verify != 1:
                        print("Digite apenas o último nome da pessoa.")
                        continue

                    while True:
                        try:
                            idadeu = int(input("Digite a idade da pessoa: "))
                        except:
                            print(lutv.cor("Por favor digite um número inteiro valido!", "amarelo"))
                            continue
                        else:
                            break
                    cadat = lutv.cadastro("cadastro_de_pessoas.txt", nomeu, lnomeu, idadeu)
                    print(cadat)
                    time.sleep(2)
                    os.system("cls")
                    break
            if opcad == "2":
                lutv.lercadat("cadastro_de_pessoas.txt")
                ss = input("Digite qualquer coisa para sair: ")
                time.sleep(2)
                os.system("cls")
    
    #jogos
    if option == "3":
        while True:
            lutv.titulo("Jogos")
            print(itjog)
            opjog = str(input("Qual sua opção? ")).strip()
            if opjog == "":
                print(lutv.cor("Escolha algo.", "amarelo"))
                time.sleep(2)
                os.system("cls")
                continue

            if opjog in "567890":
                print(lutv.cor("Digite uma opção valida!", "amarelo"))
                time.sleep(2)
                os.system("cls")
                continue    

            if opjog not in "1234" or opjog == "":
                while opjog not in "1234" or opjog == "":
                    opjog = str(input(lutv.cor("Erro, digite novamente: ", "vermelho"))).strip()

            if len(opjog) != 1:
                print(lutv.cor("Digite apenas uma opção!", "amarelo"))
                time.sleep(2)
                os.system("cls")
                continue
            
            if opjog == "4":
                time.sleep(1.5)
                os.system("cls")
                break
        
            #jogo lutas
            if opjog == "1":
                x = xp_level = xp_player = saia = count_round = defeated = cont = 0
                points_level = 10
                level = 1

                classes = [{"classe": "Guerreiro", "vitalidade": 11, "força": 13, "destreza": 13, "resistencia": 11},
                    {"classe": "Cavaleiro", "vitalidade": 14, "força": 11, "destreza": 11, "resistencia": 10},
                    {"classe": "Andarilho", "vitalidade": 10, "força": 10, "destreza": 14, "resistencia": 12}]
                mobs = [{"mob": "Guerreiro zombi", "vitalidade": 12, "força": 15, "destreza": 10, "resistencia": 9, "xp": 10},
                        {"mob": "Zombi", "vitalidade": 8, "força": 7, "destreza": 5, "resistencia": 5, "xp": 8},
                        {"mob": "Esqueleto", "vitalidade": 7, "força": 5, "destreza": 6, "resistencia": 3, "xp": 7}]

                while True:
                    #inicio    
                    cont += 1
                    if x == 0: 
                        #seleção da classe do pl
                        while True:
                            lutv.titulo("Selecione sua classe")
                            print()
                            print(lutv.cor("""[1] Guerreiro
[2] Cavaleiro
[3] Andarilho""", "ciano"))
                            n1 = str(input("Selecione a sua classe: ")).strip()
                            print()
                            if n1 not in "123" or n1 == "":
                                while n1 not in "123" or n1 == "":
                                    n1 = str(input(lutv.cor("Erro, digite novamente: ", "vermelho")))
                            if n1 == "1":
                                for k, v in (classes[0]).items():
                                    print(lutv.cor(f"A {k} é {v}.", "azul"))
                                print()
                                confirmation = str(input("Deseja continuar com essa classe? [S/N] ")).upper().strip()
                                if confirmation not in "SN" or confirmation == "":
                                    while confirmation not in "SN" or confirmation == "":
                                        confirmation = str(input(lutv.cor("Erro, digite novamente: ", "vermelho"))).upper().strip()
                                if confirmation == "S":
                                    class_player = classes[0]
                                    time.sleep(2)
                                    os.system("cls")
                                    break
                            if n1 == "2":
                                for k, v in (classes[1]).items():
                                    print(lutv.cor(f"A {k} é {v}.", "amarelo"))
                                print()
                                confirmation = str(input("Deseja continuar com essa classe? [S/N] ")).upper().strip()
                                if confirmation not in "SN" or confirmation == "":
                                    while confirmation not in "SN" or confirmation == "":
                                        confirmation = str(input(lutv.cor("Erro, digite novamente: ", "vermelho"))).upper().strip()
                                if confirmation == "S":
                                    class_player = classes[1]
                                    time.sleep(2)
                                    os.system("cls")
                                    break
                            if n1 == "3":
                                for k, v in (classes[2]).items():
                                    print(lutv.cor(f"A {k} é {v}.", "verde"))
                                print()
                                confirmation = str(input("Deseja continuar com essa classe? [S/N] ")).upper().strip()            
                                if confirmation not in "SN" or confirmation == "":
                                    while confirmation not in "SN" or confirmation == "":
                                        confirmation = str(input(lutv.cor("Erro, digite novamente: ", "vermelho"))).upper().strip()
                                if confirmation == "S":
                                    class_player = classes[2]
                                    time.sleep(2)
                                    os.system("cls")
                                    break
                            time.sleep(2)
                            os.system("cls")
                    #subir de nível
                    if x >= 1:
                        if xp_player >= points_level:
                            print(lutv.cor("Subiu de nível!", "verde"))
                            print(lutv.cor("""[1] vitalidade
[2] força
[3] destreza
[4] resistência""", "ciano"))
                            n2 = str(input("Adicionar pontos em qual status? ")).strip()
                            print()
                            if n2 not in "1234":
                                while n2 not in "1234" or n2 == "":
                                    n2 = str(input(lutv.cor("Erro, digite novamente: ", "vermelho"))).strip()
                            if n2 == '1':
                                class_player["vitalidade"] += 1
                                print(lutv.cor(f"sua vitalidade agora vale {class_player["vitalidade"]}", "ciano"))
                                points_level += points_level*0.4
                            elif n2 == '2':
                                class_player["força"] += 1
                                print(lutv.cor(f"sua força agora vale {class_player["força"]}", "ciano"))
                                points_level += points_level*0.4
                            elif n2 == '3':
                                class_player["destreza"] += 1
                                print(lutv.cor(f"sua destreza agora vale {class_player["destreza"]}", "ciano"))
                                points_level += points_level*0.4
                            elif n2 == '4':
                                class_player["resistencia"] += 1
                                print(lutv.cor(f"sua resistencia agora vale {class_player["resistencia"]}", "ciano"))
                                points_level += points_level*0.4
                        else:
                            print(f"Falta {points_level-xp_player} pontos de xp para subir de nível.")
                        print()

                    while True:
                        if count_round == 0:
                            attack_monster = attackforce_monster = defenseforce_monster = 0
                            attack_player = attackforce_player = defenseforce_player = 0

                            strength_player = class_player['força']
                            dexterity_player = class_player['destreza']


                            chosen_mob = random.choice(mobs)
                            xp_monster = 0
                            if cont % 5 == 0:
                                xp_level += 3
                            xp_monster = chosen_mob["xp"] + xp_level
                            
                            strength_monster = chosen_mob['força']
                            dexterity_monster = chosen_mob['destreza']

                            hp_player = class_player["vitalidade"] * 5
                            defense_palyer = class_player["resistencia"] + ((class_player["resistencia"]/2) * (class_player["vitalidade"]/4))


                            hp_monster = chosen_mob["vitalidade"] * 5
                            defense_monster = chosen_mob["resistencia"] + ((chosen_mob["resistencia"]/2) * (chosen_mob["vitalidade"]/4))
                            count_round = defeated = 0

                        if count_round == 0:
                            print(lutv.cor(f"analise da batalha, você escolheu a classe: {class_player['classe']}, seus status são:", "amarelo"))
                            print(lutv.cor(f"""
        vitalidade: {class_player['vitalidade']};
        força: {class_player['força']};
        destreza: {class_player['destreza']};
        resistencia: {class_player['resistencia']}.

        Seu HP é de {hp_player} pontos;
        E sua defesa é de {defense_palyer:.2f} pontos
                """, "verde"))
                            time.sleep(2)
                            print(lutv.cor(f"O mob selecionado foi: {chosen_mob['mob']}, seus status são:", "amarelo"))
                            print(lutv.cor(f"""
        vitalidade: {chosen_mob['vitalidade']};
        força: {chosen_mob['força']};
        destreza: {chosen_mob['destreza']};
        resistencia: {chosen_mob['resistencia']}.

        Seu HP é de {hp_monster} pontos;
        E sua defesa é de {defense_monster:.2f} pontos
                """, "vermelho"))
                            progress_to_battle = str(input("Tendo isso em mente, deseja prosseguir com a batalha? [S/N] ")).strip().upper()
                            if progress_to_battle not in "SN" or progress_to_battle == "":
                                while progress_to_battle not in "SN" or progress_to_battle == "":
                                    progress_to_battle = str(input(lutv.cor("Erro, digite novamente: ","vermelho"))).strip().upper()
                            if progress_to_battle == "S":
                                time.sleep(2)
                                os.system("cls")
                            if progress_to_battle == "N":
                                defeated = lutv.sorteio()
                                print()
                                if defeated == False:
                                    defeated += 1
                                    break                    
                                if defeated == True:
                                    time.sleep(2)
                                    os.system("cls")
                                    continue
                        count_round += 1
                        print()
                        print(f"Rodada {count_round}")
                        dice_player = random.randint(1, 6)
                        dice_monster = random.randint(1, 6)
                        dice_master = random.randint(1, 6)
                        print("Rolando dados")
                        print()
                        time.sleep(0.5)
                        print(lutv.cor(f"Dado do jogador: {dice_player}", "verde"))
                        print(lutv.cor(f"Dado do monstro: {dice_monster}", "vermelho"))
                        print(lutv.cor(f"Dado do mestre: {dice_master}", "amarelo"))

                        # definição de ataque player
                        if dice_player == dice_master:
                            attack_player = strength_player + dexterity_player
                        else:
                            if dice_player > dice_master:
                                attack_player = (strength_player / 2) + dexterity_player
                            if dice_player < dice_master:
                                attack_player = (strength_player / 2) + (dexterity_player / 2)

                        # definição da força de ataque player
                        if dice_player == dice_monster:
                            attackforce_player = attack_player
                        else:
                            if dice_player > dice_monster:
                                attackforce_player = attack_player * 1.5
                            if dice_player < dice_monster:
                                attackforce_player = attack_player * 0.75

                        # definição da força de defesa player
                        if dice_master == dice_player:
                            defenseforce_player = defense_palyer 
                        else:
                            if dice_master > dice_player:
                                defenseforce_player = defense_palyer * 0.75
                            if dice_master < dice_player:
                                defenseforce_player = defense_palyer * 1.5
                        
                        print()
                        lutv.linha()
                        print(lutv.cor(f"Seu ataque vale {attack_player}", "verde"))
                        print(lutv.cor(f"Sua força de ataque vale {attackforce_player}", "verde"))
                        print(lutv.cor(f"Sua defesa vale {defense_palyer}", "verde"))
                        print(lutv.cor(f"Sua força de defesa vale {defenseforce_player}", "verde"))
                        lutv.linha()
                        print("")

                        # definição do ataque monstro
                        if dice_monster == dice_master:
                            attack_monster = strength_monster + dexterity_monster
                        else:
                            if dice_monster > dice_master:
                                attack_monster = (strength_monster / 2) + dexterity_monster
                            if dice_monster < dice_master:
                                attack_monster = (strength_monster / 2) + (dexterity_monster / 2)

                        # definição da força de ataque monstro
                        if dice_monster == dice_player:
                            attackforce_monster = attack_monster
                        else:
                            if dice_monster > dice_player:
                                attackforce_monster = attack_monster * 1.5
                            if dice_monster < dice_player:
                                attackforce_monster = attack_monster * 0.75

                        # definição da força de defesa monstro
                        if dice_master == dice_monster:
                            defenseforce_monster = defense_monster 
                        else:
                            if dice_master > dice_monster:
                                defenseforce_monster = defense_monster * 0.75
                            if dice_master < dice_monster:
                                defenseforce_monster = defense_monster * 1.5
                        
                        lutv.linha()
                        print(lutv.cor(f"O ataque do mob vale {attack_monster}", "vermelho"))
                        print(lutv.cor(f"A força de ataque do mob vale {attackforce_monster}", "vermelho"))
                        print(lutv.cor(f"A defesa do mob vale {defense_monster}", "vermelho"))
                        print(lutv.cor(f"A força de defesa do mob vale {defenseforce_monster}", "vermelho"))
                        lutv.linha()
                        print()

                        attack_or_defend = str(input(f"""{lutv.cor("[1] atacar", "verde")}
{lutv.cor("[2] defender", "azul")}
qual a sua escolha? """)).strip()
                        if attack_or_defend not in "12" or attack_or_defend == "":
                            while attack_or_defend not in "12" or attack_or_defend == "":
                                attack_or_defend = str(input(lutv.cor("Erro, digite novamente: ","vermelho"))).upper().strip()
                        if attack_or_defend == "1":
                            if attackforce_player == defenseforce_monster:
                                print(lutv.cor("Seu ataque foi nulo", "amarelo"))
                            else:
                                if attackforce_player > defenseforce_monster:
                                    damage = attackforce_player - defenseforce_monster
                                    hp_monster -= damage
                                    lutv.linha()
                                    print(lutv.cor(f"Deu dano de {damage} pontos", "verde"))
                                    print(lutv.cor(f"O HP do monstro foi de {hp_monster+damage} para {hp_monster}.", "verde"))
                                    lutv.linha()
                                    print()
                                if attackforce_player < defenseforce_monster:
                                    damage = defenseforce_monster - attackforce_player
                                    hp_player -= damage
                                    lutv.linha()
                                    print(lutv.cor(f"Tomou dano de {damage} pontos", "vermelho"))
                                    print(lutv.cor(f"O seu HP foi de {hp_player + damage} para {hp_player}.", "vermelho"))
                                    lutv.linha()
                                    print()
                        if attack_or_defend == "2":
                            if attackforce_monster == defenseforce_player:
                                print("Nulo")
                            else:
                                if attackforce_monster > defenseforce_player:
                                    damage = attackforce_monster - defenseforce_player
                                    hp_player -= damage
                                    lutv.linha()
                                    print(lutv.cor(f"Tomou dano de {damage} pontos", "vermelho"))
                                    print(lutv.cor(f"O seu HP foi de {hp_player + damage} para {hp_player}.", "vermelho"))
                                    lutv.linha()
                                    print()
                                if attackforce_monster < defenseforce_player:
                                    damage = defenseforce_player - attackforce_monster
                                    hp_monster -= damage
                                    lutv.linha()
                                    print(lutv.cor(f"Deu dano de {damage} pontos", "verde"))
                                    print(lutv.cor(f"O HP do monstro foi de {hp_monster+damage} para {hp_monster}.", "verde"))
                                    lutv.linha()
                                    print()
                        time.sleep(2)
                        os.system("cls")
                        if hp_player < 0:
                            time.sleep(2)
                            lutv.linha()
                            print(lutv.cor("Você morreu", "vermelho"))
                            print(lutv.cor(f"Restou um total de {hp_monster} de HP do mob.", "ciano"))
                            print(lutv.cor(f"Total de {count_round} rodadas", "ciano"))
                            lutv.linha()
                            time.sleep(2)
                            defeated += 1
                            break
                        if hp_monster < 0:
                            time.sleep(2)
                            lutv.linha()
                            print(lutv.cor("Monstro derrotado", "verde"))
                            print(lutv.cor(f"Te restou um total de {hp_player} de HP.", "ciano"))
                            print(lutv.cor(f"Total de {count_round} rodadas", "ciano"))
                            lutv.linha()
                            time.sleep(1)
                            x += 1
                            xp_player += xp_monster
                            print(lutv.cor(f"Mais {chosen_mob['xp']} pontos de xp", "amarelo"))
                            print(lutv.cor(f"Xp total de {xp_player}", "verde"))
                            lutv.linha()
                            print()
                            time.sleep(2)
                            count_round = 0
                            break
                    if defeated >= 1:
                        break
                    egit = str(input("Quer continuar? [S/N] ")).strip().lower()
                    if egit not in "SN" or egit == "":
                        while egit not in "SN" or egit == "":
                            egit = str(input("Erro, digite novamente: "))
                    if egit == "n":
                        break
                print()
                lutv.titulo(f"{lutv.cor("Fim", "magenta")}")
            
            #jogo adivinhação
            if opjog == "2":
                time.sleep(1.5)
                os.system("cls")
                while True:
                    palavras = [["abacate", "melancia", "abacaxi", "maça", "kiwi",'acerola','amora','banana','caja','caqui','carambola','cereja','maracuja','manga','limão','laranja','pequi','pera','roma','siriguela'],
                    ['abajur','aluarde','algema','bacia','berço','bola','capa','canivete','chinelo','dardo',"didjeridu",'esmalte','extintor','faca','focineira','quadrante','punhal','retrovisor','seringa','vassoura'],
                    ['russia','canada','brasil','indonesa','paquistao','australia','india','argentina','cazaquistao','argelia','indonesia','mongolia','peru','chade','china','nigeria','bangladesh','egito','mexico','espanha']]

                    vit = tentativas = d = 0
                    usadas = []
                    presente = []
                    palavra = []
                    lpala = []
                    while True:
                        if tentativas == 0:
                            ccls = random.randint(0,2)
                            escolhida = random.choice(palavras[ccls])
                            if ccls == 0:
                                dica = "fruta"
                            if ccls == 1:
                                dica = "objeto"
                            if ccls == 2:
                                dica = "pais"
                            for c in range(0,len(escolhida)):
                                palavra.append(escolhida[c])
                                if escolhida[c] not in lpala:
                                    lpala.append(escolhida[c])    
                        lutv.linha()
                        print(f"""Dica! a palavra escolhida 
    tem {len(escolhida)} letras e é da classe {dica}.""")
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
                                n1 = str(input(lutv.cor("Erro, digite novamente: ", "vermelho"))).strip()
                        if n1 == "1":
                            print(usadas)
                        elif n1 == "2":
                            print(presente)
                        elif n1 == "3":
                            while True:
                                test = str(input("Digite uma letra: ")).strip().lower()
                                if test in usadas:
                                    print(lutv.cor("Letra já utilizada, tente novamente", "vermelho"))
                                    continue
                                if len(test) > 1:
                                    print(lutv.cor("Digite apenas uma letra, tente de novo", "vermelho"))
                                    continue
                                if test in escolhida:
                                    print(lutv.cor(f"A letra {test} está presente na palavra escolhida.", "verde"))
                                    print(lutv.cor(f"A sua letra aparece {escolhida.count(test)} vezes na palavra.", "amarelo"))
                                    presente.append(test)
                                    usadas.append(test)
                                    break
                                else:
                                    print(lutv.cor(f"A letra {test} não está presente na palavra escolhida.", "vermelho"))
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
                                print(lutv.cor("palavra errada, tente novamente.", "vermelho"))
                        tentativas += 1
                        if d == 1:
                            print(lutv.cor(f"Parabéns. Você acertou a palavra em {tentativas} tentativas!", "verde"))
                            vit += 1
                            n3 = str(input(lutv.cor("Jogar novamente? [S/N] ", "amarelo"))).strip().lower()
                            if n3 not in "sn" or n3 == "":
                                while n3 not in "sn" or n3 == "":
                                    n3  = str(input(lutv.cor("Erro digite novamente: ", "vermelho"))).strip().lower()
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
                        time.sleep(2)
                        os.system("cls")
                    print()
                    print(f"Você teve um total de {vit} vitórias.")
                    break
                time.sleep(1.5)
                os.system("cls")
            
            #jogo jokenpo
            if opjog == "3":
                while True:
                    vt = 0
                    jogadas = ["bah", "Pedra", "Papel", "Tesoura"]
                    vencedor = ""
                    while True:
                        lutv.titulo("Jokenpo")
                        print("""[1] Pedra
                    [2] Papel
                    [3] Tesoura""")
                        jogada = str(input("Qual a sua escolha? ")).strip()
                        print()
                        if jogada not in "123" or jogada == "":
                            while jogada not in "123" or jogada == "":
                                jogada = str(input(lutv.cor("Erro, digite novamente: ", "vermelho")))
                        jogador = int(jogada)
                        cpu = random.randint(1, 3)
                        if jogador == cpu:
                            vencedor = "empate"
                        else:
                            if jogador == 1:
                                if cpu == 2:
                                    vencedor = "cpu"
                                if cpu == 3:
                                    vencedor = "jogador"
                                    vt += 1
                            if jogador == 2:
                                if cpu == 1:
                                    vencedor = "jogador"
                                    vt += 1
                                if cpu == 3:
                                    vencedor = "cpu"
                            if jogador == 3:
                                if cpu == 1:
                                    vencedor = "jogador"
                                    vt += 1
                                if cpu == 2:
                                    vencedor = "cpu"
                        if vencedor == "empate":
                            print(f"""Você jogou {lutv.cor(f"{jogadas[jogador]}", "verde")}.
                    O computador jogou {lutv.cor(f"{jogadas[cpu]}", "ciano")}.
                    O jogo deu {lutv.cor(f"{vencedor}", "amarelo")}""")
                        else:
                            print(f"""Você jogou {lutv.cor(f"{jogadas[jogador]}", "verde")}.
                    O computador jogou {lutv.cor(f"{jogadas[cpu]}", "ciano")}.
                    O vencedor foi {lutv.cor(f"{vencedor}", "amarelo")}""")
                        print()
                        confirm = str(input("Quer jogar novamente? [S/N] ")).strip().lower()
                        if confirm not in "sn" or confirm == "":
                            while confirm not in "sn" or confirm == "":
                                confirm = str(input(lutv.cor("Erro, digite novamente: ", "vermelho")))
                        if confirm == "n":
                            break
                        os.system("cls")
                    print()
                    print(f"Você teve um total de {vt} vitorias!")
                    time.sleep(2)
                    os.system("cls")
                    break
    
    #sair
    if option == "4":
        break