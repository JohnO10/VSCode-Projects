from utils.index import colorize

def listar_tarefas(lista_de_tarefas_pendentes):
    if lista_de_tarefas_pendentes:
        print(colorize("\nTarefas atuais:\n", "green", "black"))
        for indice, tarefa in enumerate(lista_de_tarefas_pendentes, start=1):
            status = colorize("concluída", "green") if tarefa["concluida"] else colorize("Pendente","yellow")
            #horario = tarefa["horario"]
            print(f"{indice}. {tarefa['tarefa']} - {status}")
    else:
        print(colorize("Nenhuma tarefa encontrada.", "red", "black"))
        return