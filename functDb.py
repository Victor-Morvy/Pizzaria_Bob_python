'''
Data........: 2020-05-21
Projeto.....: Pizzaria
Arquivo.....: functDb.py
Descrição...: Este script terá todas as funções para executar dentro da db
Autor.......: Victor Hugo Martins de Oliveira
Observações.: 2020-05-21 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-30 - [R01] Funções para utilizar no que foi passado no diagrama finalizados (alguns não testados)
Referencias:
Notas......: Não vai dar tempo de fazer documentação.... rs
'''

from datetime import datetime
import os
import sqlite3
import connection

now = datetime.now()

##VERIFICA SE NÚMERO EXISTE
#retorna 1 se existe e 0 se não existe no db
#parâmetro único ddd+num_fixo
def verificaNumero(numero):
    connection.cursor.execute(f"SELECT cod_cliente, tel_fixo FROM cliente WHERE tel_fixo = {numero}")
    qt = connection.cursor.fetchone()
    #print (f"resultado é {qt}")
    if qt is None:
        return 0
    else:
        return 1
#print(verificaNumero(1138765865))#existe
#print(verificaNumero(999))#não existe

##GET CLIENTE COD BY TELEFONE
#retorna o cod_cliente utilizando o telefone
def getCod_ClienteByTelefone(telefone):
    connection.cursor.execute(f"SELECT cod_cliente FROM cliente WHERE tel_fixo = '{telefone}'")
    retorno = connection.cursor.fetchone()
    return retorno[0]

#print(getClienteCodByTelefone(1138765865))

##CADASTRAR CLIENTE
#parâmetros: nome_cli, tel_fixo, tel_cel, endereco, nr_end, complemento, bairro, uf, cep
def cadastrarCliente(nome_cli, tel_fixo, tel_cel, endereco, nr_end, complemento, bairro, cidade, uf, cep):
    connection.cursor.execute(f"INSERT INTO cliente(nome_cli, tel_fixo, tel_cels, endereco, nr_end, complemento, bairro, cidade, uf, cep) \
                              values('{nome_cli}', '{tel_fixo}', '{tel_cel}', '{endereco}', '{nr_end}', '{complemento}', '{bairro}', '{cidade}', '{uf}', '{cep}')")
    connection.connection.commit()

#cadastrarCliente("Moises Araújo", "1939874851", "19984237482", "Rua das Andorinhas", "24", "Conjunto 23, ap 12", "Jd. Macieiras", "Vinhedo", "SP", "13280000")

##DADOS CLIENTE
#esta função retornará os dados de cadastro do cliente
def dadosCliente(cod_cliente):
    connection.cursor.execute(f"SELECT * FROM cliente WHERE cod_cliente = '{cod_cliente}'")
    return connection.cursor.fetchone()

#Exemplos
#print(dadosCliente(1)) #Retorna tupla com os dados
#print(dadosCliente(1)[0]) #Retorna o cod_cliente
#print(dadosCliente(1)[1]) #Retorna o telefone fixo
#print(dadosCliente(1)[2]) #Retorna o telefone celular
#print(dadosCliente(1)[3]) #Retorna o nome
#print(dadosCliente(1)[4]) #Retorna endereço
#print(dadosCliente(1)[5]) #Retorna o número do endereço
#print(dadosCliente(1)[6]) #Retorna o complemento
#print(dadosCliente(1)[7]) #Retorna o bairro
#print(dadosCliente(1)[8]) #Retorna a cidade
#print(dadosCliente(1)[9]) #Retorna a Unidade Federativa
#print(dadosCliente(1)[10]) #Retorna o CEP

##ATUALIZAR CADASTRO
#Atualiza o cadastro do cliente
def atualizarCadastro(cod_cliente, tel_cels, nome_cli, endereco, nr_end, complemento, bairro, cidade, uf, cep):
    connection.cursor.execute(f"UPDATE cliente set tel_cels = '{tel_cels}', nome_cli = '{nome_cli}', endereco = '{endereco}', \
                              nr_end = '{nr_end}', complemento = '{complemento}', bairro = '{bairro}', cidade = '{cidade}', uf = '{uf}', cep = '{cep}' \
                              WHERE cod_cliente = '{cod_cliente}'")
    connection.connection.commit()

##EXCLUIR CLIENTE
#parâmetro: cod_cliente
def excluirCliente(id):
    connection.cursor.execute(f"DELETE from cliente where id = '{id}'")
    connection.connection.commit()

##NOME DA PIZZA
#retorna o nome da pizza
#parâmetro: id da pizza
def nomePizza(id):
    connection.cursor.execute(f"SELECT nome_pizza FROM pizza WHERE cod_pizza = '{id}'")
    retorno = connection.cursor.fetchone()
    return retorno[0]

