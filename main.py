import json
import os


class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'
    
    
    
    #FUNÇÃO MENU LOCADORA
def exibir_menu_adm_locadora():

    print("\nMENU:")
    print("1. ADICIONAR LOCADORA")
    print("2. LISTAR LOCADORA")
    print("3. ATUALIZAR LOCADORA")
    print("4. EXCLUIR LOCADORA")
    print("5. LISTAR UMA LOCADORA")
    print("6. VOLTAR AO MENU ANTERIOR")

#LISTAR LOCADORA FUNÇÃO
def listar_locadora():
    os.system('cls')
    with open('dados_locadora.json') as meu_json:
        dados =json.load(meu_json)
        
    
         
        for nome, info in dados.items():
            print("*" * 50)
            print(f"Nome: {nome}")
            print("Dados:")
            print(f"  Codigo Locadora: {info['codigo_locadora']}")
            print(f"  Contato Locadora: {info['contato_locadora']}")
            print(f"  Endereço Locadora: {info['endereco_locadora']}")
            print("=" * 50)
            
            
            
# Função para carregar os dados do arquivo json1
def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Função para salvar os dados no arquivo json   CREATE
def salvar_dados(dados, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)
    print("Dados salvos com sucesso!")


# Função para atualizar os dados no arquivo json   UPDATE
def atualizar_clientes():
    os.system('cls')
    atualizar = input("Digite o nome do cliente a ser atualizado: ").strip()
    
    with open('dados_clientes.json', 'r') as atualizar_cliente:
        atualizacao = json.load(atualizar_cliente)
        
    # Normaliza os nomes no dicionário para comparação
    nomes_normalizados = {nome.lower(): nome for nome in atualizacao.keys()}
    
    # Verifica se o nome do cliente existe
    nome_key = nomes_normalizados.get(atualizar.lower())  # Usa .lower() para normalizar
    
    if nome_key:
        print('Atualizar Dados cliente cliente')
        cpf_cliente = input('Digite O novo CPF: ')
        nascimento_cliente = input('A nova data de nascimento: ')
        numero_cliente = input('Digite o noco número para contato: ')
        cnh_cliente = input('Digite o novo número de sua CNH: ')
        
        # Atualiza os dados do cliente
        atualizacao[nome_key] = {
            'cpf': cpf_cliente,
            'nascimento': nascimento_cliente,
            'numero': numero_cliente,
            'cnh': cnh_cliente
        }
        
        # Salvar os dados no arquivo JSON
        with open('dados_clientes.json', 'w') as salvar_dados:
            json.dump(atualizacao, salvar_dados, indent=4)  # Salva os dados atualizados
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print(f'Cliente {nome_key} atualizado com sucesso!')
    else:
        print(f"Cliente '{atualizar}' não encontrado.")
            
            
  
# Função para Ler  os dados do arquivo json1    READ
def listar_clientes():
    with open('dados_clientes.json') as meu_json:
        dados =json.load(meu_json)
    
   
        for nome, info in dados.items():
            print("*" * 50)
            print(f"Nome: {nome}")
            print("Dados:")
            print(f"  CPF: {info['cpf']}")
            print(f"  Data de Nascimento: {info['nascimento']}")
            print(f"  Número: {info['numero']}")
            print(f"  CNH: {info['cnh']}")
            print("=" * 50)


# Função para APAGAR  os dados do arquivo json1   DELETE
def apagar_usuario():
    apagar = input("Digite o nome do Cliente a ser apagado: ").strip()  # Remove espaços em branco

    with open('dados_clientes.json', 'r') as apagar_dados:
        data = json.load(apagar_dados)

        # Normaliza os nomes no dicionário para comparação
        nomes_normalizados = {nome.lower(): nome for nome in data.keys()}

        # Verifica se o nome do cliente existe
        nome_key = nomes_normalizados.get(apagar.lower())  # Usa .lower() para normalizar

        if nome_key:
            data.pop(nome_key)  # Remove o cliente
            
            # Salvar os dados atualizados no mesmo arquivo
            with open('dados_clientes.json', 'w') as salvar_dados:
                json.dump(data, salvar_dados, indent=4)  # Salva os dados atualizados
                print("CLIENTE APAGADO COM SUCESSO")
        else:
            print(f"Cliente '{apagar}' não encontrado.")
            

