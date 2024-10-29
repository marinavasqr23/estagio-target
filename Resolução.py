


#Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
#Imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?

indice =13
k=0
soma=0

while k < indice:
    k=k+1
    soma=soma+k

print(soma)

#SOMA=91


#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

fibo=[0,1]

numero = int (input ("Digite um numero inteiro: "))

while fibo[-1] < numero:
    prox_fibo= fibo[-1] + fibo[-2]
    fibo.append(prox_fibo)

if numero in fibo:
    print(" Pertence a sequência")
else:
    print("Não pertence a sequência")


#Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open('faturamento_diario.json', 'r') as json_arquivo:
    dados = json.load(json_arquivo)

total = 0
valores = []  

for dia in dados['faturamento']:
    valor = dia['valor']
    total += valor
    valores.append(valor)  

media = total / len(dados['faturamento'])

menor = min(valores)
maior = max(valores)

dias = sum(1 for valor in valores if valor > media)

print(f'Menor faturamento: R$ {menor:.2f}')
print(f'Maior faturamento: R$ {maior:.2f}')
print(f'Número de dias com faturamento superior a média: {dias}')



#Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

valor = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
nome = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo', 'Outros']
total = sum(valor)
i=0
for i in range(5):
    percentual = (valor[i]/total)*100
    print(f"O percentual de representação do Estado de {nome[i]} é {percentual:.2f}% do valor total da distribuidora")


#Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

novo_nome=[]
nome = input("Digite uma palavra:")
m=len(nome)
for i in range (m):
    novo_nome.append(nome[m-i-1])

invertido =""
for char in novo_nome:
    invertido+=char

print(invertido)
