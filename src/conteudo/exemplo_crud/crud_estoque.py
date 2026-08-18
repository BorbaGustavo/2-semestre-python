# teste feito 100% com IA
import sys

# Lista global que simula o banco de dados
estoque = []


def buscar_produto_por_codigo(codigo):
    """Função auxiliar para buscar um produto pelo código (retorna índice e produto)."""
    for index, produto in enumerate(estoque):
        if produto["codigo"] == codigo:
            return index, produto
    return None, None


def ler_codigo_unico():
    """Lê e valida o código do produto garantindo unicidade."""
    while True:
        try:
            codigo = int(input("Código do Produto (Apenas números): "))
            if codigo <= 0:
                print("❌ O código deve ser um número inteiro positivo!")
                continue

            _, produto_existente = buscar_produto_por_codigo(codigo)
            if produto_existente:
                print(
                    f"❌ Erro: O código {codigo} já está cadastrado para o produto '{produto_existente['nome']}'."
                )
                continue

            return codigo
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.")


def ler_inteiro_positivo(mensagem):
    """Lê e valida um número inteiro maior ou igual a zero."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("❌ O valor não pode ser negativo!")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.")


def ler_float_positivo(mensagem):
    """Lê e valida um número decimal positivo."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor <= 0:
                print("❌ O preço deve ser maior que zero!")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida! Digite um valor numérico (ex: 29.90).")


def ler_texto_nao_vazio(mensagem):
    """Garante que o texto inserido não seja vazio."""
    while True:
        texto = input(mensagem).strip()
        if not texto:
            print("❌ O campo não pode ficar em branco!")
            continue
        return texto


def cadastrar_produto():
    """1. Create - Inserção de um novo produto."""
    print("\n--- CADASTRAR PRODUTO ---")
    codigo = ler_codigo_unico()
    nome = ler_texto_nao_vazio("Nome do Produto: ")
    categoria = ler_texto_nao_vazio("Categoria (ex: Eletrônicos, Escritório): ")
    quantidade = ler_inteiro_positivo("Quantidade em Estoque: ")
    fornecedor = ler_texto_nao_vazio("Fornecedor: ")
    preco = ler_float_positivo("Preço Unitário (R$): ")

    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "fornecedor": fornecedor,
        "preco": preco,
    }

    estoque.append(novo_produto)
    print(f"\n✅ Produto '{nome}' cadastrado com sucesso!")


def listar_produtos():
    """2. Read - Exibição dos dados do estoque."""
    print("\n--- LISTA DE PRODUTOS ---")
    if not estoque:
        print("ℹ️ Nenhum produto cadastrado no estoque.")
        return

    print("-" * 75)
    print(
        f"{'CÓDIGO':<8} | {'NOME':<20} | {'CATEGORIA':<15} | {'ESTOQUE':<8} | {'PREÇO (R$)':<10}"
    )
    print("-" * 75)
    for p in estoque:
        print(
            f"{p['codigo']:<8} | {p['nome']:<20} | {p['categoria']:<15} | {p['quantidade']:<8} | R$ {p['preco']:<8.2f}"
        )
    print("-" * 75)


def atualizar_produto():
    """3. Update - Alteração de um produto existente."""
    print("\n--- ATUALIZAR PRODUTO ---")
    if not estoque:
        print("ℹ️ Nenhum produto para atualizar.")
        return

    try:
        codigo = int(input("Digite o código do produto que deseja alterar: "))
    except ValueError:
        print("❌ Código inválido! Digite apenas números.")
        return

    _, produto = buscar_produto_por_codigo(codigo)

    if not produto:
        print(f"❌ Produto com o código {codigo} não encontrado.")
        return

    print(f"\nEditando produto: {produto['nome']}")
    print("(Pressione ENTER para manter o valor atual)")

    # Atualização do Nome
    novo_nome = input(f"Novo Nome [{produto['nome']}]: ").strip()
    if novo_nome:
        produto["nome"] = novo_nome

    # Atualização da Categoria
    nova_categoria = input(f"Nova Categoria [{produto['categoria']}]: ").strip()
    if nova_categoria:
        produto["categoria"] = nova_categoria

    # Atualização da Quantidade
    qtd_input = input(f"Nova Quantidade [{produto['quantidade']}]: ").strip()
    if qtd_input:
        try:
            qtd_val = int(qtd_input)
            if qtd_val >= 0:
                produto["quantidade"] = qtd_val
            else:
                print("⚠️ Valor inválido! Quantidade mantida.")
        except ValueError:
            print("⚠️ Entrada inválida! Quantidade mantida.")

    # Atualização do Fornecedor
    novo_fornecedor = input(f"Novo Fornecedor [{produto['fornecedor']}]: ").strip()
    if novo_fornecedor:
        produto["fornecedor"] = novo_fornecedor

    # Atualização do Preço
    preco_input = (
        input(f"Novo Preço [{produto['preco']:.2f}]: ").strip().replace(",", ".")
    )
    if preco_input:
        try:
            preco_val = float(preco_input)
            if preco_val > 0:
                produto["preco"] = preco_val
            else:
                print("⚠️ Valor inválido! Preço mantido.")
        except ValueError:
            print("⚠️ Entrada inválida! Preço mantido.")

    print("\n✅ Produto atualizado com sucesso!")


def excluir_produto():
    """4. Delete - Exclusão de um produto do estoque."""
    print("\n--- EXCLUIR PRODUTO ---")
    if not estoque:
        print("ℹ️ Nenhum produto para excluir.")
        return

    try:
        codigo = int(input("Digite o código do produto a ser excluído: "))
    except ValueError:
        print("❌ Código inválido!")
        return

    index, produto = buscar_produto_por_codigo(codigo)

    if produto:
        confirmacao = (
            input(
                f"Tem certeza que deseja excluir '{produto['nome']}'? (S/N): "
            )
            .strip()
            .upper()
        )
        if confirmacao == "S":
            estoque.pop(index)
            print("✅ Produto excluído com sucesso!")
        else:
            print("ℹ️ Operação cancelada.")
    else:
        print(f"❌ Produto com o código {codigo} não foi encontrado.")


def main():
    """Função principal com a estrutura do menu."""
    while True:
        print("\n=============================")
        print("   SISTEMA DE ESTOQUE (CRUD) ")
        print("=============================")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Sair")
        print("=============================")

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            excluir_produto()
        elif opcao == "5":
            print("\nSaindo do sistema... Até logo!")
            sys.exit()
        else:
            print("❌ Opção inválida! Escolha um número entre 1 e 5.")


if __name__ == "__main__":
    main()
