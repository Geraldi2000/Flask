from flask import Flask, render_template, request, redirect
#Cria uma classe
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

lista = []

app = Flask(__name__)

imagens = ['static/images.jpeg', 'static/Pericles.jpeg', 'static/wisky-1.png', 'static/wisky-2.jpg', 'static/wisky-3.jpg']

@app.route('/')
def hello_world():  # put application's code here
    list = [
        {'Nome': 'Royal Salute', "Preco": "42000.00 R$", 'imagem': "static/images.jpg"},
        {'Nome': 'Kaue2', "Preco": "42.00 R$", 'imagem': "static/images.jpg"},
        {'Nome': 'Kaue3', "Preco": "42.00 R$", 'imagem': "static/images.jpg"},
        {'Nome': 'Kaue4', "Preco": "42.00 R$", 'imagem': "static/images.jpg"},
        {'Nome': 'Kaue5', "Preco": "42.00 R$", 'imagem': "static/images.jpg"}
    ]
    return render_template('index.html', nomeLoja='Puro malte', cat=lista)
    
#Criando uma nova rota
@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogos')

@app.route("/form")
def form():
    return render_template("index.html")

@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

app.run(debug=True)

