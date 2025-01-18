n1 = "08370874304".replace(".", "").replace("-", "").replace(" ", "")

# validação 1 digito cpf
n1int = []
for c in n1:
    n = int(c)
    n1int.append(n)
e = s = 0
for c in range(10, 1, -1):
    s += n1int[e] * c
    e += 1
ss = (s*10) % 11
if ss > 9:
    dig1 = 0
else:
    dig1 = ss

#validação 2 digito cpf
n2int = []
for c in n1:
    n = int(c)
    n2int.append(n)
d = p = 0
for c in range(11, 1, -1):
    p += n2int[d] * c
    d += 1
sss = (p*10) % 11
if sss > 9:
    dig2 = 0
else:
    dig2 = sss

print(dig1)
print(dig2)
