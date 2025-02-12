from colorama import Fore, Back, Style, init
init(autoreset=True)

def mostrar_menu():
    print("\nMenu\n")
    print("1 - Calcular Kv e mAs")
    print("0 - Sair\n")


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
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Erro, foi digitado uma letra ou caractere especial! Por favor, digite apenas números.")

def obter_numero_float(mensagem):
    while True:
        try:
            numero_float = float(input(mensagem))
            return numero_float
        except ValueError:
            print("Erro, foi digitado uma letra ou caractere especial! Por favor, digite apenas números.")


def verificar_local_exame(local_exame):
    locais_validos = ["torax", "abdomen", "extremidade", "cranio"]
    while local_exame not in locais_validos:
        print("\nLocal do exame não especificado nos parâmetros.\n")
        opcoes = "[1] Tentar novamente\n[0] Voltar para o menu\n"
        tentar_novamente = input(opcoes).strip().lower()
        if tentar_novamente == "1":
            local_exame = input("Informe o local do exame (torax, abdomen, extremidade, cranio): ").strip().lower()
        elif tentar_novamente == "0":
            print("Foi um prazer lhe ajudar até aqui! Voltando para o menu...")
            return None
        else:
            print("Opção inválida. Tente novamente.")
    return local_exame


def obter_info_paciente():
    nome_paciente = str(input("Informe o nome do paciente: \n")).title()
    idade_paciente = obter_numero_inteiro("Informe a idade do paciente: \n")
    peso_paciente = obter_numero_float("Informe o peso do paciente: \n")
    local_exame = input("Informe o local do exame (torax, abdomen, extremidade, cranio): \n").strip().lower()
    local_exame = verificar_local_exame(local_exame)
    if local_exame is None:
        return None
    return nome_paciente, idade_paciente, peso_paciente, local_exame

def calcular_kv(info_paciente):
    nome_paciente, idade_paciente, peso_paciente, local_exame = info_paciente
    fator_local = {
        "torax": 1.0,
        "abdomen": 1.2,
        "extremidade": 0.8,
        "cranio": 1.1
    }
    
    fator = fator_local[local_exame]
    espessura_local = obter_numero_float("Informe a espessura do local (cm): \n")
    constante_aparelho = obter_numero_float("Informe a constante do aparelho: \n")
    kv_calculo = (espessura_local * 2 + constante_aparelho)

    info_paciente = {
        "nome": nome_paciente,
        "idade": idade_paciente,
        "peso": peso_paciente,
        "local_exame": local_exame,
        "kv": kv_calculo,
        "espessura_local": espessura_local,
        "constante_aparelho": constante_aparelho
    }
    return info_paciente

def imprimir_info_paciente(info_paciente):
    print("\n\n")
    print(f'Nome do paciente: {info_paciente["nome"]}')
    print(f'Idade do paciente: {info_paciente["idade"]}')
    print(f'Peso do paciente: {info_paciente["peso"]}')
    print(f'Local do exame: {info_paciente["local_exame"]}')
    print(f'O Kv é: {info_paciente["kv"]}')

def calcular_mAs(info_paciente):
    mas_com_grade = info_paciente["kv"] / 2  # dentro da grade
    mas_sem_grade = info_paciente["kv"] / 3  # fora da grade
    imprimir_info_paciente(info_paciente)
    print(f'O mAs dentro da grade é: {mas_com_grade}')
    print(f'O mAs fora da grade é: {mas_sem_grade}')

info_paciente = None

while True:
    mostrar_menu()
    opcao = obter_numero_inteiro("Escolha uma opção: ")
    if opcao == 1:
        info_paciente = obter_info_paciente()
        if info_paciente:
            info_paciente = calcular_kv(info_paciente)
            calcular_mAs(info_paciente)
    elif opcao == 0:
        break
    else:
        print("Opção inválida ou inexistente!")