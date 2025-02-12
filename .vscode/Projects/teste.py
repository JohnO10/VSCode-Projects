import tkinter as tk
from tkinter import messagebox, ttk
import re

def is_float(val):
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
    

def obter_info_paciente():
    nome_paciente = entry_nome.get().title()
    tentativa = tk.BooleanVar(value=True)
    try:
        idade_paciente = int(entry_idade.get())
    except ValueError:
        mostrar_erro("Idade deve ser um número inteiro.", tentativa, root)
        if not tentativa.get():
            return None

    try:
        peso_paciente = float(entry_peso.get())
    except ValueError:
        mostrar_erro("Peso deve ser um número flutuante.", tentativa, root)
        if not tentativa.get():
            return None

    local_exame = entry_local.get().strip().lower()
    local_exame = verificar_local_exame(local_exame, root)
    if local_exame is None:
        return None
    return nome_paciente, idade_paciente, peso_paciente, local_exame

def verificar_local_exame(local_exame, root):
    locais_validos = ["torax", "abdomen", "extremidade", "cranio"]
    tentativa = tk.BooleanVar(value=True)
    while local_exame not in locais_validos:
        mostrar_erro("Local do exame não especificado nos parâmetros.", tentativa, root)
        if not tentativa.get():
            return None
        local_exame = entry_local.get().strip().lower()
    return local_exame

def calcular_kv(info_paciente):
    nome_paciente, idade_paciente, peso_paciente, local_exame = info_paciente
    fator_local = {
        "torax": 1.0,
        "abdomen": 1.2,
        "extremidade": 0.8,
        "cranio": 1.1
    }
    
    fator = fator_local[local_exame]
    espessura = entry_espessura.get()
    constante = entry_constante.get()
    tentativa = tk.BooleanVar(value=True)
    if not is_float(espessura):
        mostrar_erro("Espessura deve ser um número.", tentativa, root)
        if not tentativa.get():
            return None
    if not is_float(constante):
        mostrar_erro("Constante deve ser um número.", tentativa, root)
        if not tentativa.get():
            return None
    espessura_local = float(espessura)
    constante_aparelho = float(constante)
    kv_calculo = (espessura_local * 2 + constante_aparelho)

    info_paciente = {
        "nome": nome_paciente,
        "idade": idade_paciente,
        "peso": peso_paciente,
        "local_exame": local_exame,
        "kv": kv_calculo,
        "espessura_local": espessura_local,
        "constante_aparelho": constante_aparelho
    }
    return info_paciente


def imprimir_info_paciente(info_paciente):
    messagebox.showinfo("Informações do Paciente",
                        f'Nome do paciente: {info_paciente["nome"]}\n'
                        f'Idade do paciente: {info_paciente["idade"]}\n'
                        f'Peso do paciente: {info_paciente["peso"]}\n'
                        f'Local do exame: {info_paciente["local_exame"]}\n'
                        f'O Kv é: {info_paciente["kv"]}')

def calcular_mAs(info_paciente):
    mas_com_grade = info_paciente["kv"] / 2  # dentro da grade
    mas_sem_grade = info_paciente["kv"] / 3  # fora da grade
    imprimir_info_paciente(info_paciente)
    messagebox.showinfo("Resultados de mAs",
                        f'O mAs dentro da grade é: {mas_com_grade}\n'
                        f'O mAs fora da grade é: {mas_sem_grade}')

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


def processar_dados():
    info_paciente = obter_info_paciente()
    if info_paciente:
        info_paciente = calcular_kv(info_paciente)
        if info_paciente:  # Verificar se o cálculo de kv foi bem-sucedido
            calcular_mAs(info_paciente)
            salvar_dados_paciente(info_paciente)


root = tk.Tk()
root.title("Aplicativo Radiológico")
root.geometry("400x350")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 10))
style.configure("TEntry", padding=5)

ttk.Label(root, text="Nome do Paciente").grid(row=0, column=0, padx=10, pady=10)
entry_nome = ttk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Idade do Paciente").grid(row=1, column=0, padx=10, pady=10)
entry_idade = ttk.Entry(root)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(root, text="Peso do Paciente").grid(row=2, column=0, padx=10, pady=10)
entry_peso = ttk.Entry(root)
entry_peso.grid(row=2, column=1, padx=10, pady=10)

ttk.Label(root, text="Local do Exame").grid(row=3, column=0, padx=10, pady=10)
entry_local = ttk.Entry(root)
entry_local.grid(row=3, column=1, padx=10, pady=10)

ttk.Label(root, text="Espessura do Local (cm)").grid(row=4, column=0, padx=10, pady=10)
entry_espessura = ttk.Entry(root)
entry_espessura.grid(row=4, column=1, padx=10, pady=10)

ttk.Label(root, text="Constante do Aparelho").grid(row=5, column=0, padx=10, pady=10)
entry_constante = ttk.Entry(root)
entry_constante.grid(row=5, column=1, padx=10, pady=10)

ttk.Button(root, text="Calcular Kv e mAs", command=processar_dados).grid(row=6, columnspan=2, padx=10, pady=20)

root.mainloop()
