from pieces import piece

class fou (piece):
    def __init__(self, color, name):
        self.name = "fou"
        self.color = color
        self.position = none

    def mooves (self, position):
        #deplace la piece dans les bonnes directions en x