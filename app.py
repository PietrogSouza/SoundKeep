from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)



@app.route("/")
@app.route("/home", methods=["GET"])
def pagina_principal():


    #conectando no banco de dados
    conexao = mysql.connector.connect(
        host= "localhost",
        port= "3306",
        user= "root",
        password= "root",
        database= "soundkeep"
    )

    cursor = conexao.cursor(dictionary=True)

    #executando a consulta
    cursor.execute("""

            SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;
                    
                   """)
    
    #recuperando os dados
    musicas = cursor.fetchall()

    #fechando a conexão
    conexao.close()

    return render_template("principal.html", musicas = musicas)
    






if __name__ == "__main__":
    app.run(debug=True)