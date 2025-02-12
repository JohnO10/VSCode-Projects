from utils.index import colorize
import re

def gerar_arquivo_concluidas(tarefas_concluidas):
    with open("Tarefas concluídas.txt", "w") as file:
        for indice, concluida in enumerate(tarefas_concluidas, start=1):
            if isinstance(concluida, dict) and 'tarefa' in concluida:
                file.write(f'{indice}. {concluida["tarefa"]}' + "\n")
            else:
                file.write(f'{indice}. {concluida}' + "\n")
    print(colorize("Tarefas salvas em 'Tarefas concluídas.txt'.", "green" ))

'''''
dicionario = {f'concluidas': "\x1b[34m45\x1b[0m", 'concluida': True}

def remover_ansi(texto):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', texto)

# Remover caracteres de escape do valor da chave 'concluidas'
dicionario['concluidas'] = remover_ansi(dicionario['concluidas'])

tarefas_concluidas = [{'tarefa': dicionario['concluidas'], 'concluida': dicionario['concluida']}]

'''