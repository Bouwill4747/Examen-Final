from Outils import Outils

outils = Outils()
outils.input_nombres()

print("\n")
print(50 * "*")
outils.afficher_liste()
print("\nResultats")
print("Minimum :", outils.min())
print("Maximum :", outils.max())
print("Somme :", outils.somme())
print("Moyenne :", outils.moyenne(), "\n")
print(50 * "*")