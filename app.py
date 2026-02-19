from flask import Flask, render_template
import mysql.connector
from model.genero import recuperar_generos
from model.musica import recuperar_musicas

app = Flask(__name__)



@app.route("/")
@app.route("/home", methods=["GET"])
def pagina_principal(): 
    #recuperando as musicas
    musicas = recuperar_musicas()
    #recuperando os generos
    generos = recuperar_generos()
    #mostrando a página
    return render_template("principal.html", musicas = musicas, generos = generos)
    

@app.route("/admin")
def pagina_admin():
    #recuperando as musicas
    musicas = recuperar_musicas()
    #recuperando os generos
    generos = recuperar_generos()
    #mostrando a página
    return render_template("administracao.html", musicas = musicas, generos = generos)
    

if __name__ == "__main__":
    app.run(debug=True)