from utils.index import colorize
from utils.index import obter_numero_inteiro
from components.listar_tarefas import listar_tarefas

def concluir_tarefa(lista_de_tarefas_pendentes, tarefas_concluidas):
    listar_tarefas(lista_de_tarefas_pendentes)
    indice = obter_numero_inteiro(colorize("Digite o número da tarefa que deseja marcar como concluída: ", "lightcyan")) - 1
    if 0 <= indice < len(lista_de_tarefas_pendentes):
        lista_de_tarefas_pendentes[indice]["concluida"] = True
        concluidas = lista_de_tarefas_pendentes.pop(indice)
        tarefas_concluidas.append(concluidas)
        mensagem = f"Tarefa '{concluidas['tarefa']}' foi marcada como concluída e movida para a lista de tarefas concluídas com sucesso!"
        print(colorize(mensagem, "green", "black"))
        #print(colorize(f"Tarefa '{concluidas['tarefa']}' foi marcada como concluída e movida para a lista de tarefas concluídas com sucesso!", "green", "black"))
    else:
        print(colorize("Número inválido.", "red", "black"))
        mensagem = colorize("[1] Tentar novamente\n", "lightcyan") + colorize("[0] Voltar para o menu\n", "lightblue")
        tentar_novamente = input(mensagem)
        if tentar_novamente == "0":
            print(colorize("Ok, voltando para o menu...", "green", "black"))
            return
        if tentar_novamente == "1":
            concluir_tarefa(lista_de_tarefas_pendentes, tarefas_concluidas)