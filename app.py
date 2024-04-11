menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    
    #deposito
    if opcao == 'd':
        saldo_adicionado = float(input('Digite o valor de deposito: '))
        
        
        if saldo_adicionado > 0:
            saldo += saldo_adicionado
            extrato += f"Deposito de R${saldo_adicionado:.2f}\n"
        else:
            print("Digite um valor válido")

    
    #saque
    elif opcao == 's':
        valor_saque = float(input('Digite o valor que deseja sacar: '))
        
        #confere se o valor não é maior do que o disponivel na conta
        if valor_saque > saldo:
            print('O valor de saque é maior do que o disponivel em sua conta. Digite um valor válido.')


        #confere se não é maior que 500 
        elif valor_saque > 500:
            print('Operação negada. O valor máximo permitido para saque é de R$500.00')
        
        
        elif numero_saques >= LIMITE_SAQUES:
            print('Operação bloqueada. São permitidos apenas 3 saques por dia.')
            

        
        elif valor_saque > 0:
            numero_saques += 1
            saldo -= valor_saque
            print(f'Saque de R${valor_saque} realizado.')
            extrato += f'Saque de R${valor_saque}.'
        
            
    #extrato
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    
    #sair
    elif opcao == "q":
        break
    
    else:
        print("Invalido. Insira uma entrada correta.")