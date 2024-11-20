#Biblioteca para usar o banco de dados Sqlite 
import sqlite3
import datetime 
from datetime import datetime
import pandas as pd
import numpy as np

conn =sqlite3.connect('moratech.db')
cursor = conn.cursor()

def iniciaBd():
    cursor.execute("""
    CREATE TABLE  IF NOT EXISTS funcionarios(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf VARCHAR(11) NOT NULL,
            funcionario_id INTEGER NOT NULL,
            quantidade INTEGER 
    );  
    
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS administradores(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf INTEGER NOT NULL,
        email VARCHAR(115) NOT NULL,
        senha VARCHAR(115) NOT NULL
        
        );
    
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ponto(
        funcionario_id INTEGER NOT NULL,
        tipo_ponto VARCHAR(50),
        horario VARCHAR(115)
        
        );
    
    """)


def cadastraAdm(nome, cpf , email , senha):
    c_nome = nome
    c_cpf = cpf
    c_email = email
    c_senha= senha
    cursor.execute("""
    INSERT INTO administradores(nome, cpf, email , senha)
    VALUES(?,?,?,?)               
    """, (c_nome, c_cpf, c_email, c_senha))
    conn.commit()
#cadastraAdm ('guiherme', 342342342, 'guilherme@gmail.com ', 1234)
  
def insereFuncionario(nome, cpf , id):
    p_nome = nome
    p_cpf = cpf
    p_id = id 
    cursor.execute("""
    INSERT INTO funcionarios (nome, cpf , funcionario_id,quantidade)
    VALUES(?,?,?,?)
    """,(p_nome, p_cpf, p_id,0)) 
    conn.commit()
    print("Funcionario Inserido")
#insereFuncionario('funcionario1',111111111, 1111)
#insereFuncionario('funcionario2',222222222, 2222)
#insereFuncionario('funcionario3',333333333, 3333)
def verificarLoginAdm(user):
    c_user = user.strip()
    cursor.execute("""
    SELECT email FROM administradores;
    """)
    
    resultado = cursor.fetchone()
    if resultado :
        userBd = resultado[0].strip() # o metodo .strip() remove espaços vazios na frente e atras da entrada
    else:
        userBd = None     
    if userBd == None:
        userPadrao = "adm"
    else:
        userPadrao = userBd
    while(c_user !=  userPadrao ):
        print("Usuario Incorreto, digite o user: ")
        c_user = input().strip()   
    print("login Efetuado")

    

def leituraBanco():
    cursor.execute("""
    SELECT * FROM funcionarios;
    """)
    
    for linha in cursor.fetchall():
        print(linha)

    
def alterarBanco(id):
    cursor.execute("""
    UPDATE funcionarios
    SET quantidade = ? 
    WHERE funcionario_id = ? 
    """ , (1, id))
    conn.commit()
    print('banco de dados atualizado')
    
    
def verificaFuncionario(funcionario):
    cursor.execute("""
    SELECT funcionario_id FROM funcionarios WHERE funcionario_id = ?                           
    """, (funcionario,))
    
    resultado = cursor.fetchone()
    if resultado:
       return 1
    else:
       return 0

        
def registrarPonto(funcionario):
    if verificaFuncionario(funcionario) == 1:
        cursor.execute("""
        SELECT quantidade FROM funcionarios WHERE funcionario_id =?
        """, (funcionario,))
        
        resultado = cursor.fetchone()
        if resultado :
            quantidade =  resultado[0]
            
        if quantidade == 0 :
            tipo_ponto = 'ENTRADA'
        if quantidade == 1:
            tipo_ponto = 'SAIDA_ALMOÇO'
        if quantidade == 2: 
            tipo_ponto = "VOLTA_ALMOÇO"
        if quantidade == 3: 
            tipo_ponto = 'SAIDA' 
        data = datetime.today()
        cursor.execute("""
        INSERT INTO ponto (funcionario_id, tipo_ponto, horario)
        VALUES(?,?,?)
        """, (funcionario, tipo_ponto , data ))
        quantidade = quantidade + 1
        if quantidade == 4:
            quantidade = 0
        print(quantidade)
        
        cursor.execute("""
        UPDATE funcionarios 
        set quantidade = ?
        WHERE funcionario_id =?
        """, (quantidade ,funcionario))
        
        conn.commit()
    else: 
        print('funcionario nao existe')
def exportarExcel(banco_dados, nomeArquivo):
    conn =sqlite3.connect(banco_dados)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT funcionario_id FROM ponto;")
    funcionarios = [row[0] for row in cursor.fetchall()]
    
    with pd.ExcelWriter(nomeArquivo, engine='openpyxl') as writer:
        for funcionario_id in funcionarios:
            
            query = f"SELECT * FROM ponto WHERE funcionario_id = {funcionario_id};"
            df = pd.read_sql_query(query, conn)
            
            
            sheet_name = f"Funcionario_{funcionario_id}"
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    conn.close()
    print('dados exportados')
    
exportarExcel("moratech.db","tabelasDePonto.xlsx")    
    
iniciaBd()
registrarPonto(1131)






#print("| Bem vindo ao sistema de gerenciamento de ponto | \n")
#print("entrar no painel de adminstrador digite o user: ")
#user = input()
#verificarLoginAdm(user)

#tipoUser = int(input("Que tipo de usuario você deseja ser? \n1.Administrador 2.Funcionario  \n Escolha: "))

#if tipoUser == 1:
#    print("Voce esta como adm")
#else:
#    print("voce esta como funcionario")



