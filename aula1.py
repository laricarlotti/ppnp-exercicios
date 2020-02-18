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


# ex2 | Saque no caixa eletrônico

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

numeroBanco = "12345"
senhaBanco = "abcde"
saldoBanco = 15000

saldoFinal = saldoBanco - valorSaque

if numeroConta == numeroBanco and senhaConta == senhaBanco:
  print(saldoFinal)
else:
  print("Transação inválida")


# ex3 | Sistema de empréstimo

# Crie um programa que determine se um empréstimo é
# aprovado baseado no perfil do usuário.
# Para que um empréstimo seja aprovado, o usuário deve
# ter entre 18 e 65 anos de idade, além de ter uma renda
# mensal três vezes maior que uma parcela.
# Nesse sistema, o usuário escolhe o valor desejado para
# empréstimo e a quantidade de parcelas. O sistema não
# cobra juros no empréstimo.


idadeUsuario = int(input("Quantos anos você tem? "))
rendaMensal = int(input("Quanto você ganha por mês? "))

if idadeUsuario >= 18 and idadeUsuario <= 65:
    valorDesejado = int(input("Qual valor deseja emprestado? "))
    numeroParcelas = int(input("Em quantas parcelas gostaria de pegar o empréstimo? "))
    umaParcela = valorDesejado / numeroParcelas
    if rendaMensal >= 3* umaParcela:
        print("Parabéns, o empréstimo foi aprovado")
    else:
        print("Você não atingiu valor de salário suficiente")
else:
    print("Você não se encaixa no perfil de idade")
