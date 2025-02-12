from colorama import Back, Fore, Style, init
from datetime import datetime
init(autoreset=True)

def colorize(text="", fore_color=None, back_color=None):
    map_fore_colors = {
        "red": Fore.RED,
        "lightred": Fore.LIGHTRED_EX,
        "green": Fore.GREEN,
        "lightgreen": Fore.LIGHTGREEN_EX,
        "blue": Fore.BLUE,
        "yellow": Fore.YELLOW,
        "lightyellow": Fore.LIGHTYELLOW_EX,
        "cyan": Fore.CYAN,
        "lightcyan": Fore.LIGHTCYAN_EX,
        "magenta": Fore.MAGENTA,
        "lightmagenta": Fore.LIGHTMAGENTA_EX,
        "white": Fore.WHITE,
        "black": Fore.BLACK,
        "lightblue": Fore.LIGHTBLUE_EX,
    }
    map_back_colors = {
        "red": Back.RED,
        "green": Back.GREEN,
        "blue": Back.BLUE,
        "yellow": Back.YELLOW,
        "cyan": Back.CYAN,
        "magenta": Back.MAGENTA,
        "white": Back.WHITE,
        "black": Back.BLACK,
        "lightmagenta": "\033[45m",
    }
    
    fore = map_fore_colors.get(fore_color, "")
    back = map_back_colors.get(back_color, "")

    return f"{fore}{back}{text}{Style.RESET_ALL}"

def obter_numero_inteiro(mensagem):
    while True:
        try:
            lista_de_tarefas_pendentes = int(input(mensagem))
            return lista_de_tarefas_pendentes
        except ValueError:
            print(colorize("Erro, foi digitado uma letra ou caractere especial! Por favor, digite apenas números.", "red", "black")) #ctrl + d = marcar todos iguais
