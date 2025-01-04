from random import randint

from fonctions_utiles import saisi_secur, info_matrice


def suiv(joueur : int)-> int:
    return 0 if joueur == 1 else 1

def grille_vide()-> list:
    return [[" " for _ in range(3)]for _ in range(3)]

def affiche_grille(grille : list, message : str)-> None:
    print(message)
    for i in range (len(grille)):
        print("|",end="")
        for y in range(len(grille[0])):
            print(grille[i][y],end="")
            print("|",end="")
        print()
    print("-------")

def demande_position()-> tuple:
    x = saisi_secur("Entrez la ligne entre 1 et 3 : ", True, a = 1, b = 3)
    y = saisi_secur("Entrez la colonne entre 1 et 3 : ", True, a = 1, b = 3)
    return x-1, y-1

def init()-> list:
    grille_bateau = grille_vide()
    print("Positionnez vos bateaux :")
    print("Bateau 1")
    bat1 = demande_position()
    print("Bateau 2")
    bat2 = demande_position()
    while bat1 == bat2:
        print("Veuillez entrer des cases différentes pour les bateaux.")
        bat2 = demande_position()

    info_matrice(grille_bateau,bat1,valeur="B")
    info_matrice(grille_bateau,bat2,valeur="B")
    return grille_bateau

def tour(joueur : int, grille_tirs_joueur : list, grille_adversaire: list)-> None:
    if joueur == 1:
        print("C'est le tour du maître du jeu :")
        tir= (randint(0,2),randint(0,2))
        while info_matrice(grille_tirs_joueur,tir) == "x" or info_matrice(grille_tirs_joueur,tir) == ".":
            tir = (randint(0,2),randint(0,2))

        print(f"Le maître du jeu tire en position {tir[0]+1},{tir[1]+1}.")

        if info_matrice(grille_adversaire,tir) == "B":
            print("Touché coulé !")
            info_matrice(grille_tirs_joueur,tir,valeur="x")
        else:
            print("Dans l'eau...")
            info_matrice(grille_tirs_joueur,tir,valeur=".")

    else:
        print("C'est à votre tour de faire feu !:")
        affiche_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués :")
        tir = demande_position()
        if info_matrice(grille_adversaire,tir) == "B":
            print("Touché coulé !")
            info_matrice(grille_tirs_joueur,tir,valeur="x")
        else:
            print("Dans l'eau...")
            info_matrice(grille_tirs_joueur,tir,valeur=".")

def gagne(grille_tirs_joueur)-> bool:
    k = 0
    for liste in grille_tirs_joueur:
        k += liste.count("x")
    return k == 2

def jeu_bataille_navale()->bool:
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.")
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. Les bateaux coulés sont marqués par 'x'.")
    grille_bateau_joueur = init()
    affiche_grille(grille_bateau_joueur,"Découvrez votre grille de jeu avec vos bateaux :")

    grille_bateau_maitre = grille_vide()
    pos1 = (randint(0,2),randint(0,2))
    pos2 = (randint(0,2),randint(0,2))
    while pos1 == pos2:
        pos2 = (randint(0, 2), randint(0, 2))
    info_matrice(grille_bateau_maitre,pos1,valeur="B")
    info_matrice(grille_bateau_maitre,pos2,valeur="B")

    grille_tir_joueur = grille_vide()
    grille_tir_maitre = grille_vide()


    joueur = 0
    while not(gagne(grille_tir_maitre)) and not(gagne(grille_tir_joueur)):
        if joueur == 0:
            tour(joueur,grille_tir_joueur,grille_bateau_maitre)
        else:
            tour(joueur,grille_tir_maitre,grille_bateau_joueur)

        joueur = suiv(joueur)

    if gagne(grille_tir_joueur):
        print("Le joueur a gagné !\nVous remportez une clé.")
        return True
    else:
        print("Le maitre a gagné !")
        return False