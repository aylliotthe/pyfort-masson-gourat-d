"""
Module : epreuves_logiques

Ce fichier contient les fonctions nécessaires pour implémenter un jeu de bataille navale simplifié.
Le jeu oppose un joueur et un maître du jeu. Chaque joueur place deux bateaux sur une grille 3x3,
puis tente de couler les bateaux adverses en alternant les tours.
Ce fichier inclut la logique de placement des bateaux, des tirs, de vérification des conditions
de victoire, et des interactions utilisateur.

Auteurs : [Eliot Masson et Lorenzo Gourat]
"""
from random import randint

from fonctions_utiles import saisi_secur, info_matrice


def suiv(joueur: int) -> int:
    """
    Retourne l'indice du joueur suivant.

    :param joueur: [int] L'indice du joueur actuel (0 ou 1).
    :return: [int] 0 si le joueur actuel est 1, 1 si le joueur actuel est 0.
    """
    # Retourne l'indice du joueur suivant (0 ou 1)
    return 0 if joueur == 1 else 1

def grille_vide() -> list:
    """
    Crée une grille 3x3 initialisée avec des espaces vides.

    :return: [list] Une matrice 3x3 contenant des chaînes vides (" ").
    """
    # Crée une grille 3x3 initialisée avec des espaces vides
    return [[" " for _ in range(3)]for _ in range(3)]

def affiche_grille(grille: list, message: str) -> None:
    """
    Affiche une grille 3x3 avec un message descriptif.

    :param grille: [list] La matrice 3x3 représentant la grille à afficher.
    :param message: [str] Le message affiché avant la grille.
    :return: None
    """
    # Affiche un message avant la grille
    print(message)
    # Parcourt chaque ligne de la grille
    for i in range (len(grille)):
        # Affiche chaque case suivie d'un séparateur "|"
        print("|",end="")
        for y in range(len(grille[0])):
            print(grille[i][y],end="")
            print("|",end="")
        print() # Saut de ligne après chaque ligne de la grille
    # Affiche une ligne pour séparer les différentes grilles
    print("-------")


def demander_position() -> tuple:
    """
    Demande à l'utilisateur une position sur une grille 3x3.

    :return: [tuple] Les coordonnées de la position choisie (ligne, colonne), en indices 0-indexés.
    """
    # Demande la ligne à l'utilisateur (entre 1 et 3)
    x = saisi_secur("Entrez la ligne entre 1 et 3 : ", True, a = 1, b = 3)
    # Demande la colonne à l'utilisateur (entre 1 et 3)
    y = saisi_secur("Entrez la colonne entre 1 et 3 : ", True, a = 1, b = 3)
    # Retourne la position sous forme d'indices (0-indexé)
    return x-1, y-1

def init() -> list:
    """
    Initialise une grille 3x3 pour positionner deux bateaux.

    Le joueur doit entrer deux positions distinctes pour placer ses bateaux.

    :return: [list] Une matrice 3x3 contenant les bateaux ('B') à leurs emplacements respectifs.
    """
    # Crée une grille vide pour positionner les bateaux
    grille_bateau = grille_vide()
    print("Positionnez vos bateaux :")
    # Demande la position du premier bateau
    print("Bateau 1")
    bat1 = demander_position()
    # Demande la position du second bateau
    print("Bateau 2")
    bat2 = demander_position()

    # Vérifie que les deux bateaux ne sont pas positionnés au même endroit
    while bat1 == bat2:
        print("Veuillez entrer des cases différentes pour les bateaux.")
        bat2 = demander_position()

    # Place les bateaux sur la grille
    info_matrice(grille_bateau,bat1,valeur="B")
    info_matrice(grille_bateau,bat2,valeur="B")
    return grille_bateau

