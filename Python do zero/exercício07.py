# Exercício média

'''
Faça um programa que receba duas notas de 1 aluno
e diga se ele foi aprovado ou não!

Média acima de 7 Aprovado
Abaixo, Reprovado
'''

n1 = input('Nome do aluno: ')
n2 = float(input('Nota do aluno: '))
n3 = float(input('segunda nota: '))
n4 = n2 + n3 / 2
if(n4 >= 7):
    print(f'{n1} foi Aprovado')
else:
    print(f'{n1} Reprovado')
