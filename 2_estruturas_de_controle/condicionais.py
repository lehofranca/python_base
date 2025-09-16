# Estruturas de Controle:
# Permitem a execução condicional de blocos de código.
# Vamos explocar os principais tipos: Condicionais e Loops


# CONDICIONAIS:
# Permitem executar um bloco de código com base em uma condição:

# Exemplo de condicional:
idade = 20
if idade >= 18:
    print ('Você é maior de idade.')
else:
    print ('Você é menor de idade')
    
    
    
    
# LOOPS:
# O loop for é utilizado para iterar sobre uma sequência( como uma lista, tupla ou string) ou outro objeto iterável.
    
# Exemplo de Loo For:

for i in range(5):
    print(i)  
    
# O loop While continua a executar o bloco de código enquanto a condição for verdadeira:
# Exemplo de loop While:


while True:
    resposta = input ('Deseja continuar? (s/n)')
    if resposta.lower() == 'n':
        break
print('Operação finalizada')