def tour(joueur: int, grille_tirs_joueur: list, grille_adversaire: list) -> None:
    """
    Gère le déroulement d'un tour pour un joueur ou le maître du jeu.

    Le joueur ou le maître tire sur une position de la grille adverse.
    Si un bateau est touché, la position est marquée par 'x'. Sinon, elle est marquée par '.'.

    :param joueur: [int] L'indice du joueur actuel (0 = joueur, 1 = maître).
    :param grille_tirs_joueur: [list] La grille où les tirs du joueur actuel sont enregistrés.
    :param grille_adversaire: [list] La grille contenant les bateaux de l'adversaire.
    :return: None
    """
    if joueur == 1:
        # Tour du maître du jeu
        print("C'est le tour du maître du jeu :")
        # Génère une position de tir aléatoire
        tir= (randint(0,2),randint(0,2))
        # Vérifie que la case n'a pas déjà été tirée
        while info_matrice(grille_tirs_joueur,tir) == "x" or info_matrice(grille_tirs_joueur,tir) == ".":
            tir = (randint(0,2),randint(0,2))

        print(f"Le maître du jeu tire en position {tir[0]+1},{tir[1]+1}.")

        # Vérifie si le tir touche un bateau
        if info_matrice(grille_adversaire,tir) == "B":
            print("Touché coulé !")
            # Marque la case comme touchée
            info_matrice(grille_tirs_joueur,tir,valeur="x")
        else:
            print("Dans l'eau...")
            # Marque la case comme manquée
            info_matrice(grille_tirs_joueur,tir,valeur=".")

    else:
        # Tour du joueur
        print("C'est à votre tour de faire feu !:")
        # Affiche l'historique des tirs effectués
        affiche_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués :")
        # Demande une position de tir
        tir = demander_position()

        # Vérifie si le tir touche un bateau
        if info_matrice(grille_adversaire,tir) == "B":
            print("Touché coulé !")
            # Marque la case comme touchée
            info_matrice(grille_tirs_joueur,tir,valeur="x")
        else:
            print("Dans l'eau...")
            # Marque la case comme manquée
            info_matrice(grille_tirs_joueur,tir,valeur=".")


def gagne(grille_tirs_joueur) -> bool:
    """
    Vérifie si tous les bateaux (2) ont été coulés.

    :param grille_tirs_joueur: [list] La grille contenant l'historique des tirs.
    :return: [bool] True si deux cases 'x' (touché coulé) sont présentes, False sinon.
    """
    # Compte le nombre de cases marquées comme "touchées" ("x")
    compteur = 0
    for liste in grille_tirs_joueur:
        compteur += liste.count("x")
    # Retourne True si tous les bateaux (2) ont été coulés
    return compteur == 2

def jeu_bataille_navale() -> bool:
    """
    Simule un jeu simplifié de bataille navale.

    Le joueur et le maître du jeu placent chacun 2 bateaux sur une grille 3x3, puis alternent
    les tours pour tirer sur la grille adverse. Le premier à couler les 2 bateaux adverses gagne.

    :return: [bool] True si le joueur gagne, False si le maître du jeu gagne.
    """
    # Introduction des règles du jeu
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.")
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. Les bateaux coulés sont marqués par 'x'.")

    # Initialisation de la grille du joueur
    grille_bateau_joueur = init()
    affiche_grille(grille_bateau_joueur,"Découvrez votre grille de jeu avec vos bateaux :")

    # Initialisation de la grille du maître avec des bateaux placés aléatoirement
    grille_bateau_maitre = grille_vide()
    pos1 = (randint(0,2),randint(0,2))
    pos2 = (randint(0,2),randint(0,2))
    while pos1 == pos2:
        pos2 = (randint(0, 2), randint(0, 2))
    info_matrice(grille_bateau_maitre,pos1,valeur="B")
    info_matrice(grille_bateau_maitre,pos2,valeur="B")

    # Initialisation des grilles de tir
    grille_tir_joueur = grille_vide()
    grille_tir_maitre = grille_vide()


    # Initialisation du joueur qui commence (0 = joueur, 1 = maître)
    joueur = 0

    # Boucle principale du jeu (continue tant qu'aucun joueur n'a gagné)
    while not(gagne(grille_tir_maitre)) and not(gagne(grille_tir_joueur)):
        if joueur == 0:
            # Tour du joueur
            tour(joueur,grille_tir_joueur,grille_bateau_maitre)
        else:
            # Tour du maître
            tour(joueur,grille_tir_maitre,grille_bateau_joueur)

        # Passe au joueur suivant
        joueur = suiv(joueur)

    # Vérifie qui a gagné et retourne le résultat
    if gagne(grille_tir_joueur):
        print("Le joueur a gagné !\nVous remportez une clé.")
        return True
    else:
        print("Le maitre a gagné !")
        return False