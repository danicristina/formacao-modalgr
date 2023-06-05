#Função que define um dicionário para as notas, indicando um grau para cada nota.
def notas_para_graus(notas):
    graus = {
        'Dó': 'I',
        'Ré': 'II',
        'Mi': 'III',
        'Fá': 'IV',
        'Sol': 'V',
        'Lá': 'VI',
        'Si': 'VII'
    }

#Esta etapa busca pelo metodo get o grau correspondente de cada nota recebida. Caso não encontre, ele retorna "Nota Inválida".
    graus_escala = [graus.get(nota, 'Nota Inválida') for nota in notas]

    return graus_escala

#Exemplo de uso
notas_entrada = ['Ré', 'Sol', 'Dó']
graus_saida = notas_para_graus(notas_entrada)
print(graus_saida)
