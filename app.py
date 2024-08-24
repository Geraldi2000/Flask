from flask import Flask, render_template
from random import randint
ale = randint(0, 4)
for p in range(5):
    p = ale
app = Flask(__name__)
imagens = ['static/images.jpeg', 'static/Pericles.jpeg', 'static/wisky-1.png', 'static/wisky-2.jpg', 'static/wisky-3.jpg']
@app.route('/')
def hello_world():  # put application's code here
    list = [
        {'Nome': 'Geraldi', 'imagem': imagens[p]},
        {'Nome': 'Kaue2', 'imagem': imagens[p]},
        {'Nome': 'Kaue3', 'imagem': imagens[p]},
        {'Nome': 'Kaue4', 'imagem': imagens[p]},
        {'Nome': 'Kaue5', 'imagem': imagens[p]}
    ]
    return render_template('index.html', nomeLoja='Puro malte', cat=list)
app.run()
