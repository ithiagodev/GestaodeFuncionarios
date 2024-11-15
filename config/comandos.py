import os
import random
import datetime
import string

# Diretórios e caminhos dos arquivos
diretorio = "db"
caminho_arquivo = os.path.join(diretorio, "funcionarios.txt")
caminho_arquivo1 = os.path.join(diretorio, "empresa.txt")
caminho_remocao = os.path.join(diretorio, "historico.txt")

# Cabeçalho para arquivos
CABECALHO_FUNCIONARIOS = "ID | Nome | Idade | Sexo | Cargo | Funcao | Salario | Inicio\n"
CABECALHO_EMPRESA = "Nome da Empresa:\n"

# Inicializar arquivos
def inicializar_arquivo():
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
        print(f"Pasta '{diretorio}' criada.")
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write(CABECALHO_FUNCIONARIOS)
        print(f"Arquivo '{caminho_arquivo}' foi criado.")
    if not os.path.exists(caminho_arquivo1):
        with open(caminho_arquivo1, "w") as arquivo:
            arquivo.write(CABECALHO_EMPRESA)
        print(f"Arquivo '{caminho_arquivo1}' foi criado.")
    if not os.path.exists(caminho_remocao):
        with open(caminho_remocao, "w") as arquivo:
            arquivo.write("ID | Nome | Cargo | Inicio | Fim | Tempo de Trabalho\n")
        print(f"Arquivo '{caminho_remocao}' foi criado.")

# Manipulação do nome da empresa
def nome_empresa(nome_empresa=None):
    if os.path.exists(caminho_arquivo1):
        try:
            with open(caminho_arquivo1, "r") as arquivo:
                linhas = arquivo.readlines()
                if len(linhas) > 1:
                    nome_salvo = linhas[1].strip()
                    if nome_salvo:
                        return nome_salvo
        except OSError as e:
            print(f"Erro ao acessar o arquivo da empresa: {e}")
    
    if nome_empresa is None:
        nome_empresa = input("Informe o nome da empresa: ").strip()

    try:
        with open(caminho_arquivo1, "w") as arquivo:
            arquivo.write(CABECALHO_EMPRESA)
            arquivo.write(nome_empresa)
    except OSError as e:
        print(f"Erro ao salvar o nome da empresa: {e}")
        return None

    return nome_empresa

# Gerar ID único para funcionários
def gerar_id():
    return ''.join(random.choices(string.ascii_uppercase, k=3)) + ''.join(random.choices("0123456789", k=3))

# Cadastro de funcionários
def cadastrar_funcionario(nome="Não definido", idade="Não definido", sexo="Não definido", cargo="Não definido", funcao="Não definido", salario="Não definido"):
    id_funcionario = gerar_id()
    inicio = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M")
    try:
        with open(caminho_arquivo, "a") as arquivo:
            arquivo.write(f"[{id_funcionario}] | {nome} | {idade} | {sexo} | {cargo} | {funcao} | {salario:.2f} | {inicio}\n")
        print(f"Funcionário \033[32m{nome}\033[m com ID \033[33m{id_funcionario}\033[m foi cadastrado com sucesso!")
    except OSError as e:
        print(f"Erro ao salvar o funcionário: {e}")

# Exibir dados de um funcionário
def exibir_dados_funcionario(id_funcionario):
    try:
        with open(caminho_arquivo, "r") as arquivo:
            next(arquivo)
            for linha in arquivo:
                dados = linha.strip().split(" | ")
                if len(dados) >= 8 and dados[0].strip('[]') == id_funcionario:
                    print(f"ID: {dados[0]} | Nome: {dados[1]} | Idade: {dados[2]} | Sexo: {dados[3]} | "
                          f"Cargo: {dados[4]} | Função: {dados[5]} | Salário: {dados[6]} | Início: {dados[7]}")
                    return
        print(f"Funcionário com ID '\033[33m{id_funcionario}\033[m' não encontrado.")
    except FileNotFoundError:
        print("Arquivo de funcionários não encontrado.")
    except OSError as e:
        print(f"Erro ao acessar o arquivo de funcionários: {e}")

# Exibir todos os funcionários
def exibir_todos_funcionarios():
    funcionarios = []
    try:
        with open(caminho_arquivo, "r") as arquivo:
            next(arquivo)
            for linha in arquivo:
                dados = linha.strip().split(" | ")
                if len(dados) >= 8:
                    funcionarios.append(dados)
        if funcionarios:
            funcionarios.sort(key=lambda x: x[1])
            print("Lista de Todos os Funcionários em Ordem Alfabética:")
            for dados in funcionarios:
                print(f"ID: {dados[0]} | Nome: {dados[1]} | Idade: {dados[2]} | Sexo: {dados[3]} | "
                      f"Cargo: {dados[4]} | Função: {dados[5]} | Salário: {dados[6]} | Início: {dados[7]}")
        else:
            empresa = nome_empresa()
            print(f"{empresa} ainda não fez nenhuma contratação.")
    except FileNotFoundError:
        print("Arquivo de funcionários não encontrado.")
    except OSError as e:
        print(f"Erro ao acessar o arquivo de funcionários: {e}")

# Remoção de funcionários
def remover_funcionario(id_funcionario):
    funcionarios = []
    demitido = None
    try:
        with open(caminho_arquivo, "r") as arquivo:
            next(arquivo)
            for linha in arquivo:
                dados = linha.strip().split(" | ")
                if len(dados) >= 8:
                    if dados[0].strip('[]') == id_funcionario:
                        demitido = dados
                    else:
                        funcionarios.append(dados)
        
        if demitido:
            inicio = datetime.datetime.strptime(demitido[7], "%d/%m/%Y - %H:%M")
            fim = datetime.datetime.now()
            tempo_trabalho = fim - inicio
            dias = tempo_trabalho.days
            horas, resto = divmod(tempo_trabalho.seconds, 3600)
            minutos = resto // 60
            tempo_trabalho_formatado = f"{dias} dias, {horas} horas e {minutos} minutos"
            
            with open(caminho_remocao, "a") as arquivo:
                arquivo.write(f"{demitido[0]} | {demitido[1]} | {demitido[4]} | {demitido[7]} | "
                              f"{fim.strftime('%d/%m/%Y - %H:%M')} | {tempo_trabalho_formatado}\n")
                
            print(f"Funcionário \033[32m{demitido[1]}\033[m demitido após {tempo_trabalho_formatado}.")
        
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write(CABECALHO_FUNCIONARIOS)
            for funcionario in funcionarios:
                arquivo.write(" | ".join(funcionario) + "\n")
        
        if not demitido:
            print(f"Funcionário com ID '\033[33m{id_funcionario}\033[m' não encontrado.")
    except FileNotFoundError:
        print("Arquivo de funcionários não encontrado.")
    except OSError as e:
        print(f"Erro ao acessar o arquivo de funcionários: {e}")