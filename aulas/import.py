from operator import index
from typing import SupportsIndex
import pip


lista_de_tarefas = [] # memória simulada / banco de dados simulado

import colorama
from colorama import Back, Fore , Style

colorama.init()

def mostrar_menu():
    print("\nMenu")
    print(Fore.BLACK + Back.YELLOW + "1 - Adicionar tarefa" + Back.RESET + Fore.RESET)
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Atualizar tarefa")
    print("5 - Concluir tarefa e remover")
    print("0 - Sair\n")

def adicionar_tarefa():
    tarefa = input("Digite o nome da tarefa: \n")
    concluida = input("A tarefa está concluída? (s/n): ").lower() == 's'
    lista_de_tarefas.append({"tarefa": tarefa, "concluida": concluida})
    print(Fore.BLACK + Back.GREEN + "Tarefa adicionada com sucesso!" + Back.RESET + Fore.RESET)


def listar_tarefas():
    if lista_de_tarefas:
        print("\nTarefas atuais:\n")
        for indice, tarefa in enumerate(lista_de_tarefas, start=1):
            status = Fore.GREEN + "Concluída" + Fore.RESET if tarefa["concluida"] else Fore.YELLOW + "Pendente" + Fore.RESET
            print(f"{indice}. {tarefa['tarefa']} - {status}")
    else:
        print("Nenhuma tarefa encontrada.")


def remover_tarefa():
    listar_tarefas()

    if (not lista_de_tarefas):
        print("A lista de tarefas está vazia!")
        adicionar_nova_tarefa = input("Gostaria de adicionar uma nova tarefa? s/n: ").lower()
        if (adicionar_nova_tarefa == "s"):
            adicionar_tarefa()
        return

    numero_tarefa = int(input("Informe o número da tarefa: "))
    if (1 <= numero_tarefa <= len(lista_de_tarefas)):
        lista_de_tarefas.pop(numero_tarefa - 1)
        print("A tarefa foi removida!")
        listar_tarefas()
    else:
        print("Tarefa inexistente! Informe um número válido!")
        listar_tarefas()

def atualizar_tarefa():
    listar_tarefas()

    numero_tarefa = int(input("Informe o número da tarefa:"))
    if (len(lista_de_tarefas) < numero_tarefa):
        print("Número inválido!")
        return
    nova_tarefa = input("Digite o nome da tarefa:")
    lista_de_tarefas[numero_tarefa -1] = nova_tarefa
    atualizacao_concluida = input("A tarefa está concluída? (s/n): ").lower() == 's'
    lista_de_tarefas.append({"tarefa": nova_tarefa, "concluida": atualizacao_concluida})
    print(Fore.BLACK + Back.GREEN + "Tarefa foi atualizada com sucesso!" + Back.RESET + Fore.RESET)
    return

def concluir_e_remover_tarefa():
    listar_tarefas()
    indice = int(input("Digite o número da tarefa que deseja marcar como concluída e remover: ")) - 1
    if 0 <= indice < len(lista_de_tarefas):
        lista_de_tarefas[indice]["concluida"] = True
        removida = lista_de_tarefas.pop(indice)
        print(f"Tarefa '{removida['tarefa']}' marcada como concluída e removida com sucesso!")
    else:
        print("Número inválido.")

# Função principal

    #print("Tarefa concluída com sucesso e removida da sua lista!")1
      
   

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if (opcao == "1"):
        adicionar_tarefa()
    if (opcao == "2"):
        listar_tarefas()
    if (opcao == "3"):
        remover_tarefa()  
    if (opcao == "4"):
        atualizar_tarefa()
    if (opcao == "5"):
        concluir_e_remover_tarefa()
    if (opcao == "0"):
        break
    if (not opcao):
        print("Nenhuma opção foi informada!")
        continue
    if (opcao > "5" or opcao < "0"):
        print("Opção é inválida ou inexistente!")
        continue