nome = "Kauan"
deposito = 0
saques = 3
limite = 500
extrato = 1000


while True:

    print(" [a] Depositar  [b] Sacar [c] Extrato [d] Sair ") 
    resp = input( f' Olá {nome}, qual operação deseja efetuar ? .... [a, b, c, d] ')

    #if not resp :

    if resp == 'a' :
        deposito = int(input('Quanto deseja depositar ?'))
        
        print('Seu dinheiro foi depositado com sucesso.')
        extrato = extrato + deposito

    elif resp == 'b' :
        saque = float(input("Quanto deseja sacar ? "))
        if saque > limite:
            print(' Você não pode sacar mais de R$ 500,00. ')
        else:
            if saque > extrato:
                print('_ERROR_ (saldo insuficiente).')
            else:
                print(f'Saque efetuado com sucesso! Agora resta R${extrato - saque} em sua conta.')
                saques = saques - 1
                print(f'Você pode ainda pode efetuar {saques} saques.')
                extrato = extrato - saque
                if saques == 0:
                    print('_ERROR_ (você não tem mais saques disponíveis no momento.)')

    elif resp == 'c' :
        print(f' Você possui R${extrato} em sua conta')

    elif resp == 'd' :
        break

    else:
        print("_ERROR_ (digite uma das opções).")

print('Você saiu da sua conta.')

