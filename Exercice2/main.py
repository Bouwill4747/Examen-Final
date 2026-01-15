import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Doubleur de Nombre")

        self.layout = QVBoxLayout()

        self.label = QLabel("Entrez un nombre entier : ")
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    def calculer_double(self):
        pass

    def sauvegarder_resultat(self):
        pass

    def charger_resultat(self):
        pass

app = QApplication(sys.argv)
fenetre = App()
fenetre.show()
sys.exit(app.exec())
