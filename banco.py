from funcoes import *

while True:
    print(menu())
    opcao = input('Escolha uma opção: ')

    if opcao == 'x':
        fazer_login()
    elif opcao == 'a':
        extrato = depositar(extrato)
    elif opcao == 'b':
        extrato, saques = sacar(extrato, saques)
    elif opcao == 'c':
        mostrar_extrato(extrato)
    elif opcao == 'd':
        print("Saindo...")
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')
