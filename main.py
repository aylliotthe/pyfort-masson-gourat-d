"""
Module : main

Ce script simule le déroulement d'un jeu basé sur le concept de Fort Boyard.
Le jeu comporte plusieurs étapes où les joueurs participent à diverses épreuves pour gagner des clés.
Après avoir obtenu 3 clés, ils accèdent à l'épreuve finale dans la salle du trésor.

Auteurs : [Eliot Masson et Lorenzo Gourat]
"""
from epreuve_finale import salle_De_tresor
from epreuves_hasard import epreuve_hasard
from epreuves_logiques import jeu_bataille_navale
from epreuves_mathematiques import epreuve_math
from fonctions_utiles import introduction, composer_equipe, menu_epreuves, choisir_joueur
from enigme_pere_fouras import enigme_pere_fouras


def jeu():
    """
    **Jeu**

    Simule le déroulement complet d'un jeu inspiré de Fort Boyard.
    Le joueur compose une équipe, choisit des épreuves à travers un menu et tente de remporter des clés.
    Une fois 3 clés obtenues, le joueur passe à l'épreuve finale dans la salle du trésor.

    :return: None
    """
    # Présentation initiale et création de l'équipe.
    introduction()
    print()
    equipe = composer_equipe()
    print()

    # Initialisation du compteur de clés et de la liste des épreuves disponibles.
    nb_cle = 0
    liste_epreuve = [epreuve_math, jeu_bataille_navale, epreuve_hasard, enigme_pere_fouras]

    # Boucle principale : obtenir les 3 clés.
    while nb_cle != 3:
        print("Choisissez l'épreuve à laquelle vous voulez participer.")
        epreuve = menu_epreuves()
        print()

        # Choix du joueur pour l'épreuve sélectionnée.
        print("Choisissez le joueur qui va participer.")
        joueur = choisir_joueur(equipe)
        print()

        # Exécution de l'épreuve choisie.
        resultat = liste_epreuve[epreuve-1]()
        print()

        # Mise à jour des clés obtenues en cas de succès.
        if resultat:
            joueur["cles_gagnees"] += 1
            nb_cle +=1

    # Épreuve finale : salle du trésor.
    print("Vous avez obtenue 3 clés, vous passez à l'épreuve final.")
    salle_De_tresor()

# Lancement du jeu.
if __name__ == "__main__":
    jeu()