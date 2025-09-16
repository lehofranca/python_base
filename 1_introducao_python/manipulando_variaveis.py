# Você pode realizar operações matemáticas e concatenar strings com variáveis em Python.

# Operações com variáveis:
a = 10
b = 20
soma = a + b
concatenacao = 'Olá' + ' ' + 'Leonardo!'

#imprimindo os resultados
print('Soma:', soma)
print('Concatenação:', concatenacao)

# Aqui usa-se o operador +, que concatena strings
# SE você fizer 'Olá', 'Leonardo' (com vírgula) dentro de print, então não é mais uma concatenação, e sim uma tupla.

# Exemplo de uso:

concatenacao = 'Olá' +' '+ 'Leonardo!'
print(concatenacao) # Saída: Olá Leonardo!

# Usando vírgula
print('Olá','Leonardo!') # Saída: Olá Leonardo!


# Diferença:
# + → une as strings em uma única string.
# , → passa dois argumentos para o print, que imprime separados por espaço, mas não cria uma nova string.

# Outro exemplo de uso, com vírgula, na concatenação:
concatenacao = 'Olá, ' + 'Leonardo!'
print(concatenacao) # Saída: Olá, Leonardo!



# Definindo uma string: 
frase = 'Python é uma línguagem de programação poderosa, com melhor síntaxe.'

# Imprindo a string:
print(frase)