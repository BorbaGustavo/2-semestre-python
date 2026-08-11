'''
Uma função com um parâmetro n que verifique e mostre se ele é par ou ímpar;
'''

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"O valor {numero}: par")
    else:
        print(f"O valor {numero}: impar")

valor = int(input('Digite um valor: '))
par_ou_impar(valor)