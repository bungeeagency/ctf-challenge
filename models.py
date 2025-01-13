# models.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Medecin(db.Model, UserMixin):
    __tablename__ = 'medecins'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)  # Nouveau champ ajouté
    specialite = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='medecin')
    patients = db.relationship('Patient', backref='medecin', lazy=True)

    def __repr__(self):
        return f'<Medecin {self.nom} {self.prenom}>'

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    date_naissance = db.Column(db.Date, nullable=False)
    date_prise_en_charge = db.Column(db.Date, nullable=False)
    maladies_connues = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    medecin_id = db.Column(db.Integer, db.ForeignKey('medecins.id'), nullable=False)
    traitements = db.relationship('Traitement', backref='patient', lazy=True, cascade='all, delete-orphan')
    symptomes = db.relationship('Symptome', backref='patient', lazy=True, cascade='all, delete-orphan')
    salle = db.Column(db.Text)

    def __repr__(self):
        return f'<Patient {self.nom} {self.prenom}>'

class Traitement(db.Model):
    __tablename__ = 'traitements'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)

    def __repr__(self):
        return f'<Traitement {self.nom}>'

class Symptome(db.Model):
    __tablename__ = 'symptomes'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    date_apparition = db.Column(db.Date, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)

    def __repr__(self):
        return f'<Symptome {self.id}>'
