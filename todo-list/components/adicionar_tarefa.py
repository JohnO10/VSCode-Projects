from utils.index import colorize
import schedule

def adicionar_tarefa(lista_de_tarefas_pendentes):
    tarefa = input(colorize("Digite o nome da tarefa: \n", "lightmagenta")).capitalize()
    #horario = input("Digite o horário para a tarefa (HH:MM): \n")
    concluida = False

    #schedule.every().day.at(horario).do(adicionar_tarefa)
    lista_de_tarefas_pendentes.append({"tarefa": tarefa, "concluida": concluida})
    print(colorize("Tarefa adicionada com sucesso!", "black", "green"))
    return