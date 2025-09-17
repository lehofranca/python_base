#FUNÇÕES:
# As funções são blocos de códigos reutilizáveis que realizam uma tarefa específica. 
# Elas ajudam a modularizar e organizar o código, tornando-o mais legível e fácil de manter.
# Aqui criarei funções e o passo a passo delas para entender como funcionam os retonos.

# Passo 1: Definindo uma Função Simples
# Para definir uma função em Python, usamos a palavra-chave def seguida do nome da função e parênteses.
# Dentro dos parênteses, podemos incluir parâmetros (variáveis de entrada). O corpo da função é indentado.

# Definindo uma função simples
def saudacao():
    print("Olá, Mundo!")

saudacao() # Chama a função

# Olá, Mundo!

# Passo 2 - Adicionado Parâmetros:
# Podemos adicionar parâmetros à nossa função para torná-la mais flexível. 
# Parâmetros são variáveis que recebem valores quando a função é chamada

## Função com retorno
def saudacao(nome):
    print(f'Olá, {nome}!')

saudacao('Leonardo') # Chamando função com argumentos (passar um valor -argumento- para o parâmetro)

#Olá, Leonardo!

# Passo 3 - Adição de Retorno:
# Em vez de apenas imprimir um valor, podemos fazer a função retornar um valor usando a palavra-chave return.
# Armazenando o Valor Retornado:
# Armazenar o valor retornado por uma função em uma variável.

# Função com retorno:
def saudacao (nome):
    return f'Olá, {nome}!'
mensagem = saudacao('Luciqueila')
print(mensagem)

# Olá, Luciqueila!

#Passo 4 - Função com vários parâmetros:
#Podemos definir funções que aceitam múltiplos parâmetros. 
# Vamos criar uma função que soma dois números.
# Em seguida, chamar a Função com múltiplos argumentos
# Ex: chamar a função soma passando dois números como argumentos.

#Função com múltiplos parâmetros:
def soma(a, b):
    return (a+b)
resultado = soma (10,5)
print(resultado)

# Resultado: 15
# O mesmo pode ser feito com subtração, divisão, multiplicação e etc.

# Conclusão:
# Criar funções em Python é uma maneira poderosa de tornar seu código mais modular, 
# reutilizável e organizado. As funções podem aceitar parâmetros e retornar valores, o que permite uma grande flexibilidade na programação