#importa a biblioteca para trabalhar com datas.
from datetime import datetime

#recebe os dados do colaborador.
nome_colaborador = input("Digite o nome do colaborador: ")
data_admissao = input("Digite a data de admissão (dd/mm/aaaa): ")
salario_atual = float(input("Digite o salário atual: "))
valor_emprestimo = float(input("Digite o valor do empréstimo: "))

#Esta função transforma a string recebida em datetime e calcula o tempo de registro.
def calcular_tempo_de_casa(data_admissao):
    data_atual = datetime.now()
    formato = '%d/%m/%Y'  #formato para a data (dia/mês/ano)
    data_admissao = datetime.strptime(data_admissao, formato)

    tempo_casa = data_atual - data_admissao

    anos_trabalho = tempo_casa.days // 365

    return anos_trabalho

anos = calcular_tempo_de_casa(data_admissao)

#As funçoes abaixo percorrem item por item dos vetores especificados em cada uma e calcula a quantidade de notas necessarias subtraindo do valor total do emprestimo e acrescentando a string na variável resultado.
def calcular_notas_maiores(valor_emprestimo):
    notas = [100, 50, 20, 10, 5]

    resultado = f"\nValor empréstimo: {valor_emprestimo} reais\n"

    resultado += "\nNotas de maior valor:\n"
    for nota in notas:
        qtd_notas = valor_emprestimo // nota
        valor_emprestimo -= qtd_notas * nota
        if qtd_notas > 0:
            resultado += (f"- {qtd_notas} x {nota} reais\n")

    return resultado  

def calcular_notas_menores(valor_emprestimo):
    notas_menores = [20, 10, 5, 2]

    resultado = "\nNotas de menor valor:\n"
    for nota in notas_menores:
        qtd_notas = valor_emprestimo // nota
        valor_emprestimo -= qtd_notas * nota
        if qtd_notas > 0:
            resultado += (f"- {qtd_notas} x {nota} reais\n")

    return resultado

def calcular_notas_meio_a_meio(valor_emprestimo):
    notas = [100, 50, 20, 10, 5, 2]
    notas_menores = [20, 10, 5, 2]

    resultado = "\nNotas meio a meio:\n"
    valor_maiores = valor_emprestimo // 2
    valor_menores = valor_emprestimo - valor_maiores

    resultado += f"{valor_maiores} reais em notas de maior valor:\n"
    for nota in notas:
        qtd_notas = valor_maiores // nota
        valor_maiores -= qtd_notas * nota
        if qtd_notas > 0:
            resultado += (f"- {qtd_notas} x {nota} reais\n")

    resultado += f"\n{valor_menores} reais em notas de menor valor:\n"
    for nota in notas_menores:
        qtd_notas = valor_menores // nota
        valor_menores -= qtd_notas * nota
        if qtd_notas > 0:
            resultado += (f"- {qtd_notas} x {nota} reais\n")

    return resultado

#Nesta etapa são verificadas as condições para ser elegível ao empréstimo.

if valor_emprestimo % 2 != 0:
    print("Insira um valor válido!")

elif valor_emprestimo > salario_atual * 2 or anos < 5:
    print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.") 

else:
    #Caso o colaborador seja elegível, nesta variável é armazenado o resultado de todas as funções para calcular notas.
    resultado_emprestimo = (calcular_notas_maiores(valor_emprestimo)) + (calcular_notas_menores(valor_emprestimo) + (calcular_notas_meio_a_meio(valor_emprestimo)))
    print(resultado_emprestimo)