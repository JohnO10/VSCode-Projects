import tkinter as tk
from tkinter import ttk
import os

def is_float(val):
    import re
    return re.fullmatch(r'[+-]?([0-9]*[.])?[0-9]+', val) is not None

def mostrar_erro(mensagem, tentativa, root):
    erro_janela = tk.Toplevel(root)
    erro_janela.title("Erro")
    erro_janela.geometry("450x150")
    erro_janela.configure(bg="white")

    lbl_erro = ttk.Label(erro_janela, text=mensagem, background="red", foreground="white")
    lbl_erro.pack(pady=10)

    btn_frame = ttk.Frame(erro_janela)
    btn_frame.pack(pady=10)

    btn_tentar_novamente = ttk.Button(btn_frame, text="Tentar Novamente", command=erro_janela.destroy, width=20)
    btn_tentar_novamente.grid(row=0, column=0, padx=10)

    btn_cancelar = ttk.Button(btn_frame, text="Cancelar", command=lambda: fechar_tudo(tentativa, erro_janela, root), width=20)
    btn_cancelar.grid(row=0, column=1, padx=10)

    root.wait_window(erro_janela)

def fechar_tudo(tentativa, erro_janela, root):
    tentativa.set(False)
    erro_janela.destroy()
    root.destroy()
    #os.system('cls' if os.name == 'nt' else 'clear')
    

def verificar_local_exame(local_exame, root):
    locais_validos = ["torax", "abdomen", "extremidade", "cranio"]
    tentativa = tk.BooleanVar(value=True)
    while local_exame not in locais_validos:
        mostrar_erro("Local do exame não especificado nos parâmetros.", tentativa, root)
        if not tentativa.get():
            return None
        local_exame = root.entry_local.get().strip().lower
    return local_exame

def salvar_dados_paciente(info_paciente):
    with open("Dados dos Pacientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write("\n\n")
        arquivo.write(f'Nome do paciente: {info_paciente["nome"]}\n')
        arquivo.write(f'Idade do paciente: {info_paciente["idade"]}\n')
        arquivo.write(f'Peso do paciente: {info_paciente["peso"]}\n')
        arquivo.write(f'Local do exame: {info_paciente["local_exame"]}\n')
        arquivo.write(f'O Kv é: {info_paciente["kv"]}\n')
        arquivo.write(f'O mAs dentro da grade é: {info_paciente["kv"] / 2}\n')
        arquivo.write(f'O mAs fora da grade é: {info_paciente["kv"] / 3}\n')
    print("Dados do paciente salvos com sucesso!")
