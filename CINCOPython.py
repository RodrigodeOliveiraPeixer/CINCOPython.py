#5 - Crie uma matriz bidimensional. Deverá ser solicitado três nomes de alunos e quatro notas, após solicitação dos nomes e das notas deverá ser impresso os nomes acompanhados da média geral de cada aluno, deverá ser impresso também o nome do aluno que obteve a maior média e o nome do aluno que obteve a menor média.


matriz = []


for i in range(3):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for j in range(4):
        nota = float(input("Digite a nota {}: ".format(j+1)))
        notas.append(nota)
    matriz.append([nome, notas])


maior_media = 0
menor_media = 10
nome_maior_media = ""
nome_menor_media = ""
for aluno in matriz:
    nome = aluno[0]
    notas = aluno[1]
    media = sum(notas) / len(notas)
    print("Aluno:", nome)
    print("Média:", media)
    if media > maior_media:
        maior_media = media
        nome_maior_media = nome
    if media < menor_media:
        menor_media = media
        nome_menor_media = nome


print("Aluno com a maior média:", nome_maior_media)
print("Aluno com a menor média:", nome_menor_media)
