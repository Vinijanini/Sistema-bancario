    Conexão com o Banco de Dados:
        O código se conecta a um banco de dados SQLite chamado banco.db.
        Cria uma tabela chamada clientes se ela não existir, com campos para id, nome, cpf, saldo e senha.

    Classe Cliente:
        Define uma classe Cliente para representar um cliente bancário com atributos id, nome, cpf, saldo e senha.
        Inclui um método retorna_saldo() que retorna o saldo do cliente.

    Funções Auxiliares:
        lin(): Imprime uma linha de separação para melhor formatação no terminal.
        deposito(): Solicita ao usuário o valor para depósito e o retorna. Trata erros de entrada.
        saque(saldo): Solicita ao usuário o valor para saque, garantindo que não seja maior que o saldo atual. Trata erros de entrada.

    Função logou(cliente):
        Executa as ações permitidas ao cliente depois do login: depositar, sacar ou sair da conta.
        Atualiza o saldo no banco de dados após as transações de depósito ou saque.

    Função entrar():
        Permite ao usuário logar na sua conta fornecendo CPF e senha.
        Se as credenciais são corretas, chama a função logou(cliente) para gerenciar a conta do cliente.

    Função cadastro():
        Permite o cadastro de um novo cliente, incluindo validação de nome, CPF e senha.
        Adiciona o novo cliente à tabela clientes no banco de dados.

    Função sair():
        Finaliza o programa, fecha a conexão com o banco de dados e encerra a execução.

    Função Principal main():
        Exibe o menu principal com opções para criar uma nova conta, entrar em uma conta existente ou sair do programa.
        Trata erros de entrada para garantir que a escolha do usuário esteja dentro das opções válidas.

    Loop Principal:
        Executa a função main() repetidamente até que o usuário escolha sair.

Resumo das Funcionalidades

    - Cadastro de clientes: Permite criar uma nova conta bancária, com validação de CPF e senha.
    - Login de clientes: Permite aos clientes logar na conta usando CPF e senha.
    - Gerenciamento de contas: Após o login, os clientes podem depositar, sacar ou sair da conta.
    - Atualização de saldo: O saldo é atualizado no banco de dados após cada transação.
