import datetime
anoAtual = datetime.datetime.now()

nome = str(input("Digite seu nome: "))
ano = int(input("digite seu ano de nascimento: "))
altura = float(input("Digite sua altura: "))

idade = anoAtual.year - ano


if idade < 18:
    print(f"Óla {nome}, Sua idade é {idade} anos e tem {altura} metros de altura mas você ainda é menor de idade ")
else:
    print(f"Óla {nome}, Sua idade é {idade} anos e tem {altura} metros de altura e você já é maior de idade ")
