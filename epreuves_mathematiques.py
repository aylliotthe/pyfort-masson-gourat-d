from random import randint, choice

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
    while not(est_premier(n)):
        n+= 1
    return  n

def epreuve_math_premier()->bool:
    k = randint(10,20)
    print(f"Épreuve de Mathématiques:  Trouver le nombre premier supérieur le plus proche de {k}.")
    rep = saisi_secur('Votre réponse: ')
    if rep == premier_plus_proche(k) :
        print("Correct! Vous gagnez une clé.")
        return True

    print(f"Faux, la bonne réponse était {premier_plus_proche(k)}. Vous ne gagnez pas de clé.")
    return False

def epreuve_roulette_mathematique()-> bool:
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

def epreuve_math():
    liste_epreuve = [epreuve_math_factorielle, epreuve_math_premier, epreuve_roulette_mathematique]

    epreuve = choice(liste_epreuve)

    return epreuve()

print(epreuve_math())