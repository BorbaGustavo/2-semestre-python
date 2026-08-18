# fazendo Crud da academia

#C = Create
def inserir_cliente(lista_cliente):
    matricula = int(input("Digite o matricula do cliente: "))
    nome_cliente = input("Digite o nome do cliente: ")
    plano_cliente = input("Digite o plano do cliente: ")
    modalidade = input("Digite o modalidade do cliente: ")
    presenca_mes = int(input("Quanta vezes ele foi nesse Mês:"))

    dados_cliente = {
        "matricula": matricula,
        "nome_cliente": nome_cliente,
        "plano_cliente": plano_cliente,
        "modalidade": modalidade,
        "presenca_mes" : presenca_mes
    }
    lista_cliente.append(dados_cliente)


#R = READ
def buscar_cliente(
        lista_cliente, matricula):
    for i in range(len(lista_cliente)):
        if matricula == lista_cliente[i]["matricula"]:
            return i
    return -1

def exibir_cliente (lista_cliente, indice):
    client = lista_cliente[indice]
    for chave, valor in client.items():
        print(f"{chave} :  {valor}")

# U = update
def alterar_cliente(lista_cliente, indice):
    print(f'Nome do cliente: {lista_cliente[indice]["nome_cliente"]}')
    novo_nome = input("Digite o nome do cliente: ")
    print(f'Plano do Cliente: {lista_cliente[indice]["plano_cliente"]}')
    novo_plano = input("Digite o plano do cliente: ")
    print(f'Modalidade: {lista_cliente[indice]["modalidade"]}')
    novo_modalidade = input("Digite o modalidade do cliente: ")
    print(f'Presenca: {lista_cliente[indice]["presanca_mes"]}')
    novo_presenca = input("Digite o presenca do cliente: ")

    lista_cliente[indice]['nome_cliente'] = novo_nome
    lista_cliente[indice]['plano_cliente'] = novo_plano
    lista_cliente[indice]['modalidade'] = novo_modalidade
    lista_cliente[indice]['presenca_mes'] = novo_presenca


