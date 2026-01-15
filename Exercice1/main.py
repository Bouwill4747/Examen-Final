class Triangle:
    def __init__(self, n):
        self.n = n

    def ligne_croissant(self):
        lignes = []
        for i in range(1, self.n + 1):
            lignes.append("*" * i)

    def ligne_decroissant(self):
        lignes = []
        for i in range(self.n, 0, -1):
            lignes.append("*" * i)
        return lignes

class Affichage:
    def afficher(self, triangle):
        pass

n = int(input("Entrer un entier n :"))

triangle = Triangle(n)
affichage = Affichage()
affichage.afficher(triangle)