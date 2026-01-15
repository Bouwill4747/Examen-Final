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
                    self.nombres.append(nombre)
                    break
                except ValueError:
                    print("Veuillez entrer un nombre entier valide")

    def afficher_liste(self):
        print("Liste des nombres : ")
        print(self.nombres)

    def min(self):
        pass

    def max(self):
        pass

    def somme(self):
        pass

    def moyenne(self):
        pass