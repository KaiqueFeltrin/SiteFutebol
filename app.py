from flask import Flask, render_template, request,redirect
lista = []

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('Home.html', Titulo = 'Bem Vindo ao site de Futebol')

@app.route('/futebol')
def futebol():
    return render_template('Futebol.html', Banana = 'Melhores Times')

@app.route('/sobre')
def sobre():
    return render_template('Sobre.html', Banana2 = 'Sobre o nosso site')

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = 'Cadastro de Times')

@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', Titulo = 'Times cadastrados', lista=lista)

@app.route('/criar', methods=['POST'])
def criar():
    numero=request.form['numero']
    nome = request.form['nome']
    datanas = request.form['datanas']
    titulos = request.form['titulos']
    gols = request.form['gols']
    futebol = [numero,nome, datanas, titulos, gols]
    lista.append(futebol)
    return redirect('/exibir')


if __name__ == '__main__':
    app.run()
