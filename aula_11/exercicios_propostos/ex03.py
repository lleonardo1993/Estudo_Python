"""
Faca um programa que peca o primeiro nome do usuario. Se o nome tiver 4 letras ou 
menos escreva "Seu nome e curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome e normal"; maior que 6 escreva "Seu nome e muito grande". 
"""




usuario = input('Digite seu nome: ')
tamanho = len(usuario)

if tamanho <= 4:
    print(f'Seu {usuario} seu nome e curto! ')
elif tamanho <= 6:
    print(f'Seu {usuario} seu nome e normal!! ')
else:
    print(f'Seu {usuario} seu nome e muito grande! ')


