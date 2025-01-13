# app.py

import os
from flask import Flask
from models import db
from config import Config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Nom de la vue pour la page de connexion
login_manager.login_message = 'Veuillez vous connecter pour accéder à cette page.'
login_manager.login_message_category = 'info'

db.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return Medecin.query.get(int(user_id))
# Importer les modèles après l'initialisation de db
from models import *

# Importer les routes
from routes import *

def init_db():
    with app.app_context():
        db.create_all()
        # Ajouter des données initiales
        medecin1 = Medecin(nom='Dr. Dupont', specialite='Généraliste')
        medecin2 = Medecin(nom='Dr. Martin', specialite='Cardiologue')
        db.session.add(medecin1)
        db.session.add(medecin2)
        db.session.commit()
        print("Base de données initialisée avec les données de départ.")

if __name__ == '__main__':
    db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')
    if not os.path.exists(db_path):
        init_db()
    app.run(debug=True)
