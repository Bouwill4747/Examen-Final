class Outils:
    def __init__(self):
        self.nombres = []

    def input_nombres(self):
        self.nombres = []
        print("Veuillez entrer 10 nombres entiers")

        for i in range(10):
            while True:
                try:
                    nombre = int(input(f"Nombres {i + 1} : "))
                    if nombre > 0:
                        self.nombres.append(nombre)
                        break
                    else:
                        print("Veuillez mettre un nombre positif")
                except ValueError:
                    print("Veuillez entrer un nombre entier valide")

    def afficher_liste(self):
        print("Liste des nombres : ")
        print(self.nombres)

    def min(self):
        minimum = self.nombres[0]
        for nombre in self.nombres:
            if nombre < minimum:
                minimum = nombre
        return minimum

    def max(self):
        maximum = self.nombres[0]
        for nombre in self.nombres:
            if nombre > maximum:
                maximum = nombre
        return maximum

    def somme(self):
        total = 0
        for nombre in self.nombres:
            total += nombre
        return total

    def moyenne(self):
        return self.somme() / len(self.nombres)