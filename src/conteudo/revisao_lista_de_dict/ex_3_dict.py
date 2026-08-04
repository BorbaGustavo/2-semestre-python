'''3) Escreva um programa em Python que crie uma lista de 7 dicionários, a qual deve conter os seguintes dados:


· Código do Paciente (inteiro);

· Nome (string);

· Convênio (string, ex: "Particular", "Unimed");

· Médico Responsável (string);

· Idade (inteiro);

· Sinais Vitais (lista de 3 floats representando as últimas medições de temperatura corporação)'''

def exibir_menu():
    """Função apenas para imprimir as opções na tela."""
    print("\n" + "=" * 20)
    print("    CADASTRAR PACIENTE  ")
    print("=" * 20)
    print("1. Cadastro")
    print("2. Lista de pacientes")
    print("0. Sair do Programa")
    print("=" * 20)

def casdastro_paciente():
    quant_paciente =1
    for i in range (quant_paciente):
        print("1. Cod. do paciente")
        cod_paciente = int(input())
        print("2. nome")
        nome = str(input())
        print("3. Convenio")
        convenio = str(input())
        print("4. Medico responsavel")
        med_responsavel = str(input())
        print(" Idade paciente")
        idade = int(input())
        print("Sinais Vitais")
        sinal_vital = []
        for i in range (1):
            print('último registro de batimentos')
            batimentos = float(input())
            print('última temperatura corpora')
            temperatura = float(input())
            sinal_vital.append(batimentos)
            sinal_vital.append(temperatura)



        dados = {
            'cod_paciente': cod_paciente,
            'nome': nome,
            'convenio': convenio,
            'med_responsavel': med_responsavel,
            'idade': idade,
            'sinal_vital': sinal_vital,
        }
        lista_dados.append(dados)


lista_dados = []

while True:
    exibir_menu()

        # Recebe a entrada do usuário como string para evitar erros se ele digitar letras
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
            print("\n>> Cadastro Paciente")
            casdastro_paciente()
    elif opcao == '2':
        print("\n>> Lista de paciente")
        print(lista_dados)


    elif opcao == '0':
            print("\n>> Encerrando o programa. Até logo!")
            break  # Este comando quebra o loop while e finaliza a execução
    else:
            # Captura qualquer coisa que não seja 0, 1, 2 ou 3
            print("\n>> Opção inválida! Por favor, digite um número válido do menu.")
