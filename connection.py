'''
Data........: 2020-05-15
Projeto.....: Pizzaria
Arquivo.....: connection.py
Descrição...: Este módulo serve para conexões básicas ao banco de dados
Autor.......: Victor Hugo Martins de Oliveira
Observações.: 2020-05-15 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias:
'''

import os
import sqlite3

#define o local da db
fileDB = "V:\\PycharmProjects\Pizzaria\db\pizzaria.sqlite"

#verifica se o arquivo de banco de dados existe
print("Verificando se banco de dados existe...")
if not os.path.exists(fileDB):
    print(f"O arquivo {fileDB} não existe.")
    exit(-1)
else:
    pass

#criando a base de dados
connection = sqlite3.connect(fileDB)

#Get a cursor object
cursor = connection.cursor()