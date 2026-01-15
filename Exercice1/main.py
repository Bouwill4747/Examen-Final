class Triangle:
    def __init__(self, n):
        self.n = n

    def ligne_croissant(self):
        lignes = []
        for i in range(1, self.n + 1):
            lignes.append("*" * i)
        return lignes

    def ligne_decroissant(self):
        lignes = []
        for i in range(self.n, 0, -1):
            lignes.append("*" * i)
        return lignes

class Affichage:
    def afficher(self, triangle):
        for ligne in triangle.ligne_croissant():
            print(ligne)

        print() # C'est juste pour faire une séparation

        for ligne in triangle.ligne_decroissant():
            print(ligne)

def demander_entier():
    while True:
        try:
            n = int(input("Entrer un nombre : "))
            if n > 0:
                return n
            else:
                print("Erreur! Veuillez entrez un nombre entier positif")
        except ValueError:
            print("Erreur! Veuillez entrez un nombre valide")

n= demander_entier()
triangle = Triangle(n)
affichage = Affichage()
affichage.afficher(triangle)