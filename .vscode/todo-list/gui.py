import tkinter as tk
from tkinter import messagebox, ttk
from utils import verificar_local_exame, salvar_dados_paciente, mostrar_erro, is_float


def obter_info_paciente():
    nome_paciente = root.entry_nome.get().title()
    tentativa = tk.BooleanVar(value=True)
    
    if not nome_paciente:
        mostrar_erro("O campo 'Nome do Paciente' não pode estar vazio!", tentativa, root)
        if not tentativa.get():
            return None

    try:
        idade_paciente = int(root.entry_idade.get())
    except ValueError:
        mostrar_erro("Erro", "Idade deve ser um número inteiro. Ex: 1, 2, 10, 77", tentativa, root)
        if not tentativa.get():
            return None

    try:
        peso_paciente = float(root.entry_peso.get())
    except ValueError:
        mostrar_erro("Erro", "Peso deve ser um número flutuante. Ex: 10.7, 77.44", tentativa, root)
        if not tentativa.get():
            return None

    local_exame = root.entry_local.get().strip().lower()
    local_exame = verificar_local_exame(local_exame, root)
    if local_exame is None:
        return None

    return nome_paciente, idade_paciente, peso_paciente, local_exame

def calcular_kv(info_paciente):
    nome_paciente, idade_paciente, peso_paciente, local_exame = info_paciente
    fator_local = {
        "torax": 1.0,
        "abdomen": 1.2,
        "extremidade": 0.8,
        "cranio": 1.1
    }
    
    fator = fator_local[local_exame]
    espessura = root.entry_espessura.get()
    constante = root.entry_constante.get()
    tentativa = tk.BooleanVar(value=True)
    
    if not is_float(espessura):
        mostrar_erro("Erro", "Espessura deve ser um número flutuante. Ex: 10.7, 77.44", tentativa, root)
        if not tentativa.get():
            return None
    
    if not is_float(constante):
        mostrar_erro("Erro", "Constante deve ser um número flutuante. Ex: 10.7, 77.44", tentativa, root)
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

def processar_dados():
    while True:
        info_paciente = obter_info_paciente()
        if info_paciente:
            info_paciente = calcular_kv(info_paciente)
            if info_paciente:
                calcular_mAs(info_paciente)
                salvar_dados_paciente


root = tk.Tk()
root.title("Easy Radiology")
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
