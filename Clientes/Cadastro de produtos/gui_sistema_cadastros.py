import tkinter, lutv

if lutv.arqexiste("cadastro_de_produtos.txt") == False:
        lutv.criararq("cadastro_de_produtos.txt")


janela = tkinter.Tk()
largura = 210
altura = 100
wina = janela.winfo_screenheight()
winl = janela.winfo_screenwidth()
posx = (winl / 2) - (largura / 2)
posy = (wina / 2) - (altura / 2)
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
janela.title("Cadastro de produtos")
janela.resizable(False, False)


#envia cod
labelentrada_cod = tkinter.Label(janela, text="Código de barras: ")
labelentrada_cod.place(x=0, y=0)
entradacodigo = tkinter.Entry(janela, width="15")
entradacodigo.place(x=106, y=0)
#envia nome
labelentrada_nome = tkinter.Label(janela, text="Nome do produto: ")
labelentrada_nome.place(x=0, y=23)
entradanome = tkinter.Entry(janela, width="15")
entradanome.place(x=106, y=23)
#envia preco
labelentrada_preco = tkinter.Label(janela, text="preço do produto: ")
labelentrada_preco.place(x=0, y=47)
entradapreco = tkinter.Entry(janela, width="15")
entradapreco.place(x=106, y=47)

def cadat():
    n1 = entradacodigo.get()
    n2 = entradanome.get()
    n3 = entradapreco.get()
    lutv.cadastro_prod("cadastro_de_produtos.txt", n1, n2, n3)


botaoenvia = tkinter.Button(janela, text="Enviar", bg="green", fg="black", command=cadat)
botaoenvia.place(x=158,y=70)

janela.mainloop()