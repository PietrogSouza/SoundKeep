from flask import Flask, redirect, render_template, request
import mysql.connector
from model.genero import recuperar_generos
from model.musica import adicionar_musica, recuperar_musicas, excluir_musica, ativar_musica


app = Flask(__name__)



@app.route("/")
@app.route("/home", methods=["GET"])
def pagina_principal(): 
    #recuperando as musicas
    musicas = recuperar_musicas(True)
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

@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("input_nome")
    cantor = request.form.get("input_cantor")
    duracao = request.form.get("input_duracao")
    imagem = request.form.get("input_imagem")
    genero = request.form.get("select_genero")
    if adicionar_musica(nome_musica, cantor, duracao, imagem, genero):
        return redirect("/admin")
    else:
        return "ERRO AO ADICIONAR MÚSICA"
    
@app.route("/musica/delete/<codigo>")
def deletar_musica(codigo):
    excluir_musica(codigo)
    return redirect("/admin")



@app.route("/musica/ativar/<codigo>/<status>")
def mudar_status_musica(codigo, status):
    ativar_musica(codigo, status)
    return redirect("/admin")




if __name__ == "__main__":
    app.run(debug=True)