def menu_locadora(user_loc):
    print(cor.VERDE+'------------------------------------------------')
    print('        |BEM VINDO|'+user_loc)
    print('------------------------------------------------')
    
    print('| 1 - VER CARROS')
    print('| 2 - ADICIONAR  CARROS')
    print('| 3 - ATUALIZAR CARROS')
    print('| 4 - VER CARROS')
        
        

# Carregar os dados existentes 
dados_clientes = carregar_dados('dados_clientes.json')
dados_adm = carregar_dados('dados_administradores.json')
dados_locadoras = carregar_dados('dados_locadora.json')
dados_carros = carregar_dados('carros.json')


#menu principal
def menuPrincipal():
    print('=================================================')
    print(cor.AMARELO+'|BEM VINDO AO NOSSO SISTEMA DE ALUGUEL DE CARROS|')
    print('=================================================')
    print('\n1 - ADMINISTRADOR\n2 - LOCADORA\n3 - CLIENTE\n4 - SAIR')
    


#menu Secundario 
def exibir_menu():
    
    print("\nMENU:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. LISTAR UM USUÁRIO")
    print("6. VOLTAR AO MENU ANTERIOR")
    
    



def main():
    
    while True:
        
        menuPrincipal()
        entrada_inicial = int(input('\nDigite a opção desejada: '))
        os.system('cls')
    
    
        match(entrada_inicial):
            case 1:
                while True:
                  os.system('cls')
                  entrada_adm =int(input("\n|1 - ENTRAR NO SISTEMA\n|2 - VOLTAR\n"))
                

                    
                  if(entrada_adm ==1):
                     user = input('Digite seu usuário: ')
                     senha = input('Digite sua senha: ')
                     
                     if user in dados_adm:
                         if dados_adm[user]['senha']== senha:
                            print('------------------------------------------------')
                            print('        |BEM VINDO ADMINISTRADOR|')
                            print('------------------------------------------------')
                            
                            while True:
                                menuPrincipal()
                                entrada_inicial= int(input('\nDigite a opção desejada: '))
                                os.system('cls')
                                
                                match(entrada_inicial):
                                    
                                    case 1:
                                        print("Chegou aqui")
                                        break
                                    
                                    case 2:
                                        while True:
                                            exibir_menu_adm_locadora()
                                            entrada_secundaria= int(input("Digite a opção desejada:  "))
                                            
                                            match(entrada_secundaria):
                                                case 1:
                                                    print("chegou aqui ")
                                                    print("CADASTRO DE  LOCADORA")
                                                    nome_locadora =input("Digite o nome da locadora:  ")
                                                    login_locadora =input("Digite o login da locadora:  ")
                                                    codigo_locadora =input("Digite o codigo de sua locadora:  ")
                                                    senha_locadora =input("Digite senha da locadora:  ")
                                                    contato_locadora =input("Digite o numero para contato:  ")
                                                    endereco_locadora =input("Digite Endereço Locadora:  ")
                                                    
                                                    
                                                
                                                    dados_locadoras[nome_locadora]={
                                                    "login_locadora":login_locadora,
                                                    "codigo_locadora":codigo_locadora,
                                                    "senha_locadora":senha_locadora,
                                                    "contato_locadora":contato_locadora,
                                                    "endereco_locadora":endereco_locadora
                                                }
                                                    os.system('cls')
                                                    salvar_dados(dados_locadoras, 'dados_locadora.json')
                                                    print(cor.VERDE+'LOCADORA CADASTRADA COM SUCESSO')
                                                    
                                                case 2:
                                                    listar_locadora()
                                                    
                                        
                                    
                                    case 3:
                                        while True:
                                            exibir_menu()
                                            entrada_secundaria = int(input("Digite a Opção Desejada: "))
                                            
                                            match(entrada_secundaria):
                                                case 1:
                                                    print('Cadastro de cliente')
                                                    nome_cliente = input('Digite seu nome e sobrenome: ')
                                                    cpf_cliente = input('Digite seu CPF: ')
                                                    nascimento_cliente = input('Digite sua data de nascimento: ')
                                                    numero_cliente = input('Digite seu número para contato: ')
                                                    cnh_cliente = input('Digite o número de sua CNH: ')
                                    
                                                    dados_clientes[nome_cliente] = {
                                                    'cpf': cpf_cliente,
                                                    'nascimento': nascimento_cliente,
                                                    'numero': numero_cliente,
                                                    'cnh': cnh_cliente
                                                         }
                                                    os.system('cls')
                                                    salvar_dados(dados_clientes, 'dados_clientes.json')
                                                    print(f'Cliente {nome_cliente} cadastrado com sucesso!')
                                                
                                                case 2:
                                                    os.system('cls')
                                                    listar_clientes()
                                                case 3:
                                                   os.system('cls')
                                                   atualizar_clientes()
                                                case 4:
                                                  os.system('cls')
                                                  apagar_usuario()
                                
                                                case 5:
                                                 os.system('cls')
                                                 print('FEATURE EM DESENVOLVIMENTO')
                                
                                                case 6:
                                                 os.system('cls')
                                                 print('VOLTANDO AO MENU PRINCIPAL')
                                                 break
                                
                                                case __:
                                                 print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                    
                                    case 4:
                                        print("VOLTANDO...")   
                                        break     
                     else:
                         print(cor.VERMELHO+ "SENHA OU USUARIO INCORRETOS")
                         break
                         
                        
                                                    
                                            
                             
                
                  else:
                     print(cor.VERMELHO+ "VOLTANDO AO MENU ANTERIOR")
                     break
            
            case 2:
                while True:
                    locadora_entrada= int(input("|1 - LOCADORA PARCEIRA \n|2 - CADASTRAR LOCADORA \n|3 - VOLTAR AO MENU ANTERIOR:  \n"))
                    
                    
                        
                    if(locadora_entrada==1):
                        
                        nome_locadora = input('Digite o nome da locadora: ')
                        senha = input('Digite sua senha: ')
                     
                        if nome_locadora in dados_locadoras:
                           if dados_locadoras[nome_locadora]['senha_locadora']== senha:
                            
                            
                            while True:
                                menu_locadora(nome_locadora)
                                break
                            
                            
                            
                            
                            
                        else:
                         print(cor.VERMELHO+ "SENHA OU USUARIO INCORRETOS")
                         break
                            
                        
                        
                    elif(locadora_entrada ==2):
                        
                            
                        print("CADASTRO DE  LOCADORA")
                        nome_locadora =input("Digite o nome da locadora:  ")
                        login_locadora =input("Digite o login da locadora:  ")
                        codigo_locadora =input("Digite o codigo de sua locadora:  ")
                        senha_locadora =input("Digite senha da locadora:  ")
                        contato_locadora =input("Digite o numero para contato:  ")
                        endereco_locadora =input("Digite Endereço Locadora:  ")
                        
                        
                      
                        dados_locadoras[nome_locadora]={
                          "login_locadora":login_locadora,
                          "codigo_locadora":codigo_locadora,
                          "senha_locadora":senha_locadora,
                          "contato_locadora":contato_locadora,
                          "endereco_locadora":endereco_locadora
                      }
                        os.system('cls')
                        salvar_dados(dados_locadoras, 'dados_locadora.json')
                        print(cor.VERDE+'LOCADORA CADASTRADA COM SUCESSO')
                        
                    elif(locadora_entrada==3):
                        os.system("cls")
                        print(cor.CIANO+"VOLTANDO AO MENU ANTERIOR!!!")
                        break
                    else:
                        os.system('cls')
                        print(cor.VERMELHO+ "OPÇÃO INVALIDA")
                        
                            
                            
                          
            case 4:
                print(cor.VERDE+"ENCERRANDO PROGRAMA...")
                break
            
            case __:
                print(cor.VERMELHO+" OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                        

                        
                    
                        
                        
        
    
    
    
    
if __name__ == "__main__":
    main()
    
    
