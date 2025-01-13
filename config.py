# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'votre_cle_secrete'  # Remplacez par une clé secrète sécurisée
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'hopital.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
