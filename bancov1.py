menu = '''
[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrado = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrado += f"Deposito no valor de: {valor_deposito:.2f} \n"
        else:
            print("operação falho, digite um valor valido. ")
        
        
        
    elif opcao == "s":
        
        valor_saque = float(input("digite o valor que será sacado: "))
         
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES
         
        if excedeu_saldo:
             print("operação falhou, voce não tem saldo suficiente. ")
        elif excedeu_limite:
            print("operação falhou, o valor de saque excede o valor limite. ")
        elif excedeu_saque:
            print("Operação falhou, Numero maxima de saques excedido. ")
            
        elif saldo > 0:
                      
            saldo -= valor_saque
            extrado += f"Valor sacado: {valor_saque:.2f} \n"
            numero_saques += 1
        else:
            print("operação falhou o valor informado não e valido")      
                     
        
    elif opcao == "e":
        print("\n==================EXTRATO================")
        print("Não foram realizadas movimentações. " if not extrado else extrado)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("============================================")
        
       
        
    elif opcao == "q":
        print("Obrigado por ultilizar o banco")
        break
    else:
        print("Operação invalida, seleciona uma opção valida")
        
   