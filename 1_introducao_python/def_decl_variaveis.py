# importa biblioteca para formatação de números no padrão brasileiro:


import locale
locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252') # Define local como Brasil


# Função para exibir informações do funcionário:


def exibir_dados(numero,nome, salario):
    """
    Recebe número, nome e salário de um funcionário 
    e imprime os dados formatados.
    """
    
    print (f"Número: {numero}")
    print (f"Nome: {nome}")
    # Formata o salário no padrão brasileiro:
    print(f"Salário: {locale.currency(salario,grouping=True)}")
    
# Exemplo de uso da função:
    
numero = 33
nome = 'Leonardo'
salario = 50000.00
 
exibir_dados(numero, nome, salario)
 
 # locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252') → configura Python para usar padrão brasileiro.
 # locale.currency(salario, grouping=True) → formata 50000.00 como R$ 50.000,00.
 # Função exibir_dados(...) → reutilizável para qualquer número, nome e salário.
 