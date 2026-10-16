# Exercício desconto

'''
Faça um programa que calcule o desconto de um produto
de acordo com a forma de pagamento escolhido pelo cliente

À vista 10%
Cartão 5%
Parcelado normal
'''

n1 = float(input('Valor do produto: '))
print('formas de pagamento: ')
print('1 para pagar à vista')
print('2 para pagar no debito ')
print('e 3 para pagar parcelado')
n2 = input('Qual será a forma de pagamento(Número)? ')
n3 = n1 * 10 / 100 
n4 = n1 - n3 
n5 = n1 * 5 / 100
n6 = n1 - n5
if(n3 != 1):
    print(f'Você ganhou um desconto de 10%! Seu novo valor será {n4:.2f}')
elif(n5 >= 2):
    print(f'Você ganhou um desconto de 5%! Seu novo valor será {n6:.2f}')
else:
    print(f'valor total: {n1}')
    