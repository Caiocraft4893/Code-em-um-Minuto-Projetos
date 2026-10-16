# Exercício

'''
Faça um programa que receba o peso e a altura do usuário
e calcule o seu IMC utilizando a fórmula abaixo
'''

'''    IMC = peso / (altura*altura)    '''

n1 = float(input('insira seu peso: '))
n2 = float(input('insira sua altura: '))
n3 = n1 / (n2**2)
print(f'seu imc é {n3:.2f}')
