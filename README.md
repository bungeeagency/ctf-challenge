# Restau' RT - Vulnerable Restaurant CTF

## 🎯 À propos du CTF
Restau' RT est une application web volontairement vulnérable développée comme un CTF (Capture The Flag) dans le cadre d'un projet étudiant. Ce projet simule un système de réservation de restaurant avec plusieurs vulnérabilités web à découvrir et à exploiter.

## 🚩 Challenges
L'application contient plusieurs vulnérabilités intentionnelles, notamment :
- Injection SQL dans le système d'authentification admin
- Vulnérabilités XSS dans le formulaire de réservation
- Failles de sécurité dans la gestion des réservations
- Autres vulnérabilités à découvrir...

**Note aux participants**: Le but est de trouver et d'exploiter ces vulnérabilités. Plusieurs flags sont cachés dans l'application !

## 💻 Fonctionnalités de l'Application

### Interface Client
- Système de réservation de tables
- Formulaire de contact
- Menu du restaurant
- Section testimonials

### Interface Admin
- Panneau d'administration (à compromettre 😉)
- Gestion des réservations
- Système d'authentification vulnérable

## 🛠 Technologies Utilisées
- **Backend**: Python Flask
- **Base de données**: SQLite
- **Frontend**: HTML, JavaScript
- **Styles**: Tailwind CSS
- **API**: Flask-RESTful
- **ORM**: SQLAlchemy

## ⚙️ Installation

1. Clonez le repository
```bash
git clone https://github.com/bungeeagency/ctf-challenge.git
cd restau-rt-ctf
```

2. Créez un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Sur Linux/Mac
# ou
venv\Scripts\activate  # Sur Windows
```

3. Installez les dépendances
```bash
pip install -r requirements.txt
```

4. Initialisez la base de données
```bash
flask db init
flask db migrate
flask db upgrade
```

5. Lancez l'application
```bash
python main.py
```

## 🎮 Comment jouer
1. Démarrez l'application en local
2. Explorez l'application à la recherche de vulnérabilités
3. Utilisez des outils comme Burp Suite, SQLMap, ou vos propres scripts
4. Trouvez et soumettez les flags cachés
5. Documentez vos trouvailles et vos méthodes d'exploitation

## 🎯 Objectifs pédagogiques
- Comprendre les vulnérabilités web courantes
- Apprendre à identifier les failles de sécurité
- Pratiquer l'exploitation de vulnérabilités dans un environnement contrôlé
- Développer des compétences en pentest web

## ⚠️ Avertissement
Cette application est INTENTIONNELLEMENT VULNÉRABLE. Ne déployez PAS cette application en production et ne l'hébergez pas sur un serveur public. Elle est conçue uniquement pour l'apprentissage de la sécurité web dans un environnement local contrôlé.


## 👥 Crédits
Projet développé dans le cadre d'un CTF étudiant par Locqmen HAMDI.
