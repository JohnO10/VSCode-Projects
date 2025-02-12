

lista_de_tarefas = []  # memória simulada / banco de dados simulado

import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

def mostrar_menu():
    print(Fore.BLACK + Back.YELLOW + "\nMenu" + Back.RESET + Fore.RESET)
    print(Fore.BLACK + Back.YELLOW + "1 - Adicionar tarefa" + Back.RESET + Fore.RESET)
    print(Fore.BLACK + Back.YELLOW + "2 - Listar tarefas" + Back.RESET + Fore.RESET)
    print(Fore.BLACK + Back.YELLOW + "3 - Remover tarefa" + Back.RESET + Fore.RESET)
    print(Fore.BLACK + Back.YELLOW + "4 - Atualizar tarefa" + Back.RESET + Fore.RESET)
    print(Fore.BLACK + Back.YELLOW + "5 - Concluir tarefa e remover" + Back.RESET + Fore.RESET)
    print(Fore.BLACK + Back.YELLOW + "0 - Sair\n" + Back.RESET + Fore.RESET)

def obter_numero_inteiro(mensagem):
    while True:
        try:
            lista_de_tarefas = int(input(mensagem))
            return lista_de_tarefas
        except ValueError:
            print(Fore.RED + Back.BLACK + "Erro, foi digitado uma letra ou caractere especial! Por favor, digite apenas números." + Back.RESET + Fore.RESET)

def adicionar_tarefa():
    tarefa = input("Digite o nome da nova tarefa: \n")
    concluida = input("A tarefa está concluída? (s/n): ").lower() == 's'
    lista_de_tarefas.append({"tarefa": tarefa, "concluida": concluida})
    print(Fore.BLACK + Back.GREEN + "Tarefa adicionada com sucesso!" + Back.RESET + Fore.RESET)
    return

def listar_tarefas():
    if lista_de_tarefas:
        print(Fore.BLACK + Back.YELLOW + "\nTarefas atuais:\n" + Back.RESET + Fore.RESET * 40)
        for indice, tarefa in enumerate(lista_de_tarefas, start=1):
            status = Fore.GREEN + "Concluída" + Fore.RESET if tarefa["concluida"] else Fore.YELLOW + "Pendente" + Fore.RESET
            print(f"{indice}. {tarefa['tarefa']} - {status}")
    else:
        print(Fore.RED + Back.BLACK + "Nenhuma tarefa encontrada." + Back.RESET + Fore.RESET)

def remover_tarefa():
    listar_tarefas()

    if not lista_de_tarefas:
        print(Fore.RED + Back.BLACK + "A lista de tarefas está vazia!" + Back.RESET + Fore.RESET)
        adicionar_nova_tarefa = input("Gostaria de adicionar uma nova tarefa? s/n: ").lower()
        if adicionar_nova_tarefa == "s":
            adicionar_tarefa()
        return

    numero_tarefa = obter_numero_inteiro("Informe o número da tarefa: ")
    if 1 <= numero_tarefa <= len(lista_de_tarefas):
        lista_de_tarefas.pop(numero_tarefa - 1)
        print(Fore.BLACK + Back.GREEN + "A tarefa foi removida!" + Back.RESET + Fore.RESET)
        listar_tarefas()
    else:
        print(Fore.RED + Back.BLACK + "Tarefa inexistente! Informe um número válido!" + Back.RESET + Fore.RESET)
        listar_tarefas()

def atualizar_tarefa():
    if lista_de_tarefas:
        listar_tarefas()

        numero_tarefa = obter_numero_inteiro("Informe o número da tarefa: ")
        if 1 <= numero_tarefa <= len(lista_de_tarefas):
            nova_tarefa = input("Digite o nome da tarefa: ")
            atualizacao_concluida = input("A tarefa está concluída? (s/n): ").lower() == 's'
            lista_de_tarefas[numero_tarefa - 1] = {"tarefa": nova_tarefa, "concluida": atualizacao_concluida}
            print(Fore.BLACK + Back.GREEN + "Tarefa foi atualizada com sucesso!" + Back.RESET + Fore.RESET)
        else:
            print(Fore.RED + Back.BLACK + "Tarefa inexistente!" + Back.RESET + Fore.RESET)
            mensagem = Fore.LIGHTMAGENTA_EX + "[1] Tentar novamente\n" + Fore.RESET + Fore.LIGHTBLUE_EX + "[0] Voltar para o menu\n" + Fore.RESET
            tentar_novamente = input(mensagem)
            if tentar_novamente == "0":
                print(Fore.GREEN + Back.BLACK + "Ok, voltando para o menu..." + Back.RESET + Fore.RESET)
                return
            if tentar_novamente == "1":
                atualizar_tarefa() #recursão
    else:
        print("Ops, sinto muito... A sua lista está vazia!") 
        adicionar_nova_tarefa = input("Gostaria de adicionar nova tarefa agora? (s/n): ").lower()
        if adicionar_nova_tarefa == 's':
            adicionar_tarefa()
            return
        else:
            listar_tarefas()

def concluir_e_remover_tarefa():
    listar_tarefas()
    indice = obter_numero_inteiro("Digite o número da tarefa que deseja marcar como concluída e remover: ") - 1
    if 0 <= indice < len(lista_de_tarefas):
        lista_de_tarefas[indice]["concluida"] = True
        removida = lista_de_tarefas.pop(indice)
        print(Fore.GREEN + Back.BLACK + f"Tarefa '{removida['tarefa']}' marcada como concluída e removida com sucesso!" + Back.RESET + Fore.RESET)
    else:
        print(Fore.RED + Back.BLACK + "Número inválido." + Back.RESET + Fore.RESET)

# Função principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        atualizar_tarefa()
    elif opcao == "5":
        concluir_e_remover_tarefa()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print(Fore.RED + Back.BLACK + "Hum, algo não saiu conforme o esperado, tente novamente!" + Back.RESET + Fore.RESET)
