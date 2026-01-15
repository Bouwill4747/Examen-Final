import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QLineEdit, QPushButton, QMessageBox

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(500, 350)

        self.setWindowTitle("Doubleur de Nombre")

        self.layout = QVBoxLayout()

        self.label = QLabel("Entrez un nombre entier : ")
        self.layout.addWidget(self.label)

        self.input_nombre = QLineEdit()
        self.layout.addWidget(self.input_nombre)

        self.btn_calculer = QPushButton("Calculer le double")
        self.btn_calculer.clicked.connect(self.calculer_double)
        self.layout.addWidget(self.btn_calculer)

        self.label_resultat = QLabel("Resultat : ")
        self.layout.addWidget(self.label_resultat)

        self.btn_sauvegarder_resultat = QPushButton("Sauvegarder le resultat")
        self.btn_sauvegarder_resultat.clicked.connect(self.sauvegarder_resultat)
        self.layout.addWidget(self.btn_sauvegarder_resultat)

        self.btn_charger = QPushButton("Charger un resultat")
        self.btn_charger.clicked.connect(self.charger_resultat)
        self.layout.addWidget(self.btn_charger)

        self.setLayout(self.layout)

    def calculer_double(self):
        texte = self.input_nombre.text().strip()

        if texte == "":
            QMessageBox.information(self, "Erreur", "Le champ est vide")
            return

        try:
            nombre = int(texte)
        except ValueError:
            QMessageBox.warning(self, "Erreur", "Veuillez entre un nombre entier valide")
            return

        resultat = nombre * 2
        self.label_resultat.setText(f"Resultat : {resultat}")

    def sauvegarder_resultat(self):
        pass

    def charger_resultat(self):
        pass

app = QApplication(sys.argv)
fenetre = App()
fenetre.show()
sys.exit(app.exec())
