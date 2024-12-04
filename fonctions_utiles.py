def saisi_secur(texte : str, borne : bool = None, *, check : type = int, a : int = None, b: int = None) -> str or int:
    while True:
        try:
            rep = check(input(texte))
            break
        except ValueError:
            print("Merci de rentrer une valeur valide")

    if borne:
        while not (min(a, b) <= rep <= max(a, b)):
            print("Merci de rentrer une valeur valide")
            rep = check(input(texte))

    return  rep