##INDICA SABORES
#retorna list com últimos 3 pedidos
#parâmetro: cod_cliente
def indicarPedido(cod_cliente):
    connection.cursor.execute(f'SELECT a.nome_pizza, b.nome_pizza \
    FROM itens_pedido c \
    INNER JOIN pedido d on (c.cod_ped = d.cod_ped)\
    INNER JOIN pizza a on (a.cod_pizza = c.cod_pizza_um)\
    LEFT JOIN pizza b on (b.cod_pizza = c.cod_pizza_dois)\
    WHERE d.cod_cli = {cod_cliente}\
    ORDER BY c.cod_item DESC\
    LIMIT 3')

    return connection.cursor.fetchall()

#EXEMPLO
#print(indicarPedido(1))
#print(indicarPedido(1)[0])
#print(indicarPedido(1)[2][1])
#print(indicarPedido(1)[2][0])

##A PIZZA É SALGADA OU DOCE?
#retorna o valor 'Salgado' ou 'Doce' fazendo a consulta no banco
#parâmetro: cod_pizza
def tipoPizza(id):
    connection.cursor.execute(f"SELECT tipo_pizza FROM pizza WHERE cod_pizza = '{id}'")
    retorno = connection.cursor.fetchone()
    return retorno[0]

##PIZZAS SALGADAS
#Retorna list com o codigo da pizza e o nome das pizzas salgadas
def pizzasSalgadas():
    connection.cursor.execute(f"SELECT cod_pizza, nome_pizza FROM pizza WHERE tipo_pizza = 'Salgada'")
    retorno = connection.cursor.fetchall()
    return retorno

#EXEMPLOS SALGADAS
#print(pizzasSalgadas()) #Retorna list com cod_pizza e nome_pizza das pizzas
#print(pizzasSalgadas()[1]) #Retorna uma tupla com o cod_pizza e nome_pizza da array 1
#print(pizzasSalgadas()[1][0]) #Retorna o cod_pizza da array 1
#print(pizzasSalgadas()[1][1]) #Retorna o nome_pizza da array 1

##PIZZAS DOCES
#Retorna list com o nome das pizzas doces
def pizzasDoces():
    connection.cursor.execute(f"SELECT cod_pizza, nome_pizza FROM pizza WHERE tipo_pizza = 'Doce'")
    retorno = connection.cursor.fetchall()
    return retorno

#EXEMPLOS DOCES
#print(pizzasDoces()) #Retorna list com cod_pizza e nome_pizza das pizzas
#print(pizzasDoces()[1]) #Retorna uma tupla com o cod_pizza e nome_pizza da array 1
#print(pizzasDoces()[1][0]) #Retorna o cod_pizza da array 1
#print(pizzasDoces()[1][1]) #Retorna o nome_pizza da array 1

##CRIA PEDIDO
#Cria o pedido para adicionar as pizzas no mesmo, usado para quando iniciar os pedidos dos clientes
def criaPedido(cod_cli):
    dataAgora = now.strftime("%Y-%m-%d")
    horaAgora = now.strftime("%H:%M:%S")

    connection.cursor.execute(f"INSERT INTO pedido(data_ped, hora_ped, cod_cli, total_ped)\
    VALUES ('{dataAgora}', '{horaAgora}', {cod_cli}, 0)")
    connection.connection.commit()

#criaPedido(1)

##ÚLTIMO PEDIDO ADICIONADO AO BANCO
#retorna o codigo do último resultado banco de dados, na tabela pedido (pedido onde serão armazenados os itens do pedido)
def ultimoPedido():
    connection.cursor.execute("SELECT MAX(cod_ped) FROM pedido")
    retorno = connection.cursor.fetchone()
    return retorno[0]

#print(ultimoPedido())

##VALOR PIZZA
#retorna o valor da pizza
def valorPizza(id_pizza):
    connection.cursor.execute(f"SELECT valor_custo from pizza WHERE cod_pizza = '{id_pizza}'")
    retorno = connection.cursor.fetchone()
    return retorno[0]

#print(valorPizza(2))

##VALOR PIZZA MAIS CARA
#retorna o valor da pizza mais cara, se for selecionado pizza 2 sabores
def valorPizzaMaisCara(pizza_um, pizza_dois):
    if valorPizza(pizza_um) > valorPizza(pizza_dois):
        return valorPizza(pizza_um)
    else:
        return valorPizza(pizza_dois)

#print(valorPizzaMaisCara(2, 4))


##ADICIONAR PIZZA NO PEDIDO
#retorna 0 se deu errado, retorna 1 se deu certo
#adiciona pizza no pedido criado
#Parâmetro tamanho: p, m, g, gg
def addPizza(cod_pedido, tamanho, quantidade, sabor_um, sabor_dois = None):
    precoFinal = 0
    if sabor_dois is not None:
        if tipoPizza(sabor_um) == "Doce" or tipoPizza(sabor_dois) == "Doce":
            print("!!!ERRO!!! Não é possível adicionar pizzas doces em pizzas de dois sabores.")
            return 0
        elif sabor_um == sabor_dois:
            print("!!!ERRO!!! Não é possível adicionar meio sabor da mesma pizza.")
            return 0
        else:
            precoFinal = valorPizzaMaisCara(sabor_um, sabor_dois)
    else:
        precoFinal = valorPizza(sabor_um)

    if tamanho == "m":
        precoFinal *= 1.15 * quantidade
    elif tamanho == "g":
        precoFinal *= 1.25 * quantidade
    elif tamanho == "gg":
        precoFinal *= 1.35 * quantidade
    else:
        print("!!!ERRO!!! O parâmetro tamanho aceita apenas os valores 'm', 'g', 'gg'")
        return 0

    connection.cursor.execute(f"INSERT INTO itens_pedido(cod_ped, cod_pizza_um, cod_pizza_dois, quantidade, valor_total) \
    VALUES ('{cod_pedido}', '{sabor_um}', '{sabor_dois}', '{quantidade}', '{precoFinal:.2f}')")
    connection.connection.commit()
    return 1

