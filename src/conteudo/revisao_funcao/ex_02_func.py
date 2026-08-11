'''
Uma função com dois parâmetros (a e b) que mostre o maior deles;
'''

def mostar_maior_numero(num1, num2):
    if num1 < num2:
        return print(num2, "é maior")
    else:
        return print(num1, "é maior")


num1 = 2
num2 = 4
mostar_maior_numero(num1, num2)