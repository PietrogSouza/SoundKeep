from database.conexao import conectar

def adicionar_usuario(usuario:str, senha:str):
    """Adicionar um usuário para o bando de dados"""

    try:
        #conectando a banco
        conexao, cursor = conectar()

        #executando o insert
        cursor.execute("""
                        INSERT INTO cadastro
                            (usuario, senha)
                        VALUES
                            (%s, %s);
                       """,
                       [usuario, senha]
                       )
        
        #salvando os dados
        conexao.commit()
        #fechando a conexão
        conexao.close()

        return True
    except Exception as erro:
        print(erro)
        return False