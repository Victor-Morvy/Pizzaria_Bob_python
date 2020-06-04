'''
Data........: 2020-05-21
Projeto.....: Pizzaria
Arquivo.....: criaBanco.py
Descrição...: Este script executará querys que limpará o banco de dados se existir dados e criará um novo
Autor.......: Victor Hugo Martins de Oliveira
Observações.: 2020-05-21 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias:
'''


import os
import sqlite3

import connection

#Criacao de tabelas
def create_table():
    connection.cursor.executescript("\
    DROP TABLE IF EXISTS cliente;\
    \
    CREATE TABLE IF NOT EXISTS cliente (\
        cod_cliente INTEGER PRIMARY KEY AUTOINCREMENT\
                            NOT NULL,\
        tel_fixo    STRING  NOT NULL,\
        tel_cels    STRING,\
        nome_cli    STRING  NOT NULL,\
        endereco    STRING  NOT NULL,\
        nr_end      STRING  NOT NULL,\
        complemento STRING,\
        bairro      STRING  NOT NULL,\
        cidade      STRING  NOT NULL,\
        uf          STRING  NOT NULL,\
        cep         STRING  NOT NULL\
    );\
    \
    DROP TABLE IF EXISTS pizza;\
    CREATE TABLE IF NOT EXISTS pizza (\
            cod_pizza       INTEGER PRIMARY KEY AUTOINCREMENT\
                                    NOT NULL,\
            tipo_pizza      STRING  NOT NULL,\
            data_criacao    STRING  NOT NULL,\
            data_inativacao STRING,\
            nome_pizza      STRING  NOT NULL,\
            ingredientes    STRING  NOT NULL,\
            valor_custo     REAL    NOT NULL\
        );\
        \
    DROP TABLE IF EXISTS pedido;\
    CREATE TABLE IF NOT EXISTS pedido (\
            cod_ped   INTEGER PRIMARY KEY AUTOINCREMENT\
                              NOT NULL,\
            data_ped  STRING  NOT NULL,\
            hora_ped  STRING  NOT NULL,\
            cod_cli   INTEGER REFERENCES cliente (cod_cliente) \
                              NOT NULL,\
            total_ped REAL    NOT NULL\
        );\
        \
    DROP TABLE IF EXISTS itens_pedido;\
    CREATE TABLE IF NOT EXISTS itens_pedido (\
        cod_ped        INTEGER REFERENCES pedido (cod_ped) \
                               NOT NULL,\
        cod_item       INTEGER PRIMARY KEY AUTOINCREMENT\
                               NOT NULL,\
        cod_pizza_um   INTEGER REFERENCES pizza (cod_pizza) \
                               NOT NULL,\
        cod_pizza_dois INTEGER DEFAULT NULL,\
        quantidade     INTEGER NOT NULL,\
        valor_total    REAL    NOT NULL\
    );\
    ")

#create_table()

#Criação de pizzas
def create_pizzas():
    lista_pizzas = [
    (1, 'Salgada', '2020-05-30', 'Alho e Óleo', 'Alho frito picado, parmesão ralado e azeitonas', 22.9),
    (2, 'Salgada', '2020-05-30', 'Allici', 'Alicci importado, rodelas de tomate, parmesão e azeitonas', 28.9),
    (3, 'Salgada', '2020-05-30', 'Atum', 'Atum, cebola e azeitona', 22.9),
    (4, 'Salgada', '2020-05-30', 'Bacon', 'Bacon coberto com muzzarela e azeitonas', 26.9),
    (5, 'Salgada', '2020-05-30', 'Berinjela', 'Berinjela, cobertura com muzzarela, manjericão e parmesão', 23.9),
    (6, 'Salgada', '2020-05-30', 'Caipira', 'Frango desfiado, coberto com catupiry e milho verde e azeitonas', 26.9),
    (7, 'Salgada', '2020-05-30', 'Calabresa', 'Linguiça calabresa, cebola e azeitonas', 19.9),
    (8, 'Salgada', '2020-05-30', 'Cinco Queijos', 'Muzzarela, parmesão, catupiry, gorgonzola e provolone', 29.9),
    (9, 'Salgada', '2020-05-30', 'Escarola', 'Escarola refogada, muzzarela e azeitonas', 24.9),
    (10, 'Salgada', '2020-05-30', 'Executiva', 'Milho Verde, catupiry e azeitonas', 22.9),
    (11, 'Salgada', '2020-05-30', 'Peruana', 'Atum, cebola, muzzarela e azeitonas', 26.9),
    (12, 'Salgada', '2020-05-30', 'Palmito', 'Palmito com muzzarela e azeitonas', 26.9),
    (13, 'Doce', '2020-05-30', 'Banana', 'Banana fatiada com, cobertura com leite condensado e canela em pó', 21.9),
    (14, 'Doce', '2020-05-30', 'Brigadeiro', 'Chocolate, leite condensado e chocolate granulado', 23.9),
    (15, 'Doce', '2020-05-30', 'Prestígio', 'Chocolate coberta com côco', 23.9)]

    connection.cursor.executemany("INSERT INTO 'pizza' ('cod_pizza', 'tipo_pizza', 'data_criacao', 'nome_pizza', 'ingredientes', 'valor_custo') \
                        values (?, ?, ?, ?, ?, ?)", lista_pizzas)

    if connection.connection.commit():
        print('Dados inseridos com sucesso!')
    else:
        print('Erro ao inserir dados!')

#create_pizzas()