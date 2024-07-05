def menu():
    menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar usuário
[5] Criar conta
[6] Listar contas
[5] Sair

=> ''' 
    return int(input(menu))

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f'Você depositou o valor de R$ {deposito:.2f} na sua conta.\n'
        print('Guardando dinheiro...')
        print('Sua operação foi realizada com sucesso!')
    else:
        print('A operação falhou! Valor informado é inválido.')
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, LIMITE_SAQUES):
    if saque > limite:
        print(f'Esse valor está além do limite de saque. Por favor, digite um valor de até R$ {limite:.2f}.')
    elif numero_saques == LIMITE_SAQUES:
        print('Limite de saques diários atingidos.')
    elif saque > 0:
        if saque > saldo:
            print('Você não possui dinheiro na sua conta bancária!')
        elif saque <= saldo:
            saldo -= saque
            extrato += f'Você sacou o valor de R$ {saque:.2f} da sua conta.\n'
            numero_saques += 1
            print('Sacando...')
            print('Seu saque foi aprovado!')
    else:
        print('Operação cancelada')
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print(extrato)
    print(f'Saldo atual da conta: R$ {saldo:.2f}')
    return saldo, extrato

def criar_usuario(usuarios):
    cpf = int(input('Informe o seu CPF: '))
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Já existe uma conta com esse CPF')
        return
    nome = input('Informe o seu nome: ')
    data_nascimento = input('Informe sua data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe seu endereço (logradouro, número - bairro - cidade/sigla estado): ')
    usuarios.append({'nome': nome, 'data de nascimento': data_nascimento, 'cpf': cpf, 'endereço': endereco})
    
    print('Usuário cadastrado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = int(input('Informe seu CPF: '))
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': AGENCIA, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('Usuário não encontrado, não foi possível criar sua conta')
    
def listar_contas(contas):
    for conta in contas:
        linha = f'''
Agência: {conta['agencia']}
Número da conta: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}\n
'''
        print(linha)

def main():
    AGENCIA = '0001'
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            deposito = float(input('Informe o valor do depósito: '))
            
            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == 2:
            saque = float(input('Digite o valor que deseja sacar: '))
            saldo, extrato = sacar(
                saldo=saldo, 
                saque=saque, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == 3:
            saldo, extrato = exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            print('Operação finalizada')
            break

        else:
            print('Por favor, digite uma opção válida')

main()