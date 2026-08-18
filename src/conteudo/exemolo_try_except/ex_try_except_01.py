# Tratamento de erros no python

# Exemplo tratando erros simples

try:
    num1= int(input("digite numero inteiro "))
    num2= int(input("digite numero inteiro "))

    soma = num1 + num2
    print(soma)

except ValueError: # excuta quando não compilado
    print("Os dados devem ser númericos inteiros")

finally:
    print("Programa finalizado com sucesso")