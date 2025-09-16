# Tamanho da string:

frase = 'Olá, pessoal!'
tamanho = len(frase)
print('Tamanho da string:', tamanho) # Saída: Tamanho da string: 13


# Transformando em maiúsculas:

maiusculas = frase.upper()
print('Maiúsculas:', maiusculas)


minúsculas = frase.lower()
print('Minúsculas:', minúsculas)

# Observações:

# upper() → transforma todos os caracteres para maiúsculas.

# lower() → transforma todos os caracteres para minúsculas.

# A variável que armazena o resultado precisa ser usada no print.



#Substituindo palavras na string:

frase = "Estou estudando Python todos os dias."
nova_frase = frase.replace('Python','Javascript')
print(frase)
print('Nova frase:',nova_frase)