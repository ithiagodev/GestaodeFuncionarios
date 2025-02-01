# Gestão de Funcionários
Aplicação de gerenciamento de funcionários em Python. Permite registrar, visualizar, e remover funcionários, além de manter um histórico de demissões e organizar as informações em arquivos de texto para armazenamento persistente.

## Requisitos
Este projeto é desenvolvido inteiramente em Python. Para garantir o funcionamento correto, certifique-se de que sua versão do Python é compatível com o código utilizado.

## Estrutura dos Arquivos
1. **Main Script (ex.: `Painel.py`)**: Arquivo principal para iniciar a aplicação. Contém a função `painel`, responsável pelo menu de opções e chamada de funções principais.
2. **Funções de Gestão**:
   - **Cadastro**: Adiciona novos funcionários com nome, idade, sexo, cargo, função e salário.
   - **Visualização**: Exibe dados de um funcionário específico ou lista todos os funcionários ordenados alfabeticamente.
   - **Remoção**: Remove um funcionário e registra a demissão no histórico com detalhes do tempo de trabalho.
3. **Diretório `db/`**:
   - **funcionarios.txt**: Registro principal de funcionários com suas informações.
   - **empresa.txt**: Armazena o nome da empresa.
   - **historico.txt**: Registra o histórico de demissões com data e tempo de trabalho.

## Como Executar
No terminal, execute:
```bash
python Painel.py
```
O menu interativo permitirá navegar entre as opções de cadastro, exibição e remoção de funcionários.

## Fluxo de Funcionamento
1. **Inicialização**: Verifica e cria automaticamente os arquivos e pastas necessários.
2. **Painel de Controle**: Menu com opções interativas para realizar todas as operações de gestão de funcionários.
3. **Armazenamento em Arquivos**: Mantém dados em arquivos `.txt`, possibilitando fácil leitura e manipulação dos dados registrados.
