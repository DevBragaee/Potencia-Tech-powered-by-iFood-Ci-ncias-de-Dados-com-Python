

menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    


    => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
#confirma = ''
#voltar = ''

while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:  # Aqui foi acrescentado apos a validacao do valor do deposito uma pergunta ao usuario se ele realmente comfirma a operacao desejada,simulando 
               # simulando um sistema real !
               

               confirma_operacao = """

[c]Confirma operacao?
[v]Voltar
                => """
               #while True:
               opcao_dois = input(confirma_operacao)
               if opcao_dois == "c": # Só apos a confirmacao pelo usuario ! o saldo e extrato sao atualizados num possivel BD
                  saldo += valor
                  extrato += f"Depósito: R$ {valor:.2f}\n" # extrato atualizado  em seguida mensagem ao usuario "sucesso na operaca"
                  print("operacao realizada com sucesso")
            
                         
                            #(valor > 0 and confirma_operacao == "c") == False
                 
               
               
               elif opcao_dois == "v": # caso a opcao seja  cancelar a operacao corrente ! a interface do usuario voltara para tela inicial de "menu",sem atualiza o extrato e saldo
                    opcao_dois = menu
                    print("operacao cancelada")
                      
               else :
                      print(" Por favor selecione novamente a operação desejada.")





            else:
                       print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
             
             valor = float(input("Informe o valor do saque: "))
             confirma_operacao = """

[c]Confirma operacao?
[v]Voltar
                => """

             excedeu_saldo = valor > saldo

             excedeu_limite = valor > limite

             excedeu_saques = numero_saques >= LIMITE_SAQUES

             if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

             elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

             elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

             elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

             else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

            