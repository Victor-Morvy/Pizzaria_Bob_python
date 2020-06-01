'''
Data........: 2020-05-15
Projeto.....: Pizzaria
Arquivo.....: Main.py
Descrição...: Auqui estará os menus, inicialmente, posteriormente será dividido em outros módulos
Autor.......: Victor Hugo Martins de Oliveira
Observações.: 2020-05-15 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias:
'''


from datetime import datetime
import os
import functDb

#global pedidos = []

_pedido = functDb.ultimoPedido()
print(_pedido)

#Menu principal
def menuPrincipal():
    opc = 0

    while opc != 9:
        print("MENU PRINCIPAL")
        print("1 - Realizar Pedido")
        print("2 - Cadastrar Cliente")
        print("3 - Alterar Cadastro do Cliente")
        print("4 - Consultar Pedidos")
        print("5 - Administração")
        print("9 - Sair")
        opc = int(input())

        #seleção da opção
        if opc == 1:
            #limpa pedidos da lista
            pedidos.clear()
            realizarPedido()
        elif opc == 2:
            cadastrarCliente()
        elif opc == 3:
            alterarCadastroCliente()
        elif opc == 4:
            consultarPedidos()
        elif opc == 5:
            adminMenu()
        elif opc == 9:
            continue
        else:
            print("Opção inválida")

def main():
    menuPrincipal()

if __name__ == '__main__':
    main()

#Função para saber se o cliente tem cadastro
def realizarPedido():
    opc = 0
    while opc != 9:
        print("O cliente tem cadastro?")
        print("1 - Sim.")
        print("2 - Não.")
        print("9 - Voltar.")
        opc = int(input())

        if opc == 1:
            getClienteTel()
        elif opc == 2:
            cadastrarCliente()
        elif opc == 9:
            menuPrincipal()
        else:
            print("Opção inválida")

#Função para achar o telefone do cliente no banco de dados
def getClienteTel():
    print("Digite o ddd do cliente mais o número fixo:")
    telefone = int(input())
    #irá consultar o db através do módulo pedido e retornará true se existir o cadastro

    if pedido.existeCadastroTel(telefone):
        #getIdByTelefone retorna o id do cliente relacionado ao telefone
        fazerPedido(getIdByTelefone(telefone))
    else:
        #Se não achar o cadastro do telefone, automáticamente chamará o menu para cadastro de Cliente
        print(f"Não foi encontrado registros no banco de dados com o telefone {telefone}")
        cadastrarCliente()

#Função para fazer o pedido das pizzas
def fazerPedido(clienteId):
    consultaUltimosPedidos(clienteId)

    opc = 0

    #Será adicionado as pizzas primeiramente em uma array do pedido, depois subida para o banco de dados
    while opc != 9:
        print("FAZER PEDIDO")
        print("1 - Adicionar Pizza")
        print("2 - Remover Pizza")
        print("3 - Finalizar pedido")
        print("9 - Cancelar e voltar para o menu principal")
        opc = int(input())

        if opc == 1:
            adicionarPizza(clienteId)
        elif opc == 2:
            removerPizza()
        elif opc == 3:
            pedido.finalizaPedido(clienteId)
        elif opc == 9:
            main()
        else:
            print("Opção inválida")

def adicionarPizza(clienteId):
    opc = 0

    print("SELECIONAR TIPO")
    print("1. Inteira")
    print("2. Meia")
    print("3. Voltar")
    opc = int(input())

    if opc == 1:
        tipo_pizza = 1
    elif opc == 2:
        tipo_pizza = 2
    elif opc == 3:
        fazerPedido(clienteId)
    else:
        print("Opção inválida")




#Função para cadastrar o cliente
def cadastrarCliente():
    print("CADASTRAR CLIENTE")
    nome = input("Digite o nome completo do cliente:")
    tel_fixo = input("Digite o telefone fixo com ddd:")
    tel_celular = input("Digite o telefone celular com ddd:")
    endereco = input("Digite o endereço de entrega:")
    numero = input("Digite o número do imóvel:")
    complemento = input("Digite um complemento, se tiver:")
    bairro = input("Digite o bairro:")
    cidade = input("Digite a cidade:")
    estado_uf = input("Digite o estado:")
    cep = input("Digite o CEP:")

    #checa se já existe o tel_fixo cadastrado no banco de dados
    if client.existeCadastroTel(tel_fixo):
        print("Já existe este telefone no banco de dados")
    else:
        #Se tudo ocorrer bem na inserção de dados, retornará true
        if cliente.finalizarCadastro(nome, tel_fixo, tel_celular, endereco, numero, complemento, bairro, cidade, estado_uf, cep):
            print("Cliente cadastrado com sucesso!")
        else:
            print("Houve algum erro ao cadastrar o cliente, tente novamente")







