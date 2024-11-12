import os
from datetime import datetime


def calcular_dias(data_retirada, data_devolucao):
    formato = "%d/%m/%Y"
    data_retirada = datetime.strptime(data_retirada, formato)
    data_devolucao = datetime.strptime(data_devolucao, formato)
    dias = (data_devolucao - data_retirada).days
    return dias


def cadastro_cliente():
    print("Bem-vindo ao sistema de cadastro!\n")
    nome = input("Digite seu nome completo: ").strip()
    cpf = input("Digite seu CPF (apenas números): ").strip()
    
   
    dados_clientes[nome] = {
        'cpf': cpf,
    }
    print(f"\nCadastro realizado com sucesso!\nBem-vindo, {nome}!")


def aluguel_carro(dados_locadoras, dados_carros):
 
    for locadora, dados in dados_locadoras.items():
        endereco_locadora = dados.get('endereco_locadora', 'Endereço não disponível')
        contato_locadora = dados.get('contato_locadora', 'Contato não disponível')
        print(f"Locadora: {locadora} - Endereço: {endereco_locadora} - Contato: {contato_locadora}")
    escolha_locadora = input('Qual a locadora de sua opção? ').strip()
    os.system('cls')

   
    carros_locadora = {carro: dados for carro, dados in dados_carros.items() if dados.get('locadora') == escolha_locadora}

    if not carros_locadora:
        print("Não há carros disponíveis nesta locadora.")
        return


    for carro, dados in carros_locadora.items():
        marca = dados.get('marca', 'Marca não disponível')
        ano = dados.get('ano', 'Ano não disponível')
        tipo = dados.get('tipo', 'Tipo não disponível')
        cor = dados.get('cor', 'Cor não disponível')
        print(f"Carro: {carro} - Marca: {marca} - Ano: {ano} - Tipo: {tipo} - Cor: {cor}")
    
    escolha_carro = input('Escolha o carro desejado: ').strip()
    os.system('cls')


    if escolha_carro not in carros_locadora:
        print("Carro não disponível na locadora selecionada.")
        return

    
    data_retirada = input('Digite a data de retirada (dd/mm/aaaa): ')
    data_devolucao = input('Digite a data de devolução (dd/mm/aaaa): ')

    dias_aluguel = calcular_dias(data_retirada, data_devolucao)
    if dias_aluguel <= 0:
        print("A data de devolução deve ser posterior à data de retirada.")
        return

    
    preco_por_dia = 50 
    valor_total = preco_por_dia * dias_aluguel

 
    print(f"\nResumo do aluguel:\nCarro: {escolha_carro}\nLocadora: {escolha_locadora}\n"
          f"Data de Retirada: {data_retirada}\nData de Devolução: {data_devolucao}\n"
          f"Duração: {dias_aluguel} dias\nValor Total: R${valor_total:.2f}")
    print("\nObrigado por usar nosso sistema! Esperamos vê-lo novamente em breve.\n")


dados_locadoras = {
    'Locadora A': {'endereco_locadora': 'Rua ABC, 123', 'contato_locadora': '1234-5678'},
    'Locadora B': {'endereco_locadora': 'Rua XYZ, 456', 'contato_locadora': '9876-5432'}
}

dados_carros = {
    'Carro1': {'locadora': 'Locadora A', 'marca': 'Fiat', 'ano': 2020, 'tipo': 'Sedan', 'cor': 'Preto'},
    'Carro2': {'locadora': 'Locadora A', 'marca': 'Chevrolet', 'ano': 2021, 'tipo': 'SUV', 'cor': 'Branco'},
    'Carro3': {'locadora': 'Locadora B', 'marca': 'Honda', 'ano': 2019, 'tipo': 'Hatch', 'cor': 'Vermelho'}
}


dados_clientes = {}

verificação_cliente = input('Você já é um cliente cadastrado? (s/n) ').lower()
os.system('cls')
if verificação_cliente == "s":
    nome_cliente = input('Digite seu nome: ').strip()
    os.system('cls')
    
    if nome_cliente in dados_clientes:
        print(f"Bem-vindo de volta, {nome_cliente}!\n")
        cpf_cliente = dados_clientes[nome_cliente]['cpf']
        print(f"Seu CPF: {cpf_cliente}\n")

        print('1- Atualizar informações\n2- Aluguel de carros\n')
        decisao_03 = int(input('Digite a opção desejada: '))
        os.system('cls')

        if decisao_03 == 1:
            print("Atualizando informações...")
            
        elif decisao_03 == 2:
            aluguel_carro(dados_locadoras, dados_carros)
    else:
        
        cadastro_cliente()
        print("\nAgora você pode fazer o aluguel de carros.")
        aluguel_carro(dados_locadoras, dados_carros)
else:
   
    cadastro_cliente()
    print("\nAgora você pode fazer o aluguel de carros.")
    aluguel_carro(dados_locadoras, dados_carros)
