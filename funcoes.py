clientes = []
saques = 3
limite = 500
extrato = 1000

def fazer_login():
    global clientes

    cpf_cadastrados = [cliente[2] for cliente in clientes]

    cpf = input('Digite os números do seu CPF: ')

    if cpf in cpf_cadastrados:
        print('ERRO: CPF já cadastrado')
    else:
        nome = input('Digite seu nome: ')
        data_nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')
        logradouro = input('Digite seu logradouro - bairro - cidade/sigla do estado: ')

        novo_cliente = [nome, data_nascimento, cpf, logradouro]
        clientes.append(novo_cliente)
        print('Cadastro realizado com sucesso!')

def depositar(extrato):
    deposito = float(input('Quanto deseja depositar? '))
    if deposito > 0:
        print('Seu dinheiro foi depositado com sucesso.')
        extrato += deposito
    else:
        print("ERRO (operação não efetuada).")
    return extrato

def sacar(extrato, saques):
    saque = float(input("Quanto deseja sacar? "))

    if saque < 0:
        print('ERRO (digite um número válido).')
    elif saque > limite:
        print('Você não pode sacar mais de R$ 500,00.')
    else:
        if saque > extrato:
            print('ERRO (saldo insuficiente).')
        else:
            extrato -= saque
            saques -= 1
            print(f'Saque efetuado com sucesso! Agora resta R${extrato:.2f} em sua conta.')
            print(f'Você ainda pode efetuar {saques} saques.')
            if saques <= 0:
                print('ERRO (você não tem mais saques disponíveis no momento.)')
    return extrato, saques

def mostrar_extrato(extrato):
    print(f'Você possui R${extrato:.2f} em sua conta.')

def main():
    global extrato, saques, clientes

def menu():
    return """
        [x] cadastrar
        [a] Depositar
        [b] Sacar 
        [c] Extrato 
        [d] Sair
    """

if __name__ == "__main__":
    main()

    