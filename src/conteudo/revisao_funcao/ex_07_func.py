'''
uma função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento. O cálculo do valor a ser pago é feito da seguinte forma: para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso. A função deverá retornar o valor da prestação.
'''


def valorPagamento(prestacao, dias_atrasados):
    if dias_atrasados == 0:
        return prestacao

    multa = prestacao * 0.03
    juros = prestacao * (0.001 * dias_atrasados)
    return prestacao + multa + juros

valor = float(input("Digite o valor da prestação: R$ "))
dias = int(input("Digite a quantidade de dias em atraso: "))

total_a_pagar = valorPagamento(valor, dias)

print(f"Valor a ser pago: R$ {total_a_pagar:.2f}")

valor = float(input("Digite o valor da prestação: R$ "))
dias = int(input("Digite a quantidade de dias em atraso: "))

total_a_pagar = valorPagamento(valor, dias)

print(f"Valor a ser pago: R$ {total_a_pagar:.2f}")