from utils.index import colorize


def gerar_arquivo_pendentes(lista_de_tarefas_pendentes):
     with open("Tarefas pendentes.txt", "w") as file:
        for indice, pendente in enumerate(lista_de_tarefas_pendentes, start=1):
            if isinstance(pendente, dict) and 'tarefa' in pendente:
                file.write(f'{indice}. {pendente["tarefa"]}' + "\n")
            else:
                file.write(f'{indice}. {pendente}' + "\n")
        print(colorize("Tarefas salvas em 'Tarefas pendentes.txt'.", "green" ))