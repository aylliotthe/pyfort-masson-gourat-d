def saisi_secur(texte : str, borne : bool = None, *, check : type = int, a : int or str = None, b: int or str = None) -> str or int:
    """
    **Saisi_secur**

    Fonction qui s'assure que la valeur entrée par l'utilisateur est correct à la demande.

    :param texte: [str] = texte de a question qui va être demandé à l'utilisateur
    :param borne: [bool] = si la valeur entrée doit être dans une plage
    :param check: [type] = le type de la valeur entrée par l'utilisateur
    :param a: [int or str] = une des bornes de la plage de la valeur entrée
    :param b: [int or str] = une des bornes de la plage de la valeur entrée
    :return: [int or str] = la valeur entrée par l'utilisateur conforme, de type de check
    """


    while True:
        try:
            rep = check(input(texte))
            break
        except ValueError:
            print("Merci de rentrer une valeur valide")

    if borne:
        while not (min(a, b) <= rep <= max(a, b)):
            print("Merci de rentrer une valeur valide")
            rep = saisi_secur(texte,borne,check = check,a = a,b=b)

    return  rep

def info_matrice(matrice : list, position : tuple,*,valeur = None)-> None or str or int:
    """
    **info_matrice**

    Fonction qui renvoie la valeur d'une case dans une matrice ou la modifie

    :param matrice: [list] = la matrice
    :param position: [tuple] = tuple qui correspond à la position de la case
    :param valeur: [Any] = valeur que prendra la case
    :return: [Any] = la valeur de la case ou rien et modifie la case
    """
    if valeur is None:
        return  matrice[position[0]][position[1]]
    else:
        matrice[position[0]][position[1]] = valeur
