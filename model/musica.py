from database.conexao import conectar

def recuperar_musicas():
    #passo 1 e 2 feito
    conexao, cursor = conectar()

    #executando a consulta
    cursor.execute("""

            SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;
                    
                   """)
    
    #recuperando os dados
    musicas = cursor.fetchall()

    #fechando a conexão
    conexao.close()

    return musicas

def adicionar_musica(cantor:str, nome_musica:str, duracao:str, imagem:str, genero:str) -> bool:
    """
    Adiciona música ao banco de dados
    """

    try:
        #conectando a banco
        conexao, cursor = conectar()

        #executando o insert
        cursor.execute("""

                INSERT INTO musica 
                    (cantor, nome, duracao, url_imagem, nome_genero)
                VALUES 
                    (%s, %s, %s, %s, %s);

                    """,
                    [cantor, nome_musica, duracao, imagem, genero]
                    )
        
        #salvando os dados
        conexao.commit()
        #fechando a conexão
        conexao.close()

        return True
    except Exception as erro:
        print(erro)
        return False
    