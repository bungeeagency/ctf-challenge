# 🎯 CTF Challenges Collection

Suite de challenges CTF orientés apprentissage développée dans le cadre de mes études en cybersécurité. Chaque défi est conçu pour simuler des scénarios réels de sécurité.

## 🎮 Challenges Disponibles

### 🌐 Web
- **SQLi Hero**
  - Exploitation d'injections SQL sur une application bancaire
  - Difficulté: ⭐⭐
  - Flag: `CTF{...}`
  - Points: 200

- **XSS Master**
  - Cross-Site Scripting dans un réseau social
  - Difficulté: ⭐⭐⭐
  - Flag: `CTF{...}`
  - Points: 300

### 🔐 Crypto
- **Hash Cracker**
  - Analyse et crack de hashes custom
  - Difficulté: ⭐⭐
  - Flag: `CTF{...}`
  - Points: 250

### 🔍 Forensics
- **Packet Detective**
  - Investigation d'une intrusion réseau
  - Difficulté: ⭐⭐⭐⭐
  - Flag: `CTF{...}`
  - Points: 400

## 🛠 Technologies Utilisées

- **Web Challenges**
  ```python
  from flask import Flask, request
  app = Flask(__name__)
  # Vulnerable endpoints...
  ```

- **Scripts d'analyse**
  ```python
  import scapy.all as scapy
  # Network analysis...
  ```

## 🚀 Installation

```bash
# Cloner le repo
git clone https://github.com/locqmenhamdi/ctf-challenges

# Installer les dépendances
cd ctf-challenges
pip install -r requirements.txt

# Lancer les challenges
docker-compose up -d
```

## 📋 Prérequis

- Python 3.8+
- Docker & Docker Compose
- Navigateur web moderne
- Wireshark
- Burp Suite (recommandé)

## 🎯 Solutions

Les solutions sont disponibles dans le dossier `/solutions` mais sont chiffrées.
Pour les déchiffrer:
```bash
python decrypt_solution.py <challenge_name>
```

## 🏆 Hall of Fame

| Challenge | First Blood | Time |
|-----------|-------------|------|
| SQLi Hero | @h4ck3r | 45min |
| XSS Master | @securityguru | 1h20 |

## 💡 Conseils

- **Web**: Utilisez Burp Suite pour analyser les requêtes
- **Crypto**: Pensez aux encodages classiques
- **Forensics**: Examinez les métadonnées

## 🛡️ Disclaimer

Ces challenges sont conçus pour l'apprentissage. N'utilisez ces techniques que sur des systèmes autorisés.

## 🔄 Mise à jour

```bash
# Mettre à jour les challenges
git pull
docker-compose down
docker-compose up -d --build
```

## 📚 Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CTF Field Guide](https://trailofbits.github.io/ctf/)
- [PicoCTF Resources](https://picoctf.org/resources)

## 🐛 Bug Bounty

Si vous trouvez un bug (non intentionnel), ouvrez une issue !
Rewards:
- Bug critique: Mention spéciale
- Bug majeur: Point bonus

## 🔜 Roadmap

- [ ] Buffer Overflow Challenge
- [ ] JWT Attack Scenario
- [ ] Docker Escape Challenge
- [ ] API Security Tests

## 🤝 Contribution

1. Fork le projet
2. Créez votre branche (`git checkout -b challenge/nom`)
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## 📝 License

MIT License - voir [LICENSE.md](LICENSE.md)

---
Made with ☠️ by Locqmen HAMDI
BUT RT - Cybersecurity Track

```ascii
  ____  _____  _____    ____ _           _ _                           
 / ___|_   _||  ___|  / ___| |__   __ _| | | ___ _ __   __ _  ___   
| |     | |  | |_    | |   | '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \  
| |___  | |  |  _|   | |___| | | | (_| | | |  __/ | | | (_| |  __/  
 \____| |_|  |_|      \____|_| |_|\__,_|_|_|\___|_| |_|\__, |\___|  
                                                        |___/         
```
