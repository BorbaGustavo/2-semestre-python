'''Escreva um programa em Python que crie uma lista de 7 dicionários, a qual deve conter os seguintes dados:


· Matrícula (inteiro);

· Nome (string);]

· Plano (string, ex: "Anual", "Mensal")

· Modalidade (string, ex: "Musculação", "Crossfit")

· Presenças no Mês

Em seguida, exiba todos os alunos da academia.'''


def coleta_dados(quant_alunos):

    for aluno in range(quant_alunos):
        print("1. matricula")
        matricula = int(input())
        print("2. nome")
        nome = str(input())
        print("3. plano")
        plano = str(input())
        print("4. Modalidade")
        modalidade = str(input())
        print(" numero de Presença")
        presenca_mes = int(input())

        dados = {
            'Matricula': matricula,
            'Nome': nome,
            'Plano': plano,
            'Modalidade': modalidade,
            'Presanca': presenca_mes,
        }
        lista_dados.append(dados)


print('cadastro aluno da academia!')
quant_aluno = int(input("Quantos alunos deseja cadastrar?"))
lista_dados = []

coleta_dados(quant_aluno)

print(lista_dados)
