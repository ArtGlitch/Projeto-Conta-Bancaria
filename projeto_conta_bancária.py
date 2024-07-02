menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input('Digite qual o valor deseja depositar: '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Você depositou o valor de R$ {deposito:.2f} na sua conta.\n'
            print('Guardando dinheiro...')
            print('Sua operação foi realizada com sucesso!')
        else:
            print('A operação falhou! Valor informado é inválido.')

    elif opcao == 2:
            saque = float(input('Digite o valor que deseja sacar: '))
            if saque > limite:
                print(f'Esse valor está além do limite de saque. Por favor, digite um valor de até R$ {limite}.')
            elif numero_saques == LIMITE_SAQUES:
                print('Limite de saques diários atingidos.')
            elif saque <= limite and saque > 0:
                if saque > saldo:
                    print('Você não possui dinheiro na sua conta bancária!')
                elif saque <= saldo:
                    saldo -= saque
                    extrato += f'Você sacou o valor de R$ {saque} da sua conta.\n'
                    numero_saques += 1
                    print('Sacando...')
                    print('Seu saque foi aprovado!')
            else:
                print('Operação cancelada')


    elif opcao == 3:
        print(extrato)
        print(f'Saldo atual da conta: R$ {saldo:.2f}')

    elif opcao == 4:
        print('Operação finalizada')
        break
    else:
        print('Por favor, digite uma opção válida')
