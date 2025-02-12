from utils.index import colorize

def mostrar_menu():
    print(colorize("\nMenu", "blue", "black"))
    print(colorize("1 - Adicionar tarefa", "blue", "black")) #ctrl + shift + k = apagar linha
    print(colorize("2 - Listar tarefas", "blue", "black")) #alt + shift + tecla para baixo = gera cópia da linha
    print(colorize("3 - Gerar arquivo de tarefas pendentes", "blue", "black"))
    print(colorize("4 - Remover tarefa imediatamente", "blue", "black"))
    print(colorize("5 - Reverter tarefa concluída", "blue", "black"))
    print(colorize("6 - Atualizar tarefa", "blue", "black"))
    print(colorize("7 - Concluir tarefa", "blue", "black"))
    print(colorize("8 - Mostrar tarefas concluídas", "blue", "black"))
    print(colorize("9 - Gerar arquivo de tarefas concluídas", "blue", "black"))
    print(colorize("0 - Sair\n", "blue", "black"))