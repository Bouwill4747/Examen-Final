class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.vie = 100

    def attaquer(self, degats):
        self.vie -= degats

        if self.vie <= 0:
            self.vie = 0
            print(f"{self.nom} a perdu {degats} points de vie.")
            print(f"{self.nom} est mort. Merci d'avoir jouer :D ")
            exit()
        else:
            print(f"{self.nom} a perdu {degats} points de vie.")

    def soigner(self, points):
        self.vie += points
        if self.vie > 100:
            self.vie = 100
        print(f"{self.nom} a gagner {points} points de vie.")

    def afficher(self):
        print(f"\nNom : {self.nom} | Vie : {self.vie}\n")

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