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