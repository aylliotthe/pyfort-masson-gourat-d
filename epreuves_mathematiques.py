from random import randint, choice

from fonctions_utiles import saisi_secur


def factorielle(n : int) -> int :
    """
    **Factorielle**

    Fonction qui calcule la factorielle d'un entier

    Exemple d'utilisation ::

        factorielle(7)

    :param n: [int]
    :return: [int] = factorielle de n
    """
    if n == 1:
        return  1
    else:
        return n * factorielle(n-1)

def epreuve_math_factorielle()->bool:
    """
    **Epreuve_math_factorielle**

    Fonction qui éxécute l'épreuve mathématique factorielle

    Demande la factorielle d'un entier entre 1 et 10 à un joueur et vérifie s'il a raison.

    :return: [bool] optient une clé ou non
    """
    k = randint(1,10)
    print(f"Épreuve de Mathématiques: Calculer la factorielle de {k}.")
    rep = saisi_secur('Votre réponse: ')
    if rep == factorielle(k) :
        print("Correct! Vous gagnez une clé.")
        return True

    print(f"Faux, la bonne réponse était {factorielle(k)}. Vous ne gagnez pas de clé.")
    return False

def est_premier(n: int) -> bool:
    """
    **Est_premier**

    Fonction qui vérifie si un entier est premier

    :param n: [int]
    :return: [bool] = si n est premier ou non
    """
    if n <= 1:
        return False  #Les nombres <= 1 ne sont pas premiers
    div = [i for i in range(1, n + 1) if n % i == 0]
    return div == [1, n]

def premier_plus_proche(n : int)-> int:
    """
    **Premier_plus_proche**

    Fonction qui renvoie le nombre premier supérieur le plus proche d'un nombre entré

    :param n: [int]
    :return: [int] = nombre premier supérieur le plus proche de n
    """
    while not(est_premier(n)):
        n+= 1
    return  n

def epreuve_math_premier()->bool:
    """
    **Epreuve_math_premier**

    Fonction qui éxécute l'épreuve mathématique premier

    Demande l'entier premiers supérieur d'un entier entre 10 et 20 à un joueur et vérifie s'il a raison.

    :return: [bool] optient une clé ou non
    """
    k = randint(10,20)
    print(f"Épreuve de Mathématiques:  Trouver le nombre premier supérieur le plus proche de {k}.")
    rep = saisi_secur('Votre réponse: ')
    if rep == premier_plus_proche(k) :
        print("Correct! Vous gagnez une clé.")
        return True

    print(f"Faux, la bonne réponse était {premier_plus_proche(k)}. Vous ne gagnez pas de clé.")
    return False

def epreuve_roulette_mathematique()-> bool:
    """
    **Epreuve_roulette_mathematique**

    Fonction qui éxécute l'épreuve roulette mathématique

    Demande la somme/produit/soustraction de 5 entier entre 1 et 20 à un joueur et vérifie s'il a raison.

    :return: [bool] optient une clé ou non
    """
    liste = [randint(1,20) for i in range(5)]
    op = choice(["addition","soustraction","multiplication"])
    if op == "addition":
        juste = 0
        for i in liste:
            juste += i
    if op == "soustraction":
        juste = liste[0]
        for i in liste[1:]:
            juste -= i
    else:
        juste = 1
        for i in liste:
            juste *= i

    print("Épreuve de Mathématiques:  Nombres sur la roulette :",liste)
    print(f"Calculez le résultat en combinant ces nombres avec une {op}.")
    rep = saisi_secur('Votre réponse: ')
    if rep == juste:
        print("Correct! Vous gagnez une clé.")
        return True

    print(f"Faux, la bonne réponse était {juste}. Vous ne gagnez pas de clé.")
    return False

def epreuve_math()-> bool:
    """
    **Epreuve_math**

    Execute une des épreuves mathématique au hazard.

    :return: [bool] = si le joueur à obtenue une clé à l'épreuve
    """
    liste_epreuve = [epreuve_math_factorielle, epreuve_math_premier, epreuve_roulette_mathematique]

    epreuve = choice(liste_epreuve)

    return epreuve()

if __name__ == "__main__":
    epreuve_math()
