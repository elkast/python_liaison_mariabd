from flask import Flask, request, render_template
from modules import envoyer_donnees, lire_donnees

app = Flask(__name__)

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ORS'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/envoyer', methods=['POST'])
def envoyer():
    nom = request.form.get('nom')
    email = request.form.get('email')
    envoyer_donnees(nom, email, config)
    return f"Données envoyées : {nom}, {email}"

@app.route('/afficher')
def afficher():
    utilisateurs = lire_donnees(config)
    return render_template('afficher.html', utilisateurs=utilisateurs)

if __name__ == '__main__':
    app.run(debug=True)
