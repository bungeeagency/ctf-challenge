# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SelectField, SubmitField, HiddenField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from models import Medecin


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')

class PatientForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    prenom = StringField('Prénom', validators=[DataRequired()])
    date_naissance = DateField('Date de naissance', format='%Y-%m-%d', validators=[DataRequired()])
    date_prise_en_charge = DateField('Date de prise en charge', format='%Y-%m-%d', validators=[DataRequired()])
    maladies_connues = TextAreaField('Maladies connues')
    medecin_id = SelectField('Médecin', coerce=int, validators=[DataRequired()])
    salle = StringField('Salle', validators=[DataRequired()])
    submit = SubmitField('Enregistrer')

class MedecinForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    prenom = StringField('Prénom', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired()])
    specialite = StringField('Spécialité', validators=[DataRequired()])
    submit = SubmitField('Enregistrer')
    
    

class TraitementForm(FlaskForm):
    nom = StringField('Nom du traitement', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Enregistrer')

class SymptomeForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    date_apparition = DateField('Date d\'apparition', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Enregistrer')

class DeleteForm(FlaskForm):
    patient_id = HiddenField('Patient ID', validators=[DataRequired()])
    submit = SubmitField('Supprimer')

# forms.py

from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField
from wtforms.validators import DataRequired

class ChangeStatusForm(FlaskForm):
    patient_id = HiddenField('Patient ID', validators=[DataRequired()])
    submit = SubmitField('Confirmer')

