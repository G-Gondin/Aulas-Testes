from lutv import cor
frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Von Rossum."
Frase = frase.lower()
temja = []
cont = {}
ct = {}
print(f"""Na frase:
{frase}

""")


for c in range(0, len(Frase)):
    if Frase[c] != " " and Frase != ".":
        if Frase[c] not in temja:
            temja.append(Frase[c])

for c in range(0, len(temja)):
    ct[f"{temja[c]}"] = Frase.count(f"{temja[c]}")

for k, v in ct.items():
    print(f"A letra {cor(k, "ciano")} apareceu {cor(v, "verde")} vezes.")

