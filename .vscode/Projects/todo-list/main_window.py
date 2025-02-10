from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QHBoxLayout, QDialog
from PySide6.QtGui import QAction 
import re
from datetime import datetime

def is_float(val):
    return re.fullmatch(r'[+-]?([0-9]*[.])?[0-9]+', val) is not None   

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        # Todo: Configurar o título e o tamanho da janela
        self.setWindowTitle("Aplicativo Radiológico")
        self.setGeometry(100, 100, 600, 400)

        # Menu de ajuda
        # Todo: Adicionar menu de ajuda e ação de instrução
        self.menu_bar = self.menuBar()
        ajuda_menu = self.menu_bar.addMenu("Ajuda")
        ajuda_action = QAction("Instruções", self)
        ajuda_action.triggered.connect(self.mostrar_ajuda)  # Conecta ao método mostrar_ajuda
        ajuda_menu.addAction(ajuda_action)

        # Central widget e layout principal
        # Todo: Criar layout principal e central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Campos de entrada de dados
        # Todo: Criar e adicionar labels e campos de entrada
        labels_and_entries = [
            ("Nome do Paciente", QLineEdit(self)),
            ("Idade do Paciente", QLineEdit(self)),
            ("Peso do Paciente", QLineEdit(self)),
            ("Local do Exame (torax, abdomen, extremidade, cranio)", QLineEdit(self)),
            ("Espessura do Local (cm)", QLineEdit(self)),
            ("Constante do Aparelho", QLineEdit(self)),
        ]

        self.entries = []

        for label_text, entry in labels_and_entries:
            h_layout = QHBoxLayout()
            label = QLabel(label_text)
            h_layout.addWidget(label)
            h_layout.addWidget(entry)
            self.layout.addLayout(h_layout)
            self.entries.append(entry)

        # Atribuir entradas a atributos para fácil acesso
        # Todo: Associar os campos de entrada aos atributos da classe
        self.entry_nome, self.entry_idade, self.entry_peso, self.entry_local, self.entry_espessura, self.entry_constante = self.entries

        # Botão de cálculo
        # Todo: Adicionar botão de cálculo com estilo e conexão para processar dados
        btn_calcular = QPushButton("Calcular Kv e mAs", self)
        btn_calcular.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 5px;")
        btn_calcular.clicked.connect(self.processar_dados)
        self.layout.addWidget(btn_calcular)

    # Método para exibir a caixa de ajuda
    # Todo: Implementar o método mostrar_ajuda
    def mostrar_erro(self, mensagem):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(mensagem)
        msg.setWindowTitle("Erro")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec() 
    
    def mostrar_ajuda(self):
        ajuda_dialog = QDialog(self)
        ajuda_dialog.setWindowTitle("Ajuda")
        layout = QVBoxLayout()
        
        ajuda_texto = (
            "Preencha os campos conforme as instruções:\n\n"
            "Nome do Paciente: Digite o nome completo do paciente.\n"
            "Idade do Paciente: Digite a idade em anos.\n"
            "Peso do Paciente: Digite o peso em kg.\n"
            "Local do Exame: Especifique o local do exame (torax, abdomen, extremidade, cranio).\n"
            "Espessura do Local: Digite a espessura do local em cm.\n"
            "Constante do Aparelho: Digite a constante do aparelho.\n"
        )
        
        ajuda_label = QLabel(ajuda_texto)
        layout.addWidget(ajuda_label)
        
        btn_fechar = QPushButton("Fechar")
        btn_fechar.clicked.connect(ajuda_dialog.accept)
        layout.addWidget(btn_fechar)
        
        ajuda_dialog.setLayout(layout)
        ajuda_dialog.exec() 

    def processar_dados(self):
        info_paciente = self.obter_info_paciente()
        if info_paciente:
            info_paciente = self.calcular_kv(info_paciente)
            if info_paciente:  # Verificar se o cálculo de kv foi bem-sucedido
                self.calcular_mAs(info_paciente)
                self.salvar_dados_paciente(info_paciente)
    
    def obter_info_paciente(self):
        nome_paciente = self.entry_nome.text().title()
        
        if not nome_paciente:
            self.mostrar_erro("Nome do paciente não pode estar vazio.")
            return None
        
        try:
            idade_paciente = int(self.entry_idade.text())
        except ValueError:
            self.mostrar_erro("Idade deve ser um número inteiro.")
            return None
        
        try:
            peso_paciente = float(self.entry_peso.text())
        except ValueError:
            self.mostrar_erro("Peso deve ser um número flutuante.")
            return None
        
        local_exame = self.entry_local.text().strip().lower()
        local_exame = self.verificar_local_exame(local_exame)
        if local_exame is None:
            return None
        
        return nome_paciente, idade_paciente, peso_paciente, local_exame
    
    def verificar_local_exame(self, local_exame):
        locais_validos = ["torax", "abdomen", "extremidade", "cranio"]
        
        if local_exame not in locais_validos:
            self.mostrar_erro("Local do exame não especificado nos parâmetros.")
            return None
        
        return local_exame
    
    def calcular_kv(self, info_paciente):
        nome_paciente, idade_paciente, peso_paciente, local_exame = info_paciente
        fator_local = {
            "torax": 1.0,
            "abdomen": 1.2,
            "extremidade": 0.8,
            "cranio": 1.1
        }
        
        fator = fator_local[local_exame]
        espessura = self.entry_espessura.text()
        constante = self.entry_constante.text()
        
        if not is_float(espessura):
            self.mostrar_erro("Espessura deve ser um número.")
            return None
        
        if not is_float(constante):
            self.mostrar_erro("Constante deve ser um número.")
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

    def calcular_mAs(self, info_paciente):
        mas_com_grade = info_paciente["kv"] / 2  # dentro da grade
        mas_sem_grade = info_paciente["kv"] / 3  # fora da grade
        self.imprimir_info_paciente(info_paciente)
        QMessageBox.information(None, "Resultados de mAs",
                                f'O mAs dentro da grade é: {mas_com_grade}\n'
                                f'O mAs fora da grade é: {mas_sem_grade}')
    
    def imprimir_info_paciente(self, info_paciente):
        QMessageBox.information(None, "Informações do Paciente",
                                f'Nome do paciente: {info_paciente["nome"]}\n'
                                f'Idade do paciente: {info_paciente["idade"]}\n'
                                f'Peso do paciente: {info_paciente["peso"]}\n'
                                f'Local do exame: {info_paciente["local_exame"]}\n'
                                f'O Kv é: {info_paciente["kv"]}')

    def salvar_dados_paciente(self, info_paciente):
        data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("Dados dos Pacientes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write("\n\n")
            arquivo.write(f'Data e Hora: {data_hora_atual}\n')
            arquivo.write(f'Nome do paciente: {info_paciente["nome"]}\n')
            arquivo.write(f'Idade do paciente: {info_paciente["idade"]}\n')
            arquivo.write(f'Peso do paciente: {info_paciente["peso"]}\n')
            arquivo.write(f'Local do exame: {info_paciente["local_exame"]}\n')
            arquivo.write(f'O Kv é: {info_paciente["kv"]}\n')
            arquivo.write(f'O mAs dentro da grade é: {info_paciente["kv"] / 2}\n')
            arquivo.write(f'O mAs fora da grade é: {info_paciente["kv"] / 3}\n')
        print("Dados do paciente salvos com sucesso!")


