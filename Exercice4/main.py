class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.vie = 100

    def attaquer(self, degats):
        pass

    def soigner(self, points):
        pass

    def afficher(self):
        pass

nom = input("Entrez le nom de votre personnage : ")
personnage = Personnage(nom)

while True:

    choix = input("Votre choix : ")

    if choix == "1":
        break

    elif choix == "2":
        break

    elif choix == "3":
        break

    else:
        print("Choix invalide")