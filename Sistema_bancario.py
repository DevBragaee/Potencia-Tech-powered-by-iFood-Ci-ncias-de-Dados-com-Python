
import textwrap   # import do modulo  "textwarap"(com algumas funcoes para manipular textos)


def menu():  # definicao da funcao 'menu' com as opcoes para o usuario acrescimo da funcao "inativar_conta"
    menu = """\n
    ================== MENU =====================
    [1] - Saque
    [2] - Depósito
    [3] - Extrato
    [4] - Novo Usuário
    [5] - Nova Conta
    [6] - Listar Contas
    [7] - Listar Usuários
    [8] - Inativar Conta Usuario 
    [0] - Sair
    ==============================================
    => """
    return input(textwrap.dedent(menu))  # Retorno da funcao 'menu' ( com 'textwrap' recebendo como parametro a variavel "menu") 

        # PARAMETROS RECEBIDOS PELO METODO "KEYWORDS ONLY" 
def sacar(*, saldo, valor_saque, extrato, limite, num_saque, limite_saques): 
    saldo_excedido = valor_saque > saldo
    limite_excedido = valor_saque > limite
    saque_excedido = num_saque >= limite_saques
        # restricoes para que ocorra o saque
    if saldo_excedido: # restricao para saldo !
        print("\n  Operação falhou! Você não tem saldo suficiente! ")

    elif limite_excedido: # restricao para o limite de saque excedido!
        print("\n  Operação falhou! Limite de saque excedido! ")

    elif saque_excedido: # restricao para o numero de saques permitidos diarios excedido!
        print("\n  Operação falhou! Número máximo de saques excedido! ")

    elif valor_saque > 0: # caso nao ocorra nehuma das restricoes acima o saque é realizado.O saldo é atualizado e o numero de saques tambem !
        saldo -= valor_saque
        extrato += f"Saque:\t\tR$ {valor_saque:.2f}\n"
        num_saque += 1
        print('\n === Saque realizado com sucesso! ===')
    
    else:
        print("Operação falhou! Valor informado é inválido!")
    return saldo, extrato   # retorno  do "saldo e extrato " para serem usados nas outros metodos! 
    
    # metodo depositar recebendo os parametros 'saldo, valor_deposito, extrato'!
def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito:\tR$ {valor_deposito:.2f}\n"
        print('\n === Depósito realizado com sucesso! ===')
    else:
        print("\n  Operação falhou! Valor informado é inválido!")
    
    return extrato,saldo
        
        # FUNCAO 'EXIBIR EXTRATO RECEBENDO OS ARGUMENTOS POR "POSICIONAL E POR NOME"
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
    return extrato

def criar_usuario(usuarios): # Recebendo a array de usuarios como parametro
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios) # ''usuario' recebe a funcao que filtra usuarios 

    if usuario: # se verdadeiro
        print("\n  Já existe usuário com esse CPF! ")
        return 
    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd/mm/aaa): ")
    endereco = input("Informe o endereço (logradouro, numero, bairro, cidade/sigla estado): ")
       # Adicionando novo usuario á lista de usuarios 
    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})
    
    print("---------- Usuário cadastrado com sucesso!' ----------------")

def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
   
    return usuarios_filtrados[0] if usuarios_filtrados else None
    

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ==== Conta criada com sucesso! =====")
        return {"agencia": agencia, "num_conta": num_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado,  criação de conta nao concluido ! ")
    return None
 
 
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['num_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 60)
        print(textwrap.dedent(linha))
        print(contas)  # esse print Para debugar

def listar_usuarios(usuarios):
    for usuario in usuarios:
        linha = f"""\
            
            CPF: \t\t {usuario['cpf']}
            Titular:\t {usuario['nome']}
            """
        print("=" * 60)
        print(textwrap.dedent(linha)) 

def inativar_conta(cpf,usuarios,contas):
    cpf = input("Informe o CPF do Titular da Conta que deseja Inativar: ")
    inativar = filtrar_usuario(cpf, usuarios)
    if inativar:
        print("\n ==== Conta Localizada com sucesso! =====")
        print("\n ==== Deseja excluir conta? =====")
        contas -= 1
        usuarios = usuarios.drop[0]
        

        return cpf,usuarios,contas
        
    
    print("\n Usuário não encontrado, fluxo de criação de conta encerrado ! ")
      
    
    
    



def main():
    agencia = "0001"
    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    num_saque = 0
    limite_saques = 3
    extrato = ""
    numero_conta = 1

    while True:
    
        opcao = menu()

        if opcao == "1":
            valor_saque = float(input("Digite o valor a ser sacado: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor_saque = valor_saque,
                extrato = extrato,
                limite = limite,
                num_saque = num_saque,
                limite_saques = limite_saques,
            )
        elif opcao == "2":
            valor_deposito = float(input("Digite o valor do depósito: "))

            saldo, extrato = depositar(saldo,valor_deposito, extrato)
     
        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            num_conta = len(contas) + 1
            conta = criar_conta(agencia, num_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
        
        
        elif opcao == "6":
            listar_contas(contas)

        elif opcao =="7":
            listar_usuarios(usuarios)
        elif opcao == "8":
           # numero_conta = len(contas) - 1
            conta = inativar_conta(contas, usuarios)
            contas -= 1


        elif opcao == "0":
            break

        else:
            print("Opção Inválida, por favor tente novamente...")

main()