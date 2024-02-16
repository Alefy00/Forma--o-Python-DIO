import textwrap

def menu():
    menu = '''
    ==================== MENU ===================
    [d]\tDepósito
    [s]\tSaque
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair

    => '''
    return input(textwrap.dedent(menu))

def deposito(saldo, extrato):
    valor_deposito = float(input("Digite o valor a ser depositado: "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito no valor de: R${valor_deposito:.2f} \n"
        print(f"O valor de R${valor_deposito:.2f} foi depositado")
    else:
        print("Operação falhou: digite um valor válido. ")
    return saldo, extrato

def sacar(saldo, extrato, limite, LIMITE_SAQUES, numero_saques):
    valor_saque = float(input("Digite o valor que será sacado: "))

    if valor_saque <= 0:
        print("Operação falhou: valor de saque inválido.")
    elif valor_saque > saldo:
        print("Operação falhou: você não tem saldo suficiente.")
    elif valor_saque > limite:
        print("Operação falhou: o valor de saque excede o limite de saque.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou: número máximo de saques excedido.")
    else:
        saldo -= valor_saque
        extrato += f"Valor sacado: {valor_saque:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")

    return saldo, extrato, numero_saques

def extrato_conta(saldo, extrato):
    print("\n==================EXTRATO================")
    print("Não foram realizadas movimentações. " if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("============================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("\n Já existe um usuário com esse CPF! ")
            return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-yyyy): ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("====== Usuário criado com sucesso! ======")

def criar_conta(usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            numero_conta = len(contas) + 1
            contas.append({"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario})
            print("\n==== Conta criada com sucesso! ====")
            return

    print("\nUsuário não encontrado. O fluxo de criação de conta foi encerrado.")

def listar_contas(contas):
    print("\n================= LISTA DE CONTAS =================")
    for conta in contas:
        print(f"\nAgência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
    print("====================================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = deposito(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, LIMITE_SAQUES, numero_saques)
        elif opcao == "e":
            extrato_conta(saldo, extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            criar_conta(usuarios, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Obrigado por utilizar o banco")
            break
        else:
            print("Operação inválida, selecione uma opção válida.")

if __name__ == "__main__":
    main()
