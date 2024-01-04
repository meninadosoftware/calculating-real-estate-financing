valorImovel = float(input('Qual o valor do imóvel? R$ '))
salárioComprador = float(input('Qual o seu salário mensal ? R$ '))
tempoParcelas = int(input('Quantos anos de financiamento ? '))
prestação = (valorImovel / (tempoParcelas*12))
minimo = salárioComprador * 30/100
print('Para pagar uma casa de R$ {:.2f} em {} anos ' .format(valorImovel, tempoParcelas))
print('A prestação será de R$ {:.2f}'.format(prestação))
if prestação <= minimo:
     print('Financiamento APROVADO!')
else:
    print('Financiamento NEGADO!')


