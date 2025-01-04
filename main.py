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
    equipe = composer_equipe()

    nb_cle = 0
    liste_epreuve = [epreuve_math, jeu_bataille_navale, epreuve_hasard, enigme_pere_fouras]
    while nb_cle != 0:
        epreuve = menu_epreuves()
        joueur = choisir_joueur(equipe)
        resultat = liste_epreuve[epreuve-1]()

        if resultat:
            joueur["cles_gagnees"] += 1
            nb_cle +=1

    print("Vous avez obtenue 3 clés, vous passez à l'épreuve final.")
    salle_De_tresor()