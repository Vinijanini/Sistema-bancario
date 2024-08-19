import sqlite3

#conecta o banco de dados e o cursor
banco = sqlite3.connect('banco.db')
cursor = banco.cursor()

#cria a tabela#
cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, cpf text, saldo DECIMAL(10, 2) NOT NULL, senha text)')

#Classe do objeto "cliente"#
class Cliente:
    def __init__(self, id, nome, cpf, saldo, senha):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.senha = senha

    #Método que retorna o saldo#
    def retorna_saldo(self):
        return self.saldo

#função de linha (apenas para organização)#
def lin():
    print('-=' * 13)

#função de depósito#
def deposito():
    lin()
    print('Depositar')
    lin()

    try:
        valor_deposito = float(input('Valor para depositar:'))
        return valor_deposito
    except:
        print('Erro no depósito!')

#função de saque#
def saque(saldo):
    lin()
    print('Saque')
    lin()

    # tratamento de erro#
    while True:
        try:
            valor_saque = float(input('Valor de saque:'))

            #tratamento de erro caso o valor de saque seja maior que o saldo bancário#
            while valor_saque > saldo:
                print('Erro!, você não tem esse saldo!')
                valor_saque = float(input('Valor de saque:'))

            break
        except:
            print('Erro no saque!')

    return valor_saque

#função que será executada assim que o usuário logar em sua conta bancária#
def logou(cliente):
    cliente_logado = Cliente(
        cliente['id'],
        cliente['nome'],
        cliente['cpf'],
        cliente['saldo'],
        cliente['senha']
    )
    saldo = cliente_logado.retorna_saldo()
    while True:
        lin()
        print(' - Conta bancária -')
        lin()

        #print com o nome e o saldo da cliente#
        print(f'{cliente_logado.nome} - Saldo R${saldo:.2f}')
        lin()
        print('[1] Depositar')
        print('[2] Sacar')
        print('[3] Sair da conta')

        #tratamento de erro#
        while True:
            try:
                escolha = int(input('>>>>>>>>>>>>>>>>'))

                while escolha not in range(1, 4):
                    print('Opção inválida')
                    escolha = int(input('>>>>>>>>>>>>>>>>'))

                break
            except:
                print('Opção inválida')

        #condicionais avaliando a variável "escolha"#
        match escolha:
            #caso o cliente queira depositar#
            case 1:
                saldo += deposito()

                #inserção do novo saldo com o depósito aplicado no banco de dados#
                try:
                    cursor.execute('UPDATE clientes SET saldo = "' + str(saldo) + '" WHERE id = "' + str(cliente['id']) + '" ')
                    banco.commit()
                    print('Depósito efetuado!')
                except:
                    print('Erro no depósito :(')

            #caso o cliente queira sacar#
            case 2:

                if saldo == 0:
                    print('Você não tem saldo para saque :(')
                else:
                    saldo -= saque(saldo)

                    #inserção do novo saldo com o saque aplicado no banco de dados#
                    try:
                        cursor.execute('UPDATE clientes SET saldo = "' + str(saldo) + '" WHERE id = "' + str(cliente['id']) + '" ')
                        banco.commit()
                        print('Saque efetuado!')
                    except:
                        print('Erro no saque :(')

            #caso o cliente queira deslogar de sua conta bancária#
            case 3:
                print('Deslogado com sucesso!')
                break

#função de login de conta#
def entrar():
    cliente_logado = {}
    lin()
    print('Logar em conta')
    lin()

    #usuário digita seu cpf e sua senha#
    cpf_log = str(input('Digite seu CPF:'))
    senha_log = str(input('Digite sua senha:'))

    clientes_cadastrados = [cliente for cliente in cursor.execute("SELECT * FROM clientes").fetchall()]

    for cliente in clientes_cadastrados:

        #se o cpf e senha passados pelo clientes baterem com uma conta, a variável "cliente_logado" se torna um objeto populado pelos dados da conta#
        if cliente[2] == cpf_log and cliente[-1] == senha_log:
            cliente_logado = {
                'id': cliente[0],
                'nome': cliente[1],
                'cpf': cliente[2],
                'saldo': cliente[3],
                'senha': cliente[4]
            }

    #caso o objeto "cliente_logado" esteja vazio, significa os dados recebidos no loguin não batem com nenhuma conta bancária#
    if cliente_logado == {}:
        print('CPF ou Senha inválidos!')

    #caso o cliente consiga logar, a função "logou" é executada#
    else:
        print('Logado com sucesso!')
        logou(cliente_logado)

#função de cadastro#
def cadastro():
    lin()
    print('Criar conta')
    lin()
    nome = str(input('Digite seu nome:')).title()

    #tratamento de erro#
    while not(nome.replace(' ', '').isalpha()):
        print('Nome inválido!, digite apenas letras!')
        nome = str(input('Digite seu nome:')).title()

    cpf = str(input('CPF (apenas números):'))
    cpfs_cadastrados = [CPF[2] for CPF in cursor.execute("SELECT * FROM clientes").fetchall()]

    #tratamento de erro#
    while len(cpf) != 11 or cpf in cpfs_cadastrados or cpf.isalpha():
        print('CPF inválido! ou já existe')
        cpf = str(input('CPF (apenas números):'))

    senha = str(input('Nova senha:'))

    #confirmação de senha#
    confirm = str(input('Confirmar senha:'))
    while senha != confirm:
        print('Senhas diferentes!')
        senha = str(input('Nova senha:'))
        confirm = str(input('Confirmar senha:'))

    novo_cliente = Cliente(None, nome, cpf, 0, senha)

    #Inserção do novo cliente ao banco de dados#
    try:
        cursor.execute('INSERT INTO clientes (nome, cpf, saldo, senha) VALUES ("' + novo_cliente.nome + '", "' + novo_cliente.cpf + '", "' + str(0) + '", "' + novo_cliente.senha + '")')
        banco.commit()
        print('Conta cadastrada com sucesso!')
    except:
        print('Erro no cadastro :(')

#função de finalizar o programa#
def sair():
    print('programa finalizado!')
    banco.close()
    quit()

#função principal#
def main():
    lin()
    print('Menu Principal')
    lin()
    print('[1] Criar nova conta')
    print('[2] Entrar em minha conta')
    print('[3] Sair')

    #tratamento de erro#
    while True:
        try:
            esc = int(input('>>>>>>>>>>>>>>>>>'))
            while esc not in range(1, 4):
                print('opção inválida!')
                esc = int(input('>>>>>>>>>>>>>>>>>'))
            break
        except ValueError:
            print('opção inválida')

    #condicionais avaliando a variável "escolha"#
    match esc:
        case 1:
            cadastro()

        case 2:
            entrar()

        case 3:
            sair()

#a função principal será executada infinitamente ate que o usuário queira sair#
while True:
    main()