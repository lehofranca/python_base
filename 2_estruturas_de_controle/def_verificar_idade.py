# Função DEF:
    
def verificar_idade():

    idade_usuario = int(input('Digite a sua idade:'))

# Verifica se é maior ou menor de idade:

    if idade_usuario >= 18:
        print ('Você é maior de idade')
    
    else:
        print ('Você é menor de idade.')
    
# Chama a função:
verificar_idade()           