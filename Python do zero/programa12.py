# Estrutura condicional parte 3

# Maior que 0                  if = primeira verificação
# Igual a 0                    elif = segunda verificação (caso o if seja falso)
# Menor que 0         else = verificação final (caso nehuma das alternativas forem verdadeiras)

n = 1

if(n > 0):
    print('Número é maior que 0')
elif(n < 0):
    print('Número é menor que 0 ')
else:
    print('Número é 0')
    