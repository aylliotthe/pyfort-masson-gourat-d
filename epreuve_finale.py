from json import load

from random import choice

from fonctions_utiles import saisi_secur


def salle_De_tresor():
    with open('data/indicesSalle.json', 'r', encoding= 'utf-8') as f:
        jeu_tv = load(f)

    annee = choice([i for i in jeu_tv["Fort Boyard"]])
    emission = choice([y for y in jeu_tv["Fort Boyard"][annee]])

    indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]
    mot_code = jeu_tv["Fort Boyard"][annee][emission]["MOT-CODE"]

    print("Bienvenue dans la salle de tresor !")
    print("Vous devez trouver un mot clé à l'aide d'indices.")
    print("Voici les trois premiers indices : ")
    for i in range(3):
        print(indices[i])
    k = 3
    reponse_correcte = False

    while k > 0 and not reponse_correcte :
        rep = saisi_secur("Veuillez entrer votre réponse : ", check=str).upper()
        if rep == mot_code :
            reponse_correcte = True
        else :
            k -= 1
            if k > 0:
                print(f"Il vous reste {k} essais.")
                print(f"L'indice suivant est : {indices[-k]}")
            else:
                print(f"Le mot code était {mot_code}.")

    if reponse_correcte :
        print("Bravo vous avez trouvé le mot code, vous remportez donc le jeu.")
    else:
        print("Vous n'avez pas trouvé le mot code, vous perdez donc le jeu.")

