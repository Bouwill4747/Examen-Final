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

n = int(input("Entrer un entier n : "))

triangle = Triangle(n)
affichage = Affichage()
affichage.afficher(triangle)