#EXEMPLOS
#addPizza(ultimoPedido(), "m", 2, 2, 12) #pizza dois sabores salgados
#addPizza(ultimoPedido(), "m", 1, 14, 12) #pizza meia doce, meia salgada (retorna erro)
#addPizza(ultimoPedido(), "g", 2, 8) #pizza apenas um sabor salgado
#addPizza(ultimoPedido(), "m", 2, 6, 15) #pizza meia salgada, meia doce (retorna erro)
#addPizza(ultimoPedido(), "gg", 1, 13) #pizza um sabor doce
#addPizza(ultimoPedido(), "2", 1, 13) #parâmetro de tamanho errado (retorna erro)

##VALOR TOTAL DO PEDIDO
#Retorna o valor total de um pedido pela id do pedido
def valorTotalPedido(cod_pedido):
    connection.cursor.execute(f"SELECT SUM(valor_total) FROM itens_pedido WHERE cod_ped = '{cod_pedido}'")
    retorno = connection.cursor.fetchone()
    return retorno[0]

#print(valorTotalPedido(6))

##RETORNA ITENS PEDIDO
#Retorna em uma tupla os dados do pedido
#parâmetros 0 - sabor_1 | 1 - sabor_2 | 2 - ingredientes_pizza_1 | 3 - ingredientes_pizza_2 | 4 - quantidade | 5 - valor total
#obs: retorna None caso não seja pizza de dois sabores
def retornaItensPedido(cod_pedido):
    connection.cursor.execute(f"SELECT pi.nome_pizza as pizza_a, po.nome_pizza as pizza_b, pi.ingredientes as ingredientes_a, po.ingredientes as ingredientes_b, pe.quantidade, pe.valor_total\
    FROM itens_pedido pe\
    INNER JOIN pizza pi on (pe.cod_pizza_um = pi.cod_pizza)\
    LEFT JOIN pizza po on (pe.cod_pizza_dois = po.cod_pizza)\
    WHERE pe.cod_ped = '{cod_pedido}'")

    return connection.cursor.fetchall()

#EXEMPLOS
#print(retornaItensPedido(6)) #Retorna list de todos os pedidos
#print(retornaItensPedido(6)[1]) #Retorna a tupla do pedido de íncice 0
#print(retornaItensPedido(6)[1][0]) #Retorna o sabor 1 da pizza
#print(retornaItensPedido(6)[1][1]) #Retorna o sabor 2 da pizza
#print(retornaItensPedido(6)[1][2]) #Retorna os ingredientes do sabor 1 da pizza
#print(retornaItensPedido(6)[1][3]) #Retorna os ingredientes do sabor 2 da pizza
#print(retornaItensPedido(6)[1][4]) #Retorna a quantidade de pizzas
#print(retornaItensPedido(6)[1][5]) #Retorna o valor total quantidade*preços

##EXCLUIR PEDIDO
#exclui da tabela todos os itens_pedido que tenham o mesmo cod_pedido e depois exclui o pedido com o cod_pedido
def excluirPedido(cod_pedido):
    connection.cursor.execute(f"DELETE FROM itens_pedido WHERE cod_ped = '{cod_pedido}'")
    connection.connection.commit()

    connection.cursor.execute(f"DELETE FROM pedido WHERE cod_ped = '{cod_pedido}'")
    connection.connection.commit()

##FINALIZA PEDIDO
#esta função irá setar o valor final do pedido no codigo do pedido, apenas para futuras consultas
#pode ser utilizado para futura implementação, quando o valor maior que 0, está definido como pedido fechado.
def finalizaPedido(cod_pedido):
    connection.cursor.execute(f"UPDATE pedido SET total_pedido = '{valorTotalPedido(cod_pedido)}' WHERE '{cod_pedido}'")
    connection.connection.commit()

##TROCO
#esta função calcula automáticamente o troco, retornará -1 se houver algum erro
def troco(cod_pedido, valor):
    valorPedido = valorTotalPedido(cod_pedido)
    if valorPedido > valor:
        print("!!!ERRO!!! O cliente deverá dar um valor maior ou igual o valor do pedido")
        return -1
    else:
        return (valorPedido - valor)*(-1)

#EXEMPLOS
#print(f"O troco será R$ {troco(6, 350):.2f}")
#print(f"O troco será R$ {troco(6, 200):.2f}")


##Finaliza a conexão com o banco de dados
connection.connection.close()