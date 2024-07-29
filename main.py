# BIBLIOTECAS
import re 

# Classe CriarCadastro
class CriarCadastro:
    
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
    DataNascimento = None 
    
    # Informação Pessoa Jurídica
    NomeFantasia = None 
    RazaoSocial = None 
    CNPJ = None 
    
    # Inicialização do Objeto
    def __init__(self, cadastro):
         self.TipoCadastro = cadastro 
    
    def iniciarCadastro(self):
        print("\n"*99)
        if self.TipoCadastro.lower() == "fisica" or self.TipoCadastro.lower() == "fisico":
            self.verificarDados("Email", input("Digite um E-Mail (nome@dominio.com): "))
            self.verificarDados("Celular",  input("Digite seu número de Celular para contato (+XX XX 9XXXX-XXXX): "))
            self.verificarDados("Telefone", input("Digite seu número de Telefone para contato ((XX) 9XXXX-XXXX): "))
            self.verificarDados("Nome", input("Digite seu Nome: "))
            self.verificarDados("Data_Nascimento", input("Digite sua data de Nascimente (DD/MM/AA): "))
            self.verificarDados("CPF", input("Digite seu CPF (XXX.XXX.XXX-XX): "))
            self.verificarDados("CEP", input("Digite o CEP da sua rua/residencia  ex:(XXXXX-XXX): "))
                
        elif self.TipoCadastro.lower() == "juridica" or self.TipoCadastro.lower() == "juridico":
            self.verificarDados("Email", input("Digite um E-Mail (nome@dominio.com): "))
            self.verificarDados("Telefone", input("Digite se número de Telefone para contato ((XX) 9XXXX-XXXX):"))
            self.verificarDados("RazaoSocial", input("Digite sua Razão Social: "))
            self.verificarDados ("CEP", input("Digite seu CEP (XXXXX-XXX): "))
            self.verificarDados("CNPJ", input("Digite seu CNPJ (XX.XXX.XXX/XXXX-XX): "))
        # Caso seja invalida, então vai recomeçar o cadastro. #   
        else:
            print("RESPOSTA INVALIDA\n\nDigite 'Fisica' para Pessoa Física. \nDigite 'Juridica' para Pessoa Juridica\nDigite: ")
            self.iniciarCadastro()
    
    # Verificação da senha digitada.
    def verificarSenha(self, cSenha):
        if cSenha == self.Senha: 
            self.SenhaConfirmada = True
        else:
            print("Senha não é COMPATIVEL, digite novamente.")

    # Verificar o tamanho e a quantidade de casas a ser digitadas. Função Recursiva 
    def verificarDados(self, dados, valor):
        if dados == "CPF":
            padrao = re.compile(r'^\d{3}\.?\d{3}\.?\d{3}\-?\d{2}')  # Cria um padrão no formato (XXX.XXX.XXX-XX)
            if padrao.match(valor): # Faz uma verificação se o valor está no mesmo padrão
                self.CPF = valor
            else:
                self.verificarDados("CPF", input("CPF INVALIDO \nDigite seu CPF (XXX.XXX.XXX-XX): "))
        
        elif dados == "Telefone":
            padrao = re.compile(r'^\(\d{2}\)\s9?\d{4}-?\d{4}$')  # Cria um padrão no formato (XX) 9XXXX-XXXX
            if padrao.match(valor): # Faz uma verificação se o valor está no mesmo padrão
                self.TelefoneContato = valor
            else:
                self.verificarDados("Telefone", input("TELEFONE INVALIDO\nDigite seu número de Telefone para contato ((XX) 9XXXX-XXXX): "))
        
        elif dados == "Celular":
            padrao = re.compile(r'^\+55\s\d{2}\s\d{4,5}-?\d{4}$')  # Cria um padrão no formato +XX XX 9XXXX-XXXX
            if padrao.match(valor): # Faz uma verificação se o valor está no mesmo padrão
                self.Celular = valor
            else:
                self.verificarDados("Celular", input("CELULAR INVALIDO\nDigite seu número de Celular para contato (+XX XX 9XXXX-XXXX): "))
        
        elif dados == "Data_Nascimento":
            padrao = re.compile(r'\d{2}\/\d{2}\/\d{4}')  # Cria um padrão no formato XX/XX/XXXX
            if padrao.match(valor): # Faz uma verificação se o valor está no mesmo padrão
                self.DataNascimento = valor
            else:
                self.verificarDados("Data_Nascimento", input("DATA DE NASCIMENTO INVALIDA\nDigite o ano que você nasceu (DD/MM/AA): "))
        
        elif dados == "CEP":
            padrao = re.compile(r'\d{5}\-\d{3}')  # Cria um padrão no formato XXXXX-XXX
            if padrao.match(valor): # Faz uma verificação se o valor está no mesmo padrão
                self.Endereco = valor
            else:
                self.verificarDados("CEP", input("CEP INVALIDO\nDigite seu CEP (XXXXX-XXX): "))
                
        elif dados == "CNPJ":
            padrao = re.compile(r'\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}') # Cria um padrão no formato XX.XXX.XXX/XXXX-XX
            if padrao.match(valor): # Faz uma verificação se o valor está no mesmo padrão
                self.CNPJ = valor 
            else:
                self.verificarSenha("Digite seu CNPJ (XX.XXX.XXX/XXXX-XX): ")
        elif dados == "Nome":
            if len(valor) > 1: # Verifica se o nome tem mais de um caractere
                self.Nome = valor 
            else: 
                self.verificarDados("Nome", input("TAMANHO DO NOME É INVALIDO\nDigite seu Nome: "))
                
        elif dados == "Email":
            padrao = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$') # Cria um padrão no formato nome@dominio.com
            if padrao.match(valor.lower()): # Faz uma verificação se o valor está no mesmo padrão
                self.EmailContato = valor 
            else:
                self.verificarDados("Email", input("EMAIL Invalido!\nDigite um E-Mail (nome@dominio.com): "))
        
        elif dados == "RazaoSocial":
            if len(valor) > 0: # Verifica se a Razão Social não está vazia
                self.RazaoSocial = valor 
            else:
                self.verificarDados("RazaoSocial", input("RAZAO SOCIAL INVALIDA\nDigite sua Razão Social: "))

    # Imprimir as informações
    def imprimirinfo(self):
        if self.TipoCadastro == "fisica" :
            print(f"\n---- | INFORMAÇÕES DO CADASTRO | ----")
            print("Tipo de Cadastro: " , self.TipoCadastro)
            print("Email:" , self.EmailContato ) 
            print("Telefone para contato: " , self.TelefoneContato) 
            print("Celular para contato:" , self.Celular )  
            print("Nome do cliente: " , self.Nome ) 
            print("Data de nascimento: " , self.DataNascimento )
            print("CPF:" , self.CPF)
            print("CEP:" , self.Endereco ,"\n\n")
        else:
            print(f"\n---- | INFORMAÇÕES DO CADASTRO | ----")
            print("Tipo de cadastro:" , self.TipoCadastro )   
            print("Email:" , self.EmailContato )
            print("Telefone para contato:" , self.TelefoneContato)
            print("Razao social:" , self.RazaoSocial) 
            print("CNPJ:" , self.CNPJ, "\n\n" )

# Inicio do Programa
def main():
    while True: 
        Confirmar = input("Deseja começar o cadastro? (S/N): ")

        # Verificar se o usuário quer continuar o cadastro
        if Confirmar.lower() == 'nao' or Confirmar.lower() == "n" or Confirmar.lower() == "não":
            break
        elif Confirmar.lower() == 'sim' or Confirmar.lower() == "s":
            print("CONTINUANDO...\n\n")
        else:
            print("Resposta Invalida! \n\n")
            continue
        
        # Iniciar o processo de Cadastro
        TipoCadastro = input("Qual seu tipo de cadastro? \nDigite 'Fisica' para Pessoa Física. \nDigite 'Juridica' para Pessoa Juridica\nDigite: ")
        Cadastro = CriarCadastro(TipoCadastro)
        Cadastro.iniciarCadastro()
        
        # Caso a senha de confirmação não seja igual a senha proposta, então vai re-fazer
        while Cadastro.SenhaConfirmada != True:
            Cadastro.Senha = input("Digite uma senha: ")
            Cadastro.verificarSenha(input("Digite a senha novamente: "))
        
        print("PARABÉNS , cadastro realizado com sucesso!! \n")
        Cadastro.imprimirinfo()
        
        break
main()
