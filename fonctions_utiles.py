"""
Module : fonctions_utiles

Contient les fonctions principales utilisées pour gérer les interactions avec les utilisateurs, les épreuves, et la gestion de l'équipe.

Auteurs : [Eliot Masson et Lorenzo Gourat]
"""


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
    # Boucle pour demander une saisie utilisateur tant qu'elle n'est pas valide

    while True:
        try:
            # Conversion de la saisie utilisateur au type attendu
            rep = check(input(texte))
            break
        except ValueError:
            # Message en cas de saisie invalide
            print("Merci de rentrer une valeur valide")

    # Si une borne est spécifiée, vérifier que la valeur est dans les limites
    if borne:
        while not (min(a, b) <= rep <= max(a, b)):
            print("Merci de rentrer une valeur valide")
            # Relancer la saisie sécurisée pour redemander une valeur valide
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
    # Vérifier si une nouvelle valeur est fournie pour modification
    if valeur is None:
        # Retourner la valeur de la case demandée
        return  matrice[position[0]][position[1]]
    else:
        # Modifier la valeur de la case spécifiée
        matrice[position[0]][position[1]] = valeur

def introduction() -> None:
    """
    **Introduction**

    Affiche un message d'introduction expliquant les objectifs du jeu,
    notamment la collecte de clés à travers des épreuves pour accéder à l'épreuve finale.

    :return: None
    """
    # Message de bienvenue
    print("Bienvenue dans Fort Boyard")
    # Explication de l'objectif du jeu
    print("Vous devez remporter des clés en gagnant des épreuves.")
    # Condition pour accéder à l'épreuve finale
    print("Après avoir récupéré 3 clés vous accéderez à l'épreuve final.")

def composer_equipe() -> list:
    """
    **Composer_equipe**

    Permet à l'utilisateur de composer une équipe de joueurs avec des noms, professions,
    et de désigner un leader. Si aucun leader n'est désigné, le premier joueur devient leader par défaut.

    :return: [list] = Une liste de dictionnaires représentant chaque membre de l'équipe
    """
    # Explication de la composition de l'équipe
    print("Vous allez maintenant composer votre équipe.")

    # Saisie sécurisée du nombre de joueurs dans l'équipe (entre 1 et 3)
    nombre_joueurs = saisi_secur("Entrez le nombre de joueur, maximum 3 personnes : ",True, a= 1,b = 3)

    equipe = []
    presence_leader = False  # Indique si un leader a été désigné

    # Boucle pour créer les joueurs
    for i in range(nombre_joueurs):
        # Saisie du nom du joueur
        nom = saisi_secur(f'Entrez le nom du joueur {i+1} : ',check=str)
        # Saisie de la profession du joueur
        profession = saisi_secur(f'Entrez la profession de {nom} : ',check=str)

        # Vérification si le joueur est désigné comme leader
        if not presence_leader :
            leader = saisi_secur("Ce joueur est-il le leader ? Si oui, entrez 1 sinon 0 : ", True, a=0, b=1)
            leader = True if leader == 1 else False
            if leader:
                presence_leader = True  # Marquer qu'un leader a été choisi


        equipe.append({'nom' : nom, "profession" : profession,'leader' : leader, 'cles_gagnees' : 0})

    # Si aucun leader n'a été désigné, le premier joueur devient leader par défaut
    if not presence_leader:
        equipe[0]['leader'] = True

    return equipe

def menu_epreuves()-> int:
    """
    **Menu_epreuves**

    Affiche un menu permettant de choisir parmi plusieurs épreuves et retourne le choix de l'utilisateur.

    :return: [int] = Le numéro correspondant à l'épreuve choisie
    """
    texte = "1. Épreuve de Mathématiques\n2. Épreuve de Logique\n3. Épreuve du hasard\n4. Énigme du Père Fouras\nChoix : "
    # Saisie sécurisée pour choisir une épreuve parmi les options disponibles
    return saisi_secur(texte,True, a = 1,b= 4)


def choisir_joueur(equipe : list) -> dict:
    """
    **Choisir_joueur**

    Permet de sélectionner un joueur d'une équipe en affichant une liste numérotée avec leurs noms, professions et rôles
    (Leader ou Membre).

    :param equipe: [list] = Liste de dictionnaires représentant les joueurs

    :return: [dict] = Le dictionnaire représentant le joueur sélectionné.
    """
    texte = ""
    nombre_joueurs = 1
    # Construire le texte avec les détails des joueurs

    for joueur in equipe:
        # Vérification du rôle (Leader ou Membre)
        if joueur['leader']:
            role = 'Leader'
        else :
            role = 'Membre'
        # Ajouter le joueur au texte

        texte += f'{nombre_joueurs}. {joueur["nom"]} ({joueur["profession"]}) - {role}\n'
        nombre_joueurs+=1

    # Ajouter une instruction pour choisir un joueur
    texte += 'Entrez le numéro du joueur : '

    # Saisie sécurisée pour sélectionner un joueur parmi la liste
    numero_joueur= saisi_secur(texte, True, a=1, b=len(equipe))
    return equipe[numero_joueur-1]