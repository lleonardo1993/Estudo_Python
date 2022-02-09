# Operadores Relacionais 
# == > >= < <= !=

#num_1 = 3 # int
#num_2 = 2 #int

#var_1 = 'leonardo'
#var_2 = 'ferreira'
#expressao = (var_1 != var_2)

#print(expressao)

# print( 2 == '1')

nome = input("Qual o seu nome? ")
idade = input("Qual sua idade? ")

# Limite para pegar emprestimo
idade_menor = 20 # Muito Jovem
idade_maior = 30 # Passou da idade


idade = int(idade) # Cast da idade

if idade >= idade_menor and idade <= idade_maior :
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} NAO pode pegar o emprestimo.')