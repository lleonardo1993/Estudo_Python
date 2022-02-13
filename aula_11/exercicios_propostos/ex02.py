"""
Faca um programa que pergunte a hora ao usuario e, baseando-se 
no horario descrito, exiba a saudacao apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""




"""
horario = input('Digite um horario entre 0 e 23: ')

if  horario.isdigit():
    horario = int(horario)
        
    if horario < 0 or horario > 23:
            print('Horario deve estar entre 0 e 23: ')
    else:
        if horario <= 11:
            print('Bom dia')
        elif horario <=17:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
        print('Porfavor, Digite um horario entre 0 e 23: ')
"""
horario = input('Digite um horario entre 0 e 23: ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Digite um horario entre 0 e 23: ')
    else:
        if horario <= 11:
            print('Bom dia !')
        elif horario <= 17:
            print('Boa Tarde !')
        else:
            print('Boa Noite !!')
else:
    print('Porfavor, Entre com um horario entre 0 e 23')
