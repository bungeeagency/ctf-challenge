# create_users.py

from app import app
from models import db, Medecin
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()
    # Création de l'administrateur
    admin = Medecin(
        nom='Admin',
        specialite='Administration',
        email='admin@mail.hopital-h6.net',
        mot_de_passe=generate_password_hash('tpRT9025'),
        role='admin',
        prenom='admin'
    )

    # Création du médecin
    medecin = Medecin(
        nom='Dupont',
        prenom='Martin',
        specialite='Généraliste',
        email='medecin@mail.hopital-h6.net',
        mot_de_passe=generate_password_hash('tpRT9025'),
        role='medecin'
    )

    # Ajout des utilisateurs à la session
    db.session.add(admin)
    db.session.add(medecin)

    # Sauvegarde dans la base de données
    try:
        db.session.commit()
        print("Les utilisateurs ont été créés avec succès.")
    except Exception as e:
        db.session.rollback()
        print(f"Une erreur est survenue : {e}")
