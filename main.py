import random
             # Importa a biblioteca random para gerar aleatórios!
alunos = []

for i in range(4):

    nomes = input("Digite os nomes dos alunos: ")  # Solicita os nomes dos alunos
    alunos.append(nomes)  # Adiciona o nome à lista de alunos

random.shuffle(alunos )  # Embaralha a lista de alunos

print(f'Ordem sorteada foi: {alunos}')  # Exibe a ordem sorteada dos alunos
# Fim do código