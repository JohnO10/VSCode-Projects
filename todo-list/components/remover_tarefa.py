from utils.index import colorize
from utils.index import obter_numero_inteiro
from components.adicionar_tarefa import adicionar_tarefa
from components.listar_tarefas import listar_tarefas


def remover_tarefa(lista_de_tarefas_pendentes):
    listar_tarefas(lista_de_tarefas_pendentes)

    if not lista_de_tarefas_pendentes:
        print(colorize("A lista de tarefas está vazia!", "red", "black"))
        adicionar_nova_tarefa = input(colorize("Gostaria de adicionar uma nova tarefa? s/n: ", "lightcyan")).lower()
        if adicionar_nova_tarefa == "s":
            adicionar_tarefa()
        return

    numero_tarefa = obter_numero_inteiro(colorize("Informe o número da tarefa: ", "lightcyan"))
    if 1 <= numero_tarefa <= len(lista_de_tarefas_pendentes):
        lista_de_tarefas_pendentes.pop(numero_tarefa - 1)
        print(colorize("A tarefa foi removida!", "black", "green"))
        if len(lista_de_tarefas_pendentes) < 1:
            return
        else:
            listar_tarefas(lista_de_tarefas_pendentes)
    else:
        print(colorize("Tarefa inexistente! Informe um número válido!", "red", "black"))
        mensagem = colorize("[1] Tentar novamente\n", "lightgreen") + colorize("[0] Voltar para o menu\n", "lightgreen")
        tentar_novamente = input(mensagem)
        if tentar_novamente == "0":
            print(colorize("Ok, voltando para o menu pricipal...", "green", "black"))
            return
        if tentar_novamente == "1":
            remover_tarefa()