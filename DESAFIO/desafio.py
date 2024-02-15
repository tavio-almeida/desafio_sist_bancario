menu = """

[A] Depositar
[B] Sacar
[C] Extrato
[D] Sair

=> """

saldo = 0
limite = 500
extrato = ''
num_saque = 0
limite_saque = 3

while True:
  
  opcao = input(menu) 


  if opcao == 'A':
    valor = float(input('Digite o valor que deseja depositar: ')) 
  
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
    
    else:
       print('Valor inválido')
   

  elif opcao == 'B':
    valor = float (input ('Digite o valor que deseja sacar: ') )

    exc_saldo = valor > saldo
    exc_lim = valor > limite
    exc_saque = num_saque >= limite_saque

    if exc_saldo:
      print('Saldo insuficiente')

    elif exc_lim:
      print('Valor maior que o permitido!')

    elif exc_saque:
      print('Limite de saque excedido')

    elif valor > 0:
      saldo -= valor
      extrato += f'Saque: R$ {valor:.2f}\n'  
      num_saque += 1

    else:
      print('Valor inválido')    
  
  elif opcao == 'C':
    print(f'\n------Extrato------')
    print('Não foram realizados movimentações' if not extrato else extrato)
    print(f'\nSeu saldo é: R$  {saldo:.2f}')
    print(f'------Extrato------')
  
  elif opcao == 'D':
    break

  else:
    print('Opção inválida, selecione novamente a opção desejada')
