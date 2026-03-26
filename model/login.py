from database.conexao import conectar

def verificar_usuario(login:str, senha:str) -> list:
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT usuario, senha FROM cadastro WHERE usuario = $s and senha = $s, 

                    """,
                    [login, senha]
                    )
    usuario = cursor.fetchone()
    if usuario is not None:
        try:
            return True
        except Exception as erro:
            print(erro)
            return False