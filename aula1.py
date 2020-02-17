# ex1 | Conversão de moedas

# Crie um programa que faça a conversão de um valor em
# reais para dólares americanos.
# O programa deve solicitar o valor em reais para o usuário
# e, usando uma taxa de câmbio fixa, deve mostrar na tela
# o resultado da conversão. 

valorReal = int(input("Digite o valor em reais"))
taxaCambio = 4.18

valorDolar = valorReal * taxaCambio
print(valorDolar)


# ex2 | saque no caixa eletrônico

# Crie um programa que simule um saque feito no caixa
# eletrônico. O programa deve solicitar ao usuário o número
# da conta, sua senha e valor para saque.
# Com essas informações, ele deve verificar se o número da
# conta e a senha são válidos, e se o saldo é suficiente para
# o saque.
# Por fim, ele deve mostrar o saldo atualizado na tela.

numeroConta = int(input("Qual é o número da sua conta? "))
senhaConta = input("Digite a sua senha ")
valorSaque = int(input("Quanto você quer sacar? "))

numeroBanco = 12345
senhaBanco = "abcde"
saldoBanco = 15000

saldoFinal = saldoBanco - valorSaque

if numeroConta == numeroBanco and senhaConta == senhaBanco:
  print(saldoFinal)
else:
  print("Transação inválida")