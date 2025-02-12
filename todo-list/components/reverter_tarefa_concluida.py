from utils.index import colorize  # Certifique-se de que este caminho está correto
from components.mostrar_tarefas_concluidas import mostrar_tarefas_concluidas
from utils.index import obter_numero_inteiro

def reverter_tarefa_concluida(tarefas_concluidas, lista_de_tarefas_pendentes):
    mostrar_tarefas_concluidas(lista_de_tarefas_pendentes)
    concluidas = input(colorize("Digite o número da tarefa que deseja reverter: ", "lightcyan"))
    if concluidas in tarefas_concluidas:
        lista_de_tarefas_pendentes[concluidas]["concluida"] = True
        tarefas_concluidas.remove(concluidas)
        lista_de_tarefas_pendentes.append(concluidas)
        print(f"Tarefa '{concluidas}' foi restaurada com sucesso para a lista de tarefas pendentes.")
    else:
        print(f"Tarefa '{concluidas}' não encontrada na lista de tarefas concluídas.")