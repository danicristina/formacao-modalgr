a = []
b = []

# Função que percorre o vetor a, verifica se existe um numero igual no vetor b e se o mesmo não existe no vetor c. Se condições forem atendidas ele adiciona o numero no vetor c.
def busca_repetido(a, b):
    c = []
    for numero in a:
        if numero in b and numero not in c:
            c.append(numero)
    
    return c

#Exemplo de uso
a = [1, 2, 3, 4, 5, 6, 8, 90, 10, 25, 35, 40, 80, 90, 10, 11, 15, 18, 94, 32]
b = [2, 5, 90, 80, 5, 10, 90, 20, 15, 12, 62, 74, 25, 32, 30, 24, 85, 99, 100, 30]

c = busca_repetido(a, b)
print('Vetor com números repetidos:')
print(c)

#Opção para receber dados via entrada do usuário. Restringe a quantidade de números para 20 por vetor e indica a forma correta para inserção dos dados.

"""
try:
    print("Digite os 20 números do primeiro vetor separados por espaço:")
    a = list(map(int, input().split()))

    if len(a) > 20:
        print("Digite apenas 20 números!")
    else:
        print("Digite os 20 números do segundo vetor separados por espaço:")
        b = list(map(int, input().split()))

    if len(b) > 20:
        print("Digite apenas 20 números!")
    else:
        c = busca_repetido(a, b)
        print('Vetor com números repetidos:')
        print(c)
except:
    print('Verifique sua digitação, digite os números separados apenas por espaço.')
"""