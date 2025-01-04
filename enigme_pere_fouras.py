"""
Module : enigmes_pere_fouras

Ce module gère les fonctionnalités liées aux énigmes du Père Fouras
Il permet de charger une liste d'énigmes à partir d'un fichier JSON, d'en sélectionner une aléatoirement,
et de simuler une interaction avec le joueur pour résoudre l'énigme.

Auteurs : [Eliot Masson et Lorenzo Gourat]
"""
from json import load

from random import choice

from fonctions_utiles import saisi_secur


def charger_enigmes() -> list:
    """
    **Charger_enigmes**

    Ouvre le fichier engimes du pere fouras et renvoie une liste de dictionnaire qui corespondent a une énigme et sa réponse

    :return: [list] liste de dictionnaire avec les énigmes et les questions
    """
    with open('data/enigmesPF.json', 'r', encoding='utf-8') as f:
        donnees = load(f)

    # Transformation des données pour n'extraire que les questions et réponses pertinentes
    return [{"question":dico["question"] ,"reponse": dico["reponse"]} for dico in donnees]

def enigme_pere_fouras()-> bool:
    """
    **Enigme_pere_fouras**

    Fonction qui éxécute simule une énigme du père fouras

    Pose une énigme et donne au joueur <>3 tentative pour y répondre

    :return: [bool] optient une clé ou non
    """
    # Charger les énigmes depuis le fichier
    liste_enigme = charger_enigmes()

    # Sélection aléatoire d'une énigme
    enigme = choice(liste_enigme)
    question = enigme["question"]
    juste = enigme["reponse"].lower()

    # Initialisation des tentatives
    tentatives_restantes = 3

    # Affichage de la question
    print(question)

    # Boucle pour les tentatives du joueur
    while tentatives_restantes > 0:
        # Demander la réponse au joueur
        rep = saisi_secur("Veuillez entrer votre réponse à l'énigme : ",check=str).lower()

        # Vérifier la réponse
        if rep == juste :
            print("Correct! Vous gagnez une clé.")
            return True
        else:
            tentatives_restantes -=1
            print(f"Faux, ce n'est pas la bonne réponse. Il vous reste {tentatives_restantes} essais.")

    # Réponse incorrecte après toutes les tentatives
    print(f"Faux, la bonne réponse était {juste}. Vous ne gagnez pas de clé.")
    return False