import database 


# Verificar se Usuário existe
def existe_usuario(id):
    existe: False
    try:
        conect = database.criar_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM usuario WHERE id = '{id}'" 
        cursor.execute()
        lista_usuario = cursor.fetchall()
        if len(lista_usuario) == 0:
            existe = False
        else:
            existe = True
    except Exception as ex:
        print(f'Erro na verificacao do usuario: {ex}')

    return existe
# fim: existe_usuario

def lista_usuarios():
    usuarios = list()
    try:
        conect = database.criar_db()
        cursor = conect.cursor() 
        sql = 'SELECT * FROM usuario ORDER BY nome'
        cursor.execute(sql)
        lista_usuario = cursor.fetchall()
        # Tratar dados para uma estrutura JSON
        for usuario in lista_usuario:
            usuarios.append(
                {
                  'id': usuario[0],
                  'nome': usuario[1],
                  'email': usuario[2],
                  'senha': usuario[3],
                  'login': usuario[4]
                }
            )
    except Exception as ex:
        print(f'Erro: Listar usuario: {ex}')
    
    return usuarios
# Fim: lista_usuarios() 

def obter_usuario_id(id):
    usuarios = list()
    try:
        conect = database.criar_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM usuario WHERE id = '{id}'" 
        cursor.execute(sql)
        lista_usuario = cursor.fetchall()
        # Tratar dados para uma estrutura JSON
        for usuario in lista_usuario:
            usuarios.append(
                {
                  'id': usuario[0],
                  'nome': usuario[1],
                  'email': usuario[2],
                  'senha': usuario[3],
                  'login': usuario[4]
                }
            )
    except Exception as ex:
        print(f'Erro: obter usuario pelo id: {ex}')

    return usuarios
# Fim: obter_usuario_id(id)

def criar_usuario(usuario):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"INSERT INTO usuario(nome, email, senha, login) VALUES('{usuario['nome']}','{usuario['email']}', '{usuario['senha']}', '{usuario['login']}')"
        cursor.execute(sql)
        last_id = cursor.lastrowid
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusão: {ex}')

    return last_id 
# Fim: criar_usuario(usuario)


def atualizar_usuario(usuario):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"UPDATE usuario SET nome = '{usuario['nome']}', email = '{usuario['email']}', senha = '{usuario['senha']}', login = '{usuario['login ']}' WHERE id = '{usuario['id']}' "
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na atualização: {ex}')

# Fim: criar_usuario(usuario)

def deletar_usuario(id):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM usuario WHERE id = {id}'
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na deleção do usuario: {ex}')
# Fim: atualizar_usuario




    