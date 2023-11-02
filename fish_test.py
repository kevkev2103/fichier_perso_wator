#creation de la classe poisson
from random import choice
class Poisson :
    def __init__(self,Id,energie,position,grossesse):
        self.Id = Id
        self.energie = energie
        self.position = position
        self.grossesse = grossesse

    def deplacement(self,liste_choix_deplacement):
        world.liste_choix_deplacement()
        choix_du_deplacement = randome.choice(liste_choix_deplacement)
        for x in liste_choix_deplacement:
            if x == "haut":
                self.position = world.tableau[[0]-1][1]
            elif x == "bas":
                self.position = world.tableau[[0]+1][1]
            elif x == "gauche":
                self.position = world.tableau[0][[1]-1]
            elif x == "droite":
                self.position = world.tableau[0][[1]+1]
