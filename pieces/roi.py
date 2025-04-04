from pieces import piece

class roi (piece):
    def __init__(self, color, name):
        self.name = "roi"
        self.color = color
        self.position = none

    def mooves (self, position):
        #deplace la piece dans les bonnes directions de 1 case omnidirectionnel