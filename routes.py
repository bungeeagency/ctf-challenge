# routes.py

from app import app
from flask import render_template, redirect, url_for, flash, request
from models import db, Patient, Medecin, Traitement, Symptome
from forms import (
    PatientForm,
    MedecinForm,
    TraitementForm,
    SymptomeForm,
    DeleteForm,
    ChangeStatusForm,
    LoginForm# Importation du formulaire
)
from decorators import roles_required

# routes.py
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        medecin = Medecin.query.filter_by(email=form.email.data).first()
        if medecin and check_password_hash(medecin.mot_de_passe, form.mot_de_passe.data):
            login_user(medecin)
            flash('Connexion réussie.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Email ou mot de passe incorrect.', 'error')
    return render_template('login.html', form=form)

@app.route('/')
@login_required
def index():
    patients = Patient.query.filter_by(is_active=True).all()
    return render_template('index.html', patients=patients)

@app.route('/patient/add', methods=['GET', 'POST'])
@login_required
@roles_required('medecin', 'admin')
def add_patient():
    form = PatientForm()
    form.medecin_id.choices = [(medecin.id, medecin.nom) for medecin in Medecin.query.all()]
    if form.validate_on_submit():
        patient = Patient(
            nom=form.nom.data,
            prenom=form.prenom.data,
            date_naissance=form.date_naissance.data,
            date_prise_en_charge=form.date_prise_en_charge.data,
            maladies_connues=form.maladies_connues.data,
            medecin_id=form.medecin_id.data,
            salle=form.salle.data
        )
        db.session.add(patient)
        db.session.commit()
        flash('Patient ajouté avec succès!', 'success')
        return redirect(url_for('index'))
    return render_template('add_patient.html', form=form)

@app.route('/patient/<int:id>')
@login_required
@roles_required('medecin', 'admin')
def patient_detail(id):
    patient = Patient.query.get_or_404(id)
    delete_form = DeleteForm()
    change_status_form = ChangeStatusForm()  # Création du formulaire
    return render_template(
        'patient_detail.html',
        patient=patient,
        delete_form=delete_form,
        change_status_form=change_status_form  # Passage au template
    )

# routes.py

@app.route('/patient/<int:id>/deactivate', methods=['POST'])
@login_required
@roles_required('medecin', 'admin')
def deactivate_patient(id):
    patient = Patient.query.get_or_404(id)
    form = ChangeStatusForm()
    if form.validate_on_submit():
        if int(form.patient_id.data) != patient.id:
            flash('Requête invalide.', 'error')
            return redirect(url_for('patient_detail', id=id))
        patient.is_active = False
        try:
            db.session.commit()
            flash('Le patient a été marqué comme inactif.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Une erreur est survenue lors de la mise à jour du statut du patient.', 'error')
            return redirect(url_for('patient_detail', id=id))
    else:
        flash('Requête non valide.', 'error')
        return redirect(url_for('patient_detail', id=id))



@app.route('/patient/<int:id>/activate', methods=['POST'])
@login_required
@roles_required('medecin', 'admin')
def activate_patient(id):
    patient = Patient.query.get_or_404(id)
    form = ChangeStatusForm()
    if form.validate_on_submit():
        if form.patient_id.data != str(patient.id):
            flash('Requête invalide.', 'error')
            return redirect(url_for('patient_detail', id=id))
        patient.is_active = True
        try:
            db.session.commit()
            flash('Le patient a été réactivé.', 'success')
            return redirect(url_for('patient_detail', id=id))
        except Exception as e:
            db.session.rollback()
            flash('Une erreur est survenue lors de la mise à jour du statut du patient.', 'error')
            return redirect(url_for('patient_detail', id=id))
    else:
        flash('Requête non valide.', 'error')
        return redirect(url_for('patient_detail', id=id))

# Les autres routes restent inchangées
@app.route('/medecin/add', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def add_medecin():
    form = MedecinForm()
    if form.validate_on_submit():
        mot_de_passe_hache = generate_password_hash(form.mot_de_passe.data)
        medecin = Medecin(
            nom=form.nom.data,
            prenom=form.prenom.data,  # Nouveau champ
            specialite=form.specialite.data,
            email=form.email.data,
            mot_de_passe=mot_de_passe_hache,
            role='medecin'  # Vous pouvez permettre la sélection du rôle si nécessaire
        )
        db.session.add(medecin)
        db.session.commit()
        flash('Médecin ajouté avec succès!', 'success')
        return redirect(url_for('index'))
    return render_template('add_medecin.html', form=form)

@app.route('/patients/inactive')
@login_required
@roles_required('medecin', 'admin')
def inactive_patients():
    patients = Patient.query.filter_by(is_active=False).all()
    return render_template('inactive_patients.html', patients=patients)

@app.route('/patient/<int:patient_id>/traitement/add', methods=['GET', 'POST'])
@login_required
@roles_required('medecin', 'admin')
def add_traitement(patient_id):
    form = TraitementForm()
    if form.validate_on_submit():
        traitement = Traitement(
            nom=form.nom.data,
            description=form.description.data,
            patient_id=patient_id
        )
        db.session.add(traitement)
        db.session.commit()
        flash('Traitement ajouté avec succès!', 'success')
        return redirect(url_for('patient_detail', id=patient_id))
    return render_template('add_traitement.html', form=form, patient_id=patient_id)

@app.route('/patient/<int:patient_id>/symptome/add', methods=['GET', 'POST'])
@login_required
@roles_required('medecin', 'admin')
def add_symptome(patient_id):
    form = SymptomeForm()
    if form.validate_on_submit():
        symptome = Symptome(
            description=form.description.data,
            date_apparition=form.date_apparition.data,
            patient_id=patient_id
        )
        db.session.add(symptome)
        db.session.commit()
        flash('Symptôme ajouté avec succès!', 'success')
        return redirect(url_for('patient_detail', id=patient_id))
    return render_template('add_symptome.html', form=form, patient_id=patient_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Vous avez été déconnecté.', 'success')
    return redirect(url_for('login'))
