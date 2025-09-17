# ZERODIVISIONERROR:
# Esta é uma exceção em Python que ocorre quando uma operação de divisão é realizada com um divisor igual a zero.
# Essa exceção é lançada para evitar resultados indefinidos ou matematicamente inválidos. Quando esse erro ocorre, 
# a execução do programa é interrompida e uma mensagem de erro é exibida, indicando que a divisão por zero é impossível.

 
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print ("Erro de divisão por 0", e)
    
# Erro de divisão por zero: division by zero    


# TYPEERROR:
# Esta é uma exceção em Python que ocorre quando uma operação é realizada em um objeto de um tipo incompatível.
# Essa exceção é comumente lançada quando uma função é chamada com o número errado de argumentos ou quando operações
# são realizadas com tipos de dados incompatíveis.    
    
try:
        result = "10" + 5
except TypeError as e:
    print ("Erro de tipo:", e)
    
    
# Erro de tipo : can only cocatenate str (not "int") to str  

# NAMERROR:
# Esta é uma exceção em Python que ocorre quando um identificador (nome de variável, função, classe, etc.) não é encontrado no escopo atual.
# Essa exceção é comumente lançada quando o interpretador Python não consegue associar um nome a um objeto existente.

try:
    print (variavel_inexistente)
except NameError as e:
    print ("Erro de nome", e)
   
# Erro de nome name 'variavel_inexistente' is not defined 

# VALUEERROR:
# Esta é uma exceção em Python que ocorre quando uma função recebe um argumento do tipo correto, 
# mas com um valor inadequado. Essa exceção é comumente lançada quando uma operação espera um argumento de um tipo específico, 
# porém o valor fornecido não é válido para essa operação.

try:
    int ("abc")
except ValueError as e:
     print ("Erro de valor",e) 

# Erro de valor invalid literal for int() with base 10: 'abc'


# INDEXERROR:
# Esta é uma exceção em Python que ocorre quando você tenta acessar um índice em uma sequência (como uma lista, tupla ou string) fora dos limites válidos.
# Em Python, os índices geralmente começam em 0 e vão até o comprimento da sequência menos um.

try:
    my_list = [1,2,3]
    print(my_list[4])
except IndexError as e:
    print("Erro de índice", e)    
    
# Erro de índice list index out of range


# KEYERROR:
# Esta é uma exceção em Python que ocorre quando você tenta acessar uma chave que não está presente em um dicionário.
# Em Python, os dicionários são estruturas de dados que mapeiam chaves a valores. 
# Se você tentar acessar uma chave que não existe no dicionário, um KeyError será gerado.
    
    
try:
     my_dict = {"key": "value"}
     print(my_dict["invalid_key"])
except KeyError as e:
    print ("Erro de chave:", e)
    print("Erro de chave", e)
    
# Erro de chave 'invalid_key'

# Exemplo real:

try:
    pessoa = {
        "nome": "Leonardo",
        "idade": 33,
        "cidade": " São Paulo"
    }
    
# Tentando acessar uma chave que não existe:    
    print(pessoa["profissao"])
except KeyError as e:
    print("Erro de chave:", e)
# Usando .get() para evitar o erro de definir um valor padrão    
    print(pessoa.get("profissao","Não informada"))
    
# Erro de chave: 'profissao'       

# FILENOTFOUNDERROR:
# Esta é uma exceção em Python que ocorre quando um arquivo ou diretório especificado não pode ser encontrado durante uma operação de leitura, 
# escrita ou manipulação de arquivos.

try:
    with open ("arquivo_inexistente.txt", "r") as file: # Neste caso poderia utilizar arquivo txt, csv, e etc.
        content = file.read()
except FileNotFoundError as e:
    print ("Erro de arquivo não encontrado:",e)        
        
# Erro de arquivo não encontrado: [Errno 2] No such file or directory: 'arquivo_inexistente.txt'

# IMPORTERROR:
# Esta é uma exceção em Python que ocorre quando um módulo ou pacote não pode ser importado corretamente. Essa exceção é comumente lançada quando 
# o interpretador Python não consegue encontrar o módulo especificado em sys.path
# (uma lista de diretórios onde o Python procura por módulos).
 
try:
    import modulo_inexistente
except ImportError as e:
    print("Erro de importação:", e)
    
# Erro de importação: No module named 'modulo_inexistente'        

# Exemplo real:

try:
    import matematica_avancada
except ImportError as e:
    print("Erro de importação", e)
    
# Erro de importação No module named 'matematica_avancada'

# ATTRIBUTEERROR:
# Esta é uma exceção em Python que ocorre quando uma tentativa de acesso a um atributo de um objeto não é bem-sucedida.
# Essa exceção é comumente lançada quando um objeto não possui o atributo especificado.

class Exemplo:
    def __init__(self):
      self.atributo = "valor"
      
try:
    obj = Exemplo()
    print(obj.atributo_inexistente)
except AttributeError as e:
    print("Erro de atributo:", e) 
    
# Erro de atributo: 'Exemplo' object has no attribute 'atributo_inexistente'

# Exemplo real:

class Carro:
    def __init__(self,modelo,ano):
        self.modelo = modelo
        self.ano = ano 
        # Note que não foi definido self.cor de propósito.
try:
    # Criação do objeto:
    meu_carro = Carro("Jeep",2025)
    
    # Tentando acessar um atributo que não existe:
    print(meu_carro.cor)
    
except AttributeError as e:
    # Captura o erro e informa:
    
    print("Erro de atributo:", e)
    # Pode-se definir um valor padrão ou informar ao usuário
    print("Atributo 'cor' não existe. Usando valor padrão: 'Não definido'")
    meu_carro.cor = "Não definido"
    print("Cor do carro:, meu_carro.cor")
    
# # Erro de atributo: 'Carro' object has no attribute 'cor'
# Atributo 'cor' não existe. Usando valor padrão: 'Não definido'
# Cor do carro:, meu_carro.cor                             