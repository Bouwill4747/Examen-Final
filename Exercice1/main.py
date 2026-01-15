class Triangle:

    def __init__(self, n):
        self.n = n

    def ligne_croissant(self):
        pass

    def ligne_decroissant(self):
        pass

class Affichage:

    def afficher(self, triangle):
        pass

n = int(input("Entrer un entier n :"))

triangle = Triangle(n)
affichage = Affichage()
affichage.afficher(triangle)