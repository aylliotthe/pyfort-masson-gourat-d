# Fort Boyard

## 1. Présentation Générale

### Titre du Projet
Fort Boyard

### Contributeurs
- **Eliot Masson**
- **Lorenzo Gourat**

### Description
Ce projet est une simulation d'un jeu inspiré de l'émission télévisée Fort Boyard. Le joueur forme une équipe, participe à diverses épreuves pour récolter des clés, et accède à une épreuve finale pour remporter le trésor.

### Fonctionnalités Principales
- Formation d'équipe personnalisée.
- Participation à des épreuves de différentes catégories : épreuves logiques, mathématiques, et de hasard.
- Gestion de la salle du trésor, avec une mécanique de devinettes basées sur des indices.

### Technologies Utilisées
- **Langage de Programmation** : Python 3.10+
- **Bibliothèques** : Random, JSON

### Installation
#### Clôner le dépôt
```bash
git clone https://github.com/votre-repo/fort-boyard.git
cd fort-boyard
```
#### Configuration de l'environnement
- Assurez-vous que Python 3.10+ est installé sur votre système.
- Installez les dépendances si nécessaire (aucune bibliothèque externe obligatoire pour ce projet).

### Utilisation
#### Exécution de l'application
```bash
python main.py
```
#### Exemple d'utilisation
1. Lancez le script principal.
2. Formez une équipe de joueurs.
3. Choisissez et participez à différentes épreuves.
4. Accédez à la salle du trésor et tentez de remporter le trésor.

---

## 2. Documentation Technique

### Algorithme du Jeu
1. Initialiser le jeu avec une introduction et la création de l'équipe.
2. Définir les épreuves disponibles.
3. Boucle principale :
   - Choisir une épreuve et un joueur.
   - Exécuter l’épreuve et déterminer si une clé est gagnée.
4. Une fois trois clés obtenues, accéder à l’épreuve finale dans la salle du trésor.
5. Fin du jeu : afficher les résultats.

### Détails des Fonctions Implémentées
#### Fichier : **main.py**
- `jeu()` : Gère le flux principal du jeu.

#### Fichier : **epreuves_logiques.py**
- `jeu_bataille_navale()` : Simule un jeu de bataille navale simplifié.
- `affiche_grille(grille, message)` : Affiche une grille avec un message.
- `demander_position()` : Gère la saisie des positions.

#### Fichier : **epreuves_hasard.py**
- `bonneteau()` : Jeu de bonneteau où le joueur doit trouver une clé cachée.
- `jeu_lance_des()` : Jeu de lancer de dés pour obtenir un six.
- `epreuve_hasard()` : Sélectionne aléatoirement une épreuve de hasard.

#### Fichier : **epreuves_mathematiques.py**
- `epreuve_math()` : Gère une épreuve basée sur des questions mathématiques.

#### Fichier : **enigme_pere_fouras.py**
- `enigme_pere_fouras()` : Propose une énigme à résoudre.

#### Fichier : **epreuve_finale.py**
- `salle_De_tresor()` : Gère l’épreuve finale de la salle du trésor.

### Gestion des Entrées et Erreurs
- Utilisation de `saisi_secur()` pour vérifier les entrées utilisateur.
- Validation des intervalles et des types de données (e.g., positions sur une grille).
- Gestion des cas de saisie incorrecte avec des messages d’erreur explicites.

### Bugs Connus
- Aucun bug majeur identifié à ce jour.

---

## 3. Journal de Bord

### Chronologie du Projet
- **Avant les vacances** : travaille commun sur fonctions_utiles.py; epreuves_mathematiques.py; epreuves_logiques.py; et enigme_pere_fouras.py
- **Vacances de Noël** : travaille individuel sur epreuves_hasard.py; epreuve_finale.py et main.py

### Répartition des Tâches
- Eliot Masson : travaile en commun sur l'ensemble et travaille individuel sur epreuve_finale.py et main.py
- Lorenzo Gourat : travaile en commun sur l'ensemble et travaille individuel sur epreuves_hasard.py

---

## 4. Tests et Validation

### Stratégies de Test
- Tests unitaires pour chaque épreuve (validation des résultats attendus).
- Tests d’intégration pour le flux complet du jeu.

