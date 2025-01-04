"""
Module : epreuves_hasard

Ce module implémente des épreuves de hasard inspirées de Fort Boyard.
Les épreuves incluent des jeux comme le bonneteau et le lancer de dés, où le joueur doit tenter sa chance pour obtenir une clé.

Auteurs : [Lorenzo Gourat]
"""
from random import choice, randint


def bonneteau() -> bool:
    """
    **Bonneteau**

    Simule un jeu de bonneteau où le joueur doit deviner sous quel bonneteau se cache une clé.
    Le joueur dispose de deux essais pour réussir.

    :return: [bool] = True si le joueur trouve la clé dans les deux essais, False sinon.
    """
    # Liste des bonneteaux disponibles.
    goblets = ['A', 'B', 'C']

    print("Bienvenue au jeu du bonneteau !")
    print("La clé est cachée sous l'un des bonneteaux : A, B ou C.")
    print("Vous avez deux essais pour deviner où se trouve la clé.")

    # Le joueur a deux tentatives.
    for i in range(1, 3):
        # Clé cachée sous un bonneteau aléatoire.
        cle = choice(goblets)

        print(f"\nTentative {i} :")
        print(f"Bonneteaux disponibles : {', '.join(goblets)}")

        # Demande au joueur de choisir un bonneteau.
        choix_joueur = input("Choisissez un bonneteau (A, B ou C) : ").upper()

        # Vérifie si le choix est valide.
        if choix_joueur in goblets:
            if choix_joueur == cle:
                print(f"Bravo ! Vous avez trouvé la clé sous le bonneteau {cle}.")
                return True
            else:
                print(f"Dommage ! La clé n'était pas sous le bonneteau {choix_joueur}.")
        else:
            print("Choix invalide. Veuillez choisir parmi A, B ou C.")

    print("\nVous avez utilisé vos deux essais. Vous avez perdu !")
    print(f"La clé se trouvait sous le bonneteau {cle}.")
    return False

def jeu_lance_des() -> bool:
    """
    **Jeu_lance_des**

    Simule un jeu où le joueur et le maître lancent chacun deux dés sur trois manches maximum.
    L'objectif est de faire un six pour remporter la clé.

    :return: [bool] = True si le joueur gagne (fait un six), False sinon.
    """
    nb_essai = 3

    # Le joueur et le maître ont chacun trois essais au maximum.
    for i in range(nb_essai):
        print(f'Il reste {nb_essai-i-1} essais restants.')
        input("Appuyer sur 'Entrée' pour lancer les dés.")

        # Lancer des dés pour le joueur.
        des_joueur = (randint(1,6),randint(1,6))
        print(f"Vos dés on fait {des_joueur[0]} et {des_joueur[1]}")
        if des_joueur[0] == 6 or des_joueur[1] == 6:
            print("Vous avez fait un six vous gagnez.")
            return True


        # Lancer des dés pour le maître.
        des_maitre = (randint(1,6),randint(1,6))
        print(f"Les dés du maitre on fait {des_maitre[0]} et {des_maitre[1]}")
        if des_maitre[0] == 6 or des_maitre[1]:
            print("Le maitre a fait un six vous perdez.")
            return False

        print("Personne n'a fait de six, on passe à la manche suivante.")

    print("Personne n'a réussi à faire 6 en 3 manches, c'est une égalité vous ne remportez par la clé.")
    return False

def epreuve_hasard()-> bool:
    """
    **Epreuve_hasard**

    Execute une des épreuves de hasard au hazard.

    :return: [bool] = si le joueur à obtenue une clé à l'épreuve
    """
    # Liste des épreuves disponibles.
    liste_epreuve = [jeu_lance_des, bonneteau]

    # Sélection d'une épreuve aléatoire.
    epreuve = choice(liste_epreuve)

    # Exécution de l'épreuve choisie.
    return epreuve()