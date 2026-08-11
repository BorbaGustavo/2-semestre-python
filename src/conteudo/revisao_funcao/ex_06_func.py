'''
uma função chamada somaImposto, que possua dois parâmetros: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas e deve retornar o custo com o imposto.
'''

def somaImposto(taxaImposto, custo):
    # com taxa fica 1.xx ele aplica valor direto ficaria, custo * 1.xx
        soma_imposto =  custo * (1 + taxaImposto / 100)
        return soma_imposto

# Exemplo de uso:
custo_inicial = 100.00
taxa = 15.0  # 15% de imposto

custo_final = somaImposto(taxa, custo_inicial)

print(f"Custo final com imposto: R$ {custo_final:.2f}")
# Saída: Custo final com imposto: R$ 115.0

