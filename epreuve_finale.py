"""
Module : epreuve_final

Ce module implémente la simulation de l'épreuve finale de la salle du trésor.
Les joueurs doivent deviner un mot-code à l'aide d'indices, avec un nombre limité de tentatives.

Auteurs : [Eliot Masson]
"""
from json import load

from random import choice

from fonctions_utiles import saisi_secur


def salle_De_tresor() -> None:
    """
    **Salle_De_tresor**

    Simule l'épreuve finale de la salle du trésor dans Fort Boyard.
    Les joueurs doivent deviner un mot-code en se basant sur une série d'indices.
    Trois essais sont donnés, avec un indice supplémentaire révélé après chaque réponse incorrecte.

    :return: None
    """
    # Chargement des données des indices et mots-codes depuis un fichier JSON.
    with open('data/indicesSalle.json', 'r', encoding= 'utf-8') as f:
        jeu_tv = load(f)

    # Sélection aléatoire d'une année et d'une émission dans les données.
    annee = choice([i for i in jeu_tv["Fort Boyard"]])
    emission = choice([y for y in jeu_tv["Fort Boyard"][annee]])

    # Récupération des indices et du mot-code associés à l'émission choisie.
    indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]
    mot_code = jeu_tv["Fort Boyard"][annee][emission]["MOT-CODE"]

    # Instructions de l'épreuve pour le joueur.
    print("Bienvenue dans la salle de tresor !")
    print("Vous devez trouver un mot clé à l'aide d'indices.")
    print("Voici les trois premiers indices : ")
    for i in range(3):
        print(indices[i])
    essais_restants = 3
    reponse_correcte = False

    # Boucle pour gérer les tentatives du joueur.
    while essais_restants > 0 and not reponse_correcte :
        # Saisie sécurisée de la réponse du joueur.
        rep = saisi_secur("Veuillez entrer votre réponse : ", check=str).upper()

        # Vérification de la réponse.
        if rep == mot_code :
            reponse_correcte = True
        else :
            essais_restants -= 1
            if essais_restants > 0:
                print(f"Il vous reste {essais_restants} essais.")
                print(f"L'indice suivant est : {indices[-essais_restants]}")
            else:
                print(f"Le mot code était {mot_code}.")

    # Résultat final de l'épreuve.
    if reponse_correcte :
        print("Bravo vous avez trouvé le mot code, vous remportez donc le jeu.")
    else:
        print("Vous n'avez pas trouvé le mot code, vous perdez donc le jeu.")