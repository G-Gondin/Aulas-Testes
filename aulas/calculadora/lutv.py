def cor(msg, cor="branco"):
    import colorama
    colorama.init()
    color = {
        "vermelho": colorama.Fore.RED,
        "verde": colorama.Fore.GREEN,
        "amarelo": colorama.Fore.YELLOW,
        "azul": colorama.Fore.BLUE,
        "preto": colorama.Fore.BLACK,
        "ciano": colorama.Fore.CYAN,
        "magenta": colorama.Fore.MAGENTA,
        "branco": colorama.Fore.WHITE,
        "reset": colorama.Fore.RESET}
    n1 = f"{color[f'{cor}']}{msg}{color['reset']}"
    return n1

