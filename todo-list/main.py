lista_de_tarefas_pendentes = []  # memória simulada / banco de dados simulado
tarefas_concluidas = []
from colorama import Back, Fore, Style, init


init(autoreset=True)

from components.menu import mostrar_menu
from components.adicionar_tarefa import adicionar_tarefa
from components.listar_tarefas import listar_tarefas
from components.gerar_arquivo_pendentes import gerar_arquivo_pendentes
from components.remover_tarefa import remover_tarefa
from components.reverter_tarefa_concluida  import reverter_tarefa_concluida
from components.atualizar_tarefa import atualizar_tarefa
from components.concluir_tarefa import concluir_tarefa
from components.mostrar_tarefas_concluidas import mostrar_tarefas_concluidas
from components.gerar_arquivo_concluidas import gerar_arquivo_concluidas


def main():
    while True:
        mostrar_menu()
        opcao = input(Fore.LIGHTCYAN_EX + "Escolha uma opção: " + Style.RESET_ALL)
        if opcao == "1":
            adicionar_tarefa(lista_de_tarefas_pendentes)
        elif opcao == "2":
            listar_tarefas(lista_de_tarefas_pendentes)
        elif opcao == "3":
            gerar_arquivo_pendentes(lista_de_tarefas_pendentes)
        elif opcao == "4":
            remover_tarefa(lista_de_tarefas_pendentes) 
        elif opcao == "5":
            reverter_tarefa_concluida(lista_de_tarefas_pendentes, tarefas_concluidas)
        elif opcao == "6":
            atualizar_tarefa(lista_de_tarefas_pendentes)
        elif opcao == "7":
            concluir_tarefa(lista_de_tarefas_pendentes, tarefas_concluidas)
        elif opcao == "8":
            mostrar_tarefas_concluidas(tarefas_concluidas)
        elif opcao == "9":
            gerar_arquivo_concluidas(tarefas_concluidas)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print(Fore.LIGHTRED_EX + Back.BLACK + "Hum, algo não saiu conforme o esperado...\nTente novamente inserindo apenas o número da opções desejadas disponíveis no menu!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()