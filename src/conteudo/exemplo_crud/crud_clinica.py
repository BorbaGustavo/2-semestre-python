import sys

pacientes = []


def buscar_paciente_por_codigo(codigo):
    """Auxiliar: localiza o paciente pelo código e retorna o índice e os dados."""
    for index, paciente in enumerate(pacientes):
        if paciente["codigo"] == codigo:
            return index, paciente
    return None, None


def ler_codigo_unico():
    """Valida o código do paciente garantindo unicidade (Chave Primária)."""
    while True:
        try:
            codigo = int(input("Código do Paciente (Apenas números): "))
            if codigo <= 0:
                print("❌ O código deve ser um número inteiro positivo!")
                continue

            _, existente = buscar_paciente_por_codigo(codigo)
            if existente:
                print(
                    f"❌ Erro: O código {codigo} já está cadastrado para o(a) paciente '{existente['nome']}'."
                )
                continue

            return codigo
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.")


def ler_texto(mensagem):
    """Valida entradas de texto para não permitir campos vazios."""
    while True:
        texto = input(mensagem).strip()
        if not texto:
            print("❌ O campo não pode ficar em branco!")
            continue
        return texto


def ler_idade():
    """Valida a idade do paciente."""
    while True:
        try:
            idade = int(input("Idade: "))
            if 0 <= idade <= 130:
                return idade
            print("❌ Digite uma idade válida (entre 0 e 130 anos).")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.")


def ler_sinais_vitais():
    """Lê e valida uma lista de 3 medições de temperatura corporal."""
    temperaturas = []
    print("Sinais Vitais - Informe as últimas 3 medições de temperatura (°C):")
    for i in range(1, 4):
        while True:
            try:
                temp = float(
                    input(f"  • Medição {i}: ").strip().replace(",", ".")
                )
                if 30.0 <= temp <= 45.0:
                    temperaturas.append(temp)
                    break
                print(
                    "❌ Valor fora do limite aceitável de temperatura corporal (30°C - 45°C)!"
                )
            except ValueError:
                print(
                    "❌ Entrada inválida! Digite um número decimal (ex: 36.5)."
                )
    return temperaturas


def cadastrar_paciente():
    """CREATE - Cadastra um novo paciente."""
    print("\n--- CADASTRAR PACIENTE ---")
    codigo = ler_codigo_unico()
    nome = ler_texto("Nome do Paciente: ")
    convenio = ler_texto("Convênio (ex: Particular, Unimed): ")
    medico = ler_texto("Médico Responsável: ")
    idade = ler_idade()
    sinais_vitais = ler_sinais_vitais()

    novo_paciente = {
        "codigo": codigo,
        "nome": nome,
        "convenio": convenio,
        "medico": medico,
        "idade": idade,
        "sinais_vitais": sinais_vitais,
    }

    pacientes.append(novo_paciente)
    print(f"\n✅ Paciente '{nome}' cadastrado com sucesso!")


def exibir_pacientes():
    """READ - Exibe a lista de pacientes cadastrados."""
    print("\n--- LISTA DE PACIENTES ---")
    if not pacientes:
        print("ℹ️ Nenhum paciente cadastrado no sistema.")
        return

    print("-" * 90)
    print(
        f"{'CÓDIGO':<8} | {'NOME':<20} | {'IDADE':<6} | {'CONVÊNIO':<15} | {'MÉDICO':<18} | {'SINAIS VITAIS (°C)'}"
    )
    print("-" * 90)
    for p in pacientes:
        temps_formatadas = (
            f"[{p['sinais_vitais'][0]:.1f}, {p['sinais_vitais'][1]:.1f}, {p['sinais_vitais'][2]:.1f}]"
        )
        print(
            f"{p['codigo']:<8} | {p['nome']:<20} | {p['idade']:<6} | {p['convenio']:<15} | {p['medico']:<18} | {temps_formatadas}"
        )
    print("-" * 90)


def atualizar_paciente():
    """UPDATE - Atualiza os dados de um paciente existente."""
    print("\n--- ATUALIZAR PACIENTE ---")
    if not pacientes:
        print("ℹ️ Nenhum paciente cadastrado para alterar.")
        return

    try:
        codigo = int(input("Digite o código do paciente que deseja alterar: "))
    except ValueError:
        print("❌ Código inválido! Digite apenas números.")
        return

    _, paciente = buscar_paciente_por_codigo(codigo)

    if not paciente:
        print(f"❌ Paciente com o código {codigo} não encontrado.")
        return

    print(f"\nEditando cadastro do(a) paciente: {paciente['nome']}")
    print("(Pressione ENTER para manter o valor atual)")

    # Atualização do Nome
    novo_nome = input(f"Novo Nome [{paciente['nome']}]: ").strip()
    if novo_nome:
        paciente["nome"] = novo_nome

    # Atualização do Convênio
    novo_convenio = input(f"Novo Convênio [{paciente['convenio']}]: ").strip()
    if novo_convenio:
        paciente["convenio"] = novo_convenio

    # Atualização do Médico
    novo_medico = input(f"Novo Médico [{paciente['medico']}]: ").strip()
    if novo_medico:
        paciente["medico"] = novo_medico

    # Atualização da Idade
    idade_input = input(f"Nova Idade [{paciente['idade']}]: ").strip()
    if idade_input:
        try:
            idade_val = int(idade_input)
            if 0 <= idade_val <= 130:
                paciente["idade"] = idade_val
            else:
                print("⚠️ Idade fora dos limites! Valor mantido.")
        except ValueError:
            print("⚠️ Entrada inválida! Idade mantida.")

    # Atualização dos Sinais Vitais
    atualizar_sinais = (
        input("Deseja atualizar as medições de sinais vitais? (S/N): ")
        .strip()
        .upper()
    )
    if atualizar_sinais == "S":
        paciente["sinais_vitais"] = ler_sinais_vitais()

    print("\n✅ Registro do paciente atualizado com sucesso!")


def excluir_paciente():
    """DELETE - Remove um paciente da lista."""
    print("\n--- EXCLUIR PACIENTE ---")
    if not pacientes:
        print("ℹ️ Nenhum paciente cadastrado para excluir.")
        return

    try:
        codigo = int(input("Digite o código do paciente a ser excluído: "))
    except ValueError:
        print("❌ Código inválido!")
        return

    index, paciente = buscar_paciente_por_codigo(codigo)

    if paciente:
        confirmacao = (
            input(
                f"Tem certeza que deseja excluir o prontuário de '{paciente['nome']}'? (S/N): "
            )
            .strip()
            .upper()
        )
        if confirmacao == "S":
            pacientes.pop(index)
            print("✅ Registro excluído com sucesso!")
        else:
            print("ℹ️ Operação cancelada.")
    else:
        print(f"❌ Paciente com o código {codigo} não foi encontrado.")

def main():
    """Estrutura do menu principal."""
    while True:
        print("\n==================================")
        print("   SISTEMA CLÍNICO - GESTÃO CRUD ")
        print("==================================")
        print("1. Cadastrar Paciente")
        print("2. Exibir Pacientes")
        print("3. Atualizar Dados do Paciente")
        print("4. Excluir Paciente")
        print("5. Sair")
        print("==================================")

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            exibir_pacientes()
        elif opcao == "3":
            atualizar_paciente()
        elif opcao == "4":
            excluir_paciente()
        elif opcao == "5":
            print("\nSaindo do sistema... Até logo!")
            sys.exit()
        else:
            print("❌ Opção inválida! Escolha um número entre 1 e 5.")


if __name__ == "__main__":
    main()