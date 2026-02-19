from database.conexao import conectar

def recuperar_generos():

    conexao, cursor = conectar()

    #executando a consulta do genero
    cursor.execute("SELECT nome, icone, cor FROM genero;")

    #recuperando os dados do genero
    generos = cursor.fetchall()

    #fechando a conexão
    conexao.close()

    return generos