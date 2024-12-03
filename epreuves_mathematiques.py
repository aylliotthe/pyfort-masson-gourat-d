from random import randint
from fonctions_utiles import saisi_secur


def factorielle(n : int) -> int:
    """
    **Factorielle**

    Fonction qui calcule la factorielle d'un entier

    Exemple d'utilisation ::

        factorielle(7)

    :param n: [int]
    :return: factorielle de n
    """
    if n == 1:
        return  1
    else:
        return n * factorielle(n-1)

def epreuve_math_factorielle()->bool:
    k = randint(1,10)
    print(f"Épreuve de Mathématiques: Calculer la factorielle de {k}.")
    rep = saisi_secur('Votre réponse: ')
    if rep == factorielle(k) :
        print("Correct! Vous gagnez une clé.")
        return True
    print(f"Faux, la bonne réponse était {factorielle(k)}. Vous ne gagnez pas de clé.")
    return False

def est_premier(n: int) -> bool:
    if n <= 1:
        return False  #Les nombres <= 1 ne sont pas premiers
    div = [i for i in range(1, n + 1) if n % i == 0]
    return div == [1, n]

def premier_plus_proche(n : int)-> int:
