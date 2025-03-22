# Importa o módulo statistics para cálculos estatísticos
import statistics

# Dicionário com os alunos e suas notas (exemplo inicial, valores podem ser dinâmicos)
alunos = {
    'Lucas': 0,
    'Mateus': 0,
    'Felipe': 0,
    'Daniel': 0,
    'Paulo': 0,
    'Eduardo': 0
}

# Exibe os nomes dos alunos
print('Nós temos os seguintes alunos:', list(alunos.keys()))

# Função para atualizar as notas dos alunos
def atualizar_notas(alunos):
    for aluno in alunos:
        # Solicita a nota sem mostrar detalhes além do nome
        nota = float(input(f'Insira a nota do aluno {aluno}: '))
        alunos[aluno] = nota
    print('\nAs notas foram atribuídas com sucesso!\n')

# Calcula estatísticas importantes
def calcular_estatisticas(alunos):
    # Lista de notas
    notas = list(alunos.values())
    
    # Calcula média
    media = round(statistics.mean(notas), 2)  # Arredonda a média para 2 casas decimais
    print(f"Média das notas: {media}")

        
        # Calcula mediana
    mediana = statistics.median(notas)
    print(f"Mediana das notas: {mediana}")
        
        # Calcula moda
    moda = statistics.mode(notas)
    print(f"Moda das notas: {moda}")
        
        # Calcula desvio padrão
    desvio_padrao = round(statistics.stdev(notas),2)
    print(f"Desvio Padrão das notas: {desvio_padrao}")
        
        # Identifica menor e maior nota
    menor = min(notas)
    maior = max(notas)
    print(f"Menor nota: {menor}")

    print(f"Maior nota: {maior}")

# Função principal para rodar o sistema
def sistema_notas():
    # Atualiza as notas dos alunos
    atualizar_notas(alunos)

    # Mostra todas as estatísticas
    print("\nEstatísticas das Notas:")
    calcular_estatisticas(alunos)

# Executa o sistema
sistema_notas()
