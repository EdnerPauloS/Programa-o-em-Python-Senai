import statistics  # Importa o módulo statistics para cálculos estatísticos

# Salários das empresas
empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

def calcular_estatisticas(nome_empresa, salarios):
    """
    Função para calcular e exibir estatísticas básicas de uma empresa.
    """
    print(f"\nEstatísticas da {nome_empresa}:")
    
    # Calcula a média arredondada para 2 casas decimais
    media = round(statistics.mean(salarios), 2)
    print(f"Média dos salários: {media}")
    
    # Calcula a mediana
    mediana = statistics.median(salarios)
    print(f"Mediana dos salários: {mediana}")
    
    # Calcula a moda (salário mais comum)
    try:
        moda = statistics.mode(salarios)
        print(f"Moda dos salários: {moda}")
    except statistics.StatisticsError:
        print("Moda dos salários: Não há moda definida (valores únicos).")
    
    # Calcula o desvio padrão arredondado para 2 casas decimais
    desvio_padrao = round(statistics.stdev(salarios), 2)
    print(f"Desvio Padrão dos salários: {desvio_padrao}")
    
    # Retorna os valores calculados
    return media, mediana, desvio_padrao

# Lista de empresas e salários
empresas = {
    "Empresa 1": empresa1,
    "Empresa 2": empresa2,
    "Empresa 3": empresa3,
    "Empresa 4": empresa4
}

# Analisando cada empresa e armazenando os resultados
resultados = {}
for nome, salarios in empresas.items():
    resultados[nome] = calcular_estatisticas(nome, salarios)

# Decisão: Escolher manualmente uma empresa
print("\nDECISÃO FINAL:")
print("As estatísticas de todas as empresas foram exibidas acima.")
print("Agora você pode decidir qual empresa escolher com base na média, mediana, moda e desvio padrão.")

# Opção para escolher uma empresa
print("\nEscolha uma das empresas:")
for idx, empresa in enumerate(empresas.keys(), start=1):
    print(f"{idx} - {empresa}")

# Input para escolha do usuário
escolha = int(input("Digite o número da empresa escolhida: "))

# Valida a escolha e exibe a justificativa
empresa_escolhida = list(empresas.keys())[escolha - 1]
print(f"\nVocê escolheu: {empresa_escolhida}")

# Detalhe os resultados da empresa escolhida
media, mediana, desvio_padrao = resultados[empresa_escolhida]
print(f"Resumo da {empresa_escolhida}:")
print(f"Média Salarial: {media}")
print(f"Mediana Salarial: {mediana}")
print(f"Desvio Padrão Salarial: {desvio_padrao}")

print("\nCom base nesses dados, a escolha foi feita  análisando os salários exibidos.")
