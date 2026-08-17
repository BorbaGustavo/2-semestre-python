
def main():
    list_cliente = []

    opcao = 1

    while opcao != 6:
        print("\n1 - Cadastrar Cliente")
        print("2 - Alterar Cliente")
        print("3 - Excluir Cliente")
        print("4 - Exibir dados de um cliente")
        print("5 - Exibir dados de clientes com mais 10MIL reais")
        print("6 - sair")

        opcao = int(input("Digite a opção desejada: (1 a 6)"))
        if (opcao >= 1 and opcao <= 6):

            match opcao:
                case 1:
                    inserir_cliente(list_cliente)
                case 2:
                    codigo_alterar = int(input("Digite o ocdigo do cliente: "))
                    indice = buscar_cliente(list_cliente, codigo_alterar)
                    if indice != -1:
                        alterar_cliente(list_cliente,indice)
                    else:
                        print("Nenhum cliente foi encontrado. Codigo inexistente")
                case 2:
                    codigo_excluir = int(input("Digite o codigo do cliente: "))
                    indice = buscar_cliente(list_cliente, codigo_excluir)
                    if indice != -1:
                        excluir_cliente(list_cliente, indice)
                case 4:
                    codigo_exibir = int(input("Digite o codigo do cliente: "))
                    indice = buscar_cliente(list_cliente, codigo_exibir)
                    if indice != -1:
                        exibir_cliente(list_cliente, indice)
                    else:
                        print("Nenhum cliente foi encontrado.")
                case 5:
                    exibir_cliente_10k(list_cliente)
                case 6:
                    break
        else:
            print("Opção Invalida.")



#funções do CRUD
# C = CREATE
def inserir_cliente(list_cliente):
    cod_cliente = int(input("Digite o codigo do cliente: "))
    nome_cliente = input("Digite o nome do cliente: ")
    numero_agencia = int(input("Digite numero da agencia do cliente:"))
    numero_conta = int(input("Digite o numero da conta do cliente:"))
    saldo_cliente = float(input("Digite o saldo do cliente: "))

    dados_cliente = {
        "cod_cliente": cod_cliente,
        "nome_cliente": nome_cliente,
        "numero_agencia": numero_agencia,
        "numero_conta": numero_conta,
        "saldo_cliente": saldo_cliente,
    }

    list_cliente.append(dados_cliente)

# R = READ
def buscar_cliente(list_cliente, codigo):
    for i in range(len(list_cliente)):
        if codigo == list_cliente[i]["cod_cliente"]:
            return i
    return -1

def exibir_cliente(list_cliente, indice):
   client = list_cliente[indice]
   for chave, valor in client.items():
       print(f"{chave} :  {valor}")

def exibir_cliente_10k(list_cliente):
   # fazendo um foreach melhor
   for cliente in list_cliente:
       if cliente["saldo_cliente"] > 10000:
           print(cliente)
# u = Update
def alterar_cliente(list_cliente, indice):
    print(f'Nome cliente: {list_cliente[indice]["nome_cliente"]}')
    novo_nome = input("Digite o novo nome do cliente: ")
    print(f'Numero cliente: {list_cliente[indice]["numero_agencia"]}')
    novo_numero_agencia = int(input("Digite o numero da agencia do cliente: "))
    print(f'Numero conta cliente: {list_cliente[indice]["numero_conta"]}')
    novo_numero_conta = int(input("Digite o numero da conta do cliente: "))
    print(f'Saldo cliente: {list_cliente[indice]["saldo_cliente"]}')
    novo_saldo = float(input("Digite o saldo do cliente: "))

    list_cliente[indice]['nome_cliente'] = novo_nome
    list_cliente[indice]['numero_agencia'] = novo_numero_agencia
    list_cliente[indice]['numero_conta'] = novo_numero_conta
    list_cliente[indice]['saldo_cliente'] = novo_saldo


# R = REMOVE
def excluir_cliente(list_cliente, indice):
    list_cliente.pop(indice)
    print("Dados do cliente excluidos")


if (__name__ == "__main__"):
    main()