# fazendo Crud da academia

def main():
    list_cliente = [
        {
            "matricula": 101,
            "nome_cliente": "Ana Silva",
            "plano_cliente": "Anual",
            "modalidade": "Musculação",
            "presenca_mes": 18
        },
        {
            "matricula": 102,
            "nome_cliente": "Carlos Eduardo",
            "plano_cliente": "Mensal",
            "modalidade": "CrossFit",
            "presenca_mes": 12
        },
        {
            "matricula": 103,
            "nome_cliente": "Mariana Costa",
            "plano_cliente": "Trimestral",
            "modalidade": "Natação",
            "presenca_mes": 8
        },
        {
            "matricula": 104,
            "nome_cliente": "Roberto Alves",
            "plano_cliente": "Anual",
            "modalidade": "Pilates",
            "presenca_mes": 22
        },
        {
            "matricula": 105,
            "nome_cliente": "Fernanda Lima",
            "plano_cliente": "Mensal",
            "modalidade": "Musculação",
            "presenca_mes": 5
        }
    ]
    opcao = 0

    while (opcao != 5):
        print('''
        1. Realziar matricula
        2. Alterar dados da matricula
        3. Exibir Dados do cliente
        4. Excluir cliente
        5. Sair do programa
        ''')

        opcao = int(input("Digite uma opção: (1 a 5)"))
        if (opcao >= 1 and opcao <= 5):
            match opcao:
                case 1:
                    inserir_cliente(list_cliente)
                case 2:
                    matricula = int(input("Digite um nuemro matricula:"))
                    indice = buscar_cliente(list_cliente, matricula)
                    alterar_cliente(list_cliente,indice)
                case 3:
                    matricula = int(input("Digite um nuemro matricula:"))
                    indice = buscar_cliente(list_cliente, matricula)
                    exibir_cliente(list_cliente,indice)
                case 4:
                    matricula = int(input("Digite um nuemro matricula:"))
                    indice = buscar_cliente(
                    list_cliente, matricula)
                    deletar_cliente(list_cliente, indice)
                case 5:
                    print("Encerrando ....")
                    break



#R = READ
def buscar_cliente(lista_cliente, matricula):
    try:
        for i, cliente in enumerate(lista_cliente):
            if cliente["matricula"] == matricula:
                return i

    except IndexError:
        print("ERROR: Nehuma matricula foi encontrada com esse numero")
        return -1


def exibir_cliente (lista_cliente, indice):
    client = lista_cliente[indice]
    for chave, valor in client.items():
        print(f"{chave} :  {valor}")



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

def deletar_cliente(lista_cliente, indice):
    lista_cliente.pop(indice)
    print("Dados do cliente excluidos")

if __name__ == '__main__':
    main()
