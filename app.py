from flask import Flask, redirect, render_template, request, session
import mysql.connector
from model.genero import recuperar_generos
from model.musica import adicionar_musica, recuperar_musicas, excluir_musica, ativar_musica
from model.cadastro import adicionar_usuario
from model.login import verificar_usuario

app = Flask(__name__)

app.secret_key = "123590"


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
    if "usuario_logado" not in session:
        return redirect("/login")
    
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

@app.route("/cadastro", methods=["GET"])
def pagina_cadastro():
    return render_template("cadastro.html")


@app.route("/usuario/cadastro", methods=["POST"])
def cadastro_usuario():

    usuario = request.form.get("usuario_cadastro")
    senha = request.form.get("senha_cadastro")

    adicionar_usuario(usuario, senha)
    return redirect("/home")

@app.route("/login", methods=["GET"])
def pagina_login():
    if "usuario_logado" in session:
        return redirect("/admin")
    
    return render_template("login.html")

@app.route("/usuario/login", methods=["POST"])
def login_usuario():
    login = request.form.get("usuario")
    senha = request.form.get("senha")
    usuario = verificar_usuario(login, senha)

    if usuario != None:
        session["usuario_logado"] = usuario
        return redirect("/admin")
    else:
        return redirect("/login")

    




if __name__ == "__main__":
    app.run(debug=True)