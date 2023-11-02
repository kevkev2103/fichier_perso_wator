
from random import randint


#initialisation du monde
class Monde:
    def __init__(self, longueur:int,largeur:int,nb_poissons:int,nb_requins:int):
        self.longueur = longueur
        self.largeur = largeur
        self.nb_requins = nb_requins
        self.nb_poissons = nb_poissons

#creation de la grille   
    def grille(self):
        tableau = [["*" for x in range(self.largeur)] for y in range(self.longueur)]
        texte= ""
        for ligne in tableau:
            for colonne in ligne:
                texte = texte+str(colonne)+ " "
            texte = texte + "\n"
        print(texte)



monde = Monde(10,10,0,0)
monde.grille()



