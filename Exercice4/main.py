class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.vie = 100

    def attaquer(self, degats):
        self.vie -= degats

        if self.vie <= 0:
            self.vie = 0
            print(f"{self.nom} a perdu {degats} points de vie.\n")
            print(50 * "*")
            print(f"{self.nom} est mort. Merci d'avoir jouer :D ")
            print(50 * "*")
            exit()
        else:
            print(f"{self.nom} a perdu {degats} points de vie.\n")

    def soigner(self, points):
        self.vie += points
        if self.vie > 100:
            self.vie = 100
        print(f"{self.nom} a gagner {points} points de vie.\n")

    def afficher(self):
        print(f"\nNom : {self.nom} | Vie : {self.vie}\n")

nom = input("Entrez le nom de votre personnage : ")
personnage = Personnage(nom)

while True:

    print(50 * "-")
    personnage.afficher()
    print(50 * "-")
    print("| Faite un choix parmis les suivants : ")
    print("| 1. Attaquer le personnage")
    print("| 2. Soigner le personnage de vie")
    print("| 3. Quitter")
    print(50 * "-", "\n")
    choix = input("Votre choix : ")

    if choix == "1":
        try:
            degats = int(input("\nCombiens de degats voulez vous faire a votre personnage (0-100) : "))
            if 0 <= degats <= 100:
                personnage.attaquer(degats)
            else:
                print("\nVeuillez entrez un nombre entre 0 et 100")
        except ValueError:
            print("\nVeuillez entrez un nombre entier valide")

    elif choix == "2":
        try:
            soin = int(input("\nVous voulez soigner votre personnage de combiens de points (0-100) : "))
            if 0 <= soin <= 100:
                personnage.soigner(soin)
            else:
                print("\nVeuillez entrez un nombre entre 0 et 100")
        except ValueError:
            print("\nVeuillez entrez un nombre entier valide")

    elif choix == "3":
        print(20 * "*")
        print("Merci d'avoir jouer, Au revoir!")
        print(20 * "*")
        break

    else:
        print("Choix invalide")