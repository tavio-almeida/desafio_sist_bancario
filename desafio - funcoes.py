import textwrap

def menu ():
  menu = """\n

  [A] Depositar
  [B] Sacar
  [C] Extrato
  [D] Criar conta
  [E] Criar usuário
  [F] Sair

  => """
  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
  if valor > 0:
    saldo+=valor
    extrato+= f"Depósito: \tR$ {valor:.2f}\n"
    print("\n Depósito realizado!")
  else:
    print("\nValor inválido")
  return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, num_saque, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = num_saque >= limite_saques

  if excedeu_saldo:
    print("\n Saldo insuficiente")

  elif excedeu_limite:
        print("\n Valor excede o limite")

  elif excedeu_saques:
        print("\n Limite de saques excedido")

  elif valor > 0:
    saldo -= valor
    extrato += f"saque: \t\tR$ {valor:.2f}\n"
    num_saque += 1
    print("\n Saque realizado!")
  else:
    print("\n Valor inválido")

  return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
  print(f'\n------Extrato------')
  print('Não foram realizados movimentações' if not extrato else extrato)
  print(f'\nSeu saldo é: R$  {saldo:.2f}')
  print(f'------Extrato------')

def criar_usuario(usuarios):
  cpf = input("Informe o CPF (APENAS NÚMEROS): ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("\n Já existe usuário com o CPF informado")
    return
  
  nome = input("Informe o nome: ")
  data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
  endereco = input("Informe o endereço (Logradouro, num, bairro, cidade/estado): ")

  usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
  print("Usuário foi criado!")

def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Digite o CPF: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Conta foi criada!")
    return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
  
  print("\nUsuário não encontrado")

def main(): 
  saldo = 0
  limite = 500
  extrato = ''
  num_saque = 0
  usuarios = []
  contas = []

  LIMITE_SAQUE = 3
  AGENCIA = "0001"

  while True:  
    opcao = menu()


    if opcao == 'A':
      valor = float(input('Digite o valor que deseja depositar: ')) 
      saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao == 'B':
      valor = float (input ('Digite o valor que deseja sacar: ') )
      saldo, extrato = sacar (
          saldo=saldo,
          valor=valor,
          extrato=extrato,
          limite=limite,
          num_saque=num_saque,
          limite_saques=LIMITE_SAQUE,
        )
    
    elif opcao == 'C':
      exibir_extrato(saldo, extrato=extrato)
    
    elif opcao == 'D':
      numero_conta=len(contas) + 1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)
      if conta():
        contas.append(conta)

    elif opcao == 'E':
      criar_usuario(usuarios)   
    
    elif opcao == 'F':
      break

    else:
      print('Opção inválida, selecione novamente a opção desejada')

main()













    
