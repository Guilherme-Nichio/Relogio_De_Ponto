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
    
    CREATE TABLE IF NOT EXISTS adminstradores(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
        cpf INTEGER NOT NULL
        email VARCHAR(115) NOT NULL
        senha VARCHAR(115) NOT NULL
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
    
def leituraBanco():
    cursor.execute("""
    SELECT * FROM funcionarios;
    """)
    
    for linha in cursor.fetchall():
        print(linha)


def alterarBanco(novo_nome, id):
    cursor.execute("""
    UPDATE funcionarios
    SET nome = ? 
    WHERE funcionario_id = ? 
    """ , (novo_nome, id))
    conn.commit()
    print('banco de dados atualizado')


iniciaBd()

tipoUser = int(input("Que tipo de usuario você deseja ser? \n1.Administrador 2.Funcionario  \n Escolha: "))

if tipoUser == 1:
    print("Voce esta como adm")
else:
    print("voce esta como funcionario")



