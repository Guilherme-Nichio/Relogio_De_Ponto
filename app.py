#Biblioteca para usar o banco de dados Sqlite 
import sqlite3

conn =sqlite3.connect('moratech.db')
cursor = conn.cursor()

def iniciaBd():
    cursor.execute("""
    CREATE TABLE  IF NOT EXISTS funcionarios(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf VARCHAR(11) NOT NULL,
            funcionario_id INTEGER NOT NULL
    );  
    """)
    
    print('tabela criada com sucesso')

def insereFuncionario(nome, cpf , id):
    p_nome = nome
    p_cpf = cpf
    p_id = id 
    cursor.execute("""
    INSERT INTO funcionarios (nome, cpf , funcionario_id)
    VALUES(?,?,?)
    """,(p_nome, p_cpf, p_id)) 
    conn.commit()
    print("Funcionario Inserido")
    


iniciaBd()
nome = input('Digite seu nome')
cpf = int(input('Digite seu cpf'))
id_funcionario = int(input('Digite seu id'))

insereFuncionario(nome,cpf,id_funcionario)



