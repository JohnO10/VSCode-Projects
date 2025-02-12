from utils.index import colorize
from utils.index import obter_numero_inteiro
from components.listar_tarefas import listar_tarefas
from components.adicionar_tarefa import adicionar_tarefa

def atualizar_tarefa(lista_de_tarefas_pendentes):
    if lista_de_tarefas_pendentes:
        listar_tarefas(lista_de_tarefas_pendentes)

        numero_tarefa = obter_numero_inteiro(colorize("Informe o número da tarefa: ", "lightcyan"))
        if 1 <= numero_tarefa <= len(lista_de_tarefas_pendentes):
            nova_tarefa = input(colorize("Digite o nome da nova tarefa: ", "lightcyan")).capitalize()
            atualizacao_concluida = False
            #atualizacao_concluida = input(colorize("A tarefa está concluída? (s/n): ", "lightcyan")).lower() == 's'
            lista_de_tarefas_pendentes[numero_tarefa - 1] = {"tarefa": nova_tarefa, "concluida": atualizacao_concluida}
            print(colorize("Tarefa foi atualizada com sucesso!", "black", "green"))
        else:
            print(colorize("Tarefa inexistente!", "red", "black"))
            mensagem = colorize("[1] Tentar novamente\n", "lightcyan") + colorize("[0] Voltar para o menu\n", "lightblue")
            tentar_novamente = input(mensagem)
            if tentar_novamente == "0":
                print(colorize("Ok, voltando para o menu...", "green", "black"))
                return
            if tentar_novamente == "1":
                atualizar_tarefa(lista_de_tarefas_pendentes) #recursão
    else:
        print(colorize("Ops, sinto muito... A sua lista está vazia!", "lightred")) 
        adicionar_nova_tarefa = input(colorize("Gostaria de adicionar nova tarefa agora? (s/n): ", "lightcyan")).lower()
        if adicionar_nova_tarefa == 's':
            adicionar_tarefa(lista_de_tarefas_pendentes)
            return
        else:
            listar_tarefas(lista_de_tarefas_pendentes)
