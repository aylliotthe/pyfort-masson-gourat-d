from json import load

from random import choice

from fonctions_utiles import saisi_secur


def charger_enigmes() -> list:
    """
    **Charger_enigmes**

    Ouvre le fichier engimes du pere fouras et renvoie une liste de dictionnaire qui corespondent a une énigme et sa réponse

    :return: [list] liste de dictionnaire avec les énigmes et les questions
    """
    with open('data/enigmesPF.json', 'r', encoding='utf-8') as f:
        donnees = load(f)

    return [{"question":dico["question"] ,"reponse": dico["reponse"]} for dico in donnees]

def enigme_pere_fouras()-> bool:
    """
    **Enigme_pere_fouras**

    Fonction qui éxécute simule une énigme du père fouras

    Pose une énigme et donne au joueur <>3 tentative pour y répondre

    :return: [bool] optient une clé ou non
    """
    liste_enigme = charger_enigmes()
    enigme = choice(liste_enigme)
    question = enigme["question"]
    juste = enigme["reponse"].lower()
    k = 3
    print(question)
    while k > 0:
        rep = saisi_secur("Veuillez entrer votre réponse à l'énigme : ",check=str).lower()
        if rep == juste :
            print("Correct! Vous gagnez une clé.")
            return True
        else:
            k -=1
            print(f"Faux, ce n'est pas la bonne réponse. Il vous reste {k} essais.")

    print(f"Faux, la bonne réponse était {juste}. Vous ne gagnez pas de clé.")
    return False