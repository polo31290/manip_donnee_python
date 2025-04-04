from pieces import piece

class pion (piece):
    def __init__(self, color, name):
        self.name = "pion"
        self.color = color
        self.position = none

    def mooves (self, position):
        #deplace la piece dans les bonnes directions uniquement devant lui sauf pour attaquer