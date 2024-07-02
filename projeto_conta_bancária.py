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
        saldo += deposito
        extrato += f'Você depositou o valor de R$ {deposito} na sua conta.\n'
        print('Guardando dinheiro...')
        print('Sua operação foi realizada com sucesso!')

    elif opcao == 2:
        while numero_saques < LIMITE_SAQUES:
            saque = float(input('Digite o valor que deseja sacar: '))
            if saque > limite:
                print(f'Esse valor está além do limite de saque. Por favor, digite um valor de até R$ {limite}.')
            elif saque <= limite and saque > 0:
                if saque <= saldo:
                    saldo -= saque
                    extrato += f'Você sacou o valor de R$ {saque} da sua conta.\n'
                    print('Sacando...')
                    print('Seu saque foi aprovado!')
            elif saque == 0:
                print('Operação cancelada')
            else:
                print('Você não possui dinheiro em sua conta bancária!')
            numero_saques += 1
            if numero_saques == LIMITE_SAQUES:
                print('Seu limite de saques diários foi atingido.')
                break
            break


    elif opcao == 3:
        print(extrato)
        print(f'\nSaldo atual da conta: {saldo}')

    elif opcao == 4:
        print('Operação finalizada')
        break
    else:
        print('Por favor, digite uma opção válida')
