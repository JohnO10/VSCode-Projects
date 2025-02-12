from utils.index import colorize

def mostrar_tarefas_concluidas(tarefas_concluidas):
    print(colorize("\nTarefas Concluídas:\n", "blue", "black"))
    for indice, concluidas in enumerate(tarefas_concluidas, start=1):
        status = colorize("Concluída", "green")
        print(colorize(f"{indice}. {concluidas['tarefa']} - {status}", "green", "black"))

