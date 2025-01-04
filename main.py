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
    introduction()
    print()
    equipe = composer_equipe()
    print()

    nb_cle = 0
    liste_epreuve = [epreuve_math, jeu_bataille_navale, epreuve_hasard, enigme_pere_fouras]
    while nb_cle != 3:
        print("Choisissez l'épreuve à laquelle vous voulez participer.")
        epreuve = menu_epreuves()
        print()

        print("Choisissez le joueur qui va participer.")
        joueur = choisir_joueur(equipe)
        print()

        resultat = liste_epreuve[epreuve-1]()
        print()
        if resultat:
            joueur["cles_gagnees"] += 1
            nb_cle +=1

    print("Vous avez obtenue 3 clés, vous passez à l'épreuve final.")
    salle_De_tresor()

jeu()