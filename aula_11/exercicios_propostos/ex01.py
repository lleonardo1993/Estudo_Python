"""
Faca um programa que peca ao usuario para digitar um numero inteiro, 
informe se este numero e par ou impar. Caso usuario nao digite um numero
inteiro, informe que nao e um numero inteiro.
"""

numero_inteiro = input('Digite um numero inteiro: ')

# funcao isdigit, verifica se o numero e inteiro


"""
if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} Numero Par: ')
    else:
        print(f'{numero_inteiro} Numero Impar')
else:
    print('Isso nao e um numero inteiro')
"""

# exercicio com not codigo invertido

if not numero_inteiro.isdigit():
    numero_inteiro = input('Isso nao e um numero inteiro')
else:
    numero_inteiro = int(numero_inteiro)

    if not numero_inteiro % 2 == 0:
        print(f'{numero_inteiro}, e impar')
    else:
        print(f'{numero_inteiro}, e par')
