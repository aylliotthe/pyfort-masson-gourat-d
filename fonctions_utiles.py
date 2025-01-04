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

def introduction():
    print("Bienvenue dans Fort Boyard")
    print("Vous devez remporter des clés en gagnant des épreuves.")
    print("Après avoir récupéré 3 clés vous accéderez à l'épreuve final.")

def composer_equipe():
    print("Vous allez maintenant composer votre équipe.")
    k = saisi_secur("Entrez le nombre de joueur, maximum 3 personnes : ",True, a= 1,b = 3)

    equipe = []
    presence_leader = False
    for i in range(k):
        nom = saisi_secur(f'Entrez le nom du joueur {i+1} : ',check=str)
        profession = saisi_secur(f'Entrez la profession de {nom} : ',check=str)
        if not presence_leader :
            leader = saisi_secur("Ce joueur est_il le leader, si oui entrez 1 sinon 0 : ", True, a = 0,b = 1 )
            leader = True if leader == 1 else False
            if leader:
                presence_leader = True


        equipe.append({'nom' : nom, "profession" : profession,'leader' : leader, 'cles_gagnees' : 0})

    if not presence_leader:
        equipe[0]['leader'] = True

    return equipe

def menu_epreuves():
    texte = "1. Épreuve de Mathématiques\n2. Épreuve de Logique\n3. Épreuve du hasard\n4. Énigme du Père Fouras\nChoix : "
    return saisi_secur(texte,True, a = 1,b= 4)

def choisir_joueur(equipe) :
    texte = ""
    k = 1
    for joueur in equipe:
        if joueur['leader']:
            role = 'Leader'
        else :
            role = 'Membre'
        texte += f'{k}. {joueur["nom"]} ({joueur["profession"]}) - {role}\n'
        k+=1

    texte += 'Entrez le numéro du joueur : '
    k= saisi_secur(texte, True, a=1, b=len(equipe))
    return equipe[k-1]