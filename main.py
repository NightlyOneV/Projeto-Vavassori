# BIBLIOTECAS
import re 

# VETOR PARA GUARDAR OBJETOS
usuarios=[] 

# Criação da classe "Cadastro"
class Criar_Cadastro:
    
    # Informação Sensível
    Senha = None
    SenhaConfirmada = None
    
    # Informação Geral
    TipoCadastro = None
    EmailContato = None 
    TelefoneContato = None
    Endereco = None
    
    # Informação Pessoa Física
    Nome = None 
    CPF = None 
    Celular = None 
    Data_Nascimento = None 
    
    # Informação Pessoa Jurídica
    NomeFantasia = None 
    Razao_Social = None 
    CNPJ = None 
    
    # Inicialização do Objeto
    def __init__(self, cadastro):
         self.TipoCadastro = cadastro 
    
    # Verificação da senha digitada.
    def verificarSenha(self, cSenha):
        if cSenha == self.Senha: 
            self.SenhaConfirmada = True
        else:
            print("Senha não é COMPATIVEL, digite novamente.")

    # verificar o tamanho e a quantidade de casas a ser digitadas. 
def verificarDados(self, dados, valor):
    if dados == "CPF":
        padrao = re.compile(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}')  # Verifica se é XXX.XXX.XXX-XX
        if padrao.match(valor):
            self.CPF = valor
        else:
            self.verificarDados("CPF", input("CPF INVALIDO \nDigite seu CPF (XXX.XXX.XXX-XX): "))
    
    elif dados == "Telefone":
        padrao = re.compile(r'^\(\d{2}\)\s9?\d{4}-\d{4}$')  # Verifica se é (XX) 9XXXX-XXXX
        if padrao.match(valor):
            self.TelefoneContato = valor
        else:
            self.verificarDados("Telefone", input("TELEFONE INVALIDO\nDigite telefone para contato ((XX) 9XXXX-XXXX):"))
    
    elif dados == "Celular":
        padrao = re.compile(r'^\+55\s\d{2}\s\d{4,5}-\d{4}$')  # Verifica se é +XX XX 9XXXX-XXXX
        if padrao.match(valor):
            self.Celular = valor
        else:
            self.verificarDados("CELULAR", input("CELULAR INVALIDO\nDigite telefone para contato (+XX XX 9XXXX-XXXX):"))
    
    elif dados == "Data_Nascimento":
        padrao = re.compile(r'\d{2}\/\d{2}\/\d{4}')  # Verifica se é XX/XX/XXXX
        if padrao.match(valor):
            self.Data_Nascimento = valor
        else:
            self.verificarDados("Data_Nascimento", input("DATA DE NASCIMENTO INVALIDA\nDigite o ano que você nasceu (DD/MM/AA): "))
    
    elif dados == "CEP":
        padrao = re.compile(r'\d{5}\-\d{3}')  # Verifica se é XXXXX-XXX
        if padrao.match(valor):
            self.Endereco = valor
        else:
            self.verificarDados("CEP", input("CEP INVALIDO\nDigite seu CEP (XXXXX-XXX): "))


    # Imprimir as informações
    def imprimirinfo(self, indice):
        if self.TipoCadastro == "fisica" :
            print(f"\n----INFORMAÇÕES DO CADASTRO #{indice+1}----")
            print("Tipo de Cadastro: " , self.TipoCadastro)
            print("Email:" , self.EmailContato ) 
            print("Telefone para contato: " , self.TelefoneContato) 
            print("Celular para contato:" , self.Celular )  
            print("Nome do cliente: " , self.Nome ) 
            print("Data de nascimento: " , self.Data_Nascimento )
            print("CPF:" , self.CPF)
            print("Endereço:" , self.Endereco ,"\n\n")
        else:
            print(f"\n----INFORMAÇÕES DO CADASTRO #{indice+1}----")
            print("Tipo de cadastro:" , self.TipoCadastro )   
            print("Email:" , self.EmailContato )
            print("Telefone para contato:" , self.TelefoneContato)
            print("Razao socal:" , self.Razao_Social) 
            print("CNPJ:" , self.CNPJ, "\n\n" )
            
# Retornar os usuarios existentes
def retornar_usuario ():    
    for i in range (len(usuarios)):
        usuarios[i].imprimirinfo(i)

# Inicio do Programa
def main():
    PararCadastro = False
    
    # Enquanto o usuário não querer parar o cadastro vai acontecer o processo de cadastração
    while not PararCadastro: 
        Confirmar = input("Deseja começar um novo cadastro? (S/N): ")

        # Verificar se o usuário quer continuar o cadastro
        if Confirmar.lower() == 'nao' or Confirmar.lower() == "n" or Confirmar.lower() == "não":
           
            retornar_usuario()
            PararCadastro = True 
            break
        elif Confirmar.lower() == 'sim' or Confirmar.lower() == "s":
            print("CONTINUANDO...\n\n")
        else:
            print("Resposta Invalida! \n\n")
            continue
        
        # Pergunta para o usuário qual o tipo de cadastro dele
        tipoCadastro = input("Qual seu tipo de cadastro? \nDigite 'Fisica' para Pessoa Física. \nDigite 'Juridica' para Pessoa Juridica: ")
        
        # Verificar se o usuario quer se cadastrar como pessoa fisica ou juridica
        if tipoCadastro.lower() == "fisica" or tipoCadastro.lower() == "fisico":
            Cadastro = Criar_Cadastro("fisica")
            Cadastro.EmailContato = input("Digite seu email para contato: ")
            Cadastro.verificarDados ("Celular",  input("Digite Celular para contato (+XX XX 9XXXX-XXXX) :"))
            Cadastro.verificarDados("Telefone", input("Digite telefone para contato ((XX) 9XXXX-XXXX) :"))
            Cadastro.Nome = input("Digite seu nome: ")
            Cadastro.verificarDados ("Data_Nascimento", input("Digite sua data de Nascimente (DD/MM/AA): "))
            Cadastro.verificarDados ("CPF", input("Digite seu CPF (XXX.XXX.XXX-XX): "))
            Cadastro.verificarDados ("CEP", input("Digite seu CEP (XXXXX-XXX): "))

        elif tipoCadastro.lower() == "juridica" or tipoCadastro.lower() == "juridico":
            Cadastro = Criar_Cadastro("juridica")
            Cadastro.EmailContato = input("Digite seu email para contato: ")
            Cadastro.TelefoneContato = input("Digite seu Telefone de contato: ")
            Cadastro.Razao_Social = input("Digite sua razão social: ")
            Cadastro.CNPJ = input("Digite seu CNPJ (XX.XXX.XXX/XXXX-XX): ")
            Cadastro.Endereco = ("CEP", input("Digite seu CEP (XXXXX-XXX): "))
        # Caso seja invalida, então vai recomeçar o cadastro.   
        else:
            print("RESPOSTA INVALIDA\n\n")
            continue
        
        # Caso a senha de confirmação não seja igual a senha proposta, então vai re-fazer
        while Cadastro.SenhaConfirmada != True:
            Cadastro.Senha = input("Digite uma senha: ")
            Cadastro.verificarSenha(input("Digite a senha novamente: "))
        
        print("PARABÉNS , cadastro realizado com sucesso!! \n")
            
        usuarios.append(Cadastro)

main()
