def identmao1(jogad):
    n = []
    for c in range(0, 2):
        n.append(jogad[c]["carta"])
    if n[0] == n[1]:
        mao = "par"
    else:
        mao = "carta alta"
    return mao



def ispar(play, mesa):
    a = []
    for c in range(0, 2):
        a.append(play[c]["carta"])
    for c in range(0, 5):
        a.append(mesa[c]["carta"])
    repetidos = []
    for c in range(0, len(a)):
        if a.count(a[c]) == 2:
            if len(repetidos) == 0:
                repetidos.append(a[c])
            else:
                if a[c] != repetidos[0]:
                    repetidos.append(a[c])
    if len(repetidos) == 1:
        return True
    else:
        return False

def is2par(play, mesa):
    a = []
    for c in range(0, 2):
        a.append(play[c]["carta"])
    for c in range(0, 5):
        a.append(mesa[c]["carta"])
    repetidos = []
    for c in range(0, len(a)):
        if a.count(a[c]) == 2:
            if len(repetidos) == 0:
                repetidos.append(a[c])
            else:
                if a[c] != repetidos[0]:
                    if len(repetidos) == 2:
                        if a[c] != repetidos[1]:
                            repetidos.append(a[c])
                    else:
                        repetidos.append(a[c])
    if len(repetidos) == 2:
        return True
    else:
        return False

def istrinca(play, mesa):
    a = []
    for c in range(0, 2):
        a.append(play[c]["carta"])
    for c in range(0, 5):
        a.append(mesa[c]["carta"])
    repetidos = []
    for c in range(0, len(a)):
        if a.count(a[c]) == 3:
            if len(repetidos) == 0:
                repetidos.append(a[c])
            else:
                if a[c] != repetidos[0]:
                    repetidos.append(a[c])
    if len(repetidos) >= 1:
        return True
    else:
        return False

def istrai(play, mesa):
    a = []
    for c in range(0,2):
        a.append(play[c]["peso"])
    for c in range(0,5):
        a.append(mesa[c]["peso"])
    a.sort()
    d = 0
    for c in range(0, 7):
        z = a[c]
        if c != 6:
            x = a[c+1] 
        if x == z+1:
            d += 1
        if d == 4:
            return True
    else:
        return False
    
def isflush(play, mesa):
    a = []
    for c in range(0, 2):
        a.append(play[c]["naip"])
    for c in range(0, 5):
        a.append(mesa[c]["naip"])
    for c in range(0, len(a)):
        if a.count(a[c]) == 5:
            return True
    else:
        return False

def isfull(play, mesa):
    if istrinca(play, mesa) == True and ispar(play, mesa) == True:
        return True
    if istrinca(play, mesa) == True and is2par(play, mesa) == True:
        return True
    else:
        return False

def isquadra(play, mesa):
    a = []
    for c in range(0, 2):
        a.append(play[c]["carta"])
    for c in range(0, 5):
        a.append(mesa[c]["carta"])
    repetidos = []
    for c in range(0, len(a)):
        if a.count(a[c]) == 4:
            if len(repetidos) == 0:
                repetidos.append(a[c])
            else:
                if a[c] != repetidos[0]:
                    repetidos.append(a[c])
    if len(repetidos) == 1:
        return True
    else:
        return False
    
def istraiflush(play, mesa):
    ...
def isroyal(play, mesa):
    a = []
    for c in range(0, 2):
        a.append(play[c]["naip"])
    for c in range(0, 5):
        a.append(mesa[c]["naip"])
    np = []
    for c in range(0, len(a)):
        if a.count(a[c]) >= 5:
            np.append(a[c])
    print(np)
    
    
    
    
    
    
    
    
    
    
    
    
    a = []
    for c in range(0,2):
        a.append(play[c])
    for c in range(0, 5):
        a.append(mesa[c])
        d = 0
    for c in range(0, 7):
        ...
    if d == 0:
        return False

    a.sort(key=lambda value: value["peso"], reverse=True)
    for c in range(0, 7):
        print(f"""
{a[c]}
        """)    



def testemao(play, mesa):
    c = 0
    if ispar(play, mesa) == True:
        mao = "par"
        c += 1
    if is2par(play, mesa) == True:
        mao = "dois pares"
        c += 1
    if istrinca(play, mesa) == True:
        mao = "trinca"
        c += 1
    if c == 0:
        mao = "carta alta"
    return mao
