from config.comandos import *

def painel():
    import time
    import sys, os
    sys.path.insert(0, os.path.abspath(os.curdir))

    # Definições Globais
    diretorio = "db"
    caminho_arquivo1 = os.path.join(diretorio, "empresa.txt")

    # Funções de Validação
    def leiaint(msg):
        while True:
            try:
                n = int(input(msg))
            except (ValueError, TypeError):
                print("\033[31mERRO\033[m! Por favor, digite um número válido.")
                continue
            except KeyboardInterrupt:
                print("\n\033[31mUsuário preferiu não digitar esse dado\033[m!")
                return 0
            else:
                return n

    def leiastr(msg):
        while True:
            try:
                n = input(msg).strip()
                if not n.replace(" ", "").isalpha():
                    raise ValueError("Nome inválido.")
            except ValueError:
                print("\033[31mERRO!\033[m Por favor, digite um texto válido.")
                continue
            except KeyboardInterrupt:
                print("\n\033[31mUsuário preferiu não digitar esse dado.\033[m")
                return None
            else:
                return n

    def leiafloat(msg):
        while True:
            try:
                n = float(input(msg))
            except (ValueError, TypeError):
                print("\033[31mERRO\033[m! Por favor, digite um número válido.")
                continue
            except KeyboardInterrupt:
                print("\n\033[31mUsuário preferiu não digitar esse dado\033[m!")
                return 0
            else:
                return n

    def linha(tam=42):
        return "-" * tam

    def cabeçalho(txt, cor="\033[34m"):
        print(linha())
        print(f'{cor}{txt.center(42)}\033[m')
        print(linha())

    inicializar_arquivo()

    if os.path.exists(caminho_arquivo1):
        try:
            with open(caminho_arquivo1, "r") as arquivo:
                nome_salvo = arquivo.read().strip()
                if nome_salvo and nome_salvo != "Nome da Empresa:":
                    cabeçalho(f"Empresa: {nome_salvo}")
                else:
                    cabeçalho("INICIANDO PROGRAMA")
        except OSError:
            print("\033[31mERRO!\033[m Não foi possível carregar o nome da empresa.")
    else:
        cabeçalho("INICIANDO PROGRAMA")

    nome_empresa()

    # Menu Principal
    def menu():
        cabeçalho("GESTÃO DE FUNCIONÁRIOS")
        print("Digite 1 para \033[32mCADASTRAR UM NOVO FUNCIONÁRIO\033[m")
        print("Digite 2 para exibir os \033[33mDADOS DE UM FUNCIONÁRIO\033[m")
        print("Digite 3 para exibir os \033[33mDADOS DE TODOS OS FUNCIONÁRIOS\033[m")
        print("Digite 4 para \033[31mREMOVER UM FUNCIONÁRIO\033[m")
        print("Digite 5 para \033[31mSAIR DA GESTÃO DE FUNCIONÁRIOS\033[m")

    while True:
        menu()
        opcao = leiaint("Escolha uma das opções para prosseguir: ")

        match opcao:
            case 1:
                cabeçalho("Informe os dados do novo funcionário", cor="\033[32m")
                nome = leiastr("Nome: ").capitalize()
                idade = leiaint("Idade: ")
                while True:
                    sexo = input("Sexo [M/F]: ").strip().upper()
                    if sexo in "MF":
                        break
                    print("\033[31mERRO!\033[m Digite apenas \033[32mM\033[m ou \033[31mF\033[m.")
                cargo = leiastr("Cargo: ")
                funcao = leiastr("Função: ")
                salario = leiafloat("Salário: ")
                cadastrar_funcionario(nome, idade, sexo, cargo, funcao, salario)

            case 2:
                cabeçalho("Dados de um funcionário", cor="\033[33m")
                Id = input("Digite o ID do funcionário: ").strip()
                exibir_dados_funcionario(Id)

            case 3:
                cabeçalho("Dados de todos os funcionários", cor="\033[33m")
                exibir_todos_funcionarios()

            case 4:
                cabeçalho("REMOVER FUNCIONÁRIO", cor="\033[31m")
                Id = input("Digite o ID do funcionário: ").strip()
                remover_funcionario(Id)

            case 5:
                cabeçalho("FINALIZANDO...", cor="\033[31m")
                time.sleep(2)
                print("\033[32mPrograma encerrado. Volte sempre!\033[m")
                break

            case _:
                print("\033[31mOpção inválida!\033[m Escolha entre 1 e 5.")