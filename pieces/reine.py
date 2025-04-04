from pieces import piece

class reine (piece):
    def __init__(self, color, name):
        self.name = "reine"
        self.color = color
        self.position = none

    def mooves (self, position):
        #deplace la piece dans les bonnes directions omnidirectionnel