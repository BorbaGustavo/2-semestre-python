'''2) Escreva um programa em Python que crie uma lista de 7 dicionários, a qual deve conter os seguintes dados:


· Código do Produto;

· Nome (string);

· Categoria (string, ex: "Eletrônicos", "Escritório");

· Quantidade em Estoque (inteiro);

· Fornecedor (string);

· Preço Unitário (float)

Em seguida, exiba todos os produtos da loja.'''


def exibir_menu():
    """Função apenas para imprimir as opções na tela."""
    print("\n" + "=" * 20)
    print("    CADASTRAR PRODUTO  ")
    print("=" * 20)
    print("1. Cadastro")
    print("2. Lista de Produtos")
    print("0. Sair do Programa")
    print("=" * 20)

def cadastro_produto():
    for produto in range(1,7):
        print("1. Cod. do Produto")
        cod_produto = int(input())
        print("2. nome")
        nome = str(input())
        print("3. Categoria")
        categoria = str(input())
        print("4. Quantidade")
        qtd = int(input())
        print(" Fonecedor")
        fonecedor = str(input())
        print("Preço unitairo")
        preco_unitario = float(input())


        dados = {
            'Codigo_produto' : cod_produto,
            'Nome' : nome,
            'Categoria' : categoria,
            'Quantidade' : qtd,
            "Fonecedor" : fonecedor,
            "Preco_unitario" : preco_unitario,
        }
        lista_dados.append(dados)

lista_dados = []
    # O 'while True' cria um loop infinito que só vai parar quando encontrar um 'break'
while True:
    exibir_menu()

        # Recebe a entrada do usuário como string para evitar erros se ele digitar letras
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
            print("\n>> Cadastro de Produto")
            cadastro_produto()
    elif opcao == '2':
        print("\n>> Lista de Produtos")
        print(lista_dados)


    elif opcao == '0':
            print("\n>> Encerrando o programa. Até logo!")
            break  # Este comando quebra o loop while e finaliza a execução
    else:
            # Captura qualquer coisa que não seja 0, 1, 2 ou 3
            print("\n>> Opção inválida! Por favor, digite um número válido do menu.")


